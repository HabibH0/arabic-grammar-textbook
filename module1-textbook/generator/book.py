"""Generic builder for modules written in the standard lesson/answers markdown format (Modules 2 onwards).

Module 1 keeps its own pipeline (build_app.py) because its exercises were re-authored by hand as
interactive multiple-choice items. Every other module is read straight from its two markdown files:
lesson text is converted to HTML, and each practice task becomes an open exercise whose worked solution
comes from the answers file.
"""
import re, html, glob, os
import common
from common import inline, AR

SET_NAMES = {'G': 'Guided', 'I': 'Independent', 'R': 'Review'}
# **1G — Guided**   **1G — Guided.** text   **1R — Cumulative review:** text   **1G**   **1R:** text
SET = re.compile(r'^\*\*(\d+[GIR])(?:\s*[—–]\s*([^*]+?))?[.:]?\*\*[.:]?\s*(.*)$')
NUM = re.compile(r'^(\d+)\.\s+(.*)$')
REVQ = re.compile(r'^(?:####\s+([A-E]\d)\b.*|\*\*([A-E]\d)\b\.?\s*(.*?)\*\*[.:]?\s*(.*))$')
PASSAGE = re.compile(r'^\*\*[A-Za-z][^*]{0,40}\*\*$')    # **Passage 2**
EXM = re.compile(r'^\*\*([^*]+)\*\*(?:\s+[—–]\s+(.*))?$')


def arabic_heavy(t):
    return not re.search(r'[A-Za-z]', t) and re.search('[' + AR + ']', t)


# ---------------------------------------------------------------- markdown → HTML

def table_html(rows):
    cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
    head, body = cells[0], [r for r in cells[1:] if not re.match(r'^:?-+:?$', r[0] or '-')]
    h = ''.join(f'<th>{inline(x)}</th>' for x in head)
    b = ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in body)
    return f'<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


def md_block(md):
    """Small markdown renderer for prompts and solutions: paragraphs, nested lists, tables, sub-headings."""
    lines = md.strip('\n').split('\n')
    out, stack, i = [], [], 0     # stack of (indent, tag)

    def close_to(indent):
        while stack and stack[-1][0] >= indent:
            out.append(f'</li></{stack.pop()[1]}>')

    while i < len(lines):
        raw = lines[i].rstrip()
        if not raw.strip():
            i += 1; continue
        if raw.lstrip().startswith('|'):
            close_to(0)
            t = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                t.append(lines[i].strip()); i += 1
            out.append(table_html(t)); continue
        ind = len(raw) - len(raw.lstrip())
        s = raw.strip()
        m = re.match(r'(\d+\.|[-*]) (.*)', s)
        if m:
            tag = 'ol' if m.group(1)[0].isdigit() else 'ul'
            if stack and stack[-1][0] == ind and stack[-1][1] == tag:
                out.append(f'</li><li>{inline(m.group(2))}')
            elif stack and stack[-1][0] >= ind:
                close_to(ind + 1)
                if stack and stack[-1][0] == ind:
                    out.append(f'</li></{stack.pop()[1]}>')
                stack.append((ind, tag)); out.append(f'<{tag}><li>{inline(m.group(2))}')
            else:
                stack.append((ind, tag)); out.append(f'<{tag}><li>{inline(m.group(2))}')
            i += 1; continue
        if stack and ind > 0:            # continuation of a list item
            out.append(f'<br>{inline(s)}'); i += 1; continue
        close_to(0)
        if s.startswith('#'):
            out.append(f'<p class="sub"><b>{inline(s.lstrip("# "))}</b></p>')
        else:
            out.append(f'<p>{inline(s)}</p>')
        i += 1
    close_to(0)
    return ''.join(out)


