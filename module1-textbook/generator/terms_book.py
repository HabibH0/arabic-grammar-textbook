"""English-to-Arabic grammatical terms for Modules 2 onwards.

These modules are mostly written with Arabic terms already, but their explanations, exercises and solutions still use
English ones ("subject", "predicate", "accusative", …). This list runs before Module 1's list (terms.T) and handles the
compound and module-specific wordings first. Patterns are case-insensitive and word-bounded; most specific first.
Module 1 itself is unchanged: it still uses terms.T alone.
"""
import re
import terms

AR = terms.ARL

T_BOOK = [
    # --- objects and their positions
    (r'first objects?', 'مفعول به أوّل'), (r'second objects?', 'مفعول به ثانٍ'), (r'third objects?', 'مفعول به ثالث'),
    (r'(?:fronted|advanced) first object', 'مفعول به أوّل مقدّم'), (r'fronted object', 'مفعول به مقدّم'),
    (r'direct objects?', 'مفعول به صريح'), (r'mediated object relationship', 'مفعول به غير صريح'),
    (r'object[- ]pronouns?', 'ضمير مفعول به'),
    (r'(?:both|the two|two) object (?:places|positions)', 'مكان المفعولين'), (r'object (?:places?|positions?)', 'مكان المفعول به'),
    (r'two objects', 'مفعولان'), (r'three objects', 'ثلاثة مفاعيل'), (r'one object', 'مفعول به واحد'),
    (r'objects', 'مفاعيل'), (r'object', 'مفعول به'),
    # --- subjects, predicates, nominal sentences
    (r'subject\s*[–-]\s*predicate', 'مبتدأ–خبر'), (r'underlying subject', 'مبتدأ'),
    (r'subject(?=[’\']s having the description)', 'اسم'),        # اتّصاف الاسم بالخبر (كان and its sisters)
    (r'a subject and (?:a )?predicate', 'مبتدأ وخبر'), (r'subject and predicate', 'المبتدأ والخبر'),
    (r'nominal subject', 'مبتدأ'), (r'subject of the nominal predication', 'مبتدأ'),
    (r'nominative subject construction', 'construction of المبتدأ'), (r'nominative subject position', 'محل رفع فاعل'),
    (r'verb\s*[–-]\s*subject', 'فعل–فاعل'), (r'subject tāʾ', 'تاء الفاعل'), (r'subject nouns?', 'فاعل ظاهر'),
    (r'object-form pronouns?', 'ضمير نصب'),
    (r'fixed past praise verbs?', 'فعل ماضٍ جامد للمدح'), (r'fixed past exclamation verbs?', 'فعل ماضٍ جامد للتعجّب'),
    (r'praise\s*/\s*blame verbs?', 'أفعال المدح والذمّ'), (r'praise verbs?', 'فعل مدح'), (r'praise clause', 'جملة المدح'),
    (r'(?<=as a )description', 'نعت'), (r'(?<=not a )description', 'نعت'),
    (r'implicit subjects?', 'فاعل مستتر'), (r'hidden subjects?', 'فاعل مستتر'), (r'inner subjects?', 'فاعل داخلي'),
    (r'outer subjects?', 'فاعل خارجي'), (r'subject[- ]pronouns?', 'ضمير فاعل'),
    (r'delayed subject', 'مبتدأ مؤخّر'), (r'fronted predicate', 'خبر مقدّم'), (r'delayed predicate', 'خبر مؤخّر'),
    (r'predicate clause', 'جملة الخبر'), (r'phrase predicate', 'خبر شبه جملة'),
    (r'subjects', 'فاعل'), (r'subject', 'فاعل'), (r'predicates', 'خبر'), (r'predicate', 'خبر'),
    (r'passive construction', 'مبني للمجهول'), (r'passive', 'مبني للمجهول'), (r'agent', 'فاعل'),
    # --- word classes and forms
    (r'past verbs?', 'فعل ماضٍ'), (r'imperfect verbs?', 'فعل مضارع'), (r'present verbs?', 'فعل مضارع'),
    (r'imperative verbs?', 'فعل أمر'), (r'imperatives?', 'فعل أمر'), (r'imperfect', 'مضارع'),
    (r'verbal[- ]noun equivalents?', 'مصدر مؤوّل'), (r'verbal nouns?', 'مصدر'), (r'noun[- ]equivalents?', 'مصدر مؤوّل'), (r'active participle', 'اسم فاعل'),
    (r'relative nouns?', 'اسم موصول'), (r'interrogative nouns?', 'اسم استفهام'), (r'demonstratives?', 'اسم إشارة'),
    (r'interrogative particles?', 'حرف استفهام'), (r'negative particles?', 'حرف نفي'), (r'conditional particles?', 'أداة شرط'),
    (r'particles? of emphasis', 'حرف توكيد'), (r'future particles?', 'حرف استقبال'),
    (r'prepositional phrases?', 'جار ومجرور'), (r'prepositional constructions?', 'جار ومجرور'),
    (r'place[- ]adverbs?', 'ظرف مكان'), (r'adverbs?', 'ظرف'), (r'adverbial', 'ظرف'),
    (r'conjunctions?', 'حرف عطف'), (r'feminine markers?', 'تاء التأنيث'),
    (r'verbal clauses?', 'جملة فعلية'), (r'nominal clauses?', 'جملة اسمية'), (r'interrogative (?:clauses?|sentences?)', 'جملة استفهامية'),
    (r'explanatory clauses?', 'جملة تفسيرية'), (r'clauses', 'جمل'), (r'clause', 'جملة'),
    (r'interrogative hamzah', 'همزة الاستفهام'),
    # --- case, mood and their signs
    (r'case[- ]endings?', 'علامة إعراب'), (r'case positions?', 'محل إعراب'), (r'grammatical positions?', 'محل إعراب'),
    (r'(?<=in )(?:the )?nominative(?=\s*(?:[.,;:)|]|$|case|mood|position|and|or))', 'رفع'), (r'the nominative(?=\s*(?:[.,;:)|]|$|case|mood|position|and|or))', 'رفع'), (r'(?<=in )(?:the )?accusative(?=\s*(?:[.,;:)|]|$|case|mood|position|and|or))', 'نصب'), (r'the accusative(?=\s*(?:[.,;:)|]|$|case|mood|position|and|or))', 'نصب'), (r'(?<=in )(?:the )?jussive(?=\s*(?:[.,;:)|]|$|case|mood|position|and|or))', 'جزم'), (r'the jussive(?=\s*(?:[.,;:)|]|$|case|mood|position|and|or))', 'جزم'), (r'(?<=in )(?:the )?subjunctive(?=\s*(?:[.,;:)|]|$|case|mood|position|and|or))', 'نصب'), (r'the subjunctive(?=\s*(?:[.,;:)|]|$|case|mood|position|and|or))', 'نصب'),
    (r'subjunctive', 'منصوب'), (r'indicative', 'مرفوع'), (r'moods?', 'إعراب'),
    (r'fixed on', 'مبني على'), (r'fixed endings?', 'بناء'), (r'fixed pronouns?', 'ضمير مبني'), (r'fixed nouns?', 'اسم مبني'),
    (r'governors', 'عامل'), (r'governor', 'عامل'), (r'government', 'عمل'),
    # --- meanings and constructions
    (r'conditional results?', 'جواب شرط'), (r'conditional responses?', 'جواب الشرط'), (r'responses?', 'جواب'),
    (r'conditions', 'شروط'), (r'(?<!the )conditional', 'شرطي'),
    (r'negations?', 'نفي'), (r'prohibitions?', 'نهي'), (r'commands?', 'أمر'),
    (r'exceptions?', 'استثناء'), (r'excluded items?', 'مستثنى'),
    (r'coordination', 'عطف'), (r'coordinated (?:noun|expression)s?', 'معطوف'), (r'coordinated', 'معطوف'),
    (r'specifications?', 'تمييز'), (r'circumstances?', 'حال'),
    (r'relative connections?', 'صلة'), (r'praise', 'مدح'), (r'blame', 'ذمّ'), (r'exclamations?', 'تعجّب'),
    (r'oaths?', 'قسم'), (r'emphasis', 'توكيد'), (r'attachment', 'تعلّق'), (r'intransitive', 'لازم'), (r'transitive', 'متعدٍّ'),
    (r'sound feminine plurals?', 'جمع مؤنث سالم'), (r'sound masculine plurals?', 'جمع مذكر سالم'),
    (r'feminine plurals?', 'جمع مؤنث'), (r'feminine gender', 'التأنيث'), (r'feminine', 'مؤنث'), (r'plurals?', 'جمع'),
    (r'dual', 'مثنّى'), (r'singular', 'مفرد'), (r'masculine', 'مذكّر'),
    (r'embedded questions?', 'جملة استفهامية'), (r'(?<=entire )questions?', 'جملة استفهامية'), (r'(?<=whole )questions?', 'جملة استفهامية'),
    (r'first-object', 'مفعول به أوّل'), (r'second-object', 'مفعول به ثانٍ'), (r'third-object', 'مفعول به ثالث'),
    (r'non-jussive', 'غير جازم'), (r'vocatives?', 'نداء'),
    (r'two-object', 'two-مفعول'), (r'three-object', 'three-مفعول'), (r'one-object', 'one-مفعول'),
    (r'emphatic lām', 'لام التوكيد'), (r'relative (?:clauses?|sentences?)', 'جملة الصلة'), (r'relative analysis', 'analysis as اسم موصول'),
    (r'prepositional kāf', 'كاف الجرّ'), (r'prepositional (?:use|analysis|one)', 'use as حرف جرّ'),
    (r'negative elements?', 'أداة نفي'), (r'(?<=is )negative', 'نافية'), (r'(?<=not )negative', 'نافية'),
]

