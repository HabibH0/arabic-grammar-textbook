# Arabic Grammar Textbook

An interactive Arabic grammar textbook with 21 modules, username/password accounts,
and progress synced to Neon. The static frontend is published with GitHub Pages.

## Run and test

Requires Python 3 and Node.js 24. Run `npm ci` then `npm test`.
Tests exercise the actual API against embedded Postgres (PGlite), including user
isolation, password hashing, session expiry, rate limits, stale-write detection,
offline queues, guest import and edits made while a save is in flight.

Build the textbook:

```sh
cd module1-textbook/generator
python build_book.py
```

From the repository root, serve it with:

```sh
python -m http.server 8080 --directory module1-textbook/app
```

For a local API, copy `.env.example` to `.env`, supply a development database URL,
run `node --env-file=.env backend/migrate.mjs`, then `npm run dev:api`.
Set the public API URL in `module1-textbook/app/config.js` to `http://localhost:8787`.
Keep `.env` private. Database credentials never belong in the frontend.

## Accounts and saving

- Usernames: 3–30 ASCII letters, digits or underscores, case-insensitive.
- Passwords: 12–128 characters, stored as salted scrypt hashes. No emails or email verification.
- There is no self-service password recovery. Users should retain their password in a password manager.
- Random bearer sessions expire after seven days. Only token hashes are stored in the database.
  The browser keeps its session in sessionStorage, so closing the tab requires another login.
- Guest progress remains in the original `textbook` localStorage entry. Account progress has
  a separate cache. Import fills missing exercises without replacing existing account answers.
- Edits save locally immediately and sync after a short delay. Failed saves are retained across
  reloads and retried on reconnect or **Account → Sync now**.
- Concurrent changes to the same lesson require an explicit choice in **Account**; other
  lessons save independently. Lesson resets are saved as empty records.
- Exercise scores are for self-study and are calculated in the browser, not certified assessments.

## Deployment

Frontend: `.github/workflows/pages.yml` tests, builds and publishes only
`module1-textbook/app/`. Configure GitHub Pages to use **GitHub Actions**.

Backend: `backend/index.mjs` exports a Neon Functions fetch handler. Run the schema in
`backend/schema.sql` against the dedicated Neon database. Tables are accessed by this
API only; do not expose them through an anonymous Data API role.

Deploy through the Neon CLI after logging in and linking the project:

```sh
neon functions deploy textbook --src backend/index.mjs --env ALLOWED_ORIGINS=https://habibh0.github.io
```

Neon injects `DATABASE_URL`. `ALLOWED_ORIGINS` is a comma-separated list of exact web
origins (no path or trailing slash). Configure the returned function URL in `app/config.js`.
For API-based deployment, `node backend/bundle.mjs` builds `tmp/function/index.mjs`;
zip that file at the archive root and deploy it with runtime `nodejs24`.

Backend changes require a separate Neon deployment. The Pages workflow never publishes
database credentials or deploys database migrations automatically.

See [the authoring guide](module1-textbook/README.md) for the Python generator and lesson sources.