def teach_html(md, reading_cb=None):
    """Lesson text: ### headings become anchored sections, 'Worked …' sections are boxed,
    bold Arabic example lines become example blocks, and 'Read:' tasks are handed to reading_cb
    (which returns True if it turned the task into an exercise) or shown as a reading box."""
    paras, cur = [], []
    for ln in md.split('\n'):
        if not ln.strip():
            if cur: paras.append(cur); cur = []
        elif ln.startswith('### ') or (ln.startswith('|') and cur and not cur[-1].startswith('|')) \
                or (cur and cur[-1].startswith('|') and not ln.startswith('|')):
            if cur: paras.append(cur)
            cur = [ln]
            if ln.startswith('### '): paras.append(cur); cur = []
        else:
            cur.append(ln)
    if cur: paras.append(cur)

    out, box, inbox = [], [], False
    def emit(x): (box if inbox else out).append(x)
    def close():
        nonlocal inbox
        if inbox:
            out.append('<div class="worked">' + ''.join(box) + '</div>'); box.clear(); inbox = False

    i = 0
    while i < len(paras):
        p = paras[i]; first = p[0]
        if first.startswith('### '):
            close()
            title = first[4:].strip()
            if re.match(r'Worked\b', title):
                inbox = True
            emit(f'<h2 class="sec">{inline(title)}</h2>')
        elif first.startswith('|'):
            emit(table_html(p))
        elif re.match(r'(\d+\.|-) ', first):
            emit(md_block('\n'.join(p)))
        elif re.match(r'Read\b[^:]*:', first) and len(p) == 1:     # "Read: …", "Read without a gloss: …"
            task = [first]
            if i + 1 < len(paras):
                nxt = paras[i + 1][0]
                if not nxt.startswith(('### ', '|')) and (' = ' in nxt or nxt.startswith(('**', 'Vocabulary'))):
                    task.append(nxt); i += 1
            if not (reading_cb and reading_cb(task)):
                emit('<div class="readbox">' + ''.join(f'<p>{inline(t)}</p>' for t in task) + '</div>')
        else:
            for ln in p:
                m = EXM.match(ln)
                if m and arabic_heavy(m.group(1)):
                    gl = f' <span class="gl">{inline(m.group(2))}</span>' if m.group(2) else ''
                    emit(f'<div class="exm"><b>{inline(m.group(1))}</b>{gl}</div>')
                else:
                    emit(f'<p>{inline(ln)}</p>')
        i += 1
    close()
    return ''.join(out)


def anchor(h, key):
    secs = []
    def rep(m):
        n = len(secs) + 1
        secs.append(dict(id=f'L{key}-s{n}', title=m.group(1)))
        return f'<h2 class="sec" id="L{key}-s{n}">{m.group(1)}</h2>'
    return re.sub(r'<h2 class="sec">(.*?)</h2>', rep, h), secs


def h2_sections(md):
    parts = re.split(r'\n(?=## )', '\n' + md)
    head = parts[0]
    return head, [(p.split('\n', 1)[0][3:].strip(), p.split('\n', 1)[1] if '\n' in p else '') for p in parts[1:]]


def rev_first(q):
    head, rest = (q.group(3) or '').strip(), (q.group(4) or '').strip()
    return ((f'**{head}** ' if head else '') + rest).strip()


# ---------------------------------------------------------------- answers

