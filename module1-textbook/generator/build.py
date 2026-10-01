import re, json, os, datetime
from common import inline, clean, page, text_h
from blocks import render
from teach import convert, lesson_md
from lessons import L, REVIEW

ROOT = '../workbook'
os.makedirs(ROOT + '/project', exist_ok=True)
W = 794
boards = {}


def fix_r(blocks):
    return [(b[0], '', *b[2:]) if b[0] == 'ex' and b[1] == 'R' else b for b in blocks]


def head(left, right):
    return f'<div class="head"><span class="kick">{left}</span><span class="kick">{right}</span></div>'


def foot(left):
    return f'<div class="foot"><span>{left}</span><span class="ar" lang="ar" dir="rtl">الكَلِمَةُ وَالجُمْلَةُ</span></div>'


def write(name, html):
    open(f'{ROOT}/project/{name}', 'w', encoding='utf-8').write(html)


# ---------- cover ----------
contents = ''.join(
    f'<tr><td style="width:70px">Lesson {n}</td><td style="text-align:left">{inline(L[n]["title"])}</td></tr>' for n in L)
contents += '<tr><td>Review</td><td style="text-align:left">Module review: apply the whole method</td></tr>'
contents += '<tr><td>Answers</td><td style="text-align:left">Answers and worked solutions (separate booklet)</td></tr>'
cover = f'''
<div style="height:100%;display:flex;flex-direction:column">
<div class="head"><span class="kick">Workbook</span><span class="kick">Module 1</span></div>
<div style="text-align:center;padding:12px 0 12px;border-bottom:3px double #222222;margin-bottom:6px">
<div class="kick" style="font-size:15px">Module 1</div>
<div style="font-size:40px;font-weight:600;line-height:1.1;margin:4px 0 6px">Words and Sentences</div>
<div style="font-family:'Traditional Arabic','Scheherazade New',serif;font-size:38px;line-height:1.45;color:#111111" lang="ar" dir="rtl">الكَلِمَةُ وَالجُمْلَةُ</div>
<div style="font-size:15px;color:#444444;margin-top:6px">Practice workbook</div>
</div>
<h2 style="margin-top:12px">Before you begin</h2>
<p>{inline("You should be able to recognise Arabic letters and read short vowelled words. No previous grammar is assumed. Work through one lesson at a time. Attempt the exercises before opening the accompanying answers.")}</p>
<div class="ref" style="text-align:center;margin:6px 0 8px"><p style="margin:0">In each analysis, ask: <b>What kind of word is this? What is its role? What is it connected to? What explains its ending?</b></p>
<p style="margin:2px 0 0">{inline("This is the beginning of **تَرْكِيب**: explaining how the parts of an expression work together.")}</p></div>
<p>{inline("Early examples have vowel marks and English help. Later exercises remove some of that support. When adding endings, give the grammatical ending used in connected speech; do not replace it with a pause-ending.")}</p>
<p>{inline("By the end, you should be able to classify words and sentences, locate expressed and understood subjects, analyse phrases and their attachments, and distinguish three ways in which grammatical inflection appears.")}</p>
<h2 style="margin-top:14px">Contents</h2>
<table class="toc"><tbody>{contents}</tbody></table>
<div style="flex-grow:1"></div>
<div class="foot" style="margin-top:0"><span>Name</span><span style="flex-grow:1;border-bottom:1px solid #111111;margin:0 10px 4px"></span></div>
</div>'''
write('Main.dc.html', page('Module 1 workbook cover', cover, W, 1123, fixed=True))
boards['Main.dc.html'] = dict(w=W, h=1123, title='Cover', page='workbook', paper='a4')
wb_order = ['Main.dc.html']

# ---------- lessons ----------
for n, d in L.items():
    ref, rh = convert(lesson_md(n))
    pr, ph = render(fix_r(d['practice']), n)
    body = (head('Module 1 · Workbook', f'Lesson {n}') +
            f'<h1>{inline(d["title"])}</h1>' +
            f'<div class="lesson">{ref}</div>' +
            f'<div class="practice"><h2>Practice</h2>{pr}</div>' + foot(f'Answers: answer booklet, Lesson {n}'))
    h = int(150 + rh + 22 + ph + 60)
    name = f'Lesson{n:02d}.dc.html'
    write(name, page(clean(f'Lesson {n}: {d["title"]}'), body, W, h))
    boards[name] = dict(w=W, h=h, title=f'Lesson {n}', page='workbook', print='flow', paper='a4')
    wb_order.append(name)