T2_BOOK = [
    # particle + adjective: "prohibitive لا" -> "لا الناهية", "negative ما" -> "ما النافية", "conditional إن" -> "إن الشرطية"
    (r'\bprohibitive \*\*([' + AR + ']+)\*\*', r'**\1 الناهية**'), (r'\bprohibitive ([' + AR + ']+)', r'\1 الناهية'),
    (r'\bnegative \*\*([' + AR + ']+)\*\*', r'**\1 النافية**'), (r'\bnegative ([' + AR + ']+)', r'\1 النافية'),
    (r'\bconditional \*\*([' + AR + ']+)\*\*', r'**\1 الشرطية**'), (r'\bconditional ([' + AR + ']+)', r'\1 الشرطية'),
    (r'\binterrogative \*\*([' + AR + ']+)\*\*', r'**\1 الاستفهامية**'),
    (r'\b[Cc]oordinating \*\*([' + AR + ']+)\*\*', r'**\1 العاطفة**'), (r'\b[Cc]oordinating ([' + AR + ']+)', r'\1 العاطفة'),
    (r'\b[Pp]repositional \*\*([' + AR + ']+)\*\*', r'**\1 الجارّة**'), (r'\b[Pp]repositional ([' + AR + ']+)', r'\1 الجارّة'),
    (r'\brelative \*\*([' + AR + ']+)\*\*', r'**\1 الموصولة**'), (r'\b(ما|من) relative\b', r'\1 الموصولة'), (r'\brelative (ما|من)\b', r'\1 الموصولة'),
    (r'\bimplicit (?:subject )?\*\*(هو|هي|أنت|أنتِ|أنا|نحن|هم)\*\*', r'ضمير مستتر تقديره **\1**'),
    (r'\bimplicit (?:subject )?(هو|هي|أنت|أنتِ|أنا|نحن|هم)(?![' + AR + '])', r'ضمير مستتر تقديره \1'),
]

