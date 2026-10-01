import re, html

SOURCE_DIR = '../../modules'   # where the 'Module NN - ….md' files live
from terms import convert

AR = '؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿'
AR_RUN = re.compile('[' + AR + ']+(?:[  .:!/=()\\[\\]…,\\-]*[' + AR + ']+)*')
BLANK = ''

TRANSLIT = [
    (r'\s*\(\*[^)]*?\*\)', ''), (r'\(\*[^*]+\*,\s*', '('),          # (*kalimah*) style parentheticals
    (r'[Tt]anwīn', 'تنوين'), (r'fatḥah', 'فتحة'), (r'ḍammah', 'ضمة'),
    (r'kasrah', 'كسرة'), (r'sukūn', 'سكون'), (r'iḍāfah', 'إضافة'),
    (r'naṣb', 'نصب'), (r'jazm', 'جزم'), (r'rafʿ', 'رفع'), (r'tarkīb', 'تركيب'),
    (r'iʿrāb', 'إعراب'), (r'nāsikh', 'ناسخ'), (r'\*Yaktubu\*', 'يكتبُ'),
    (r'\*huwa\*', 'هو'), (r'final tāʾs', 'final تاء letters'), (r'tāʾ', 'تاء'), (r'nūn', 'نون'), (r'long ā', 'long alif ى'),
]


USE_TERMS = True   # English-to-Arabic term conversion: 'm1' / True uses terms.py (Module 1); 'book' uses terms_book.py


def clean(s):
    for a, b in TRANSLIT:
        s = re.sub(a, b, s)
    if USE_TERMS == 'book':
        import terms_book
        s = terms_book.convert(s)
    elif USE_TERMS:
        s = convert(s)
    s = s.replace(' — ', ': ').replace('—', ': ')
    return s


def wrap_ar(t):
    out, last = [], 0
    for m in AR_RUN.finditer(t):
        out.append(html.escape(t[last:m.start()], quote=False))
        seg = html.escape(m.group(0), quote=False).replace(
            BLANK, '<span class="blank"></span>')
        out.append('<span class="ar" lang="ar" dir="rtl">' + seg + '</span>')
        last = m.end()
    out.append(html.escape(t[last:], quote=False))
    return ''.join(out)


def inline(s):
    s = clean(s).replace('___', BLANK)
    parts = re.split(r'(\*\*.+?\*\*|\*[^*\s][^*]*?\*)', s)
    res = []
    for p in parts:
        if p.startswith('**') and p.endswith('**') and len(p) > 4:
            res.append('<b>' + wrap_ar(p[2:-2]) + '</b>')
        elif p.startswith('*') and p.endswith('*') and len(p) > 2:
            res.append('<i>' + wrap_ar(p[1:-1]) + '</i>')
        else:
            res.append(wrap_ar(p))
    r = ''.join(res)
    # Latin-side blanks left outside Arabic runs
    return r.replace(BLANK, '<span class="blank"></span>')


