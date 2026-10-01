(function (root) {
  'use strict';
  const copy = value => JSON.parse(JSON.stringify(value));
  class ProgressStore {
    constructor({ apiUrl, storage, sessionStorage, fetcher, onChange = () => {}, onStatus = () => {}, scope = '' }) {
      this.apiUrl = apiUrl.replace(/\/$/, ''); this.storage = storage; this.sessions = sessionStorage;
      this.fetcher = fetcher; this.onChange = onChange; this.onStatus = onStatus;
      this.sessionKey = 'textbook-session:' + scope;
      this.cachePrefix = 'textbook-account:' + scope + ':';
      this.identity = this.read(this.sessions, this.sessionKey, null);
      if (!this.identity?.user?.id || !this.identity?.token) this.identity = null;
      this.epoch = 0; this.busy = null; this.timer = null; this.expired = false;
      this.cache = this.loadCache();
    }
    read(storage, key, fallback) { try { return JSON.parse(storage.getItem(key)) || fallback; } catch { return fallback; } }
    loadCache() {
      return this.identity ? this.read(this.storage, this.cachePrefix + this.identity.user.id,
        { all: {}, last: {}, versions: {}, pending: {}, conflicts: {} }) : null;
    }
    get user() { return this.identity?.user || null; }
    get hasPending() { return !!this.cache && Object.keys(this.cache.pending).length > 0; }
    persistCache() {
      if (!this.identity) return;
      try { this.storage.setItem(this.cachePrefix + this.user.id, JSON.stringify(this.cache)); }
      catch { this.onStatus('Browser storage is full or unavailable. Keep this tab open until syncing completes.'); }
    }
    saveNavigation(value) {
      if (!this.cache) return;
      for (const key of ['last', 'mod', 'lastMod']) this.cache[key] = value[key];
      this.persistCache();
    }
    async request(path, method = 'GET', body, identity = this.identity) {
      if (!this.apiUrl) throw new Error('Accounts are not connected yet. Guest progress still saves in this browser.');
      const response = await this.fetcher(this.apiUrl + path, {
        method, headers: { ...(body ? { 'Content-Type': 'application/json' } : {}), ...(identity ? { Authorization: 'Bearer ' + identity.token } : {}) },
        ...(body ? { body: JSON.stringify(body) } : {}), signal: AbortSignal.timeout(20000), cache: 'no-store', credentials: 'omit'
      });
      const data = await response.json();
      if (!response.ok) { const error = new Error(data.error || 'Could not connect.'); error.status = response.status; error.data = data; throw error; }
      return data;
    }
    async login(username, password, signup = false) {
      if (this.user && this.user.username !== username.trim().toLowerCase()) throw new Error('Log out before switching accounts.');
      const data = await this.request(signup ? '/signup' : '/login', 'POST', { username, password }, null);
      this.epoch++; this.identity = data; this.expired = false;
      try { this.sessions.setItem(this.sessionKey, JSON.stringify(data)); } catch { /* Session remains in memory. */ }
      this.cache = this.loadCache(); this.onChange();
      await this.sync();
    }
    changeLesson(module, lesson, items) {
      if (!this.cache) return;
      const key = module + '/' + lesson;
      (this.cache.all['m' + module] ||= {})[lesson] = copy(items);
      this.cache.pending[key] = { module, lesson, items: copy(items), version: this.cache.versions[key] || 0 };
      this.persistCache(); this.onStatus('Saved on this device · waiting to sync');
      clearTimeout(this.timer); this.timer = setTimeout(() => this.sync(), 650);
    }
    async sync() {
      if (!this.identity || !this.apiUrl || this.expired) return;
      if (this.busy) return this.busy;
      const epoch = this.epoch;
      this.busy = this.runSync(epoch).finally(() => { this.busy = null; });
      return this.busy;
    }
    async runSync(epoch) {
      this.onStatus('Syncing progress…');
      try {
        // Fetch first so fresh sessions import remote work; never replace queued local edits.
        const data = await this.request('/progress');
        if (epoch !== this.epoch) return;
        for (const record of data.lessons) {
          const key = record.module + '/' + record.lesson;
          if (this.cache.pending[key]) continue;
          (this.cache.all['m' + record.module] ||= {})[record.lesson] = record.items;
          this.cache.versions[key] = record.version;
        }
        this.persistCache(); this.onChange();
        for (const key of Object.keys(this.cache.pending)) {
          if (this.cache.conflicts[key]) continue;
          const pending = this.cache.pending[key], sent = copy(pending);
          try {
            const result = await this.request('/progress', 'PUT', sent);
            if (epoch !== this.epoch) return;
            this.cache.versions[key] = result.version;
            if (this.cache.pending[key] === pending) delete this.cache.pending[key];
            else this.cache.pending[key].version = result.version;
          } catch (error) {
            if (epoch !== this.epoch) return;
            if (error.status !== 409) throw error;
            const remote = error.data.current;
            // A response can be lost after a successful write. Treat an identical retry as saved.
            if (JSON.stringify(remote.items) === JSON.stringify(sent.items)) {
              this.cache.versions[key] = remote.version;
              if (this.cache.pending[key] === pending) delete this.cache.pending[key];
              else this.cache.pending[key].version = remote.version;
            } else this.cache.conflicts[key] = remote;
          }
          this.persistCache();
        }
        const conflicts = Object.keys(this.cache.conflicts).length;
        this.onStatus(conflicts ? 'Sync needs a choice · open Account' : this.hasPending ? 'Saved on this device · waiting to sync' : 'Saved to your account');
        if (this.hasPending && !conflicts) { clearTimeout(this.timer); this.timer = setTimeout(() => this.sync(), 650); }
        this.onChange();
      } catch (error) {
        if (epoch !== this.epoch) return;
        if (error.status === 401) this.expired = true;
        this.onStatus(error.status === 401 ? 'Session expired · open Account to log in again' : 'Offline or unavailable · progress kept on this device');
        this.onChange();
      }
    }
    resolve(key, useLocal) {
      const remote = this.cache.conflicts[key], pending = this.cache.pending[key];
      if (!remote || !pending) return;
      this.cache.versions[key] = remote.version;
      if (useLocal) pending.version = remote.version;
      else {
        (this.cache.all['m' + pending.module] ||= {})[pending.lesson] = remote.items;
        delete this.cache.pending[key];
      }
      delete this.cache.conflicts[key]; this.persistCache(); this.onChange(); return this.sync();
    }
    importGuest(guest) {
      // Import only missing exercises. Existing account answers, including resets, win.
      for (const [mod, lessons] of Object.entries(guest.all || {})) {
        for (const [lesson, items] of Object.entries(lessons)) {
          const existing = this.cache.all[mod]?.[lesson];
          if (existing && Object.keys(existing).length === 0 && this.cache.versions[+mod.slice(1) + '/' + lesson]) continue;
          const merged = { ...items, ...(existing || {}) };
          if (JSON.stringify(merged) !== JSON.stringify(existing || {})) this.changeLesson(+mod.slice(1), lesson, merged);
        }
      }
      this.onChange(); return this.sync();
    }
    async logout() {
      if (this.hasPending) throw new Error('Sync or resolve pending progress before logging out. Your work is still saved on this device.');
      await this.request('/logout', 'POST');
      this.clearSession();
    }
    clearSession() {
      clearTimeout(this.timer); this.epoch++;
      try { this.sessions.removeItem(this.sessionKey); } catch { /* Memory-only session. */ }
      this.identity = null; this.cache = null; this.expired = false; this.onChange();
    }
  }
  root.TextbookProgressStore = ProgressStore;
})(globalThis);