COMPILED_BOOK = [(re.compile(r'(?<![\w-])' + p + r'(?![\w])', re.I), a) for p, a in T_BOOK] + terms.COMPILED


QUOTE = re.compile('“[^”' + AR + ']*”')      # a quoted English translation, e.g. “The door was opened.”


def convert(s):
    keep = []
    def hold(m):
        keep.append(m.group(0)); return f'{len(keep) - 1}'
    s = QUOTE.sub(hold, s)
    s = _convert(s)
    return re.sub('(\\d+)', lambda m: keep[int(m.group(1))], s)


def _convert(s):
    for rx, a in T2_BOOK:
        s = re.sub(rx, a, s)
    s = terms.convert(s, COMPILED_BOOK, gloss_window=14, gloss_strict=True)       # stricter: only a gloss right after its Arabic term
    s = re.sub(r'(مفعول به) (مرفوع|منصوب|مجرور) (أوّل|ثانٍ|ثالث|صريح|مقدّم)', r'\1 \3 \2', s)
    s = re.sub(r'\bimplicit فاعل', 'فاعل مستتر', s)
    s = re.sub(r'\bimplicit (هو|هي|أنت|أنتِ|أنا|نحن|هم)(?![' + AR + '])', r'ضمير مستتر تقديره \1', s)
    # adjective order after conversion: "منصوب مفعول به أوّل" -> "مفعول به أوّل منصوب"
    s = re.sub(r'(مرفوع|منصوب|مجرور|مجزوم) (مفعول به (?:أوّل|ثانٍ|ثالث|صريح)|فعل مضارع|فعل ماضٍ|معطوف|نعت|حال|تمييز|مستثنى)',
               r'\2 \1', s)
    return s
