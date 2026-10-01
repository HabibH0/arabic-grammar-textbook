import pg from 'pg';
import { createHandler } from './handler.mjs';
const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL, max: 5 });
pool.on('error', error => console.error('Database connection failed:', error.code));
export default { fetch: createHandler(pool, { allowedOrigins: (process.env.ALLOWED_ORIGINS || '').split(',').map(x => x.trim()).filter(Boolean) }) };
