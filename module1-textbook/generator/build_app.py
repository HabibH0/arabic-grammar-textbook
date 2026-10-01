import re, json, random, hashlib
from common import inline, SOURCE_DIR
from app_items import ITEMS
from lessons import L

ANS = open(SOURCE_DIR + '/Module 01 - Answers and Worked Solutions.md', encoding='utf-8').read()


def md_html(md):
    out, lst = [], None
    for raw in md.strip().split('\n'):
        line = raw.rstrip()
        if not line.strip():
            continue
        m = re.match(r'( *)(\d+\.|-) (.*)', line)
        if m:
            typ = 'ol' if m.group(2)[0].isdigit() else 'ul'
            if lst != typ:
                if lst: out.append(f'</{lst}>')
                out.append(f'<{typ}>'); lst = typ
            out.append(f'<li>{inline(m.group(3))}</li>')
        else:
            if lst: out.append(f'</{lst}>'); lst = None
            if line.startswith('#'):
                out.append(f'<p><b>{inline(line.lstrip("# "))}</b></p>')
            else:
                out.append(f'<p>{inline(line)}</p>')
    if lst: out.append(f'</{lst}>')
    return ''.join(out)


# ---- solutions by key ----
SOL = {}
body = ANS.split('\n## Module review', 1)
for sec in re.split(r'\n## Lesson ', body[0])[1:]:
    for sub in re.split(r'\n### ', sec)[1:]:
        key, txt = sub.split('\n', 1)
        key = key.strip()
        items = re.split(r'\n(?=\d+\. )', '\n' + txt.strip())
        nums = [i for i in items if re.match(r'\d+\. ', i)]
        if nums and not txt.strip().startswith(('**', 'The')) and len(nums) >= 2:
            pre = [i for i in items if not re.match(r'\d+\. ', i) and i.strip()]
            for it in nums:
                n = int(it.split('.', 1)[0])
                # keep nested bullets that follow
                SOL[f'{key}-{n}'] = md_html(re.sub(r'^\d+\. ', '', it.strip()).replace('\n   - ', '\n- '))
            if pre:
                SOL[key] = md_html('\n'.join(pre))
        else:
            SOL[key] = md_html(txt)
rev = body[1]
marks = [(m.start(), m.group(1)) for m in re.finditer(r'(?:\*\*|### )([A-E]\d)\.', rev)]
for i, (pos, key) in enumerate(marks):
    end = marks[i + 1][0] if i + 1 < len(marks) else rev.find('## Use errors')
    chunk = rev[pos:end]
    chunk = re.sub(r'^(?:### )?\*?\*?[A-E]\d\.\*?\*?\s*', '', chunk)
    chunk = re.sub(r'\n### [A-E]\. .*', '', chunk)
    first, _, rest = chunk.partition('\n')
    if first.count('**') % 2:
        first = first[::-1].replace('**', '', 1)[::-1]
    chunk = first + '\n' + rest
    SOL[key] = md_html(chunk)
REVISIT = md_html(rev[rev.find('## Use errors'):].split('\n', 1)[1])


def sol_key(it):
    if it.get('sol'):
        return it['sol']
    return it['id']


def rng(seed):
    return random.Random(int(hashlib.md5(seed.encode()).hexdigest(), 16))


def build_item(it):
    r = rng(it['id'])
    key = sol_key(it)
    s = SOL.get(key)
    assert s, ('missing solution', it['id'], key)
    d = dict(id=it['id'], type=it['type'], prompt=inline(it['prompt']), sol=s)
    if it['type'] == 'mcq':
        opts = it['opts'][:]
        if not (len(opts) == 2 and opts[0].startswith('(a)')):
            r.shuffle(opts)
        d['opts'] = [inline(o) for o in opts]
        d['ans'] = opts.index(it['ans'])
    else:
        d['cols'] = [inline(c) for c in it['cols']]
        shuffled = {}
        rows = []
        for lab, cells in it['rows']:
            row = []
            for c in cells:
                if c is None:
                    row.append(None); continue
                opts, ans = c
                k = tuple(opts)
                if k not in shuffled:
                    o = list(opts)
                    if not (o == END or o == ENDA_ or o == ['Yes', 'No']):
                        r.shuffle(o)
                    shuffled[k] = o
                o = shuffled[k]
                row.append(dict(opts=[inline(x) for x in o], ans=o.index(ans)))
            rows.append(dict(label=inline(lab), cells=row))
        d['rows'] = rows
    return d


from app_items import END, ENDA as ENDA_
from common import clean
import teach
from blocks import SRC


def anchor(html, key):
    secs = []
    def rep(m):
        n = len(secs) + 1
        secs.append(dict(id=f'L{key}-s{n}', title=m.group(1)))
        return f'<h2 class="sec" id="L{key}-s{n}">{m.group(1)}</h2>'
    html = re.sub(r'<h2 class="sec">(.*?)</h2>', rep, html)
    return html, secs


lessons = []
intro_md = SRC.split('## Before you begin', 1)[1].split('\n## Lesson 1', 1)[0]
ih, isecs = anchor('<h2 class="sec">Before you begin</h2>' + teach.convert(intro_md)[0], '0')
lessons.append(dict(key='0', title='Introduction', plain='Introduction', html=ih, secs=isecs, items=[]))
rev_md = SRC.split('## Module review: apply the whole method', 1)[1]
rev_intro = rev_md.split('\n### ', 1)[0]
ready = rev_md.split('### Ready to continue?', 1)[1]
for k in [str(i) for i in range(1, 10)] + ['R']:
    title = clean(L[int(k)]['title']) if k != 'R' else 'Module review: apply the whole method'
    if k == 'R':
        html, secs = teach.convert(rev_intro)[0], []
    else:
        html, secs = anchor(teach.convert(teach.lesson_md(int(k)))[0], k)
    lessons.append(dict(key=k, title=inline(title), plain=title, html=html, secs=secs,
                        items=[build_item(i) for i in ITEMS[k]]))
lessons[-1]['after'] = '<h2 class="sec">Ready to continue?</h2>' + teach.convert(ready)[0]
SETNAMES = {'G': 'Guided', 'I': 'Independent', 'R': 'Cumulative review'}
REVSETS = {'A': 'A|Distinctions', 'B': 'B|Endings, relationships, and corrections', 'C': 'C|Connected reading and full تركيب',
           'D': 'D|Read Arabic grammatical explanations', 'E': 'E|Final transfer task'}


def group_of(k, i):
    if k == 'R':
        return REVSETS.get(i[0], '')
    if i.endswith('-Read'):
        return '|Reading'
    m = re.match(r'(\d+)([GIR])', i)
    if not m:
        return ''
    return m.group(1) + m.group(2) + '|' + ('Brief review' if m.group(2) == 'R' and m.group(1) == '1' else SETNAMES[m.group(2)])


for l in lessons:
    l['short'] = 'Introduction' if l['key'] == '0' else 'Module review' if l['key'] == 'R' else 'Lesson ' + l['key']
    for it in l['items']:
        it['group'] = group_of(l['key'], it['id'])
lessons[0]['title'] = 'Introduction'
MODULE = dict(n=1, title='Words and Sentences', ar='الكَلِمَةُ وَالجُمْلَةُ', lessons=lessons, revisit=REVISIT)

if __name__ == '__main__':
    import build_book  # builds every module, including this one
