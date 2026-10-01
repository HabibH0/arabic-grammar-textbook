import { build } from 'esbuild';
await build({
  entryPoints: ['backend/index.mjs'], bundle: true, platform: 'node', target: 'node24', format: 'esm',
  outfile: 'tmp/function/index.mjs',
  banner: { js: "import{createRequire as __cr}from'node:module';import{fileURLToPath as __f}from'node:url';import{dirname as __d}from'node:path';const require=__cr(import.meta.url);const __filename=__f(import.meta.url);const __dirname=__d(__filename);" }
});
