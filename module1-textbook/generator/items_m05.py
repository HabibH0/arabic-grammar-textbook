# Module 5: Particles Governing Nouns. Auto-checked items; correct answers follow the Module 5 answers file.
from item_kit import M, G, R, ENDA

ITEMS = {}

ITEMS['1'] = [
    G('1G', 'Match each term, then identify it in **حَضَرَ الطُّلَّابُ إِلَّا خَالِدًا**.', ['Meaning', 'In the example'], [
        ('مستثنى', [(['governor', 'excluded item', 'group from which the item is excluded'], 'excluded item'), (['خالدًا', 'الطلابُ', 'إلّا'], 'خالدًا')]),
        ('مستثنى منه', [(['governor', 'excluded item', 'group from which the item is excluded'], 'group from which the item is excluded'), (['خالدًا', 'الطلابُ', 'إلّا'], 'الطلابُ')]),
        ('عامل', [(['governor', 'excluded item', 'group from which the item is excluded'], 'governor'), None])]),
    G('1I', 'Add endings and analyse **خرج الضيوف إلا سعيدا**, “The guests went out except Saʿīd.”', ['Analysis'], R(
        ['فعل ماضٍ مبني على الفتح', 'فاعل مرفوع بالضمة، وهو المستثنى منه', 'أداة استثناء', 'مستثنى منصوب بالفتحة', 'فاعل ثانٍ مرفوع'],
        [('خرجَ', 'فعل ماضٍ مبني على الفتح'), ('الضيوفُ', 'فاعل مرفوع بالضمة، وهو المستثنى منه'), ('إلّا', 'أداة استثناء'), ('سعيدًا', 'مستثنى منصوب بالفتحة')])),
    M('1R', 'Why does **سعيد** not become a second subject merely because it names a person?', [
        'Meaning does not decide the role: Saʿīd is excluded from the action, not another participant.',
        'It does become a second subject: a person named after the verb shares the فاعل role.',
        'Names after **إلّا** are always accusative, because **إلّا** is a verb meaning “I except”.',
        '**سعيدًا** is the object of **خرج**, so it cannot also be a subject.',
        ], 'Meaning does not decide the role: Saʿīd is excluded from the action, not another participant.'),
]

