import test from 'node:test';
import assert from 'node:assert/strict';
import '../module1-textbook/app/progress-store.js';
const storage = () => { const map = new Map(); return { getItem: k => map.get(k), setItem: (k,v) => map.set(k,v), removeItem: k => map.delete(k) }; };
const response = (data, status = 200) => new Response(JSON.stringify(data), { status });
function fixture(fetcher) {
  return new TextbookProgressStore({ apiUrl: 'https://test', storage: storage(), sessionStorage: storage(), fetcher });
}
test('offline edits survive reload and cannot leak into guest state', async () => {
  let online = true; const local = storage(), session = storage();
  const fetcher = async (url, options) => {
    if (!online) throw new Error('offline');
    if (url.endsWith('/login')) return response({ user: { id: 'alice', username: 'alice' }, token: 'token' });
    return response({ lessons: [] });
  };
  const store = new TextbookProgressStore({ apiUrl: 'https://test', storage: local, sessionStorage: session, fetcher });
  local.setItem('textbook', JSON.stringify({ all: { m1: { '1': { G: { res: 'ok' } } } } }));
  await store.login('alice', 'password'); online = false;
  store.changeLesson(1, '1', { A: { res: 'ok' } }); await store.sync(); clearTimeout(store.timer);
  assert.equal(store.hasPending, true);
  const restored = new TextbookProgressStore({ apiUrl: 'https://test', storage: local, sessionStorage: session, fetcher });
  assert.deepEqual(restored.cache.pending['1/1'].items, { A: { res: 'ok' } });
  assert.equal(JSON.parse(local.getItem('textbook')).all.m1['1'].A, undefined);
  await assert.rejects(store.logout(), /pending/);
});
test('conflicts require a choice; account answers survive guest import', async () => {
  let version = 2, items = { A: { res: 'ok' } };
  const store = fixture(async (url, options) => {
    if (url.endsWith('/login')) return response({ user: { id: 'alice', username: 'alice' }, token: 'token' });
    if (options.method === 'GET') return response({ lessons: [{ module: 1, lesson: '1', items, version }] });
    const body = JSON.parse(options.body);
    if (body.version !== version) return response({ current: { items, version } }, 409);
    items = body.items; return response({ version: ++version });
  });
  await store.login('alice', 'password');
  await store.importGuest({ all: { m1: { '1': { A: { res: 'bad' }, B: { res: 'ok' } } } } });
  assert.equal(items.A.res, 'ok'); assert.equal(items.B.res, 'ok');
  store.changeLesson(1, '1', { A: { res: 'bad' } }); version++;
  await store.sync(); assert.ok(store.cache.conflicts['1/1']);
  await store.resolve('1/1', false); assert.equal(store.hasPending, false); assert.equal(store.cache.all.m1['1'].A.res, 'ok');
  clearTimeout(store.timer);
});
test('edits made during a save remain queued with the new server version', async () => {
  let finishSave; let saving;
  const started = new Promise(resolve => { saving = resolve; });
  const store = fixture(async (url, options) => {
    if (url.endsWith('/login')) return response({ user: { id: 'alice', username: 'alice' }, token: 'token' });
    if (options.method === 'GET') return response({ lessons: [] });
    saving(); return await new Promise(resolve => { finishSave = () => resolve(response({ version: 1 })); });
  });
  await store.login('alice', 'password'); store.changeLesson(1, '1', { A: { res: 'ok' } });
  const sync = store.sync(); await started;
  store.changeLesson(1, '1', { A: { res: 'bad' } }); finishSave(); await sync;
  assert.equal(store.cache.pending['1/1'].version, 1);
  assert.equal(store.cache.pending['1/1'].items.A.res, 'bad'); clearTimeout(store.timer);
});