def text_h(s, cpl=88, lh=26):
    n = len(re.sub(r'\*', '', s))
    return max(1, -(-n // cpl)) * lh


CSS = """
body{margin:0;background:#ffffff}
.pg{box-sizing:border-box;color:#111111;font-family:Calibri,Carlito,'Segoe UI',sans-serif;font-size:16px;line-height:1.5;background:#ffffff}
.ar{font-family:'Traditional Arabic','Scheherazade New',serif;font-size:1.333em;line-height:1;unicode-bidi:isolate}
b .ar,b.ar{font-weight:700}
.blank{display:inline-block;width:34px;height:1em;border-bottom:1px solid #111111;vertical-align:-2px;margin:0 2px}
p{margin:0 0 9px}
.kick{letter-spacing:.02em;color:#111111;font-size:14px;font-weight:600}
h1{font-size:18.67px;line-height:1.2;margin:6px 0 16px;font-weight:600;text-wrap:balance}
h2{font-size:18.67px;margin:22px 0 10px;font-weight:600;color:#111111;border-bottom:1px solid #222222;padding-bottom:2px}
h3{font-size:16px;margin:14px 0 6px;font-weight:700}
.head{border-bottom:3px double #222222;padding-bottom:6px;margin-bottom:12px;display:flex;justify-content:space-between;align-items:baseline}
.ref{background:#f4f4f4;border:1px solid #222222;padding:14px 18px 8px;margin-bottom:10px}
.ref h3:first-child{margin-top:0}
table{border-collapse:collapse;width:100%;margin:6px 0 12px;font-size:16px;line-height:1.45}
th,td{border:1px solid #222222;padding:6px 9px;text-align:center;vertical-align:middle}
th{background:#ebebeb;font-weight:600}
td.w{background:#fff}
.ref table th{background:#e6e6e6}
.ref td{background:#ffffff}
.set{font-weight:700;font-size:16px;margin:20px 0 8px;display:flex;gap:8px;align-items:baseline}
.set .tag{color:#111111;}
.ex{display:grid;grid-template-columns:28px minmax(0,1fr);column-gap:6px;margin:0 0 14px}
.ex .n{color:#111111;font-weight:700;text-align:right;padding-right:2px}
.lines{background:repeating-linear-gradient(to bottom,transparent 0,transparent 31px,#a6a6a6 31px,#a6a6a6 32px);margin:4px 0 2px}
.lab{display:grid;grid-template-columns:auto minmax(0,1fr);column-gap:8px;align-items:end}
.lab .l{font-size:16px;color:#444444;padding-bottom:3px}
.disp{text-align:center;margin:8px 0 8px;font-size:16px}
.disp .ar{font-size:1.333em;line-height:1.6}
.pills{display:flex;flex-wrap:wrap;gap:12px;margin:8px 0 4px}
.pill{border:1px solid #222222;border-radius:14px;padding:2px 14px;font-size:16px}
.opts{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.6fr);gap:16px;margin:6px 0}
.box{display:inline-block;width:24px;height:18px;border:1px solid #222222;vertical-align:middle;margin-left:6px;background:#fff}
.mt td{text-align:left}
.toc{font-size:16px;line-height:1.35}
.toc td{padding:3px 9px}
.foot{margin-top:20px;border-top:1px solid #222222;padding-top:6px;font-size:14px;color:#444444;display:flex;justify-content:space-between}
ol.tight,ul.tight{margin:2px 0 6px;padding-left:20px}
ol.tight li,ul.tight li{margin:0 0 5px}
.ans h2{margin-top:24px}
.ans h3{color:#111111;margin:14px 0 6px;font-size:16px}
.ans ol,.ans ul{margin:0 0 4px;padding-left:20px}
.ans li{margin:0 0 7px}
.ans p{margin:0 0 9px}
"""

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Scheherazade+New:wght@400;700&amp;family=Carlito:ital,wght@0,400;0,700;1,400&amp;display=swap">
<style>{css}</style>
</helmet>
"""

TAIL = """
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
"""


def page(title, body, w, h, fixed=False):
    style = (f'width:{w}px;height:{h}px;padding:60px 64px;overflow:hidden' if fixed
             else f'width:{w}px;padding:60px 64px 56px')
    return (HEAD.format(title=html.escape(title), css=CSS) +
            f'<div class="pg" style="{style}">\n{body}\n</div>' +
            TAIL.format(w=w, h=h))

CSS += """
.lesson h2.sec{margin-top:24px}
.exm{margin:6px 0 10px 28px;padding-left:12px;border-left:2px solid #bbbbbb}
.exm .ar{font-size:1.333em;line-height:1.6}
.exm .gl{color:#444444;font-style:italic}
.worked{border:1px solid #222222;background:#f4f4f4;padding:12px 18px 6px;margin:8px 0 12px}
.worked h2.sec{margin-top:0;border-bottom-color:#111111}
.worked td{background:#ffffff}
.practice{margin-top:30px;border-top:3px double #222222;padding-top:2px}
"""
