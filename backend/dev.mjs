import http from 'node:http';
import { Readable } from 'node:stream';
import app from './index.mjs';
http.createServer(async (req, res) => {
  try {
    const request = new Request('http://localhost' + req.url, {
      method: req.method, headers: req.headers,
      ...(req.method !== 'GET' && req.method !== 'HEAD' ? { body: Readable.toWeb(req), duplex: 'half' } : {})
    });
    const response = await app.fetch(request);
    res.writeHead(response.status, Object.fromEntries(response.headers));
    res.end(Buffer.from(await response.arrayBuffer()));
  } catch { res.writeHead(500); res.end(); }
}).listen(Number(process.env.PORT || 8787), '127.0.0.1', () => console.log('Textbook API ready on localhost.'));
