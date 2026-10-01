import re
from common import inline, text_h, SOURCE_DIR

SRC = open(SOURCE_DIR + '/Module 01 - Words and Sentences.md', encoding='utf-8').read()


def lesson_tables():
    secs = re.split(r'\n## ', SRC)
    out = {}
    for s in secs:
        m = re.match(r'Lesson (\d+)', s)
        if not m:
            continue
        tabs, cur = [], []
        for line in s.split('\n'):
            if line.startswith('|'):
                cur.append(line)
            elif cur:
                tabs.append(cur); cur = []
        if cur:
            tabs.append(cur)
        parsed = []
        for t in tabs:
            rows = [[c.strip() for c in r.strip().strip('|').split('|')] for r in t]
            parsed.append((rows[0], [r for r in rows[2:]]))
        out[int(m.group(1))] = parsed
    return out


TABLES = lesson_tables()


def table(headers, rows, cls=''):
    h = ''.join(f'<th>{inline(x)}</th>' for x in headers)
    b = ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>', 26 + sum(
        max(34, max(text_h(c, cpl=max(10, 70 // len(r)), lh=23) for c in r) + 12) for r in rows) + 12


def lines(n):
    return f'<div class="lines" style="height:{n*26}px"></div>', n * 32 + 4


def part(p):
    k = p[0]
    if k == 'L':
        return lines(p[1])
    if k == 'lab':
        return (f'<div class="lab"><div class="l">{inline(p[1])}</div>'
                f'<div class="lines" style="height:{p[2]*32}px"></div></div>'), p[2] * 32 + 4
    if k == 'disp':
        return f'<div class="disp">{inline(p[1])}</div>', 50
    if k == 'pills':
        return '<div class="pills">' + ''.join(f'<span class="pill">{inline(o)}</span>' for o in p[1]) + '</div>', 42
    if k == 'crows':
        rows = ''.join('<tr><td>' + inline(it) + '</td><td><div class="pills" style="justify-content:center;margin:0">' +
                       ''.join(f'<span class="pill">{inline(o)}</span>' for o in opts) + '</div></td></tr>'
                       for it, opts in p[1])
        return f'<table><tbody>{rows}</tbody></table>', 44 * len(p[1]) + 10
    if k == 'fill':
        headers, rows, h = p[1], p[2], p[3]
        hh = ''.join(f'<th>{inline(x)}</th>' for x in headers)
        body = ''
        for r in rows:
            body += '<tr>' + ''.join(
                (f'<td class="w" style="height:{h}px"></td>' if c is None else f'<td>{inline(c)}</td>') for c in r) + '</tr>'
        return f'<table><thead><tr>{hh}</tr></thead><tbody>{body}</tbody></table>', 28 + len(rows) * (h + 14) + 10
    if k == 'match':
        terms, opts = p[1], p[2]
        letters = 'abcdefgh'
        left = ''.join(f'<tr><td>{inline(t)}</td><td class="w" style="width:44px"></td></tr>' for t in terms)
        right = ''.join(f'<tr><td style="width:28px"><b>{letters[i]}</b></td><td style="text-align:left">{inline(o)}</td></tr>'
                        for i, o in enumerate(opts))
        return (f'<div class="opts"><table><thead><tr><th>Term</th><th>Letter</th></tr></thead><tbody>{left}</tbody></table>'
                f'<table class="mt"><thead><tr><th></th><th>Meaning</th></tr></thead><tbody>{right}</tbody></table></div>'), 30 + 38 * max(len(terms), len(opts)) + 10
    if k == 'grid':
        n = p[1]
        body = ''.join('<tr><td class="w" style="height:34px;width:22%"></td><td class="w" style="width:42%"></td><td class="w"></td></tr>' for _ in range(n))
        return ('<table><thead><tr><th>Word</th><th>Analysis</th><th>Relationship or ending</th></tr></thead>'
                f'<tbody>{body}</tbody></table>'), 30 + n * 40 + 10
    raise ValueError(k)


def block(b, lesson=None):
    k = b[0]
    if k == 'p':
        return f'<p>{inline(b[1])}</p>', text_h(b[1]) + 6
    if k == 'h2':
        return f'<h2>{inline(b[1])}</h2>', 52
    if k == 'h3':
        return f'<h3>{inline(b[1])}</h3>', 36
    if k == 't':
        hd, rows = TABLES[lesson][b[1]]
        return table(hd, rows)
    if k == 'tab':
        return table(b[1], b[2])
    if k in ('ul', 'ol'):
        items = ''.join(f'<li>{inline(i)}</li>' for i in b[1])
        return f'<{k} class="tight">{items}</{k}>', sum(text_h(i, cpl=92) + 2 for i in b[1]) + 8
    if k == 'ref':
        inner, h = render(b[1], lesson)
        return f'<div class="ref">{inner}</div>', h + 34
    if k == 'set':
        return f'<div class="set"><span class="tag">{b[1]}</span><span>{inline(b[2])}</span></div>', 44
    if k == 'ex':
        n, t, parts = b[1], b[2], b[3]
        ph = [part(p) for p in parts]
        body = (f'<div>{inline(t)}</div>' if t else '') + ''.join(x for x, _ in ph)
        return (f'<div class="ex"><div class="n">{n}</div><div>{body}</div></div>',
                (text_h(t, cpl=94) if t else 0) + sum(h for _, h in ph) + 16)
    if k == 'raw':
        return b[1], b[2]
    raise ValueError(k)


def render(blocks, lesson=None):
    out, h = [], 0
    for b in blocks:
        x, hh = block(b, lesson)
        out.append(x); h += hh
    return '\n'.join(out), h