def parse_answers(md):
    sol, rev, revisit = {}, {}, ''
    _, secs = h2_sections(md)
    lesson_secs = [(t, b) for t, b in secs if re.match(r'Lesson \d+', t)]
    for t, body in lesson_secs:
        k = re.match(r'Lesson (\d+)', t).group(1)
        blocks, cur_key, cur = [], None, []
        for ln in body.split('\n'):
            m = re.match(r'^###\s+(\d+[A-Z])\s*$', ln) or re.match(r'^\*\*(\d+[A-Z])\.?\*\*[.:]?\s*(.*)$', ln)
            r = re.match(r'^\*\*Arabic reading[.:]?\*\*[.:]?\s*(.*)$', ln)
            if m or r:
                if cur_key: blocks.append((cur_key, cur))
                if r:
                    cur_key, cur = f'{k}-Read', [r.group(1)]
                else:
                    cur_key = m.group(1)
                    cur = [m.group(2)] if m.lastindex and m.lastindex >= 2 and m.group(2) else []
            elif cur_key:
                cur.append(ln)
        if cur_key: blocks.append((cur_key, cur))
        for key, lines in blocks:
            txt = '\n'.join(lines).strip('\n')
            sol[key] = md_block(txt)
            items, notes, n = {}, [], None
            for ln in lines:
                mm = NUM.match(ln)
                if mm:
                    n = int(mm.group(1)); items[n] = [mm.group(2)]
                elif n is not None and (ln.startswith((' ', '\t')) or not ln.strip()):
                    items[n].append(ln)
                elif ln.strip():
                    notes.append(ln); n = None
            if len(items) >= 2:
                note = md_block('\n'.join(notes)) if notes else ''
                for n, ls in items.items():
                    sol[f'{key}-{n}'] = md_block('\n'.join(ls)) + (f'<div class="solnote">{note}</div>' if note else '')
    tail = [(t, b) for t, b in secs if not re.match(r'Lesson \d+', t)]
    for t, body in tail:
        if t.startswith(('Use errors', 'Choose what to revisit')):
            revisit = md_block(body); continue
        for sub in re.split(r'\n(?=### )', '\n' + body):
            m = re.match(r'\n?### ([A-E])\.?\s', sub)
            if not m: continue
            letter = m.group(1); content = sub.split('\n', 2)[-1] if sub.startswith('\n') else sub.split('\n', 1)[-1]
            rev[letter] = md_block(content)
            if not any(REVQ.match(ln) for ln in content.split('\n')):     # plain numbered list: A-1, A-2, …
                items, n = {}, None
                for ln in content.split('\n'):
                    mm = NUM.match(ln)
                    if mm:
                        n = int(mm.group(1)); items[n] = [mm.group(2)]
                    elif n is not None and (ln.startswith((' ', '\t')) or not ln.strip()):
                        items[n].append(ln)
                    elif ln.strip():
                        n = None
                if len(items) >= 2:
                    for n, ls in items.items():
                        rev[f'{letter}-{n}'] = md_block('\n'.join(ls))
            cur_key, cur = None, []
            def flush():
                if cur_key: rev[cur_key] = md_block('\n'.join(cur))
            for ln in content.split('\n'):
                part = re.match(r'^\*\*([A-E]\d)\.(\d+)\b', ln)     # **E1.2 — …** is part 2 of E1
                if part:
                    flush()
                    cur_key, cur = f'{part.group(1)}-{part.group(2)}', [ln]
                    continue
                q = REVQ.match(ln)
                if q:
                    flush()
                    cur_key = q.group(1) or q.group(2)
                    cur = [rev_first(q)]
                elif cur_key:
                    cur.append(ln)
            flush()
    return sol, rev, revisit


# ---------------------------------------------------------------- lessons

def parse_practice(md, k):
    """Returns [(group, note, [(id, prompt_md)])]."""
    sets, cur = [], None
    for ln in md.split('\n'):
        m = SET.match(ln)
        if m:
            code = m.group(1)
            label = (m.group(2) or SET_NAMES[code[-1]]).strip().rstrip('.:')
            cur = dict(code=code, label=label, text=[m.group(3)] if m.group(3) else [], items=[])
            sets.append(cur); continue
        if cur is None or not ln.strip():
            if cur and cur['items']: cur['items'][-1][1].append('')
            continue
        n = NUM.match(ln)
        if n and not ln.startswith(' '):
            cur['items'].append((int(n.group(1)), [n.group(2)])); continue
        if cur['items']:
            cur['items'][-1][1].append(ln)
        else:
            cur['text'].append(ln)
    out = []
    for s in sets:
        g = s['code'] + '|' + s['label']
        if s['items']:
            note = md_block('\n'.join(s['text'])) if s['text'] else ''
            out.append((g, note, [(f"{s['code']}-{n}", '\n'.join(l).strip()) for n, l in s['items']]))
        else:
            out.append((g, '', [(s['code'], '\n'.join(s['text']).strip())]))
    return out


