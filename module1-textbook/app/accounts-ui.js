(function () {
  window.setupTextbookAccounts = function (store, loadGuest) {
    const dialog = document.createElement('dialog'); dialog.className = 'account-dialog';
    dialog.setAttribute('aria-labelledby', 'account-title');
    dialog.innerHTML = `<h2 id="account-title">Your progress, anywhere</h2>
      <p id="account-description">Log in or create an account to save your answers across devices.</p>
      <form id="account-form">
        <label for="account-username">Username</label>
        <input id="account-username" name="username" autocomplete="username" pattern="[A-Za-z0-9_]{3,30}" minlength="3" maxlength="30" required spellcheck="false" autocapitalize="none">
        <p class="account-help">3–30 letters, numbers or underscores. Usernames are not case-sensitive.</p>
        <label for="account-password">Password</label>
        <input id="account-password" name="password" type="password" autocomplete="current-password" minlength="12" maxlength="128" required>
        <p class="account-help">At least 12 characters. No email needed. Keep your password safe: there is no email password recovery.</p>
        <div class="account-actions"><button class="btn primary" type="submit" id="account-submit">Log in</button><button class="btn ghost" type="button" id="account-mode">Create an account</button></div>
      </form>
      <section id="account-signed-in" hidden>
        <p id="account-user"></p><p class="account-help">Your session lasts up to seven days in this tab. Guest progress stays separate.</p>
        <div class="account-actions"><button class="btn primary" id="account-sync">Sync now</button><button class="btn ghost" id="account-import">Import guest progress</button><button class="btn ghost" id="account-logout">Log out</button></div>
        <p class="account-help">Import fills missing exercises; existing account answers are kept.</p>
        <div id="account-conflicts"></div>
      </section>
      <p class="account-message" id="account-message" role="status" aria-live="polite"></p>
      <div class="account-actions"><button class="btn ghost" id="account-close">Close</button></div>`;
    document.body.appendChild(dialog);
    const $ = id => dialog.querySelector('#' + id);
    let signup = false, working = false;
    function refresh() {
      const active = !!store.user && !store.expired;
      $('account-form').hidden = active;
      $('account-signed-in').hidden = !active;
      $('account-description').textContent = store.expired ? 'Your session expired. Log in again to sync the work kept on this device.' : 'Log in or create an account to save your answers across devices.';
      $('account-user').textContent = store.user ? 'Logged in as ' + store.user.username : '';
      document.getElementById('account-open').textContent = store.user ? 'Account' : 'Log in';
      if (store.expired) { $('account-username').value = store.user.username; signup = false; }
      $('account-password').autocomplete = signup ? 'new-password' : 'current-password';
      $('account-submit').textContent = signup ? 'Create account' : 'Log in';
      $('account-mode').textContent = signup ? 'I already have an account' : 'Create an account';
      $('account-mode').hidden = !!store.user;
      const conflicts = $('account-conflicts'); conflicts.replaceChildren();
      for (const key of Object.keys(store.cache?.conflicts || {})) {
        const row = document.createElement('div'); row.className = 'account-conflict';
        const p = document.createElement('p'); p.textContent = 'Module ' + key.replace('/', ', lesson ') + ' changed on another device. Choose which lesson answers to keep.'; row.appendChild(p);
        for (const [label, local] of [['Keep this device’s answers', true], ['Use saved account answers', false]]) {
          const button = document.createElement('button'); button.className = 'btn ghost'; button.textContent = label;
          button.onclick = () => run(() => store.resolve(key, local)); row.appendChild(button);
        }
        conflicts.appendChild(row);
      }
    }
    async function run(action) {
      if (working) return; working = true;
      $('account-message').textContent = 'Please wait…';
      dialog.querySelectorAll('button').forEach(b => { b.disabled = true; });
      try { await action(); $('account-message').textContent = store.expired ? 'Please log in again.' : store.hasPending ? 'Some progress still needs syncing. Check your connection or resolve the choices below.' : 'Done.'; }
      catch (error) { $('account-message').textContent = error.message; }
      finally { working = false; dialog.querySelectorAll('button').forEach(b => { b.disabled = false; }); refresh(); }
    }
    document.getElementById('account-open').onclick = () => { refresh(); $('account-message').textContent = store.apiUrl ? '' : 'Accounts are not connected yet. Guest progress still saves in this browser.'; dialog.showModal(); };
    $('account-close').onclick = () => dialog.close();
    dialog.addEventListener('close', () => { $('account-password').value = ''; });
    $('account-mode').onclick = () => { signup = !signup; refresh(); };
    $('account-form').onsubmit = e => { e.preventDefault(); run(async () => {
      const password = $('account-password').value; $('account-password').value = '';
      await store.login($('account-username').value, password, signup);
      signup = false;
    }); };
    $('account-sync').onclick = () => run(() => store.sync());
    $('account-import').onclick = () => run(() => store.importGuest(loadGuest()));
    $('account-logout').onclick = () => run(() => store.logout());
    refresh(); return refresh;
  };
})();
