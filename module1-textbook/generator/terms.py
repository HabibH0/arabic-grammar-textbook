import re

ARL = '؀-ۿ'
# (pattern, arabic). Longest / most specific first. Patterns are case-insensitive, word-bounded.
T = [
    (r'nominative subject of a nominal sentence', 'مبتدأ مرفوع'),
    # sentence classifications
    (r'nominal sentence affected by a ناسخ', None), (r'a subject whose raised', None), (r'governed as the subject of', None), (r'(?<=and the )object', 'مفعول به'), (r'(?<=, )a description(?=, )', 'a نعت'), (r'preceding relative', 'preceding موصول'),
    (r'an implied-predicate phrase', 'a ظرف مستقرّ'), (r'implied-predicate reading', 'ظرف مستقرّ reading'),
    (r'fronted-predicate', 'خبر مقدّم'), (r'second-object position', 'second مفعول به position'),
    (r'two-object pattern', 'pattern with two مفعول به'),
    (r'Nominal and verbal structure', 'اسمية and فعلية structure'), (r'neither nominal nor', 'neither اسمية nor'),
    (r'genitive nouns?', 'اسم مجرور'), (r'nominative nouns?', 'اسم مرفوع'), (r'accusative nouns?', 'اسم منصوب'),
    (r'(?<!ask )(?<!asks )a question', 'a استفهام'), (r'or question', 'or استفهام'), (r'on the question', 'on the استفهام'),
    (r'basic nominal sentence', 'basic جملة اسمية'), (r'basic verbal sentence', 'basic جملة فعلية'),
    (r'nominal sentences?', 'جملة اسمية'), (r'verbal sentences?', 'جملة فعلية'),
    (r'nominal\s*/\s*verbal', 'اسمية / فعلية'),
    (r'report\s*/\s*performative', 'خبرية / إنشائية'),
    (r'affirmative\s*/\s*non-affirmative', 'موجب / غير موجب'),
    (r'non-affirmative', 'غير موجب'), (r'affirmative', 'موجب'),
    (r'negative report', 'negative خبرية'), (r'reportive', 'خبرية'), (r'performative', 'إنشائية'),
    (r'complete speech', 'كلام'),
    (r'containing sentence', 'الجملة الكبرى'),
    # roles
    (r'fronted predicate', 'خبر مقدّم'), (r'delayed subject', 'مبتدأ مؤخّر'),
    (r'predicate-holder', 'صاحب خبر'), (r'circumstance-holder', 'ذو حال'),
    (r'subject\s*–\s*predicate', 'مبتدأ–خبر'), (r'subject\s*–\s*verb', 'فعل–فاعل'),
    (r'outer subject', 'outer مبتدأ'),
    (r'subject[- ]pronouns?', 'ضمير فاعل'),
    (r'predicates?', 'خبر'), (r'predication', 'إسناد'),
    (r'subjects?', 'فاعل'),
    (r'direct objects?', 'مفعول به'), (r'objects?', 'مفعول به'),
    (r'relative connection', 'صلة'), (r'described noun', 'موصوف'),
    (r'addressee', 'منادى'), (r'condition', 'شرط'), (r'response', 'جواب'),
    (r'circumstance', 'حال'),
    # word classes and phrase types
    (r'prepositional phrases?', 'جار ومجرور'), (r'prepositions?', 'حرف جرّ'),
    (r'adverbial nouns?', 'ظرف'), (r'adverbial role', 'مفعول فيه'),
    (r'phrase-type', 'type of شبه جملة'), (r'phrases?', 'شبه جملة'),
    (r'noun-link', 'إضافة'), (r'iḍāfah complement', 'مضاف إليه'),
    (r'noun-equivalent', 'اسم مؤول'), (r'noun-signs?', 'علامة'),
    (r'descriptive nouns?', 'صفة'), (r'descriptive word', 'صفة'),
    (r'two nouns', 'اسمان'), (r'nouns', 'أسماء'), (r'noun', 'اسم'),
    (r'past verbs?', 'فعل ماضٍ'), (r'imperative verbs?', 'فعل أمر'), (r'imperatives?', 'أمر'),
    (r'verbs', 'أفعال'), (r'verb', 'فعل'),
    (r'particles', 'حروف'), (r'particle', 'حرف'),
    (r'implicit pronouns?', 'ضمير مستتر'), (r'detached pronouns?', 'ضمير منفصل'),
    (r'attached pronouns?', 'ضمير متصل'), (r'pronouns?', 'ضمير'),
    (r'inner sentence', 'الجملة الصغرى'), (r'sentences', 'جمل'), (r'sentence', 'جملة'),
    (r'definite article', 'أل'), (r'indefinite', 'نكرة'), (r'definite', 'معرفة'),
    (r'verbal prefix', 'حرف مضارعة'), (r'feminine marker', 'تاء التأنيث'),
    # status and inflection
    (r'nominative positions?', 'رفع position'), (r'accusative positions?', 'نصب position'),
    (r'genitive positions?', 'جرّ position'),
    (r'nominative', 'مرفوع'), (r'accusative case', 'نصب'), (r'accusative', 'منصوب'),
    (r'(?:the |being in the )genitive', 'جرّ'), (r'genitive', 'مجرور'),
    (r'jussive mood', 'جزم'), (r'jussive', 'مجزوم'),
    (r'visible inflection', 'إعراب لفظي'), (r'estimated inflection', 'إعراب تقديري'),
    (r'positional inflection', 'إعراب محلي'), (r'grammatical inflection', 'إعراب'), (r'inflection', 'إعراب'),
    (r'fixed form', 'بناء'), (r'inflectable', 'معرب'),
    (r'governing elements?', 'عامل'), (r'governed elements?', 'معمول'), (r'governors?', 'عامل'),
    (r'non-governing', 'غير عامل'),
    (r'prohibition', 'نهي'), (r'negation', 'نفي'), (r'questioning', 'استفهام'),
    (r'commands?', 'أمر'),
]
# predicative "nominal"/"verbal"
T2 = [
    (r'\b[Nn]ominal(?=\**[ ]?[.,;:)]| outside| inside| internally)', 'اسمية'),
    (r'\b[Vv]erbal(?=\**[ ]?[.,;:)]| outside| inside| internally)', 'فعلية'),
    (r'\bis nominal\b', 'is اسمية'), (r'\bis verbal\b', 'is فعلية'),
]
COMPILED = [(re.compile(r'(?<![\w-])' + p + r'(?![\w])', re.I), a) for p, a in T]
HARAKAT = re.compile('[\u064B-\u0652\u0670\u0640]')
LAST_AR = re.compile('([' + ARL + '][' + ARL + ' ]*)[^' + ARL + ']*$')