def parse_review(md):
    """Returns [(group, note, [(id, prompt_md)])] for the cumulative section."""
    out = []
    for sub in re.split(r'\n(?=### )', '\n' + md):
        m = re.match(r'\n?### ([A-E])\.?\s+(.*)', sub)
        if not m: continue
        letter, label = m.group(1), m.group(2).strip()
        body = sub.strip('\n').split('\n', 1)[1] if '\n' in sub.strip('\n') else ''
        # Text before a task (a passage and its vocabulary) belongs to the task that follows it.
        items, pending, cur = [], [], None
        for ln in body.split('\n'):
            q = REVQ.match(ln)
            if q and (q.group(2) or q.group(1)):
                key = q.group(1) or q.group(2)
                cur = [key, pending + [rev_first(q)]]; pending = []; items.append(cur)
            elif cur and PASSAGE.match(ln.strip()):
                cur = None; pending = [ln]
            elif cur:
                cur[1].append(ln)
            else:
                pending.append(ln)
        if items:
            out.append((f'{letter}|{label}', '', [(k, '\n'.join(l).strip()) for k, l in items]))
        else:
            out.append((f'{letter}|{label}', '', [(letter, body.strip())]))
    return out


def build_module(n, lesson_path, answers_path, report):
    md = open(lesson_path, encoding='utf-8').read()
    sol, rev, revisit = parse_answers(open(answers_path, encoding='utf-8').read())
    head, secs = h2_sections(md)
    hm = re.search(r'^# Module \d+:\s*(.+)$', head, re.M)
    title = hm.group(1).strip()
    ar = next((l.strip() for l in head.split('\n')[1:] if l.strip() and arabic_heavy(l)), '')
    lessons, used = [], set()
    hand = load_items(n)          # auto-checked items (items_mNN.py), if this module has them
    labels = {}                   # set code / review letter -> label, for grouping hand-authored items

    def auto(k, its):
        out = []
        for it in its:
            key = it.get('sol') or it['id']
            if key.startswith('md:'):
                s_html = md_block(key[3:])
            else:
                s_html = next((src[c] for c in sol_candidates(key) for src in (sol, rev) if c in src), None)
            if s_html is None:
                report.append(f'Module {n}: no worked solution found for {it["id"]} (looked for {key})')
            used.add(it['id']); used.add(key)
            out.append(make_item(n, it, s_html, group_for(k, it['id'], labels)))
        return out

    def item(i, prompt, group, note, sol_html):
        if sol_html is None:
            report.append(f'Module {n}: no worked solution found for {i}')
        else:
            used.add(i)
        d = dict(id=i, type='open', prompt=md_block(prompt), sol=sol_html, group=group)
        if note: d['gnote'] = note
        return d

    before = [b for t, b in secs if t.startswith('Before you begin')]
    if before:
        h, s = anchor('<h2 class="sec">Before you begin</h2>' + teach_html(before[0]), '0')
        lessons.append(dict(key='0', title='Introduction', short='Introduction', html=h, secs=s, items=[]))

    after_lessons = False
    for t, body in secs:
        lm = re.match(r'Lesson (\d+):\s*(.*)', t)
        if lm:
            k, lt = lm.group(1), lm.group(2)
            teach_md, _, prac = body.partition('\n### Practice')
            reading = []
            def cb(task, k=k):
                key = f'{k}-Read'
                if hand is not None:
                    if any(it['id'] == key for it in hand.get(k, [])) and not reading:
                        reading.append(key); return True
                    return False
                if key in sol and not any(r['id'] == key for r in reading):
                    reading.append(item(key, '\n\n'.join(task), '|Reading', '', sol[key])); return True
                return False
            h, s = anchor(teach_html(teach_md, cb), k)
            items = []
            for g, note, its in parse_practice(prac, k):
                code, label = g.split('|')
                labels[code] = label
                if hand is None:
                    for j, (i, p) in enumerate(its):
                        s_html = sol.get(i) or sol.get(i.split('-')[0])
                        items.append(item(i, p, g, note if j == 0 else '', s_html))
            if hand is None:
                items += reading
            else:
                items = auto(k, hand.get(k, []))
            lessons.append(dict(key=k, title=inline(lt), short=f'Lesson {k}', html=h, secs=s, items=items))
            after_lessons = True
        elif after_lessons and t != 'Before you begin':
            if not any(l['key'] == 'R' for l in lessons):
                rbody, _, ready = body.partition('\n### Ready to continue')
                intro = rbody.split('\n### ', 1)[0]
                items = []
                for g, note, its in parse_review(rbody):
                    code, label = g.split('|')
                    labels['R' + code] = label
                    if hand is None:
                        for j, (i, p) in enumerate(its):
                            items.append(item(i, p, g, note if j == 0 else '', rev.get(i) or rev.get(i[0])))
                if hand is not None:
                    items = auto('R', hand.get('R', []))
                short = 'Module review' if t.lower().startswith('module review') else t.split(':')[0]
                L = dict(key='R', title=inline(t), short=short, html=teach_html(intro), secs=[], items=items)
                if ready:
                    L['after'] = '<h2 class="sec">Ready to continue' + ready.split('\n', 1)[0].strip() + '</h2>' + teach_html(ready.split('\n', 1)[1] if '\n' in ready else '')
                lessons.append(L)
            else:
                R = lessons[-1]
                R['after'] = R.get('after', '') + f'<h2 class="sec">{inline(t)}</h2>' + teach_html(body)
    if hand is not None:
        for k in hand:
            if k not in {l['key'] for l in lessons}:
                report.append(f'Module {n}: items for lesson {k}, which does not exist')
    unused = [] if hand is not None else sorted(set(sol) - used - {k for k in sol if k.split('-')[0] in {i.split('-')[0] for i in used}})
    for k in unused:
        report.append(f'Module {n}: answer {k} has no matching exercise')
    return dict(n=n, title=title, ar=ar, lessons=lessons, revisit=revisit)


