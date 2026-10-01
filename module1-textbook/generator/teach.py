import re
from common import inline, text_h, AR
from blocks import SRC, table

EX = re.compile(r'^\*\*([^*]+)\*\*(?:\s+—\s+(.*))?$')


def lesson_md(n):
    s = SRC.split(f'\n## Lesson {n}:', 1)[1]
    s = s.split('\n### Practice', 1)[0]
    return s.split('\n', 1)[1]


def is_arabic_heavy(t):
    letters = re.findall(r'[A-Za-z]', t)
    return len(letters) == 0


def convert(md):
    lines = md.split('\n')
    out, h = [], 0
    i = 0
    paras = []
    # first pass: group into units
    units = []
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1; continue
        if ln.startswith('|'):
            t = []
            while i < len(lines) and lines[i].startswith('|'):
                t.append(lines[i]); i += 1
            rows = [[c.strip() for c in r.strip().strip('|').split('|')] for r in t]
            units.append(('table', rows[0], rows[2:])); continue
        if ln.startswith('### '):
            units.append(('h', ln[4:])); i += 1; continue
        m = re.match(r'(\d+\.|-) (.*)', ln)
        if m:
            typ = 'ol' if m.group(1)[0].isdigit() else 'ul'
            items = []
            while i < len(lines) and re.match(r'(\d+\.|-) ', lines[i]):
                items.append(re.match(r'(?:\d+\.|-) (.*)', lines[i]).group(1)); i += 1
            units.append((typ, items)); continue
        units.append(('p', ln)); i += 1
    # drop reading sentences (they live in Practice)
    clean_units = []
    skip_next = False
    for u in units:
        if skip_next:
            skip_next = False
            if u[0] == 'p' and ' = ' in u[1]:
                continue
        if u[0] == 'p' and u[1].startswith('Read'):
            skip_next = True; continue
        clean_units.append(u)
    # render, boxing worked sections
    html, total, inbox, box = [], 0, False, []
    def emit(x, hh):
        nonlocal total
        (box if inbox else html).append(x); total += hh
    def close_box():
        nonlocal inbox
        if inbox:
            html.append('<div class="worked">' + ''.join(box) + '</div>'); box.clear(); inbox = False
    for u in clean_units:
        if u[0] == 'h':
            close_box()
            if u[1].startswith('Worked'):
                inbox = True; total += 30
            emit(f'<h2 class="sec">{inline(u[1])}</h2>', 54)
        elif u[0] == 'table':
            x, hh = table(u[1], u[2]); emit(x, hh)
        elif u[0] in ('ol', 'ul'):
            items = ''.join(f'<li>{inline(t)}</li>' for t in u[1])
            emit(f'<{u[0]} class="tight">{items}</{u[0]}>', sum(text_h(t, cpl=82) + 6 for t in u[1]) + 10)
        else:
            m = EX.match(u[1])
            if m and is_arabic_heavy(m.group(1)):
                gl = f' <span class="gl">{inline(m.group(2))}</span>' if m.group(2) else ''
                emit(f'<div class="exm"><b>{inline(m.group(1))}</b>{gl}</div>', 46)
            else:
                emit(f'<p>{inline(u[1])}</p>', text_h(u[1]) + 9)
    close_box()
    return '\n'.join(html), total
