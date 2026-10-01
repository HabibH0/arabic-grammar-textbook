import { randomBytes, scrypt as scryptCallback, timingSafeEqual, createHash } from 'node:crypto';
import { promisify } from 'node:util';
const scrypt = promisify(scryptCallback);
const options = { N: 32768, r: 8, p: 3, maxmem: 64 * 1024 * 1024 };
export const digest = value => createHash('sha256').update(value).digest('hex');
export async function hashPassword(password) {
  const salt = randomBytes(16).toString('hex');
  const hash = await scrypt(password, salt, 64, options);
  return `scrypt$${salt}$${hash.toString('hex')}`;
}
export async function verifyPassword(password, encoded) {
  const [, salt, hash] = encoded.split('$');
  const actual = await scrypt(password, salt, 64, options);
  const expected = Buffer.from(hash, 'hex');
  return actual.length === expected.length && timingSafeEqual(actual, expected);
}
export function credentials(body) {
  const username = typeof body.username === 'string' ? body.username.trim().toLowerCase() : '';
  if (!/^[a-z0-9_]{3,30}$/.test(username)) throw new Error('Use 3–30 letters, numbers or underscores for your username.');
  if (typeof body.password !== 'string' || body.password.length < 12 || body.password.length > 128)
    throw new Error('Use a password with 12–128 characters.');
  return { username, password: body.password };
}
export function progressInput(body) {
  if (!Number.isInteger(body.module) || body.module < 1 || body.module > 999 ||
      typeof body.lesson !== 'string' || !/^(?:\d{1,3}|R)$/.test(body.lesson) ||
      !Number.isInteger(body.version) || body.version < 0 || body.version > 2147483646)
    throw new Error('Invalid lesson or version.');
  const items = body.items;
  if (!items || typeof items !== 'object' || Array.isArray(items) || Object.keys(items).length > 500)
    throw new Error('Invalid progress.');
  for (const [id, value] of Object.entries(items)) {
    if (!/^[a-zA-Z0-9_-]{1,80}$/.test(id) || ['__proto__', 'constructor', 'prototype'].includes(id) ||
        !value || typeof value !== 'object' || Array.isArray(value)) throw new Error('Invalid exercise.');
    if (Object.keys(value).some(k => !['sel', 'res', 'open', 'note'].includes(k))) throw new Error('Invalid exercise fields.');
    if (value.res != null && !['ok', 'bad'].includes(value.res)) throw new Error('Invalid result.');
    if (value.open !== undefined && typeof value.open !== 'boolean') throw new Error('Invalid reveal state.');
    if (value.note !== undefined && (typeof value.note !== 'string' || value.note.length > 10000)) throw new Error('Answer is too long.');
    if (value.sel != null && (!Array.isArray(value.sel) || value.sel.length > 300 ||
        value.sel.some(v => v !== null && (!Number.isInteger(v) || v < 0 || v > 1000)))) throw new Error('Invalid choices.');
  }
  return body;
}