rv, rvh = render(REVIEW)
body = head('Module 1 · Workbook', 'Module review') + '<h1>Module review: apply the whole method</h1>' + rv + foot('Answers: answer booklet, Module review')
h = int(120 + rvh + 60)
write('Review.dc.html', page('Module review', body, W, h))
boards['Review.dc.html'] = dict(w=W, h=h, title='Module review', page='workbook', print='flow', paper='a4')
wb_order.append('Review.dc.html')

# ---------- answers ----------
ANS = open('../source/Module_01_-_Answers_and_Worked_Solutions.md', encoding='utf-8').read()


def md_to_html(md):
    out, h = [], 0
    stack = []  # list types open
    def close_to(level):
        nonlocal out
        while len(stack) > level:
            out.append(f'</li></{stack.pop()}>')
    para = []
    for raw in md.split('\n'):
        line = raw.rstrip()
        m_h = re.match(r'(#{2,3}) (.*)', line)
        m_li = re.match(r'( *)(\d+\.|-) (.*)', line)
        if not line.strip():
            continue
        if m_h:
            close_to(0)
            tag = 'h2' if len(m_h.group(1)) == 2 else 'h3'
            out.append(f'<{tag}>{inline(m_h.group(2))}</{tag}>'); h += 56 if tag == 'h2' else 38
        elif m_li:
            lvl = len(m_li.group(1)) // 3 + 1
            typ = 'ol' if m_li.group(2)[0].isdigit() else 'ul'
            if len(stack) < lvl:
                out.append(f'<{typ}><li>'); stack.append(typ)
            else:
                close_to(lvl)
                if stack[-1] != typ:
                    close_to(lvl - 1); out.append(f'<{typ}><li>'); stack.append(typ)
                else:
                    out.append('</li><li>')
            out.append(inline(m_li.group(3))); h += text_h(m_li.group(3), cpl=82) + 7
        else:
            close_to(0)
            out.append(f'<p>{inline(line)}</p>'); h += text_h(line) + 9
    close_to(0)
    return '\n'.join(out), h


intro = ANS.split('\n## ', 1)[0].split('\n', 1)[1]
secs = re.split(r'\n(?=## )', ANS)[1:]
groups = [('Answers1.dc.html', 'Lessons 1 to 5', secs[0:5]),
          ('Answers2.dc.html', 'Lessons 6 to 9', secs[5:9]),
          ('Answers3.dc.html', 'Module review', secs[9:])]
ans_order = []
for i, (name, label, ss) in enumerate(groups):
    content, ch = md_to_html('\n'.join(ss))
    top = ''
    if i == 0:
        top = '<h1>Answers and Worked Solutions</h1>' + ''.join(
            f'<p>{inline(p)}</p>' for p in intro.strip().split('\n') if p.strip())
        ch += 150
    body = head('Module 1 · Answer booklet', label) + top + f'<div class="ans">{content}</div>' + foot(f'Answer booklet: {label}')
    h = int(110 + ch + 50)
    write(name, page(f'Answers: {label}', body, W, h))
    boards[name] = dict(w=W, h=h, title=f'Answers: {label}', page='answers', print='flow', paper='a4')
    ans_order.append(name)

# ---------- layout ----------
GAP = 80
def lay(order, y):
    x = 0
    for nme in order:
        boards[nme].update(x=x, y=y); x += W + GAP
    return x - GAP
w1 = lay(wb_order, 0)
w2 = lay(ans_order, 0)
canvas = {
    'v': 3,
    'createdOnFiles': {'v': 1, 'at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},
    'title': 'Module 1 Workbook: Words and Sentences',
    'launch': {'view': 'canvas', 'page': 'workbook'},
    'pages': [{'id': 'workbook', 'name': 'Workbook'}, {'id': 'answers', 'name': 'Answer booklet'}],
    'boards': {k: {kk: boards[k][kk] for kk in ('x', 'y', 'w', 'h', 'title', 'page', 'print', 'paper') if kk in boards[k]} for k in wb_order + ans_order},
    'order': wb_order + ans_order,
    'notes': {
        'wbTitle': {'x': 0, 'y': -260, 'text': 'Module 1 Workbook', 'kind': 'title1', 'maxW': w1, 'page': 'workbook'},
        'ansTitle': {'x': 0, 'y': -260, 'text': 'Module 1 Answer Booklet', 'kind': 'title1', 'maxW': w2, 'page': 'answers'},
    },
    'designSystems': [],
}
json.dump(canvas, open(ROOT + '/project/canvas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k in wb_order + ans_order:
    print(k, boards[k]['h'], os.path.getsize(f'{ROOT}/project/{k}'))
