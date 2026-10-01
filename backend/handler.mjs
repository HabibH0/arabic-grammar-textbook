import { randomBytes, randomUUID } from 'node:crypto';
import { credentials, digest, hashPassword, verifyPassword, progressInput } from './security.mjs';

const MAX_BODY = 128 * 1024;
class HttpError extends Error {
  constructor(status, message) { super(message); this.status = status; }
}
async function readBody(request) {
  if (!request.headers.get('content-type')?.startsWith('application/json')) throw new HttpError(415, 'Send JSON.');
  const reader = request.body?.getReader();
  if (!reader) throw new HttpError(400, 'Missing request body.');
  let length = 0; const chunks = [];
  while (true) {
    const { done, value } = await reader.read(); if (done) break;
    length += value.length;
    if (length > MAX_BODY) { await reader.cancel(); throw new HttpError(413, 'Progress is too large.'); }
    chunks.push(value);
  }
  try {
    const result = JSON.parse(Buffer.concat(chunks).toString('utf8'));
    if (!result || typeof result !== 'object' || Array.isArray(result)) throw new Error();
    return result;
  } catch { throw new HttpError(400, 'Invalid JSON.'); }
}

export function createHandler(pool, { allowedOrigins = [] } = {}) {
  const query = (text, values = []) => pool.query(text, values);
  // Same expensive password derivation for unknown users; no timing shortcut.
  let dummyHash;
  async function limit(bucket, maximum) {
    const now = new Date(), until = new Date(now.getTime() + 15 * 60 * 1000);
    const { rows } = await query(`INSERT INTO textbook_rate_limits(bucket,count,expires_at) VALUES($1,1,$2)
      ON CONFLICT(bucket) DO UPDATE SET
        count = CASE WHEN textbook_rate_limits.expires_at <= $3 THEN 1 ELSE textbook_rate_limits.count + 1 END,
        expires_at = CASE WHEN textbook_rate_limits.expires_at <= $3 THEN $2 ELSE textbook_rate_limits.expires_at END
      RETURNING count`, [bucket, until, now]);
    if (rows[0].count > maximum) throw new HttpError(429, 'Too many attempts. Try again in 15 minutes.');
  }
  async function session(request) {
    const token = request.headers.get('authorization')?.match(/^Bearer ([a-f0-9]{64})$/)?.[1];
    if (!token) throw new HttpError(401, 'Please log in again.');
    const { rows } = await query(`SELECT u.id, u.username FROM textbook_sessions s
      JOIN textbook_users u ON u.id=s.user_id WHERE s.token_hash=$1 AND s.expires_at > $2`, [digest(token), new Date()]);
    if (!rows[0]) throw new HttpError(401, 'Please log in again.');
    return { user: rows[0], token };
  }
  return async request => {
    const origin = request.headers.get('origin');
    const headers = { 'Content-Type': 'application/json', 'Cache-Control': 'no-store', 'Vary': 'Origin', 'X-Content-Type-Options': 'nosniff' };
    const respond = (body, status = 200) => new Response(JSON.stringify(body), { status, headers });
    if (origin && !allowedOrigins.includes(origin)) return respond({ error: 'Origin not allowed.' }, 403);
    if (origin) headers['Access-Control-Allow-Origin'] = origin;
    if (request.method === 'OPTIONS') {
      headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS';
      headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type';
      return new Response(null, { status: 204, headers });
    }
    try {
      const path = new URL(request.url).pathname.replace(/\/$/, '') || '/';
      if (path === '/health' && request.method === 'GET') return respond({ ok: true });
      if (['/signup', '/login'].includes(path) && request.method === 'POST') {
        const body = await readBody(request);
        let input; try { input = credentials(body); } catch (e) { throw new HttpError(400, e.message); }
        await limit('auth:global', 300);
        await limit('auth:' + input.username, 15);
        let user;
        if (path === '/signup') {
          await limit('signup:global', 30);
          const passwordHash = await hashPassword(input.password);
          const { rows } = await query(`INSERT INTO textbook_users(id,username,password_hash) VALUES($1,$2,$3)
            ON CONFLICT(username) DO NOTHING RETURNING id,username`, [randomUUID(), input.username, passwordHash]);
          if (!rows[0]) throw new HttpError(409, 'That username is unavailable.');
          user = rows[0];
        } else {
          const { rows } = await query('SELECT id,username,password_hash FROM textbook_users WHERE username=$1', [input.username]);
          dummyHash ||= hashPassword(randomBytes(32).toString('hex'));
          const valid = await verifyPassword(input.password, rows[0]?.password_hash || await dummyHash);
          if (!valid || !rows[0]) throw new HttpError(401, 'Incorrect username or password.');
          user = { id: rows[0].id, username: rows[0].username };
        }
        const token = randomBytes(32).toString('hex');
        const expires = new Date(Date.now() + 7 * 86400000);
        await query('DELETE FROM textbook_sessions WHERE expires_at <= $1', [new Date()]);
        await query('DELETE FROM textbook_rate_limits WHERE expires_at <= $1', [new Date()]);
        await query('INSERT INTO textbook_sessions(token_hash,user_id,expires_at) VALUES($1,$2,$3)', [digest(token), user.id, expires]);
        return respond({ user, token, expiresAt: expires.toISOString() }, path === '/signup' ? 201 : 200);
      }
      const { user, token } = await session(request);
      if (path === '/me' && request.method === 'GET') return respond({ user });
      if (path === '/logout' && request.method === 'POST') {
        await query('DELETE FROM textbook_sessions WHERE token_hash=$1', [digest(token)]);
        return respond({ ok: true });
      }
      if (path === '/progress' && request.method === 'GET') {
        const { rows } = await query('SELECT module,lesson,items,version FROM textbook_progress WHERE user_id=$1', [user.id]);
        return respond({ lessons: rows });
      }
      if (path === '/progress' && request.method === 'PUT') {
        let b; try { b = progressInput(await readBody(request)); } catch (e) { throw new HttpError(e.status || 400, e.message); }
        await limit('save:' + user.id, 1500);
        const values = [user.id, b.module, b.lesson, JSON.stringify(b.items)];
        const result = b.version === 0
          ? await query(`INSERT INTO textbook_progress(user_id,module,lesson,items) VALUES($1,$2,$3,$4)
              ON CONFLICT(user_id,module,lesson) DO NOTHING RETURNING version`, values)
          : await query(`UPDATE textbook_progress SET items=$4,version=version+1,updated_at=now()
              WHERE user_id=$1 AND module=$2 AND lesson=$3 AND version=$5 RETURNING version`, [...values, b.version]);
        if (!result.rows[0]) {
          const { rows } = await query('SELECT items,version FROM textbook_progress WHERE user_id=$1 AND module=$2 AND lesson=$3', values.slice(0, 3));
          return respond({ error: 'This lesson changed on another device.', current: rows[0] || { items: {}, version: 0 } }, 409);
        }
        return respond({ version: result.rows[0].version });
      }
      return respond({ error: 'Not found.' }, 404);
    } catch (error) {
      if (!error.status) console.error('Textbook API request failed:', error.code || error.name);
      if (error.status === 429) headers['Retry-After'] = '900';
      return respond({ error: error.status ? error.message : 'Could not save right now. Please retry.' }, error.status || 500);
    }
  };
}