def load_items(n):
    import importlib
    try:
        mod = importlib.import_module(f'items_m{n:02d}')
    except ModuleNotFoundError:
        return None
    return mod.ITEMS


def sol_candidates(key):
    """'2R-b' -> 2R-b, 2R ; 'B2-1' -> B2-1, B2, B ; '1G-1' -> 1G-1, 1G."""
    out, k = [key], key
    while re.search(r'-[^-]+$', k):
        k = re.sub(r'-[^-]+$', '', k); out.append(k)
    m = re.match(r'([A-E])\d', key)
    if m: out.append(m.group(1))
    return out


def group_for(k, i, labels):
    if i.endswith('-Read'):
        return '|Reading'
    if k == 'R':
        return i[0] + '|' + labels.get('R' + i[0], '')
    m = re.match(r'(\d+[GIR])', i)
    if not m:
        return ''
    return m.group(1) + '|' + labels.get(m.group(1), SET_NAMES[m.group(1)[-1]])


NOSHUFFLE = None


def make_item(n, it, sol_html, group):
    """Same conversion as Module 1's build_item: deterministic option shuffle, markdown to HTML."""
    import random, hashlib
    from app_items import END, ENDA
    global NOSHUFFLE
    NOSHUFFLE = NOSHUFFLE or [END, ENDA, ['Yes', 'No'], ['True', 'False']]
    r = random.Random(int(hashlib.md5(f'm{n}-{it["id"]}'.encode()).hexdigest(), 16))
    p = it['prompt']
    d = dict(id=it['id'], type=it['type'], prompt=md_block(p) if chr(10) in p else inline(p), sol=sol_html, group=group)
    if it['type'] == 'mcq':
        opts = it['opts'][:]
        if not (opts[0].startswith('(a)') or opts in NOSHUFFLE):
            r.shuffle(opts)
        d['opts'] = [inline(o) for o in opts]
        d['ans'] = opts.index(it['ans'])
    else:
        d['cols'] = [inline(c) for c in it['cols']]
        shuffled, rows = {}, []
        for lab, cells in it['rows']:
            row = []
            for c in cells:
                if c is None:
                    row.append(None); continue
                opts, ans = c
                key = tuple(opts)
                if key not in shuffled:
                    o = list(opts)
                    if o not in NOSHUFFLE:
                        r.shuffle(o)
                    shuffled[key] = o
                o = shuffled[key]
                row.append(dict(opts=[inline(x) for x in o], ans=o.index(ans)))
            rows.append(dict(label=inline(lab), cells=row))
        d['rows'] = rows
    return d


def find_modules(src):
    found = {}
    for p in glob.glob(os.path.join(src, 'Module *.md')):
        m = re.match(r'Module (\d+) - (.+)\.md$', os.path.basename(p))
        if not m: continue
        n = int(m.group(1))
        kind = 'answers' if m.group(2).startswith('Answers') else 'lessons'
        found.setdefault(n, {})[kind] = p
    return {n: v for n, v in sorted(found.items()) if 'lessons' in v and 'answers' in v}
