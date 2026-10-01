import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { PGlite } from '@electric-sql/pglite';
import { createHandler } from '../backend/handler.mjs';

export async function fixture() {
  const db = new PGlite();
  const schema = await readFile(new URL('../backend/schema.sql', import.meta.url), 'utf8');
  await db.exec(schema);
  const pool = { query: (text, values) => db.query(text, values), end: () => db.close() };
  const handler = createHandler(pool, { allowedOrigins: ['https://habibh0.github.io', 'http://localhost:8080'] });
  async function call(path, method = 'GET', body, token, origin = 'https://habibh0.github.io') {
    const response = await handler(new Request('https://api.test' + path, {
      method, headers: { Origin: origin, ...(body ? { 'Content-Type': 'application/json' } : {}), ...(token ? { Authorization: 'Bearer ' + token } : {}) },
      ...(body ? { body: JSON.stringify(body) } : {})
    }));
    return { status: response.status, data: response.status === 204 ? null : await response.json(), headers: response.headers };
  }
  return { pool, call, handler };
}
const password = 'a long test password';

test('accounts hash passwords, isolate users, reject stale writes and revoke sessions', async () => {
  const { call, pool } = await fixture();
  const alice = await call('/signup', 'POST', { username: 'Alice', password });
  assert.equal(alice.status, 201); assert.equal(alice.data.user.username, 'alice');
  const bob = await call('/signup', 'POST', { username: 'bob', password });
  assert.equal(bob.status, 201);
  assert.equal((await call('/signup', 'POST', { username: 'ALICE', password })).status, 409);
  assert.equal((await call('/login', 'POST', { username: 'alice', password: 'wrong test password' })).status, 401);
  assert.equal((await call('/login', 'POST', { username: 'alice', password })).status, 200);
  const rows = (await pool.query('SELECT password_hash FROM textbook_users')).rows;
  assert.ok(rows.every(x => x.password_hash.startsWith('scrypt$') && !x.password_hash.includes(password)));
  const sessionRows = (await pool.query('SELECT token_hash FROM textbook_sessions')).rows;
  assert.ok(sessionRows.every(x => x.token_hash !== alice.data.token));
  assert.equal((await call('/progress')).status, 401);
  const body = { module: 1, lesson: '1', version: 0, items: { A1: { sel: [0], res: 'ok' } } };
  assert.equal((await call('/progress', 'PUT', body, alice.data.token)).data.version, 1);
  assert.deepEqual((await call('/progress', 'GET', null, bob.data.token)).data.lessons, []);
  const stale = await call('/progress', 'PUT', { ...body, items: {} }, alice.data.token);
  assert.equal(stale.status, 409); assert.deepEqual(stale.data.current.items, body.items);
  const reset = await call('/progress', 'PUT', { ...body, version: 1, items: {} }, alice.data.token);
  assert.equal(reset.data.version, 2);
  assert.deepEqual((await call('/progress', 'GET', null, alice.data.token)).data.lessons[0].items, {});
  await call('/logout', 'POST', null, alice.data.token);
  assert.equal((await call('/progress', 'GET', null, alice.data.token)).status, 401);
  await pool.end();
});

test('validation, CORS, expired sessions and login rate limits', async () => {
  const { call, pool } = await fixture();
  assert.equal((await call('/signup', 'POST', { username: 'tiny', password: 'short' })).status, 400);
  assert.equal((await call('/health', 'GET', null, null, 'https://evil.test')).status, 403);
  const preflight = await call('/progress', 'OPTIONS');
  assert.equal(preflight.status, 204); assert.equal(preflight.headers.get('Access-Control-Allow-Origin'), 'https://habibh0.github.io');
  const account = await call('/signup', 'POST', { username: 'testuser', password });
  const token = account.data.token;
  assert.equal((await call('/progress', 'PUT', { module: 1, lesson: '1', version: 0, items: { A: { note: 'x'.repeat(10001) } } }, token)).status, 400);
  assert.equal((await call('/progress', 'PUT', { module: 1, lesson: '1', version: 0, items: { A: { note: 'x'.repeat(140000) } } }, token)).status, 413);
  await pool.query('UPDATE textbook_sessions SET expires_at=$1', [new Date(0)]);
  assert.equal((await call('/me', 'GET', null, token)).status, 401);
  await pool.query('INSERT INTO textbook_rate_limits(bucket,count,expires_at) VALUES($1,$2,$3)', ['auth:blocked', 15, new Date(Date.now() + 900000)]);
  assert.equal((await call('/login', 'POST', { username: 'blocked', password })).status, 429);
  await pool.end();
});