ITEMS['2'] = [
    G('2G-1', 'Choose the particle for each meaning.', ['Particle'], [
        ('an unattainable wish', [(['ليت', 'لعلّ'], 'ليت')]),
        ('correction of an inference', [(['كأنّ', 'لكنّ'], 'لكنّ')]),
        ('resemblance', [(['كأنّ', 'إنّ'], 'كأنّ')])]),
    G('2G-2', 'Complete and name the roles.', ['Correct', 'Role of the first noun'], [
        ('إنّ البابَ مفتوح…', [(['إِنَّ البَابَ مَفْتُوحٌ', 'إِنَّ البَابَ مَفْتُوحًا'], 'إِنَّ البَابَ مَفْتُوحٌ'), (['اسم إنّ منصوب', 'مبتدأ مرفوع'], 'اسم إنّ منصوب')]),
        ('لعلّه قريب…', [(['لَعَلَّهُ قَرِيبٌ', 'لَعَلَّهُ قَرِيبًا'], 'لَعَلَّهُ قَرِيبٌ'), (['ضمير في محل نصب اسم لعلّ', 'ضمير في محل رفع مبتدأ'], 'ضمير في محل نصب اسم لعلّ')])]),
    G('2G-3', 'In **لَيْتَنِي حَاضِرٌ** (the speaker is male):', ['Analysis'], R(
        ['حرف تمنٍّ ونصب', 'نون الوقاية، لا محل لها', 'ياء المتكلّم، ضمير متصل في محل نصب اسم ليت', 'خبر ليت مرفوع', 'اسم ليت منصوب'],
        [('ليتَ', 'حرف تمنٍّ ونصب'), ('ن', 'نون الوقاية، لا محل لها'), ('ي', 'ياء المتكلّم، ضمير متصل في محل نصب اسم ليت'), ('حاضرٌ', 'خبر ليت مرفوع')])),
    G('2I-1', 'Analyse **كأن النجم مصباح**, “The star is like a lamp.”', ['Analysis'], R(
        ['حرف تشبيه ونصب', 'اسم كأنّ منصوب بالفتحة', 'خبر كأنّ مرفوع بالضمة', 'مبتدأ مرفوع'],
        [('كأنّ', 'حرف تشبيه ونصب'), ('النجمَ', 'اسم كأنّ منصوب بالفتحة'), ('مصباحٌ', 'خبر كأنّ مرفوع بالضمة')])),
    G('2I-2', 'Analyse **لعل المريض ينام**, “Perhaps the sick person will sleep.”', ['Analysis'], R(
        ['اسم لعلّ منصوب', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره هو', 'جملة فعلية في محل رفع خبر لعلّ', 'مضارع منصوب بلعلّ', 'جملة لا محل لها'],
        [('المريضَ', 'اسم لعلّ منصوب'), ('ينامُ (its own mood)', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره هو'), ('ينام with its subject', 'جملة فعلية في محل رفع خبر لعلّ')])),
    G('2I-3', 'Contrast the two sentences.', ['Meaning'], R(
        ['expectation of a possible, welcome arrival', 'a wish without expectation that it will happen'],
        [('لعلّ الغائبَ قادمٌ', 'expectation of a possible, welcome arrival'), ('ليت الشبابَ يعودُ', 'a wish without expectation that it will happen')])),
    M('2R', 'In **حضر الطلاب إلا خالدا**, can **خالدًا** be called **اسم إنّ** because it is accusative?', [
        'No: it is مستثنى in an exception; an accusative ending alone does not identify the governor.',
        'Yes: an accusative noun after a particle is the اسم of that particle, here **إلّا**.',
        'Yes: **إلّا** contains **إنّ** (إنْ + لا), so its noun is اسم إنّ.',
        'No: it is the فاعل of **حضر**, fronted after **إلّا** for emphasis.',
        ], 'No: it is مستثنى in an exception; an accusative ending alone does not identify the governor.'),
    M('2-Read', 'Read: **تنصب هذه الحروف المبتدأ اسمًا لها، وترفع الخبر خبرًا لها.** Which two verbs name the government, and what do they say?', [
        '**تنصب** and **ترفع**: the مبتدأ becomes an accusative اسم; the خبر stays nominative as خبر.',
        '**تنصب** and **ترفع**: the مبتدأ stays nominative; the خبر becomes an accusative خبر.',
        '**تنصب** and **ترفع**: both the مبتدأ and the خبر become accusative.',
        '**اسمًا** and **خبرًا**: both name the accusative ending these particles assign.',
        ], '**تنصب** and **ترفع**: the مبتدأ becomes an accusative اسم; the خبر stays nominative as خبر.'),
]

ITEMS['3'] = [
    G('3G-1', 'Choose **إنّ / أنّ**.', ['Particle'], R(
        ['إِنَّ: quoted speech requires a clause', 'أَنَّ: a مصدر مؤوّل fills the object places'],
        [('قال سعيد: … الدرس سهل', 'إِنَّ: quoted speech requires a clause'), ('علمت … الدرس سهل', 'أَنَّ: a مصدر مؤوّل fills the object places')])),
    M('3G-2', 'In **تَبَيَّنَ أَنَّ الطَّرِيقَ آمِنٌ**, what is the فاعل of **تبيّن**?', [
        'the whole مصدر مؤوّل **أنّ الطريقَ آمنٌ**',
        '**الطريقَ** itself, fronted after **أنّ**',
        '**آمنٌ**, the خبر of **أنّ**',
        'an implicit pronoun هو referring to the route',
        ], 'the whole مصدر مؤوّل **أنّ الطريقَ آمنٌ**'),
    G('3G-3', 'Analyse **فَرِحْتُ بِأَنَّ أَخِي حَاضِرٌ**.', ['Analysis'], R(
        ['ضمير متصل في محل رفع فاعل', 'اسم أنّ منصوب بفتحة مقدّرة، وهو مضاف', 'ضمير متصل في محل جرّ مضاف إليه', 'خبر أنّ مرفوع بالضمة',
         'مصدر مؤوّل في محل جرّ بالباء', 'ضمير في محل نصب مفعول به'],
        [('ـتُ', 'ضمير متصل في محل رفع فاعل'), ('أخ', 'اسم أنّ منصوب بفتحة مقدّرة، وهو مضاف'), ('ـي', 'ضمير متصل في محل جرّ مضاف إليه'),
         ('حاضرٌ', 'خبر أنّ مرفوع بالضمة'), ('أنّ أخي حاضر', 'مصدر مؤوّل في محل جرّ بالباء')])),
    G('3I-1', '**أُعْلِنَ أنّ المجلس مفتوح**, “It was announced that the gathering is open.”', ['Analysis'], R(
        ['فعل ماضٍ مبني للمجهول', 'حرف مصدريّ ونصب', 'اسم أنّ منصوب', 'خبر أنّ مرفوع', 'مصدر مؤوّل في محل رفع نائب فاعل', 'نائب فاعل مرفوع'],
        [('أُعلنَ', 'فعل ماضٍ مبني للمجهول'), ('أَنّ (vowel: fatḥah)', 'حرف مصدريّ ونصب'), ('المجلسَ', 'اسم أنّ منصوب'), ('مفتوحٌ', 'خبر أنّ مرفوع'),
         ('أنّ المجلس مفتوح', 'مصدر مؤوّل في محل رفع نائب فاعل')])),
    M('3I-2', 'Correct **علمت أن الضيف صادقا**.', [
        'عَلِمْتُ أَنَّ الضَّيْفَ صَادِقٌ: **صادقٌ** is خبر أنّ, so it is nominative.',
        'عَلِمْتُ أَنَّ الضَّيْفُ صَادِقًا: **الضيفُ** is the subject and **صادقًا** the object.',
        'عَلِمْتُ أَنَّ الضَّيْفُ صَادِقٌ: after **علم**, the clause inside is nominal.',
        'It is already correct: **صادقًا** is the second object of **علم**.',
        ], 'عَلِمْتُ أَنَّ الضَّيْفَ صَادِقٌ: **صادقٌ** is خبر أنّ, so it is nominative.'),
    G('3I-3', 'Contrast the structures.', ['Structure'], R(
        ['أنّ forms a مصدر مؤوّل filling both object places', 'the lām suspends government (تعليق); the إنّ clause is in محل نصب'],
        [('علمت أنّ الطريقَ آمنٌ', 'أنّ forms a مصدر مؤوّل filling both object places'), ('علمت إنّ الطريقَ لآمنٌ', 'the lām suspends government (تعليق); the إنّ clause is in محل نصب')])),
    M('3R', 'Why can **أنّ الطريقَ آمنٌ** occupy رفع as a whole while **الطريقَ** is accusative inside it?', [
        'The unit’s outer role does not replace its inner grammar: it is the subject; **الطريقَ** is اسم أنّ.',
        'It cannot: **الطريقَ** should be **الطريقُ**, because the whole unit is in رفع and its first noun must agree.',
        'The whole unit is accusative too, as the object of **تبيّن**, so the outer and inner endings agree.',
        '**أنّ** has no effect inside, so **الطريقَ** takes its fatḥah from **تبيّن**.',
        ], 'The unit’s outer role does not replace its inner grammar: it is the subject; **الطريقَ** is اسم أنّ.'),
    M('3-Read', 'Read: **أنّ مع اسمها وخبرها في تأويل مصدر.** What does it say?', [
        'أنّ with its اسم and خبر is construed as a verbal-noun equivalent.',
        'أنّ on its own is a مصدر, and its اسم is its مضاف إليه.',
        'The اسم of أنّ is always a مصدر such as **صدق** or **نجاح**.',
        'أنّ with its اسم is a noun; its خبر stays outside the construction.',
        ], 'أنّ with its اسم and خبر is construed as a verbal-noun equivalent.'),
]

ITEMS['4'] = [
    M('4G-1', 'Why does **حيث إنّ خالدًا جالسٌ** normally use kasrah?', [
        '**حيث** normally takes a clause, hence **إنّ**; one analysis also allows **أنّ**.',
        '**إنّ** is used after any noun; **أنّ** is never possible after **حيث**.',
        '**حيث** is a verb meaning “because”, and verbs take **إنّ** after them.',
        '**حيث** takes a noun, hence **أنّ**; **إنّ** is a common error.',
        ], '**حيث** normally takes a clause, hence **إنّ**; one analysis also allows **أنّ**.'),
    G('4G-2', 'In the paired **فرحتُ بنجاح خالد…** examples:', ['Function'], R(
        ['noun coordination with **نجاح خالد**', 'an additional clause'],
        [('…وأنّه سالمٌ', 'noun coordination with **نجاح خالد**'), ('…وإنّه سالمٌ', 'an additional clause')])),
    G('4I-1', 'Give full tarkīb: **الضيف إنه متعب**, “The guest is indeed tired.”', ['Analysis'], R(
        ['مبتدأ مرفوع بالضمة', 'حرف توكيد ونصب', 'ضمير متصل في محل نصب اسم إنّ، يعود إلى الضيف', 'خبر إنّ مرفوع بالضمة', 'جملة اسمية في محل رفع خبر المبتدأ'],
        [('الضيفُ', 'مبتدأ مرفوع بالضمة'), ('إنّ', 'حرف توكيد ونصب'), ('ـهُ', 'ضمير متصل في محل نصب اسم إنّ، يعود إلى الضيف'), ('متعبٌ', 'خبر إنّ مرفوع بالضمة'),
         ('إنّه متعب', 'جملة اسمية في محل رفع خبر المبتدأ')])),
    G('4I-2', 'Why are **إلّا إنّهم** and **إلّا أنّه** not a contradiction?', ['Function of إلّا'], R(
        ['إلّا للحصر: restricts a statement; a clause follows', 'إلّا للاستثناء: introduces an exception; a noun equivalent follows'],
        [('إلّا إنّهم', 'إلّا للحصر: restricts a statement; a clause follows'), ('إلّا أنّه', 'إلّا للاستثناء: introduces an exception; a noun equivalent follows')])),
    G('4I-3', 'In the reason construction **استغفروا الله…**, both vowels are allowed. Analyse each.', ['Analysis'], R(
        ['a new explanatory clause', 'a مصدر مؤوّل after an omitted لام التعليل (لأنّه)'],
        [('إنّه غفورٌ رحيمٌ', 'a new explanatory clause'), ('أنّه غفورٌ رحيمٌ', 'a مصدر مؤوّل after an omitted لام التعليل (لأنّه)')])),
    G('4R', 'Translate each term.', ['Meaning'], R(
        ['a slot requiring a clause', 'a slot requiring a noun-like unit, which may contain several words'],
        [('موضع الجملة', 'a slot requiring a clause'), ('موضع المفرد', 'a slot requiring a noun-like unit, which may contain several words')])),
]

ITEMS['5'] = [
    M('5G-1', 'Arrange **إنّ / في المسجد / رجلًا**.', [
        'إِنَّ فِي المَسْجِدِ رَجُلًا: with an indefinite اسم the phrase must come between',
        'إِنَّ رَجُلًا فِي المَسْجِدِ: the اسم must directly follow the particle',
        'فِي المَسْجِدِ إِنَّ رَجُلًا: the phrase must come before the particle',
        ], 'إِنَّ فِي المَسْجِدِ رَجُلًا: with an indefinite اسم the phrase must come between'),
    G('5G-2', 'In **إنّ في المجلس خالدًا**:', ['Role'], R(
        ['خبر إنّ مقدّم (attached to an omitted general predicate)', 'اسم إنّ مؤخّر منصوب', 'مبتدأ مؤخّر'],
        [('في المجلس', 'خبر إنّ مقدّم (attached to an omitted general predicate)'), ('خالدًا', 'اسم إنّ مؤخّر منصوب')])),
    G('5G-3', 'Explain the two endings of **سعيد** in **إنّ خالدًا حاضرٌ وسعيدًا / وسعيدٌ**.', ['Explanation'], R(
        ['عطف على لفظ اسم إنّ: follows its actual نصب', 'عطف على الابتداء: follows the underlying nominative construction'],
        [('وسعيدًا', 'عطف على لفظ اسم إنّ: follows its actual نصب'), ('وسعيدٌ', 'عطف على الابتداء: follows the underlying nominative construction')])),
    G('5I-1', 'Analyse **لعل في الدار ضيفا**, “Perhaps there is a guest in the house.”', ['Analysis'], R(
        ['حرف ترجٍّ ونصب', 'اسم مجرور بالكسرة', 'متعلّق بمحذوف خبر لعلّ مقدّم', 'اسم لعلّ مؤخّر منصوب بالفتحة', 'مبتدأ مؤخّر مرفوع'],
        [('لعلّ', 'حرف ترجٍّ ونصب'), ('الدارِ', 'اسم مجرور بالكسرة'), ('في الدار', 'متعلّق بمحذوف خبر لعلّ مقدّم'), ('ضيفًا', 'اسم لعلّ مؤخّر منصوب بالفتحة')])),
    M('5I-2', 'Correct **إن خالدا وسعيدا حاضرين**.', [
        'إِنَّ خَالِدًا وَسَعِيدًا حَاضِرَانِ', 'إِنَّ خَالِدٌ وَسَعِيدٌ حَاضِرَانِ', 'إِنَّ خَالِدًا وَسَعِيدٌ حَاضِرَيْنِ', 'It is already correct.'], 'إِنَّ خَالِدًا وَسَعِيدًا حَاضِرَانِ'),
    M('5I-3', 'What is wrong with **إنّ مَنْ صمتَ نجا** when **مَنْ** is conditional?', [
        'Conditional **مَنْ** needs first position, so it cannot be اسم إنّ: **مَنْ صَمَتَ فَقَدْ نَجَا**.',
        'Nothing is wrong: conditional **مَنْ** can serve as اسم إنّ, with its whole condition and response as the خبر.',
        '**نجا** must become **ينجو**, because after **إنّ** a conditional response has to be a مضارع verb.',
        '**مَنْ** must be accusative after **إنّ**: **إنّ مَنًا صمتَ نجا**.',
        ], 'Conditional **مَنْ** needs first position, so it cannot be اسم إنّ: **مَنْ صَمَتَ فَقَدْ نَجَا**.'),
    M('5R', 'Why is **الدارِ** genitive even though its phrase serves a nominative predicate function?', [
        'The preposition governs **الدارِ** inside; the phrase’s predicate role does not cancel that.',
        'A شبه جملة predicate is always genitive as a whole, so the phrase is in محل جرّ and its noun follows that.',
        '**الدارِ** is a مضاف إليه of **في**, so it is genitive by إضافة rather than by the preposition.',
        'It is not: it should be **الدارُ**, as the predicate is nominative.',
        ], 'The preposition governs **الدارِ** inside; the phrase’s predicate role does not cancel that.'),
    M('5-Read', 'Read: **يجوز التوسّط مع المعرفة، ويجب مع النكرة.** (**يجوز** = is permitted; **يجب** = is required; **توسّط** = standing between.) What does it say?', [
        'The phrase may come between with a definite اسم, and must with an indefinite one.',
        'The phrase must come between with a definite اسم, and may with an indefinite one.',
        'The phrase may never come between إنّ and its اسم, definite or indefinite.',
        'The phrase must always come between, whether the اسم is definite or not.',
        ], 'The phrase may come between with a definite اسم, and must with an indefinite one.'),
]

ITEMS['6'] = [
    G('6G-1', 'Match each term.', ['Meaning'], R(
        ['retaining government', 'removing government', 'removing doubling', 'a distinguishing lām'],
        [('إعمال', 'retaining government'), ('إهمال', 'removing government'), ('تخفيف', 'removing doubling'), ('لام فارقة', 'a distinguishing lām')])),
    G('6G-2', '**إنِ الضيف… لصادقٌ**', ['Ending'], [
        ('with إهمال', [(['الضيفُ (مبتدأ)', 'الضيفَ (اسم إنْ)'], 'الضيفُ (مبتدأ)')]),
        ('with إعمال', [(['الضيفُ (مبتدأ)', 'الضيفَ (اسم إنْ)'], 'الضيفَ (اسم إنْ)')])]),
    M('6G-3', 'Who governs **صادقًا** in **إنْ كنتَ لصادقًا**?', [
        '**كان**, as its خبر',
        '**إنْ**, as its خبر',
        'the lām, as its خبر',
        ], '**كان**, as its خبر'),
    G('6I-1', 'Analyse **إنِ العلم لنافع** using إهمال.', ['Analysis'], R(
        ['مخفّفة من الثقيلة مهملة', 'مبتدأ مرفوع بالضمة', 'لام فارقة', 'خبر المبتدأ مرفوع بالضمة', 'اسم إنْ منصوب'],
        [('إنْ', 'مخفّفة من الثقيلة مهملة'), ('العلمُ', 'مبتدأ مرفوع بالضمة'), ('اللام', 'لام فارقة'), ('نافعٌ', 'خبر المبتدأ مرفوع بالضمة')])),
    M('6I-2', 'Correct: “In **إنِ الطالبَ لمجتهدٌ**, the lām must be called فارقة because every lām after إنْ is فارقة.”', [
        '**الطالبَ** shows إنْ governs, so the lām need not distinguish; it can be the shifted lām.',
        'The claim is correct: after lightened إنْ the lām is always فارقة, whether the particle governs or not.',
        'The lām is لام الجحود, because إنْ here is the negative particle and the lām reinforces the denial.',
        '**الطالبَ** must be **الطالبُ**, as the lām shows إنْ is not governing.',
        ], '**الطالبَ** shows إنْ governs, so the lām need not distinguish; it can be the shifted lām.'),
    M('6I-3', 'Why can **إنْ خالدٌ لصادقٌ** not be translated “Khalid is not truthful”?', [
        'It is affirmative lightened **إنْ**; the lām marks that, so it affirms Khalid is truthful.',
        'It is negative **إنْ**; the lām only adds emphasis, so it denies he is truthful.',
        'It is conditional **إنْ**; the lām introduces the response, so it means “if”.',
        'It is negative **إنْ**, because **خالدٌ** is nominative rather than accusative.',
        ], 'It is affirmative lightened **إنْ**; the lām marks that, so it affirms Khalid is truthful.'),
    G('6R', 'Compare the noun roles.', ['خالد', 'صادق'], [
        ('إنّ خالدًا صادقٌ', [(['اسم إنّ', 'مبتدأ'], 'اسم إنّ'), (['خبر إنّ', 'خبر المبتدأ'], 'خبر إنّ')]),
        ('إنْ خالدٌ لصادقٌ', [(['اسم إنّ', 'مبتدأ'], 'مبتدأ'), (['خبر إنّ', 'خبر المبتدأ'], 'خبر المبتدأ')])]),
    M('6-Read', 'Read: **الغالب بعد التخفيف الإهمال، ويجوز الإعمال.** (**الغالب** = usual.) What does it say?', [
        'Non-government is usual after lightening; government is allowed.',
        'Non-government is required after lightening; government is wrong.',
        'Government is usual after lightening; non-government is rare.',
        'Lightening is allowed only when the particle keeps governing.',
        ], 'Non-government is usual after lightening; government is allowed.'),
]

ITEMS['7'] = [
    G('7G-1', 'In **علمتُ أنْ قد وصلَ الضيفُ**:', ['Analysis'], R(
        ['ضمير الشأن محذوف', 'جملة قد وصل الضيف في محل رفع خبر أنْ', 'فاعل وصل مرفوع', 'اسم أنْ'],
        [('اسم أنْ', 'ضمير الشأن محذوف'), ('The predicate', 'جملة قد وصل الضيف في محل رفع خبر أنْ'), ('الضيفُ', 'فاعل وصل مرفوع')])),
    G('7G-2', 'Choose **قد / سـ** after lightened **أنْ**.', ['Separator'], R(
        ['قد', 'سـ'], [('أنْ … رجعَ', 'قد'), ('أنْ … يرجعُ', 'سـ')])),
    M('7G-3', 'In the worked **كأنْ** example, what governs the ending of **يحضرْ**?', [
        '**لم**, in جزم',
        '**كأنْ**, in جزم',
        '**أنْ**, in جزم',
        ], '**لم**, in جزم'),
    G('7I-1', 'Analyse **علمت أن قد فتح سعيد الباب** (lightened **أنْ**).', ['Analysis'], R(
        ['مخفّفة عاملة؛ اسمها ضمير الشأن محذوف', 'حرف تحقيق', 'فاعل مرفوع بالضمة', 'مفعول به منصوب بالفتحة', 'جملة فعلية في محل رفع خبر أنْ', 'اسم أنْ منصوب'],
        [('أنْ', 'مخفّفة عاملة؛ اسمها ضمير الشأن محذوف'), ('قد', 'حرف تحقيق'), ('سعيدٌ', 'فاعل مرفوع بالضمة'), ('البابَ', 'مفعول به منصوب بالفتحة'),
         ('قد فتح سعيد الباب', 'جملة فعلية في محل رفع خبر أنْ')])),
    G('7I-2', 'Analyse **كأن لم يسمع الضيف الخبر**, “As though the guest had not heard the report.”', ['Analysis'], R(
        ['حرف تشبيه مخفّف عامل؛ اسمها ضمير الشأن محذوف', 'مضارع مجزوم بلم، حُرّك بالكسر لالتقاء الساكنين', 'فاعل مرفوع', 'مفعول به منصوب',
         'جملة فعلية في محل رفع خبر كأنْ', 'مضارع منصوب بكأنْ'],
        [('كأنْ', 'حرف تشبيه مخفّف عامل؛ اسمها ضمير الشأن محذوف'), ('يسمعِ', 'مضارع مجزوم بلم، حُرّك بالكسر لالتقاء الساكنين'), ('الضيفُ', 'فاعل مرفوع'),
         ('الخبرَ', 'مفعول به منصوب'), ('لم يسمع الضيف الخبر', 'جملة فعلية في محل رفع خبر كأنْ')])),
    M('7I-3', 'Correct: “Lightened **أنْ** always puts the next verb in نصب, and the first visible noun is its اسم.”', [
        'Lightened أنْ governs an omitted شأن pronoun and a clause; it does not put a verb in نصب.',
        'The claim is correct: lightened أنْ governs the next verb in نصب, like ordinary أنْ.',
        'Lightened أنْ governs the next verb in جزم, and the first noun is its اسم.',
        'Lightened أنْ governs nothing; the first visible noun is a مبتدأ.',
        ], 'Lightened أنْ governs an omitted شأن pronoun and a clause; it does not put a verb in نصب.'),
    G('7R', 'Where is the اسم of the particle?', ['اسم'], R(
        ['خالدًا, expressed', 'an omitted شأن pronoun; خالدٌ is the subject of حضر'],
        [('علمتُ أنّ خالدًا حاضرٌ', 'خالدًا, expressed'), ('علمتُ أنْ قد حضرَ خالدٌ', 'an omitted شأن pronoun; خالدٌ is the subject of حضر')])),
]

ITEMS['8'] = [
    M('8G-1', 'With **ما** كافّة, choose: **إنّما الضيفُ / الضيفَ حاضرٌ**.', ['إنّما الضيفُ حاضرٌ', 'إنّما الضيفَ حاضرٌ'], 'إنّما الضيفُ حاضرٌ'),
    M('8G-2', 'Name the role of **الطالبُ** in **إنّما يكتبُ الطالبُ**.', ['فاعل يكتب', 'اسم إنّ', 'مبتدأ', 'خبر إنّ'], 'فاعل يكتب'),
    G('8I-1', 'Analyse **إنما يفتح الحارس الباب**, “The guard only opens the door.”', ['Analysis'], R(
        ['مكفوفة عن العمل', 'كافّة', 'فعل مضارع مرفوع بالضمة', 'فاعل مرفوع بالضمة', 'مفعول به منصوب بالفتحة', 'اسم إنّ منصوب'],
        [('إنّ', 'مكفوفة عن العمل'), ('ما', 'كافّة'), ('يفتحُ', 'فعل مضارع مرفوع بالضمة'), ('الحارسُ', 'فاعل مرفوع بالضمة'), ('البابَ', 'مفعول به منصوب بالفتحة')])),
    G('8I-2', 'Give both allowed patterns for **ليتما الغائب حاضر**.', ['Sentence', 'Role of الغائب'], [
        ('إعمال', [(['لَيْتَمَا الغَائِبَ حَاضِرٌ', 'لَيْتَمَا الغَائِبُ حَاضِرٌ'], 'لَيْتَمَا الغَائِبَ حَاضِرٌ'), (['اسم ليت', 'مبتدأ'], 'اسم ليت')]),
        ('إهمال', [(['لَيْتَمَا الغَائِبَ حَاضِرٌ', 'لَيْتَمَا الغَائِبُ حَاضِرٌ'], 'لَيْتَمَا الغَائِبُ حَاضِرٌ'), (['اسم ليت', 'مبتدأ'], 'مبتدأ')])]),
    M('8I-3', 'Correct: “Any written **ما** after any particle automatically removes all subsequent government.”', [
        '**ما الكافّة** blocks the listed particles (ليت allows both); it does not stop later governors.',
        'The claim is correct: any ما after a particle cancels all government that follows.',
        '**ما** never affects government; it only adds emphasis to the particle.',
        '**ما الكافّة** blocks every particle except ليت, and also stops following verbs.',
        ], '**ما الكافّة** blocks the listed particles (ليت allows both); it does not stop later governors.'),
    G('8R', 'Why does **الطالب** change role and ending?', ['Role of الطالب'], R(
        ['اسم إنّ منصوب; the clause **يكتب** is خبر إنّ', 'فاعل يكتب مرفوع; إنّ is blocked'],
        [('إنّ الطالبَ يكتبُ', 'اسم إنّ منصوب; the clause **يكتب** is خبر إنّ'), ('إنّما يكتبُ الطالبُ', 'فاعل يكتب مرفوع; إنّ is blocked')])),
    M('8-Read', 'Read: **تكفّها عن العمل، وتوسّع لها أن تدخل على الأفعال.** What does each verb say **ما** does?', [
        '**تكفّها**: it blocks their government; **توسّع**: it lets them come before verbs.',
        '**تكفّها**: it lets them come before verbs; **توسّع**: it blocks their government.',
        '**تكفّها**: it strengthens their government; **توسّع**: it turns them into nouns.',
        '**تكفّها** and **توسّع** both mean that **ما** only adds emphasis.',
        ], '**تكفّها**: it blocks their government; **توسّع**: it lets them come before verbs.'),
]

ITEMS['9'] = [
    M('9G-1', 'Choose the class-wide pattern.', ['لا ضيفَ حاضرٌ', 'لا ضيفٌ حاضرًا'], 'لا ضيفَ حاضرٌ'),
    M('9G-2', 'Explain the ending in **بلا خوفٍ**.', [
        '**لا** does not govern here; **الباء** makes **خوفٍ** genitive.',
        '**خوفٍ** is اسم لا, genitive in form and accusative in position.',
        '**خوفٍ** is genitive by **لا**, which governs like a preposition.',
        ], '**لا** does not govern here; **الباء** makes **خوفٍ** genitive.'),
    G('9G-3', 'Analyse **لا طالبَ علمٍ مذمومٌ**.', ['Analysis'], R(
        ['اسم لا منصوب بالفتحة، وهو مضاف (inflected)', 'مضاف إليه مجرور بالكسرة', 'خبر لا مرفوع بالضمة', 'اسم لا مبني على الفتح'],
        [('طالبَ', 'اسم لا منصوب بالفتحة، وهو مضاف (inflected)'), ('علمٍ', 'مضاف إليه مجرور بالكسرة'), ('مذمومٌ', 'خبر لا مرفوع بالضمة')])),
    G('9I-1', 'Analyse **لا كتاب مفقود**, “No book at all is missing.”', ['Analysis'], R(
        ['حرف لنفي الجنس يعمل عمل إنّ', 'اسم لا مبني على الفتح في محل نصب', 'خبر لا مرفوع بالضمة', 'اسم لا منصوب بالفتحة، وهو مضاف'],
        [('لا', 'حرف لنفي الجنس يعمل عمل إنّ'), ('كتابَ', 'اسم لا مبني على الفتح في محل نصب'), ('مفقودٌ', 'خبر لا مرفوع بالضمة')])),
    M('9I-2', 'Repair **لا في البيت ضيفَ**, adding **ولا طفل**.', [
        'لَا فِي البَيْتِ ضَيْفٌ وَلَا طِفْلٌ', 'لَا فِي البَيْتِ ضَيْفَ وَلَا طِفْلَ', 'لَا ضَيْفَ فِي البَيْتِ طِفْلٌ', 'لَا فِي البَيْتِ ضَيْفًا وَلَا طِفْلًا'],
        'لَا فِي البَيْتِ ضَيْفٌ وَلَا طِفْلٌ'),
    G('9I-3', 'Write “No fear and no sorrow here.”', ['Sentence'], [
        ('both instances governing', [(['لَا خَوْفَ وَلَا حُزْنَ هُنَا', 'لَا خَوْفٌ وَلَا حُزْنٌ هُنَا', 'لَا خَوْفًا وَلَا حُزْنًا هُنَا'], 'لَا خَوْفَ وَلَا حُزْنَ هُنَا')]),
        ('both non-governing', [(['لَا خَوْفَ وَلَا حُزْنَ هُنَا', 'لَا خَوْفٌ وَلَا حُزْنٌ هُنَا', 'لَا خَوْفًا وَلَا حُزْنًا هُنَا'], 'لَا خَوْفٌ وَلَا حُزْنٌ هُنَا')])]),
    G('9I-4', 'In **لا عاصيًا أباه ناجحٌ**:', ['Answer'], [
        ('What governs **عاصيًا**?', [(['لا, as its inflected اسم (شبيه بالمضاف)', 'أباه', 'ناجحٌ'], 'لا, as its inflected اسم (شبيه بالمضاف)')]),
        ('What governs **أباه**?', [(['عاصيًا, as its object', 'لا', 'ناجحٌ'], 'عاصيًا, as its object')]),
        ('What does **ناجحٌ** predicate?', [(['success of the person who disobeys his father', 'a description of the father'], 'success of the person who disobeys his father')])]),
    M('9R', 'Why does the advanced phrase have different consequences in **إنّ في البيت رجلًا** and **لا في البيت رجلٌ ولا امرأةٌ**?', [
        'إنّ still governs across its phrase predicate; لا needs its اسم next to it, so separation stops it.',
        'Both particles stop governing when a phrase separates them from their اسم, so both sentences need repetition.',
        'Both particles keep governing when a phrase separates them from their اسم; only the meanings differ.',
        'لا still governs across its phrase predicate; إنّ needs its اسم next to it.',
        ], 'إنّ still governs across its phrase predicate; لا needs its اسم next to it, so separation stops it.'),
]

ITEMS['10'] = [
    M('10G-1', 'Complete in the governing Ḥijāzī pattern: **ما الحارسُ نائم…**', ['ما الحارسُ نائمًا', 'ما الحارسُ نائمٌ'], 'ما الحارسُ نائمًا'),
    M('10G-2', 'Explain the رفع in **ما الحارسُ إلّا إنسانٌ**.', [
        '**إلّا** restricts the statement, so **ما** is مهملة: مبتدأ and خبر.',
        '**ما** still governs; **إنسانٌ** is its خبر, nominative after **إلّا**.',
        '**إنسانٌ** is مستثنى, nominative because the exception is negated.',
        '**إنسانٌ** is the فاعل of **إلّا**, which acts as a verb here.',
        ], '**إلّا** restricts the statement, so **ما** is مهملة: مبتدأ and خبر.'),
    G('10G-3', 'In **ولات حينَ مناصٍ**:', ['Analysis'], R(
        ['الحينُ (omitted)', 'خبر لات منصوب، وهو مضاف', 'مضاف إليه مجرور', 'اسم لات'],
        [('اسم لات', 'الحينُ (omitted)'), ('حينَ', 'خبر لات منصوب، وهو مضاف'), ('مناصٍ', 'مضاف إليه مجرور')])),
    G('10I-1', '**ما المسافر متعبا**', ['Sentence'], [
        ('governing usage', [(['مَا المُسَافِرُ مُتْعَبًا', 'مَا المُسَافِرُ مُتْعَبٌ', 'مَا المُسَافِرَ مُتْعَبٌ'], 'مَا المُسَافِرُ مُتْعَبًا')]),
        ('non-governing usage', [(['مَا المُسَافِرُ مُتْعَبًا', 'مَا المُسَافِرُ مُتْعَبٌ', 'مَا المُسَافِرَ مُتْعَبٌ'], 'مَا المُسَافِرُ مُتْعَبٌ')])]),
    G('10I-2', 'Identify each **إنْ**.', ['Treatment'], R(
        ['lightened affirmative, non-governing (lām فارقة)', 'additional, preventing ما from governing', 'negative, non-governing'],
        [('إنِ العلمُ لنافعٌ', 'lightened affirmative, non-governing (lām فارقة)'), ('ما إنْ خالدٌ غائبٌ', 'additional, preventing ما from governing'),
         ('إنْ خالدٌ غائبٌ (“Khalid is not absent”)', 'negative, non-governing')])),
    M('10I-3', 'Correct: “In **ما الضيفُ بمتعبٍ**, the باء turns the predicate into a مضاف إليه and removes its predicate role.”', [
        'The bā is additional: **متعبٍ** is genitive in form and accusative as خبر ما.',
        'The claim is correct: after the bā, **متعبٍ** is a مضاف إليه and not a predicate.',
        '**متعبٍ** is a مضاف إليه in محل رفع, the خبر of **الضيف**.',
        '**متعبٍ** is a حال, genitive because of the bā.',
        ], 'The bā is additional: **متعبٍ** is genitive in form and accusative as خبر ما.'),
    G('10R', 'Contrast the roles and endings.', ['الضيف', 'متعب'], [
        ('إنّ الضيفَ متعبٌ', [(['اسم إنّ منصوب', 'اسم لا مبني على الفتح', 'اسم ما مرفوع'], 'اسم إنّ منصوب'), (['خبر مرفوع', 'خبر ما منصوب'], 'خبر مرفوع')]),
        ('لا ضيفَ متعبٌ', [(['اسم إنّ منصوب', 'اسم لا مبني على الفتح', 'اسم ما مرفوع'], 'اسم لا مبني على الفتح'), (['خبر مرفوع', 'خبر ما منصوب'], 'خبر مرفوع')]),
        ('ما الضيفُ متعبًا', [(['اسم إنّ منصوب', 'اسم لا مبني على الفتح', 'اسم ما مرفوع'], 'اسم ما مرفوع'), (['خبر مرفوع', 'خبر ما منصوب'], 'خبر ما منصوب')])]),
    M('10-Read', 'Read: **يشترط لعمل ما أن يتقدّم اسمها، وألّا تقترن بإن الزائدة، وألّا يقترن خبرها بإلّا.** What are the three tests?', [
        'The اسم comes first; no additional إنْ follows ما; the خبر is not introduced by إلّا.',
        'The خبر comes first; إنْ must follow ما; the خبر is introduced by إلّا.',
        'The اسم is indefinite; ما is repeated; the خبر is a verbal clause.',
        'The اسم comes first; إنْ must follow ما; the خبر is not introduced by إلّا.',
        ], 'The اسم comes first; no additional إنْ follows ما; the خبر is not introduced by إلّا.'),
]

PAT = ['اسم منصوب وخبر مرفوع', 'مبتدأ وخبر', 'اسم مرفوع وخبر منصوب', 'مصدر مؤوّل يسدّ مسدّ مفعولين']

ITEMS['R'] = [
    G('A1', 'Supply **إنّ / أنّ** and the endings.', ['Correct form'], [
        ('قال الحارس: … الباب مفتوح', [(['إِنَّ البَابَ مَفْتُوحٌ', 'أَنَّ البَابَ مَفْتُوحٌ', 'إِنَّ البَابُ مَفْتُوحٌ'], 'إِنَّ البَابَ مَفْتُوحٌ')]),
        ('علمت … الحارس حاضر', [(['أَنَّ الحَارِسَ حَاضِرٌ', 'إِنَّ الحَارِسَ حَاضِرٌ', 'أَنَّ الحَارِسَ حَاضِرًا'], 'أَنَّ الحَارِسَ حَاضِرٌ')]),
        ('فرحت بـ… الضيف سالم', [(['بِأَنَّ الضَّيْفَ سَالِمٌ', 'بِإِنَّ الضَّيْفَ سَالِمٌ', 'بِأَنَّ الضَّيْفِ سَالِمٍ'], 'بِأَنَّ الضَّيْفَ سَالِمٌ')]),
        ('… في البيت طفلا (an independent statement)', [(['إِنَّ فِي البَيْتِ طِفْلًا', 'أَنَّ فِي البَيْتِ طِفْلًا', 'إِنَّ فِي البَيْتِ طِفْلٌ'], 'إِنَّ فِي البَيْتِ طِفْلًا')])]),
    G('A2', 'Match each sentence to its pattern.', ['Pattern'], R(PAT, [
        ('ما خالدٌ متعبًا', PAT[2]), ('إنّما العلمُ نافعٌ', PAT[1]), ('لعلّ الغائبَ حاضرٌ', PAT[0]), ('علمتُ أنّ البابَ مفتوحٌ', PAT[3])])),
    G('B1', 'Correct each sentence (keep the stated usage).', ['Correct form'], [
        ('إنما الطالبَ حاضرٌ (ما is كافّة)', [(['إِنَّمَا الطَّالِبُ حَاضِرٌ', 'إِنَّمَا الطَّالِبَ حَاضِرًا', 'إِنَّمَا الطَّالِبِ حَاضِرٌ'], 'إِنَّمَا الطَّالِبُ حَاضِرٌ')]),
        ('لا كتابٌ مفقودًا (no book at all is missing)', [(['لَا كِتَابَ مَفْقُودٌ', 'لَا كِتَابٌ مَفْقُودٌ', 'لَا كِتَابًا مَفْقُودًا'], 'لَا كِتَابَ مَفْقُودٌ')]),
        ('ما خالدٌ إلّا ضيفًا', [(['مَا خَالِدٌ إِلَّا ضَيْفٌ', 'مَا خَالِدًا إِلَّا ضَيْفٌ', 'مَا خَالِدٌ إِلَّا ضَيْفٍ'], 'مَا خَالِدٌ إِلَّا ضَيْفٌ')])]),
    M('B1-4', 'Correct: “In **علمتُ أنْ قد وصلَ خالدٌ**, خالد is اسم أنْ.”', [
        '**خالدٌ** is the subject of **وصل**; the اسم is an omitted ضمير الشأن.',
        'The claim is correct: the first visible noun after أنْ is its اسم.',
        '**خالدٌ** is the خبر of أنْ, and **قد وصل** is its اسم.',
        '**خالدٌ** is the second object of **علم**, after the fronted verb.',
        ], '**خالدٌ** is the subject of **وصل**; the اسم is an omitted ضمير الشأن.', sol='B1'),
    M('B1-5', 'Correct: “In **إنّ خالدًا يكتبُ**, the verb is منصوب because it follows an accusative اسم.”', [
        '**يكتبُ** is مرفوع; the clause is in محل رفع خبر إنّ and inherits nothing.',
        'The claim is correct: the verb takes نصب from the accusative noun before it.',
        '**يكتبُ** is مجزوم, because **إنّ** governs a following verb in جزم.',
        'The verb should be **يكتبَ**, because **إنّ** governs its خبر in نصب.',
        ], '**يكتبُ** is مرفوع; the clause is in محل رفع خبر إنّ and inherits nothing.', sol='B1'),
    M('B1-6', 'Correct: “After lightening, all six particles must stop governing.”', [
        'Lightened إنْ usually stops but may govern; أنْ and كأنْ keep governing; لكنْ does not.',
        'The claim is correct: removing the shaddah takes away government from all six particles without exception.',
        'All six keep governing after lightening, exactly as before; only their pronunciation changes.',
        'Only لكنْ keeps governing; إنْ, أنْ and كأنْ all stop.',
        ], 'Lightened إنْ usually stops but may govern; أنْ and كأنْ keep governing; لكنْ does not.', sol='B1'),
    G('C1', '**جَلَسَ سَعِيدٌ فِي المَجْلِسِ. قَالَ الحَارِسُ: إِنَّ فِي المَجْلِسِ ضَيْفًا. عَلِمَ سَعِيدٌ أَنَّ الضَّيْفَ مُتْعَبٌ. لَكِنَّ الضَّيْفَ يَقْرَأُ. لَعَلَّ الكِتَابَ نَافِعٌ. مَا الضَّيْفُ نَائِمًا.**', ['Analysis'], R(
        ['متعلق بمحذوف خبر إنّ مقدّم', 'اسم إنّ مؤخّر منصوب', 'في محل نصب مقول القول', 'مصدر مؤوّل سدّ مسدّ مفعولي علم', 'اسم لكنّ منصوب',
         'جملة فعلية في محل رفع خبر لكنّ', 'اسم ما مرفوع', 'خبر ما منصوب', 'خبر لعلّ مرفوع'],
        [('في المجلس (after إنّ)', 'متعلق بمحذوف خبر إنّ مقدّم'), ('ضيفًا', 'اسم إنّ مؤخّر منصوب'), ('the quoted إنّ clause', 'في محل نصب مقول القول'),
         ('أنّ الضيف متعب', 'مصدر مؤوّل سدّ مسدّ مفعولي علم'), ('الضيفَ (after لكنّ)', 'اسم لكنّ منصوب'), ('يقرأ (with its subject)', 'جملة فعلية في محل رفع خبر لكنّ'),
         ('نافعٌ', 'خبر لعلّ مرفوع'), ('الضيفُ (after ما)', 'اسم ما مرفوع'), ('نائمًا', 'خبر ما منصوب')])),
    M('C1-b', 'Why is **لكنّ** appropriate despite the guest’s tiredness?', [
        'Tiredness suggests he cannot read; **لكنّ** corrects that inference: he is reading.',
        '**لكنّ** expresses a wish here: the speaker wishes the tired guest were reading instead of resting.',
        '**لكنّ** expresses resemblance: the guest only looks as if he were reading, though he is tired.',
        '**لكنّ** expresses hope that the guest might begin to read.',
        ], 'Tiredness suggests he cannot read; **لكنّ** corrects that inference: he is reading.', sol='C1'),
    G('C2', '**قَالَ المُعَلِّمُ: إِنَّمَا العِلْمُ نَافِعٌ. لَا خَوْفَ وَلَا حُزْنَ هُنَا. لَيْتَ الغَائِبَ حَاضِرٌ. عَلِمْتُ أَنْ قَدْ وَصَلَ الضَّيْفُ. كَأَنْ لَمْ يَسْمَعِ الحَارِسُ الخَبَرَ.**', ['Analysis'], R(
        ['مكفوفة عن العمل', 'مبتدأ مرفوع', 'اسم لا مبني على الفتح في محل نصب', 'اسم ليت منصوب', 'مخفّفة عاملة؛ اسمها ضمير الشأن محذوف',
         'جملة فعلية في محل رفع خبر أنْ', 'مضارع مجزوم بلم، حُرّك بالكسر لالتقاء الساكنين', 'جملة فعلية في محل رفع خبر كأنْ'],
        [('إنّ (in إنّما)', 'مكفوفة عن العمل'), ('العلمُ', 'مبتدأ مرفوع'), ('خوفَ / حزنَ', 'اسم لا مبني على الفتح في محل نصب'), ('الغائبَ', 'اسم ليت منصوب'),
         ('أنْ', 'مخفّفة عاملة؛ اسمها ضمير الشأن محذوف'), ('قد وصل الضيف', 'جملة فعلية في محل رفع خبر أنْ'), ('يسمعِ', 'مضارع مجزوم بلم، حُرّك بالكسر لالتقاء الساكنين'),
         ('لم يسمع الحارس الخبر', 'جملة فعلية في محل رفع خبر كأنْ')])),
    G('C2-b', 'Passage 2: answer.', ['Answer'], [
        ('The لا sentence with both particles non-governing', [(['لَا خَوْفٌ وَلَا حُزْنٌ هُنَا', 'لَا خَوْفَ وَلَا حُزْنَ هُنَا', 'لَا خَوْفًا وَلَا حُزْنًا هُنَا'], 'لَا خَوْفٌ وَلَا حُزْنٌ هُنَا')]),
        ('Which sentence expresses a wish?', [(['لَيْتَ الغَائِبَ حَاضِرٌ', 'إِنَّمَا العِلْمُ نَافِعٌ', 'عَلِمْتُ أَنْ قَدْ وَصَلَ الضَّيْفُ'], 'لَيْتَ الغَائِبَ حَاضِرٌ')]),
        ('Does it assert that the absent person is present?', [(['No: it presents presence as desired', 'Yes'], 'No: it presents presence as desired')])], sol='C2'),
    G('D1', 'Match each statement to its example.', ['Example'], R(
        ['لعلّ المسافرَ يرجعُ / إنّ في البيت رجلًا', 'تبيّن أنّ الخبرَ صحيحٌ', 'لا في الدار رجلٌ ولا امرأةٌ', 'ليتما الغائبَ حاضرٌ / ليتما الغائبُ حاضرٌ'],
        [('قد يكون الخبر جملة، وقد يكون شبه جملة.', 'لعلّ المسافرَ يرجعُ / إنّ في البيت رجلًا'), ('المصدر المؤوّل له موقع في الجملة، ولكل كلمة داخله إعرابها.', 'تبيّن أنّ الخبرَ صحيحٌ'),
         ('لا تعمل لا لنفي الجنس إذا فُصل بينها وبين اسمها، وتجب حينئذ إعادتها.', 'لا في الدار رجلٌ ولا امرأةٌ'),
         ('ما الكافّة تكفّ هذه الحروف عن العمل، ويجوز مع ليت الإعمال والإهمال.', 'ليتما الغائبَ حاضرٌ / ليتما الغائبُ حاضرٌ')])),
    G('D2', 'Complete: **في «إنْ كنتَ لصادقًا»:**', ['Analysis'], R(
        ['مخفّفة من الثقيلة مهملة', 'ضمير متصل في محل رفع اسم كان', 'فارقة', 'خبر كان منصوب بالفتحة', 'اسم إنْ منصوب'],
        [('إنْ', 'مخفّفة من الثقيلة مهملة'), ('التاء', 'ضمير متصل في محل رفع اسم كان'), ('اللام', 'فارقة'), ('صادقًا', 'خبر كان منصوب بالفتحة')])),
    G('E1', '**عَلِمْتُ أَنَّ فِي القَرْيَةِ طَبِيبًا. إِنَّمَا يُعَالِجُ الطَّبِيبُ المَرِيضَ. لَا مَرِيضَ مُهْمَلٌ.**', ['Analysis'], R(
        ['متعلّق بمحذوف خبر أنّ مقدّم', 'اسم أنّ مؤخّر منصوب', 'مكفوفة عن العمل', 'فاعل مرفوع بالضمة', 'مفعول به منصوب بالفتحة', 'اسم لا مبني على الفتح في محل نصب', 'خبر لا مرفوع'],
        [('في القرية', 'متعلّق بمحذوف خبر أنّ مقدّم'), ('طبيبًا', 'اسم أنّ مؤخّر منصوب'), ('إنّ (in إنّما)', 'مكفوفة عن العمل'), ('الطبيبُ', 'فاعل مرفوع بالضمة'),
         ('المريضَ', 'مفعول به منصوب بالفتحة'), ('مريضَ', 'اسم لا مبني على الفتح في محل نصب'), ('مهملٌ', 'خبر لا مرفوع')])),
    G('E2', 'Express each meaning.', ['Arabic'], [
        ('Perhaps the guard is awake (**مستيقظ**)', [(['لَعَلَّ الحَارِسَ مُسْتَيْقِظٌ', 'لَعَلَّ الحَارِسُ مُسْتَيْقِظٌ', 'لَعَلَّ الحَارِسَ مُسْتَيْقِظًا'], 'لَعَلَّ الحَارِسَ مُسْتَيْقِظٌ')]),
        ('No guest at all is absent (**ضيف، غائب**)', [(['لَا ضَيْفَ غَائِبٌ', 'لَا ضَيْفٌ غَائِبًا', 'لَا ضَيْفًا غَائِبٌ'], 'لَا ضَيْفَ غَائِبٌ')]),
        ('The door is not closed (governing **ما**, **مغلق**)', [(['مَا البَابُ مُغْلَقًا', 'مَا البَابَ مُغْلَقٌ', 'مَا البَابُ إِلَّا مُغْلَقًا'], 'مَا البَابُ مُغْلَقًا')]),
        ('I knew that the traveller had returned (lightened **أنْ**, **قد**, **رجع**)', [(['عَلِمْتُ أَنْ قَدْ رَجَعَ المُسَافِرُ', 'عَلِمْتُ أَنْ رَجَعَ المُسَافِرَ', 'عَلِمْتُ أَنَّ قَدْ رَجَعَ المُسَافِرُ'], 'عَلِمْتُ أَنْ قَدْ رَجَعَ المُسَافِرُ')])]),
]
