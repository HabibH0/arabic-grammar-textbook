"""Builds the interactive textbook: app/index.html (the shell, with the module contents built in)
and one data file per module in app/modules/ (loaded only when that module is opened).

Run from inside generator/:  python build_book.py
"""
import json, os, re, hashlib
import common
import book

BOOK_TITLE = 'Arabic Grammar'
OUT = '../app'


def plain(h):
    return re.sub(r'<[^>]+>', '', h)


def main():
    mods = book.find_modules(common.SOURCE_DIR)
    os.makedirs(OUT + '/modules', exist_ok=True)
    report, manifest = [], []
    for n, paths in mods.items():
        if n == 1:
            common.USE_TERMS = True
            import build_app            # Module 1: hand-authored interactive items
            data = build_app.MODULE
        else:
            common.USE_TERMS = 'book'
            data = book.build_module(n, paths['lessons'], paths['answers'], report)
        fname = f'modules/m{n:02d}.js'
        js = '(window.BOOK_MODULES = window.BOOK_MODULES || {})[%d] = %s;\n' % (n, json.dumps(data, ensure_ascii=False))
        open(f'{OUT}/{fname}', 'w', encoding='utf-8').write(js)
        version = hashlib.md5(js.encode('utf-8')).hexdigest()[:8]   # changes whenever the module changes, so browsers reload it
        manifest.append(dict(
            n=n, title=data['title'], ar=data['ar'], file=f'{fname}?v={version}',
            interactive=(n == 1 or book.load_items(n) is not None),
            lessons=[dict(key=l['key'], short=l['short'], title=l['title'], count=len(l['items'])) for l in data['lessons']],
            total=sum(len(l['items']) for l in data['lessons'])))
        print(f"Module {n}: {len(data['lessons'])} lessons, {manifest[-1]['total']} exercises -> app/{fname} ({len(js.encode()) // 1024} KB)")

    shell = open(OUT + '/template.html', encoding='utf-8').read()
    book_json = json.dumps(dict(title=BOOK_TITLE, modules=manifest), ensure_ascii=False).replace('</', '<\\/')
    shell = shell.replace('__BOOK__', book_json)
    head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n</head>\n<body>\n')
    open(OUT + '/index.html', 'w', encoding='utf-8').write(head + shell + '\n</body>\n</html>\n')
    old = OUT + '/data.json'
    if os.path.exists(old):
        os.remove(old)              # superseded by modules/m01.js
    print('wrote app/index.html')
    if report:
        print('\nCheck these:')
        for r in report:
            print('  -', r)


main()