def _strip(x):
    return HARAKAT.sub('', x).replace('ٱ', 'ا').replace('إ', 'ا').replace('أ', 'ا').replace('ّ', '')


def is_gloss(before, arabic, window=32, strict=False):
    """English term sitting right after the Arabic term it defines (first-definition gloss)."""
    m = LAST_AR.search(before)
    if not m:
        return False
    between = before[m.end(1):]
    if len(between) > window or re.search(r'[.;]', between):
        return False
    if strict and not re.fullmatch(r'[\s,:(“"*—–-]*', between):   # only punctuation between term and gloss
        return False
    a, b = _strip(m.group(1)), _strip(arabic)
    a_words, b_words = a.split(), b.split()
    for w1 in a_words[-3:]:
        for w2 in b_words:
            w1c, w2c = w1.replace('ال', '', 1) if w1.startswith('ال') else w1, w2
            k = min(3, len(w1c), len(w2c))
            if k >= (3 if strict else 2) and any(w1c[i:i+k] in w2c for i in range(len(w1c) - k + 1)):
                return True
    return False


def convert(s, compiled=None, gloss_window=32, gloss_strict=False):
    compiled = compiled or COMPILED
    # protect protected phrases
    keep = []
    def protect(m):
        keep.append(m.group(0)); return f'{len(keep)-1}'
    for rx, a in compiled:
        def rep(m, a=a):
            if a is None:
                return protect(m)
            before = s_cur[max(0, m.start() - 60):m.start()].replace('*', '')
            if is_gloss(before, a, gloss_window, gloss_strict):
                return protect(m)  # first-definition gloss: keep English
            return a
        s_cur = s
        s = rx.sub(rep, s)
    for rx, a in T2:
        s = re.sub(rx, a, s)
    s = re.sub('(\\d+)', lambda m: keep[int(m.group(1))], s)
    def dedupe(m):
        return m.group(2) if _strip(m.group(1)).strip() == _strip(m.group(3)).strip() else m.group(0)
    s = re.sub('([' + ARL + '][' + ARL + ' ]*?)\\s*[,(]\\s*(\\*\\*([' + ARL + ' ]+)\\*\\*)\\)?', dedupe, s)
    s = re.sub(r'\b([Aa])n (?=[' + ARL + '])', r'\1 ', s)
    s = re.sub(r'(مرفوع|منصوب|مجرور|مجزوم) (اسم|فعل|فاعل|مبتدأ|خبر|مفعول به|مضارع|ضمير)', r'\2 \1', s)
    return s
