# Module 3: Special Verb Constructions. Auto-checked items; correct answers follow the Module 3 answers file.
from item_kit import M, G, R, ENDA

ITEMS = {}

L1I1 = ['فعل ماضٍ ناقص مبني على الفتح', 'اسم كان مرفوع بالضمة', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره هو', 'مفعول به منصوب بالفتحة، عامله يقرأ',
        'جملة فعلية في محل نصب خبر كان', 'خبر كان منصوب بالفتحة', 'فاعل مرفوع بالضمة']

ITEMS['1'] = [
    M('1G-1', 'Add **كان** to **الكِتَابُ نَافِعٌ**.', [
        'كَانَ الكِتَابُ نَافِعًا', 'كَانَ الكِتَابَ نَافِعٌ', 'كَانَ الكِتَابُ نَافِعٌ', 'كَانَ الكِتَابَ نَافِعًا'], 'كَانَ الكِتَابُ نَافِعًا'),
    G('1G-1b', 'Name the new roles in **كَانَ الكِتَابُ نَافِعًا**.', ['Role'], R(
        ['اسم كان مرفوع بالضمة', 'خبر كان منصوب بالفتحة', 'فاعل مرفوع بالضمة', 'مفعول به منصوب بالفتحة'],
        [('الكتابُ', 'اسم كان مرفوع بالضمة'), ('نافعًا', 'خبر كان منصوب بالفتحة')]), sol='1G-1'),
    G('1G-2', '**لن يكون… الضيفُ حاضرًا**', ['Answer'], [
        ('Correct form of the verb', [(['يكونُ', 'يكونَ', 'يكونْ'], 'يكونَ')]),
        ('What governs the verb?', [(['لن', 'الضيف', 'nothing: it is مرفوع'], 'لن')]),
        ('What governs **حاضرًا**?', [(['يكون', 'لن', 'الضيف'], 'يكون')])]),
    G('1G-3', 'In **كنتُ متأدبًا**:', ['Role'], [
        ('ـتُ', [(['في محل رفع اسم كان', 'في محل رفع فاعل'], 'في محل رفع اسم كان')]),
        ('متأدبًا', [(['خبر كان منصوب', 'حال منصوب'], 'خبر كان منصوب')])]),
    G('1I-1', 'أعرب: **كَانَ الضَّيْفُ يَقْرَأُ الكِتَابَ**, “The guest was reading the book.”', ['Analysis'], R(L1I1, [
        ('كانَ', 'فعل ماضٍ ناقص مبني على الفتح'), ('الضيفُ', 'اسم كان مرفوع بالضمة'), ('يقرأُ', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره هو'),
        ('الكتابَ', 'مفعول به منصوب بالفتحة، عامله يقرأ'), ('يقرأ الكتاب', 'جملة فعلية في محل نصب خبر كان')])),
    M('1I-2', 'Correct: “Every **كان + مضارع** describes a habit.”', [
        'It may describe one past action in progress; habit has to come from the context.',
        'It always describes a habit, because **كان** gives the مضارع a repeated sense.',
        'It always describes a future action, because the مضارع points ahead of **كان**.',
        'It always describes one completed action, because **كان** makes the مضارع past.',
        ], 'It may describe one past action in progress; habit has to come from the context.'),
    G('1I-3', 'Complete “Be patient!” with **كُنْ** and **صَابِر**.', ['Answer'], [
        ('Sentence', [(['كُنْ صَابِرًا', 'كُنْ صَابِرٌ', 'كُنْ صَابِرٍ'], 'كُنْ صَابِرًا')]),
        ('اسم كن', [(['ضمير مستتر تقديره أنت في محل رفع', 'صابرًا', 'ضمير مستتر تقديره هو'], 'ضمير مستتر تقديره أنت في محل رفع')]),
        ('خبر كن', [(['صابرًا، منصوب بالفتحة', 'ضمير مستتر تقديره أنت'], 'صابرًا، منصوب بالفتحة')])]),
    G('1R', 'Compare **ظننتُ خالدًا صادقًا** with **كان خالدٌ صادقًا**.', ['Role'], R(
        ['مفعول به أوّل', 'مفعول به ثانٍ', 'اسم كان مرفوع', 'خبر كان منصوب', 'فاعل'],
        [('**خالدًا** in ظننت خالدا صادقا', 'مفعول به أوّل'), ('**صادقًا** in ظننت خالدا صادقا', 'مفعول به ثانٍ'),
         ('**خالدٌ** in كان خالد صادقا', 'اسم كان مرفوع'), ('**صادقًا** in كان خالد صادقا', 'خبر كان منصوب')])),
    M('1-Read', 'Read: **الفعل الناقص يرفع اسمه وينصب خبره.** Why does this not make **يكتبُ** accusative in **كان خالدٌ يكتبُ**?', [
        'The خبر is a verbal clause: the clause occupies نصب, while its مضارع stays مرفوع.',
        '**يكتبُ** is the اسم of كان, which is why it is nominative rather than accusative.',
        'The rule applies only to a single-word خبر; a verbal خبر has no position at all.',
        '**كان** governs only nouns, so the verb is outside the construction entirely.',
        ], 'The خبر is a verbal clause: the clause occupies نصب, while its مضارع stays مرفوع.'),
]

ITEMS['2'] = [
    G('2G-1', 'Match each verb with its meaning.', ['Meaning'], R(
        ['became', 'was in a state at night', 'is not', 'was in a state in the evening'],
        [('أمسى', 'was in a state in the evening'), ('بات', 'was in a state at night'), ('صار', 'became'), ('ليس', 'is not')])),
    G('2G-2', 'Supply endings: **أصبح الطالبـ… نشيطـ…** and **ليس الكتابـ… جديدـ…** (active; new).', ['Ending'], R(ENDA, [
        ('الطالبـ…', 'ـُ'), ('نشيطـ…', 'ـًا'), ('الكتابـ…', 'ـُ'), ('جديدـ…', 'ـًا')])),
    G('2G-3', 'Identify the two kinds of **ما**.', ['Kind of ما'], R(
        ['negative ما: negating ceasing gives continuation', 'ما مصدرية ظرفية: “as long as”'],
        [('ما زال خالدٌ حاضرًا', 'negative ما: negating ceasing gives continuation'), ('أجلسُ ما دام خالدٌ حاضرًا', 'ما مصدرية ظرفية: “as long as”')])),
    G('2I-1', 'أعرب: **بات الطفل نائما**, “The child spent the night asleep.”', ['Analysis'], R(
        ['فعل ماضٍ ناقص مبني على الفتح', 'اسم بات مرفوع بالضمة', 'خبر بات منصوب بالفتحة', 'فاعل مرفوع بالضمة', 'حال منصوب بالفتحة'],
        [('باتَ', 'فعل ماضٍ ناقص مبني على الفتح'), ('الطفلُ', 'اسم بات مرفوع بالضمة'), ('نائمًا', 'خبر بات منصوب بالفتحة')])),
    M('2I-2', 'Complete “Continue to be patient” with **لا تَزَلْ**.', [
        '**لَا تَزَلْ صَابِرًا**: prohibitive **لا** with a مجزوم مضارع; زال has no imperative here.',
        '**لَا تَزَلْ صَابِرٌ**: **صابرٌ** is the nominative اسم of the continuation verb.',
        '**لَا تَزَلْ صَابِرًا**: **تزل** is the imperative of زال, and **لا** only adds emphasis.',
        '**لَا تَزَالُ صَابِرًا**: after negative **لا** the continuation verb stays مرفوع.',
        ], '**لَا تَزَلْ صَابِرًا**: prohibitive **لا** with a مجزوم مضارع; زال has no imperative here.'),
    G('2I-3', 'Distinguish the two verbs.', ['Analysis'], R(
        ['ناقص continuation verb: **خالدٌ** is its اسم and **حاضرًا** its خبر', 'complete verb “disappears”: **الخوفُ** is its فاعل'],
        [('لا يَزالُ خالدٌ حاضرًا', 'ناقص continuation verb: **خالدٌ** is its اسم and **حاضرًا** its خبر'),
         ('يَزُولُ الخوفُ', 'complete verb “disappears”: **الخوفُ** is its فاعل')]) + [
        ('What does the internal vowel (ā / ū) help identify?', [(['which construction it is', 'the case of the following noun', 'the tense'], 'which construction it is')])]),
    G('2R', 'Analyse **لستُ أكتبُ**, “I am not writing.”', ['Analysis'], R(
        ['فعل ماضٍ ناقص جامد مبني على السكون', 'ضمير متصل في محل رفع اسم ليس', 'فعل مضارع مرفوع بالضمة؛ فاعله مستتر تقديره أنا',
         'جملة فعلية في محل نصب خبر ليس', 'ضمير متصل في محل رفع فاعل', 'فعل مضارع منصوب بليس'],
        [('ليس (in لستُ)', 'فعل ماضٍ ناقص جامد مبني على السكون'), ('ـتُ', 'ضمير متصل في محل رفع اسم ليس'),
         ('أكتبُ', 'فعل مضارع مرفوع بالضمة؛ فاعله مستتر تقديره أنا'), ('أكتب with its subject', 'جملة فعلية في محل نصب خبر ليس')])),
    M('2-Read', 'Read: **ما في ما دام ليست نافية، وما في ما زال نافية.** How do the two constructions differ in meaning?', [
        '**ما دام** expresses a duration condition, “as long as”; **ما زال** expresses continuation.',
        '**ما دام** expresses continuation, “still”; **ما زال** expresses a duration condition.',
        'Both negate: **ما دام** means “did not last” and **ما زال** means “did not cease”.',
        'Both express duration, “as long as”; only the verbs after **ما** differ in meaning.',
        ], '**ما دام** expresses a duration condition, “as long as”; **ما زال** expresses continuation.'),
]

ITEMS['3'] = [
    G('3G-1', 'Classify each use of **كان**.', ['Use', 'The nominative noun'], [
        ('كان البابُ مفتوحًا', [(['ناقص', 'تامّ'], 'ناقص'), (['اسم كان', 'فاعل'], 'اسم كان')]),
        ('كانت حربٌ (A war occurred)', [(['ناقص', 'تامّ'], 'تامّ'), (['اسم كان', 'فاعل'], 'فاعل')])]),
    M('3G-2', 'Choose: **كان واسعًا / واسعٌ البيتُ / البيتَ**.', [
        'كَانَ وَاسِعًا البَيْتُ: a fronted خبر منصوب and a delayed اسم مرفوع',
        'كَانَ وَاسِعٌ البَيْتَ: a fronted اسم مرفوع and a delayed خبر منصوب',
        'كَانَ وَاسِعًا البَيْتَ: a fronted خبر منصوب and a delayed مفعول به',
        'كَانَ وَاسِعٌ البَيْتُ: a fronted مبتدأ and a delayed خبر, both مرفوع',
        ], 'كَانَ وَاسِعًا البَيْتُ: a fronted خبر منصوب and a delayed اسم مرفوع'),
    G('3G-3', 'Can the nūn of **يكن / أكن** be omitted?', ['Omit the nūn?'], R(
        ['Yes', 'No: keep it, with a connecting kasrah before الـ'],
        [('لم أكن غائبًا', 'Yes'), ('لم يكن الطالبُ غائبًا', 'No: keep it, with a connecting kasrah before الـ')])),
    G('3I-1', 'أعرب: **الدَّرْسَ كَانَ خَالِدٌ يَكْتُبُ**, “It was the lesson that Khalid was writing.”', ['Analysis'], R(
        ['مفعول به مقدّم منصوب، عامله يكتب', 'فعل ماضٍ ناقص مبني على الفتح', 'اسم كان مرفوع بالضمة', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره هو',
         'خبر كان مقدّم منصوب', 'مفعول به منصوب، عامله كان'],
        [('الدرسَ', 'مفعول به مقدّم منصوب، عامله يكتب'), ('كانَ', 'فعل ماضٍ ناقص مبني على الفتح'), ('خالدٌ', 'اسم كان مرفوع بالضمة'),
         ('يكتبُ', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره هو')])),
    M('3I-2', 'In **التمس خاتمًا ولو حديدًا**, what explains the two accusatives?', [
        'Understand **ولو كان الخاتمُ حديدًا**: **حديدًا** is the خبر of an omitted كان.',
        'Both are objects of **التمس**: **خاتمًا** first and **حديدًا** second.',
        '**حديدًا** is a حال describing **خاتمًا** as being made of iron.',
        'Understand **ولو التمستَ حديدًا**: **حديدًا** is the object of an omitted verb.',
        ], 'Understand **ولو كان الخاتمُ حديدًا**: **حديدًا** is the خبر of an omitted كان.'),
    M('3I-3', 'Correct: “In **لم أكُ غائبًا**, the final ḍammah proves that the verb is مرفوع.”', [
        '**أكُ** is still مجزوم: from **أكنْ**, the jussive sukūn belonged to the omitted nūn.',
        '**أكُ** is مرفوع: **لم** cannot govern a ناقص verb, so the ḍammah is visible.',
        '**أكُ** is منصوب بلم: the omitted nūn leaves an estimated fatḥah on the kāf.',
        '**أكُ** is a past verb: **لم** turns the meaning to the past, so it is fixed.',
        ], '**أكُ** is still مجزوم: from **أكنْ**, the jussive sukūn belonged to the omitted nūn.'),
    G('3R', 'Contrast **صار الضيف إلى المسجد** (“went to the mosque”) with **صار الضيف صديقا** (“became a friend”).', ['صار is', 'الضيفُ is'], [
        ('صار الضيف إلى المسجد', [(['تامّ', 'ناقص'], 'تامّ'), (['فاعل', 'اسم صار'], 'فاعل')]),
        ('صار الضيف صديقا', [(['تامّ', 'ناقص'], 'ناقص'), (['فاعل', 'اسم صار'], 'اسم صار')])]),
    M('3-Read', 'Read: **الفعل التامّ يكتفي بفاعله ولا يحتاج إلى خبر.** Which contrast is correct?', [
        '**كانت حربٌ** asserts occurrence with a فاعل; **كانت الحربُ شديدةً** needs **شديدةً** as خبر.',
        '**كانت حربٌ** needs a خبر, which is omitted; **كانت الحربُ شديدةً** is complete.',
        'Both are ناقص: **حربٌ** and **الحربُ** are each اسم كان, with an omitted خبر in one.',
        'Both are تامّ: **شديدةً** is a حال describing the war, not a خبر.',
        ], '**كانت حربٌ** asserts occurrence with a فاعل; **كانت الحربُ شديدةً** needs **شديدةً** as خبر.'),
]

ITEMS['4'] = [
    G('4G-1', 'Match each term with its meaning.', ['Meaning'], R(
        ['apprehension', 'purpose or reason', 'hope for something welcome'],
        [('ترجٍّ', 'hope for something welcome'), ('إشفاق', 'apprehension'), ('تعليل', 'purpose or reason')])),
    M('4G-2', 'Choose the valid pattern.', ['حَرَى خَالِدٌ أَنْ يَنْجَحَ', 'حَرَى خَالِدٌ يَنْجَحُ'], 'حَرَى خَالِدٌ أَنْ يَنْجَحَ'),
    M('4G-3', 'Explain the different endings in **عسى خالدٌ أن يكتبَ** and **عسى خالدٌ يكتبُ**.', [
        '**أنْ** makes the inner verb منصوب; without it, **يكتبُ** is an ordinary مرفوع مضارع.',
        '**عسى** makes the inner verb منصوب; in the second it fails to govern because **أنْ** is missing.',
        'The second is wrong: after **عسى** the verb must always be **يكتبَ**, with or without **أنْ**.',
        'In the first **يكتبَ** is the خبر itself; in the second **خالدٌ** is the خبر and **يكتبُ** a حال.',
        ], '**أنْ** makes the inner verb منصوب; without it, **يكتبُ** is an ordinary مرفوع مضارع.'),
    G('4I-1', 'أعرب: **اخلولق الضيف أن يحضر**, “The guest is likely to attend.”', ['Analysis'], R(
        ['فعل ماضٍ ناقص مبني على الفتح', 'اسم اخلولق مرفوع بالضمة', 'حرف مصدريّ ونصب', 'مضارع منصوب بأن؛ فاعله مستتر تقديره هو يعود على الضيف',
         'مصدر مؤوّل في محل نصب خبر اخلولق', 'فاعل مرفوع بالضمة'],
        [('اخلولقَ', 'فعل ماضٍ ناقص مبني على الفتح'), ('الضيفُ', 'اسم اخلولق مرفوع بالضمة'), ('أنْ', 'حرف مصدريّ ونصب'),
         ('يحضرَ', 'مضارع منصوب بأن؛ فاعله مستتر تقديره هو يعود على الضيف'), ('أن يحضر', 'مصدر مؤوّل في محل نصب خبر اخلولق')])),
    G('4I-2', 'أعرب **عسى أن ينجح الطالب** على التمام.', ['Analysis'], R(
        ['فعل ماضٍ تامّ مبني على الفتح المقدّر', 'فاعل ينجح مرفوع بالضمة', 'مصدر مؤوّل في محل رفع فاعل عسى', 'اسم عسى مرفوع', 'مصدر مؤوّل في محل نصب خبر عسى'],
        [('عسى', 'فعل ماضٍ تامّ مبني على الفتح المقدّر'), ('الطالبُ', 'فاعل ينجح مرفوع بالضمة'), ('أن ينجح الطالب', 'مصدر مؤوّل في محل رفع فاعل عسى')])),
    M('4I-3', 'Correct: “Whenever **أن** is absent after **عسى**, the construction is wrong.”', [
        '**أنْ** is frequent but may be omitted with **عسى**; it is required with **حرى** and **اخلولق**.',
        'The claim is right for every verb of hope: **عسى، حرى، اخلولق** all require **أنْ**.',
        '**أنْ** is required with **عسى** but optional with **حرى** and **اخلولق**.',
        '**أنْ** is never used after **عسى**; it belongs only with **حرى** and **اخلولق**.',
        ], '**أنْ** is frequent but may be omitted with **عسى**; it is required with **حرى** and **اخلولق**.'),
    G('4R', 'Compare **كان خالدٌ يكتبُ** and **عسى خالدٌ أن يكتبَ**.', ['Inner verb', 'Predicate position'], [
        ('كان خالدٌ يكتبُ', [(['مرفوع', 'منصوب بأن'], 'مرفوع'), (['في محل نصب خبر', 'في محل رفع'], 'في محل نصب خبر')]),
        ('عسى خالدٌ أن يكتبَ', [(['مرفوع', 'منصوب بأن'], 'منصوب بأن'), (['في محل نصب خبر', 'في محل رفع'], 'في محل نصب خبر')])]),
    M('4-Read', 'Read: **يجب اقتران خبر حرى واخلولق بأن، ويكثر ذلك في خبر عسى.** (**اقتران** = accompanying; **يجب** = is required; **يكثر** = is frequent.) What does it say?', [
        '**أن** is required with **حرى** and **اخلولق**, and frequent with **عسى**.',
        '**أن** is required with **حرى**, **اخلولق** and **عسى** alike.',
        '**أن** is frequent with **حرى** and **اخلولق**, and required with **عسى**.',
        '**أن** is required with **عسى**, and forbidden with **حرى** and **اخلولق**.',
        ], '**أن** is required with **حرى** and **اخلولق**, and frequent with **عسى**.'),
]

ITEMS['5'] = [
    M('5G-1', 'Choose the more frequent construction.', ['أوشك الضيفُ أن يحضرَ', 'أوشك الضيفُ يحضرُ'], 'أوشك الضيفُ أن يحضرَ'),
    M('5G-2', 'Choose the more frequent construction (“The child almost fell asleep”).', ['كاد الطفلُ ينامُ', 'كاد الطفلُ أن ينامَ'], 'كاد الطفلُ ينامُ'),
    G('5G-3', 'In **كاد خالدٌ يكتبُ**:', ['Answer'], [
        ('Mood of **يكتبُ**', [(['مرفوع', 'منصوب', 'مجزوم'], 'مرفوع')]),
        ('Position of **يكتب** with its implicit subject', [(['في محل نصب خبر كاد', 'في محل رفع', 'لا محل لها'], 'في محل نصب خبر كاد')])]),
    G('5I-1', 'أعرب: **يكاد الباب يسقط**, “The door is nearly falling.”', ['Analysis'], R(
        ['فعل مضارع ناقص مرفوع بالضمة', 'اسم يكاد مرفوع بالضمة', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره هو يعود على الباب',
         'جملة فعلية في محل نصب خبر يكاد', 'فاعل مرفوع بالضمة'],
        [('يكادُ', 'فعل مضارع ناقص مرفوع بالضمة'), ('البابُ', 'اسم يكاد مرفوع بالضمة'), ('يسقطُ', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره هو يعود على الباب'),
         ('يسقط with its subject', 'جملة فعلية في محل نصب خبر يكاد')])),
    M('5I-2', 'A learner says **لم يكد خالد يكتب** proves Khalid did write. Correct the inference.', [
        'Negated كاد alone does not prove occurrence; added context such as **ثم كتبَ** would.',
        'The learner is right: negated كاد always means the act happened after some delay.',
        'It proves Khalid never wrote at all, and no later context can change that.',
        'It means Khalid wrote only a little, so the writing partly occurred.',
        ], 'Negated كاد alone does not prove occurrence; added context such as **ثم كتبَ** would.'),
    G('5I-3', 'In **سقط الطفل أو كاد**, “The child fell, or nearly did”:', ['Answer'], [
        ('Omitted predicate', [(['يسقطُ', 'الطفلُ', 'سقطَ'], 'يسقطُ')]),
        ('اسم كاد', [(['ضمير مستتر تقديره هو، يعود على الطفل', 'الطفلُ', 'none'], 'ضمير مستتر تقديره هو، يعود على الطفل')])]),
    M('5R', 'Compare **يوشك خالدٌ أن يكتبَ** and **عسى خالدٌ أن يكتبَ**.', [
        'Same grammar, اسم plus **أن يكتب** as خبر; **يوشك** is near-occurrence, **عسى** hope.',
        'Same meaning, near-occurrence; **يوشك** takes a مصدر مؤوّل and **عسى** a verbal clause.',
        '**يوشك** is تامّ here with **أن يكتب** as فاعل; **عسى** is ناقص with it as خبر.',
        'Same grammar; **يوشك** expresses hope and **عسى** expresses near-occurrence.',
        ], 'Same grammar, اسم plus **أن يكتب** as خبر; **يوشك** is near-occurrence, **عسى** hope.'),
    M('5-Read', 'Read: **لا يلزم من نفي كاد إثبات وقوع الفعل.** Why may a later sentence still establish occurrence?', [
        'Negated كاد does not itself affirm the act; a later statement can add that it happened.',
        'Negated كاد always affirms the act, so a later sentence only repeats what it says.',
        'Negated كاد always denies the act, so a later sentence would contradict it.',
        'A later sentence changes the mood of the verb after كاد, which changes the meaning.',
        ], 'Negated كاد does not itself affirm the act; a later statement can add that it happened.'),
]

ITEMS['6'] = [
    M('6G-1', 'Complete “The guest began reading”: **أخذ الضيفُ ___ الكتابَ**.', ['يَقْرَأُ', 'أَنْ يَقْرَأَ', 'يَقْرَأَ', 'قَارِئًا'], 'يَقْرَأُ'),
    M('6G-2', 'Correct **أخذ خالدٌ أن يكتبَ** with **أخذ** meaning “began.”', ['أَخَذَ خَالِدٌ يَكْتُبُ', 'أَخَذَ خَالِدٌ يَكْتُبَ', 'أَخَذَ خَالِدًا يَكْتُبُ', 'أَخَذَ خَالِدٌ أَنْ يَكْتُبُ'], 'أَخَذَ خَالِدٌ يَكْتُبُ'),
    M('6G-3', 'Which describes actual beginning?', ['طفق خالدٌ يكتبُ', 'عسى خالدٌ أن يكتبَ', 'كاد خالدٌ يكتبُ'], 'طفق خالدٌ يكتبُ'),
    G('6I-1', 'أعرب: **أنشأ الطالب يحفظ الدرس**, “The student began memorising the lesson.”', ['Analysis'], R(
        ['فعل ماضٍ للشروع مبني على الفتح، يعمل عمل الناقص', 'اسم أنشأ مرفوع بالضمة', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره هو',
         'مفعول به منصوب بالفتحة، عامله يحفظ', 'جملة فعلية في محل نصب خبر أنشأ', 'فاعل مرفوع بالضمة'],
        [('أنشأَ', 'فعل ماضٍ للشروع مبني على الفتح، يعمل عمل الناقص'), ('الطالبُ', 'اسم أنشأ مرفوع بالضمة'), ('يحفظُ', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره هو'),
         ('الدرسَ', 'مفعول به منصوب بالفتحة، عامله يحفظ'), ('يحفظ الدرس', 'جملة فعلية في محل نصب خبر أنشأ')])),
    G('6I-2', 'Compare the roles after **جعل**.', ['النجارُ is', 'What follows is'], [
        ('جعل النجار الخشب بابا (made the wood into a door)', [(['فاعل', 'اسم جعل'], 'فاعل'),
            (['two objects with an underlying predication', 'a verbal clause in محل نصب خبر جعل'], 'two objects with an underlying predication')]),
        ('جعل النجار يفتح الباب (began opening the door)', [(['فاعل', 'اسم جعل'], 'اسم جعل'),
            (['two objects with an underlying predication', 'a verbal clause in محل نصب خبر جعل'], 'a verbal clause in محل نصب خبر جعل')])]),
    M('6I-3', 'Why is **مسحًا** in **طفق مسحًا** not evidence that an inception verb freely takes a simple noun as its خبر?', [
        'It stands for **طفق يمسحُ مسحًا**: the خبر is the understood verb; **مسحًا** is its مفعول مطلق.',
        'It shows **طفق** can take a simple noun as خبر, since **مسحًا** is its accusative خبر.',
        'It stands for **طفق ماسحًا**: **مسحًا** is a حال describing the subject.',
        'It stands for **طفق مسحٌ**: **مسحًا** is the اسم of **طفق**, made accusative by fronting.',
        ], 'It stands for **طفق يمسحُ مسحًا**: the خبر is the understood verb; **مسحًا** is its مفعول مطلق.'),
    G('6R', 'Compare **أوشك الطالب أن يحفظ الدرس** and **أخذ الطالب يحفظ الدرس**.', ['Meaning', 'Ending of يحفظ', 'Predicate'], [
        ('أوشك الطالب أن يحفظ الدرس', [(['near-occurrence', 'beginning'], 'near-occurrence'), (['يحفظَ', 'يحفظُ'], 'يحفظَ'),
            (['مصدر مؤوّل في محل نصب خبر', 'جملة فعلية في محل نصب خبر'], 'مصدر مؤوّل في محل نصب خبر')]),
        ('أخذ الطالب يحفظ الدرس', [(['near-occurrence', 'beginning'], 'beginning'), (['يحفظَ', 'يحفظُ'], 'يحفظُ'),
            (['مصدر مؤوّل في محل نصب خبر', 'جملة فعلية في محل نصب خبر'], 'جملة فعلية في محل نصب خبر')])]),
    M('6-Read', 'Read: **خبر فعل الشروع جملة مضارعية مجرّدة من أنْ.** What do **مضارعية** and **مجرّدة** require?', [
        'The خبر must be a مضارع clause, and it must be free of **أنْ**.',
        'The خبر must be a مضارع clause, and it must be introduced by **أنْ**.',
        'The خبر must be a past-tense clause, and it must be free of **أنْ**.',
        'The خبر must be a single noun, and it must be free of **أل**.',
        ], 'The خبر must be a مضارع clause, and it must be free of **أنْ**.'),
]

ITEMS['7'] = [
    G('7G-1', 'In **نعم الرجل خالد**, supply the endings and roles.', ['Ending', 'Role'], [
        ('الرجل…', [(['الرجلُ', 'الرجلَ'], 'الرجلُ'), (['فاعل نعم', 'مخصوص', 'تمييز'], 'فاعل نعم')]),
        ('خالد…', [(['خالدٌ', 'خالدًا'], 'خالدٌ'), (['فاعل نعم', 'مخصوص', 'تمييز'], 'مخصوص')])]),
    G('7G-2', 'In **نعم رجلًا خالدٌ**:', ['Answer'], [
        ('Role of **رجلًا**', [(['تمييز', 'فاعل', 'مفعول به'], 'تمييز')]),
        ('Where is the subject?', [(['an implicit pronoun in محل رفع فاعل', '**رجلًا**', '**خالدٌ**'], 'an implicit pronoun in محل رفع فاعل')])]),
    G('7G-3', 'Match each term with its meaning.', ['Meaning'], R(
        ['the particular one singled out', 'blame', 'fixed in its verbal paradigm', 'praise'],
        [('مدح', 'praise'), ('ذمّ', 'blame'), ('مخصوص', 'the particular one singled out'), ('جامد', 'fixed in its verbal paradigm')])),
    G('7I-1', 'أعرب: **نعم الخلق الصبر**, “What an excellent character trait patience is!”', ['Analysis'], R(
        ['فعل ماضٍ جامد لإنشاء المدح مبني على الفتح', 'فاعل مرفوع بالضمة', 'مخصوص بالمدح، مبتدأ مؤخّر مرفوع', 'جملة فعلية في محل رفع خبر مقدّم', 'تمييز منصوب'],
        [('نعمَ', 'فعل ماضٍ جامد لإنشاء المدح مبني على الفتح'), ('الخلقُ', 'فاعل مرفوع بالضمة'), ('الصبرُ', 'مخصوص بالمدح، مبتدأ مؤخّر مرفوع'),
         ('نعم الخلق', 'جملة فعلية في محل رفع خبر مقدّم')])),
    G('7I-2', 'Analyse **بئس خلق الرجل الكذب**.', ['Analysis'], R(
        ['فاعل بئس مرفوع، وهو مضاف', 'مضاف إليه مجرور بالكسرة', 'مخصوص بالذمّ، مبتدأ مؤخّر', 'فاعل ثانٍ'],
        [('خلقُ', 'فاعل بئس مرفوع، وهو مضاف'), ('الرجلِ', 'مضاف إليه مجرور بالكسرة'), ('الكذبُ', 'مخصوص بالذمّ، مبتدأ مؤخّر')])),
    M('7I-3', 'Discussing a particular dishonest man, a speaker says **بئس الرجل**. What may be omitted?', [
        'The مخصوص, since context identifies the man; **الرجلُ** stays the فاعل.',
        'The فاعل, since context identifies the man; **الرجلُ** becomes the مخصوص.',
        'The verb, since **بئس** is understood; **الرجلُ** becomes a مبتدأ.',
        'Nothing: without a مخصوص the sentence is ungrammatical.',
        ], 'The مخصوص, since context identifies the man; **الرجلُ** stays the فاعل.'),
    G('7R', 'Identify the role of nominative **خالدٌ** and what supplies the predicate.', ['Role of خالدٌ', 'Predicate'], [
        ('كان خالدٌ صادقًا', [(['اسم كان', 'مخصوص (مبتدأ مؤخّر)', 'فاعل'], 'اسم كان'),
            (['**صادقًا**, خبر كان', 'the whole **نعم الرجل**, in محل رفع خبر'], '**صادقًا**, خبر كان')]),
        ('نعم الرجلُ خالدٌ', [(['اسم كان', 'مخصوص (مبتدأ مؤخّر)', 'فاعل'], 'مخصوص (مبتدأ مؤخّر)'),
            (['**صادقًا**, خبر كان', 'the whole **نعم الرجل**, in محل رفع خبر'], 'the whole **نعم الرجل**, in محل رفع خبر')])]),
    M('7-Read', 'Read: **رجلًا تمييز منصوب، والفاعل ضمير مستتر، وخالد مخصوص بالمدح.** Which sentence is described?', [
        'نِعْمَ رَجُلًا خَالِدٌ', 'نِعْمَ الرَّجُلُ خَالِدٌ', 'كَانَ خَالِدٌ رَجُلًا', 'رَأَيْتُ رَجُلًا خَالِدًا'], 'نِعْمَ رَجُلًا خَالِدٌ'),
]

ITEMS['8'] = [
    G('8G-1', 'Divide **حبّذا** into its components.', ['Analysis'], R(
        ['فعل ماضٍ جامد للمدح', 'اسم إشارة مبني على السكون في محل رفع فاعل', 'مخصوص', 'ضمير مستتر'],
        [('حبَّ', 'فعل ماضٍ جامد للمدح'), ('ذا', 'اسم إشارة مبني على السكون في محل رفع فاعل')])),
    M('8G-2', 'Correct “**حبّذه هندٌ**” when praise is intended.', [
        '**حَبَّذَا هِنْدٌ**: **ذا** stays masculine singular whatever the مخصوص.',
        '**حَبَّذِي هِنْدٌ**: the demonstrative agrees with Hind in gender.',
        '**حَبَّتْ هِنْدٌ**: drop the demonstrative and mark the verb feminine.',
        '**حَبَّذِهِ هِنْدٌ**: the original is already correct for a feminine مخصوص.',
        ], '**حَبَّذَا هِنْدٌ**: **ذا** stays masculine singular whatever the مخصوص.'),
    G('8G-3', 'Classify **راكبًا** and **رجلًا** in the examples.', ['Role'], R(
        ['حال: a derived description of a circumstance', 'تمييز: a non-derived noun specifying a category'],
        [('راكبًا', 'حال: a derived description of a circumstance'), ('رجلًا', 'تمييز: a non-derived noun specifying a category')])),
    G('8I-1', 'أعرب: **لا حبذا الكبر**.', ['Analysis'], R(
        ['حرف نفي، لا محل له من الإعراب', 'فعل ماضٍ جامد مبني على الفتح', 'اسم إشارة مبني على السكون في محل رفع فاعل',
         'مخصوص بالذمّ، مبتدأ مؤخّر مرفوع', 'جملة فعلية منفية في محل رفع خبر مقدّم'],
        [('لا', 'حرف نفي، لا محل له من الإعراب'), ('حبَّ', 'فعل ماضٍ جامد مبني على الفتح'), ('ذا', 'اسم إشارة مبني على السكون في محل رفع فاعل'),
         ('الكبرُ', 'مخصوص بالذمّ، مبتدأ مؤخّر مرفوع'), ('لا حبّذا', 'جملة فعلية منفية في محل رفع خبر مقدّم')])),
    M('8I-2', 'A learner calls **معلّمةٍ** in **حبذا هندٌ من معلمةٍ** منصوب because it specifies Hind. Correct it.', [
        '**معلّمةٍ** is مجرور بمن; specifying through a preposition does not make it accusative.',
        '**معلّمةٍ** is a تمييز منصوب: it specifies Hind, and its fatḥah is hidden by the preposition before it.',
        '**معلّمةٍ** is the فاعل of **حبّ**, genitive in form after **من** but nominative in position.',
        '**معلّمةٍ** is the مخصوص, nominative in position, with the preposition only adding emphasis.',
        ], '**معلّمةٍ** is مجرور بمن; specifying through a preposition does not make it accusative.'),
    G('8I-3', 'In **نعم ما تقرأ**, take **ما** as a relative noun.', ['Analysis'], R(
        ['اسم موصول في محل رفع فاعل نعم', 'صلة الموصول لا محل لها من الإعراب', 'ضمير مستتر تقديره أنت', 'هـ (تقرأه), referring to ما', 'في محل نصب نعت'],
        [('ما', 'اسم موصول في محل رفع فاعل نعم'), ('تقرأ (the clause)', 'صلة الموصول لا محل لها من الإعراب'), ('Subject of تقرأ', 'ضمير مستتر تقديره أنت'),
         ('Understood object-link', 'هـ (تقرأه), referring to ما')])),
    G('8R', 'Give each word’s role.', ['Role'], R(
        ['تمييز', 'خبر كان', 'مخصوص (مبتدأ مؤخّر)', 'اسم كان'],
        [('**رجلًا** in نعم رجلًا خالدٌ', 'تمييز'), ('**خالدٌ** in نعم رجلًا خالدٌ', 'مخصوص (مبتدأ مؤخّر)'),
         ('**صادقًا** in كان خالدٌ صادقًا', 'خبر كان'), ('**خالدٌ** in كان خالدٌ صادقًا', 'اسم كان')])),
    M('8-Read', 'Read: **تلزم ذا الإفراد والتذكير بعد حبّ.** (**تلزم** = keeps to; **الإفراد** = singular; **التذكير** = masculine.) Which follows from it?', [
        'We say **حبّذا هندٌ** and **حبّذا الرجالُ**.',
        'We say **حبّذي هندٌ** and **حبّ أولاء الرجالُ**.',
        'We say **حبّذا هندٌ** but **حبّ أولاء الرجالُ**.',
        'We say **حبّذي هندٌ** but **حبّذا الرجالُ**.',
        ], 'We say **حبّذا هندٌ** and **حبّذا الرجالُ**.'),
]

ITEMS['9'] = [
    G('9G-1', '**ما أحسنَ الصبر…**', ['Answer'], [
        ('Ending', [(['الصبرَ', 'الصبرُ'], 'الصبرَ')]),
        ('Role of the noun', [(['مفعول به', 'فاعل', 'مبتدأ'], 'مفعول به')]),
        ('Subject of **أحسنَ**', [(['ضمير مستتر تقديره هو يعود على ما', 'الصبر', 'ما'], 'ضمير مستتر تقديره هو يعود على ما')])]),
    M('9G-2', 'In **أحسن بالصبر**, what is **الصبر**?', [
        'a subject: genitive in pronunciation, nominative in position',
        'an object: genitive in pronunciation, accusative in position',
        'a genitive noun with no grammatical position',
        'a حال: genitive in pronunciation, accusative in position',
        ], 'a subject: genitive in pronunciation, nominative in position'),
    G('9G-3', 'Match each term with its meaning.', ['Meaning'], R(
        ['middle root position', 'exclamation', 'consonant assimilation'],
        [('تعجّب', 'exclamation'), ('إدغام', 'consonant assimilation'), ('عين الكلمة', 'middle root position')])),
    G('9I-1', 'أعرب: **ما أحسن الصدق**, using the interrogative analysis of ما.', ['Analysis'], R(
        ['اسم استفهام للتعجّب في محل رفع مبتدأ', 'فعل ماضٍ لإنشاء التعجّب مبني على الفتح', 'مفعول به منصوب بالفتحة', 'جملة فعلية في محل رفع خبر', 'فاعل مرفوع'],
        [('ما', 'اسم استفهام للتعجّب في محل رفع مبتدأ'), ('أحسنَ', 'فعل ماضٍ لإنشاء التعجّب مبني على الفتح'), ('الصدقَ', 'مفعول به منصوب بالفتحة'),
         ('أحسن الصدق', 'جملة فعلية في محل رفع خبر')])),
    G('9I-2', 'Correct each form for exclamation.', ['Correct form'], [
        ('ما أطالَ النهرَ!', [(['مَا أَطْوَلَ النَّهْرَ!', 'مَا أَطَالَ النَّهْرَ!', 'مَا أَطْيَلَ النَّهْرَ!'], 'مَا أَطْوَلَ النَّهْرَ!')]),
        ('أَبِرَّ بخالدٍ!', [(['أَبْرِرْ بِخَالِدٍ!', 'أَبِرَّ بِخَالِدٍ!', 'أَبَرَّ خَالِدًا!'], 'أَبْرِرْ بِخَالِدٍ!')])]),
    G('9I-3', 'Exclaim about the length of a **طَرِيق** using **أَفْعِلْ بِهِ**.', ['Answer'], [
        ('Exclamation', [(['أَطْوِلْ بِالطَّرِيقِ!', 'أَطِلْ بِالطَّرِيقِ!', 'أَطْوِلِ الطَّرِيقَ!'], 'أَطْوِلْ بِالطَّرِيقِ!')]),
        ('**الطريقِ**', [(['فاعل مجرور لفظًا بالباء، مرفوع محلًّا', 'مفعول به', 'اسم مجرور لا محل له'], 'فاعل مجرور لفظًا بالباء، مرفوع محلًّا')])]),
    G('9R', 'Give the role of **الصبر** in each.', ['Role and ending'], R(
        ['مخصوص بالمدح، مبتدأ مؤخّر مرفوع بالضمة', 'مفعول به منصوب بالفتحة', 'فاعل مجرور لفظًا بالباء، مرفوع محلًّا'],
        [('نعم الخلقُ الصبرُ', 'مخصوص بالمدح، مبتدأ مؤخّر مرفوع بالضمة'), ('ما أحسنَ الصبرَ', 'مفعول به منصوب بالفتحة'),
         ('أحسنْ بالصبرِ', 'فاعل مجرور لفظًا بالباء، مرفوع محلًّا')])),
    M('9-Read', 'Read: **المجرور لفظًا قد يكون مرفوعًا محلًّا.** How does it apply to **أحسن بالصبر**?', [
        'The preposition explains the kasrah of **الصبرِ**, while the construction makes it the subject.',
        'The preposition explains the kasrah of **الصبرِ**, while the construction makes it the object.',
        '**الصبرِ** has no position: it is simply governed by the preposition.',
        '**أحسن** has an implicit subject أنت, and **بالصبر** is attached to it as a ظرف لغو.',
        ], 'The preposition explains the kasrah of **الصبرِ**, while the construction makes it the subject.'),
]

A1O = ['اسم الفعل الناقص', 'خبر الفعل الناقص', 'فاعل', 'مخصوص', 'تمييز', 'مصدر مؤوّل']
C1O = ['فعل ماضٍ ناقص مبني على الفتح', 'اسم كان مرفوع بالضمة', 'ظرف مستقرّ في محل نصب خبر كان', 'فعل ماضٍ ناقص للمقاربة مبني على الفتح',
       'مضارع منصوب بأن؛ فاعله مستتر تقديره هو', 'مصدر مؤوّل في محل نصب خبر أوشك', 'فعل ماضٍ للشروع، يعمل عمل الناقص',
       'ضمير مستتر تقديره هو في محل رفع اسم أخذ', 'جملة فعلية في محل نصب خبر أخذ']
C2O = ['اسم كان مرفوع بالضمة', 'ضمير مستتر تقديره هو في محل رفع اسم زال', 'تمييز منصوب بالفتحة', 'مخصوص، مبتدأ مؤخّر مرفوع',
       'اسم إشارة في محل رفع فاعل', 'حال منصوب بالفتحة', 'اسم استفهام للتعجّب في محل رفع مبتدأ', 'مفعول به منصوب بالفتحة']

ITEMS['R'] = [
    G('A1', 'Match each element to its label.', ['Label'], R(A1O, [
        ('**خالدٌ** in كان خالدٌ صادقًا', A1O[0]), ('**صادقًا** in كان خالدٌ صادقًا', A1O[1]), ('**حربٌ** in كانت حربٌ (A war occurred)', A1O[2]),
        ('**خالدٌ** in نعم الرجلُ خالدٌ', A1O[3]), ('**رجلًا** in نعم رجلًا خالدٌ', A1O[4]), ('**أن يحضر خالد** in عسى أن يحضر خالد (complete analysis)', A1O[5])])),
    M('A2', 'What is the difference between **ناقص** and **ناقص التصرّف**?', [
        '**ناقص**: needs an اسم and خبر. **ناقص التصرّف**: restricted forms. **كان** is only ناقص; **ما زال** is both.',
        '**ناقص**: restricted forms. **ناقص التصرّف**: needs a خبر. **كان** is both; **ما زال** is only ناقص.',
        '**ناقص**: needs an اسم and خبر. **ناقص التصرّف**: restricted forms. **كان** is both; **ما زال** neither.',
        'The two terms mean the same: both describe a verb needing an اسم and خبر, like **كان**.',
        ], '**ناقص**: needs an اسم and خبر. **ناقص التصرّف**: restricted forms. **كان** is only ناقص; **ما زال** is both.'),
    G('B1', 'Choose the correctly vowelled sentence.', ['Correct form'], [
        ('لم يكن الضيفـ… حاضرـ…', [(['لَمْ يَكُنِ الضَّيْفُ حَاضِرًا', 'لَمْ يَكُنِ الضَّيْفَ حَاضِرٌ', 'لَمْ يَكُنْ الضَّيْفُ حَاضِرٌ'], 'لَمْ يَكُنِ الضَّيْفُ حَاضِرًا')]),
        ('حرى الطالبـ… أن ينجحـ…', [(['حَرَى الطَّالِبُ أَنْ يَنْجَحَ', 'حَرَى الطَّالِبَ أَنْ يَنْجَحُ', 'حَرَى الطَّالِبُ أَنْ يَنْجَحُ'], 'حَرَى الطَّالِبُ أَنْ يَنْجَحَ')]),
        ('أخذ الطفلـ… يقرأـ… الكتابـ…', [(['أَخَذَ الطِّفْلُ يَقْرَأُ الكِتَابَ', 'أَخَذَ الطِّفْلُ يَقْرَأَ الكِتَابَ', 'أَخَذَ الطِّفْلَ يَقْرَأُ الكِتَابُ'], 'أَخَذَ الطِّفْلُ يَقْرَأُ الكِتَابَ')]),
        ('بئس الخلقـ… الكذبـ…', [(['بِئْسَ الخُلُقُ الكَذِبُ', 'بِئْسَ الخُلُقَ الكَذِبُ', 'بِئْسَ الخُلُقُ الكَذِبَ'], 'بِئْسَ الخُلُقُ الكَذِبُ')])]),
    M('B2-1', 'Correct: “**ما دام** means ‘did not last’ in every construction.”', [
        'In the duration construction it means “as long as”: its ما is مصدرية ظرفية, not negative.',
        'It means “did not last” in every use, because the ما before a past verb is always the negative particle.',
        'It means “still”, because negating the verb of lasting gives continuation, just like **ما زال**.',
        'It means “never lasted”, because ما negates and دام is past.',
        ], 'In the duration construction it means “as long as”: its ما is مصدرية ظرفية, not negative.', sol='B2'),
    M('B2-2', 'Correct **أخذ خالدٌ أن يكتبَ**, intended as “Khalid began writing.”', [
        'أَخَذَ خَالِدٌ يَكْتُبُ', 'أَخَذَ خَالِدٌ أَنْ يَكْتُبُ', 'أَخَذَ خَالِدًا يَكْتُبُ'], 'أَخَذَ خَالِدٌ يَكْتُبُ', sol='B2'),
    M('B2-3', 'Correct: “The خبر of كاد is always a single accusative noun.”', [
        'The usual خبر is a verbal clause: it occupies نصب while **يكتبُ** stays مرفوع.',
        'The claim is correct: كاد takes a single accusative noun such as **كاتبًا**.',
        'The خبر of كاد is always a مصدر مؤوّل introduced by **أنْ**.',
        'كاد is تامّ, so it takes a فاعل and needs no خبر.',
        ], 'The usual خبر is a verbal clause: it occupies نصب while **يكتبُ** stays مرفوع.', sol='B2'),
    M('B2-4', 'Correct: “The demonstrative in **حبذا هندٌ** must become feminine.”', [
        'Keep **حبّذا هندٌ**: **ذا** stays masculine singular in this formula.',
        'Say **حبّذي هندٌ**, so that **ذا** agrees with the feminine مخصوص.',
        'Say **حبّتا هندٌ**, marking the verb feminine to agree with Hind.',
        ], 'Keep **حبّذا هندٌ**: **ذا** stays masculine singular in this formula.', sol='B2'),
    M('B2-5', 'Correct: “In **أحسن بالصبر**, the noun is an ordinary object because a preposition precedes it.”', [
        'The bāʾ is زائد and the noun is the subject: genitive in form, nominative in position.',
        'The bāʾ is original and the noun is the object: genitive in form, accusative in position.',
        'The noun is a حال describing the exclamation, genitive because of the bāʾ.',
        'The verb has an implicit subject أنت, and the noun is attached to it with the bāʾ.',
        ], 'The bāʾ is زائد and the noun is the subject: genitive in form, nominative in position.', sol='B2'),
    M('B2-6', 'Correct: “**لم يكد خالدٌ يكتبُ** necessarily means that Khalid wrote.”', [
        'Negated كاد alone does not prove the writing happened; wider context may.',
        'It does prove it: negating كاد always affirms that the writing happened.',
        'It proves the opposite: Khalid certainly never wrote at any time.',
        'It means Khalid almost wrote and then did, so it states both facts.',
        ], 'Negated كاد alone does not prove the writing happened; wider context may.', sol='B2'),
    G('C1', 'Passage 1: **كَانَ الضَّيْفُ عِنْدَ البَابِ. لَمْ يَكُنْ خَالِدٌ حَاضِرًا. أَوْشَكَ خَالِدٌ أَنْ يَحْضُرَ. ثُمَّ حَضَرَ. أَخَذَ يَفْتَحُ البَابَ. صَارَ الضَّيْفُ فِي البَيْتِ.** Choose the analysis of each part.', ['Analysis'], R(C1O, [
        ('كانَ', 'فعل ماضٍ ناقص مبني على الفتح'), ('الضيفُ (first sentence)', 'اسم كان مرفوع بالضمة'), ('عند الباب', 'ظرف مستقرّ في محل نصب خبر كان'),
        ('أوشكَ', 'فعل ماضٍ ناقص للمقاربة مبني على الفتح'), ('يحضرَ', 'مضارع منصوب بأن؛ فاعله مستتر تقديره هو'), ('أن يحضر', 'مصدر مؤوّل في محل نصب خبر أوشك'),
        ('أخذَ', 'فعل ماضٍ للشروع، يعمل عمل الناقص'), ('اسم أخذ', 'ضمير مستتر تقديره هو في محل رفع اسم أخذ'), ('يفتح الباب', 'جملة فعلية في محل نصب خبر أخذ')])),
    G('C1-b', 'Passage 1: contrast the verbs in their intended meanings.', ['Answer'], [
        ('أوشك', [(['presents the event as imminent', 'presents its beginning'], 'presents the event as imminent')]),
        ('أخذ', [(['presents the event as imminent', 'presents its beginning'], 'presents its beginning')]),
        ('حضر', [(['تامّ: complete with its subject', 'ناقص: needs a خبر'], 'تامّ: complete with its subject')]),
        ('صار (صار الضيف في البيت)', [(['تامّ: complete with its subject', 'ناقص: needs a خبر'], 'ناقص: needs a خبر')])], sol='C1'),
    G('C2', 'Passage 2: **كَانَ الطَّالِبُ يَقْرَأُ. مَا زَالَ يَقْرَأُ. نِعْمَ رَجُلًا الطَّالِبُ. حَبَّذَا الطَّالِبُ قَارِئًا. مَا أَحْسَنَ الصَّبْرَ!** Choose the analysis of each part.', ['Analysis'], R(C2O, [
        ('الطالبُ (first sentence)', 'اسم كان مرفوع بالضمة'), ('اسم زال', 'ضمير مستتر تقديره هو في محل رفع اسم زال'), ('رجلًا', 'تمييز منصوب بالفتحة'),
        ('الطالبُ (third sentence)', 'مخصوص، مبتدأ مؤخّر مرفوع'), ('ذا', 'اسم إشارة في محل رفع فاعل'), ('قارئًا', 'حال منصوب بالفتحة'),
        ('ما (last sentence)', 'اسم استفهام للتعجّب في محل رفع مبتدأ'), ('الصبرَ', 'مفعول به منصوب بالفتحة')])),
    G('D1', 'Match each statement to the example that illustrates it.', ['Example'], R(
        ['**أخذ يكتبُ**', '**عسى أن يحضرَ خالدٌ**', '**الكتابَ كان خالدٌ يقرأُ**', '**نِعْمَتِ المَرْأَةُ هِنْدٌ**'],
        [('قد يكون اسم الفعل الناقص ضميرًا مستترًا.', '**أخذ يكتبُ**'), ('المصدر المؤوّل بعد عسى التامّة في محل رفع فاعل.', '**عسى أن يحضرَ خالدٌ**'),
         ('قد يتقدّم معمول الخبر على الفعل الناقص.', '**الكتابَ كان خالدٌ يقرأُ**'), ('التاء في نعمت حرف تأنيث وليست فاعلًا.', '**نِعْمَتِ المَرْأَةُ هِنْدٌ**')])),
    G('D2', '**ذا اسم إشارة في محل رفع فاعل. وخالد مخصوص بالمدح، يعرب مبتدأ مؤخّرًا، والجملة قبله في محل رفع خبر.**', ['Answer'], [
        ('Expression analysed', [(['حَبَّذَا خَالِدٌ', 'نِعْمَ الرَّجُلُ خَالِدٌ', 'هَذَا خَالِدٌ'], 'حَبَّذَا خَالِدٌ')]),
        ('Changed to blame', [(['لَا حَبَّذَا خَالِدٌ', 'حَبَّذِي خَالِدٌ', 'بِئْسَ ذَا خَالِدٌ'], 'لَا حَبَّذَا خَالِدٌ')]),
        ('What remains unchanged?', [(['ذا is still the فاعل and خالد still the مخصوص', 'nothing: every role changes'], 'ذا is still the فاعل and خالد still the مخصوص')])]),
    G('E1', '**حَرَى المُسَافِرُ أَنْ يَصِلَ. أَخَذَ المُسَافِرُ يَسْأَلُ.** Choose the analysis of each part.', ['Analysis'], R(
        ['فعل ماضٍ ناقص مبني على الفتح المقدّر', 'اسم حرى مرفوع بالضمة', 'مضارع منصوب بأن؛ فاعله مستتر تقديره هو', 'مصدر مؤوّل في محل نصب خبر حرى',
         'فعل ماضٍ للشروع، يعمل عمل الناقص', 'اسم أخذ مرفوع بالضمة', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره هو', 'جملة فعلية في محل نصب خبر أخذ'],
        [('حرى', 'فعل ماضٍ ناقص مبني على الفتح المقدّر'), ('المسافرُ (first)', 'اسم حرى مرفوع بالضمة'), ('يصلَ', 'مضارع منصوب بأن؛ فاعله مستتر تقديره هو'),
         ('أن يصل', 'مصدر مؤوّل في محل نصب خبر حرى'), ('أخذَ', 'فعل ماضٍ للشروع، يعمل عمل الناقص'), ('المسافرُ (second)', 'اسم أخذ مرفوع بالضمة'),
         ('يسألُ', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره هو'), ('يسأل with its subject', 'جملة فعلية في محل نصب خبر أخذ')])),
    G('E2', 'Produce three sentences about **الصِّدْق**.', ['Sentence', 'الصدق is'], [
        ('“Truthfulness is not blameworthy” (**ليس**, **مذموم**)', [(['لَيْسَ الصِّدْقُ مَذْمُومًا', 'لَيْسَ الصِّدْقَ مَذْمُومٌ', 'لَيْسَ الصِّدْقُ مَذْمُومٌ'], 'لَيْسَ الصِّدْقُ مَذْمُومًا'),
            (['اسم ليس مرفوع', 'مفعول به منصوب', 'فاعل مجرور لفظًا مرفوع محلًّا'], 'اسم ليس مرفوع')]),
        ('“How excellent truthfulness is” (**ما أفعل**)', [(['مَا أَحْسَنَ الصِّدْقَ!', 'مَا أَحْسَنُ الصِّدْقِ!', 'مَا أَحْسَنَ الصِّدْقُ!'], 'مَا أَحْسَنَ الصِّدْقَ!'),
            (['اسم ليس مرفوع', 'مفعول به منصوب', 'فاعل مجرور لفظًا مرفوع محلًّا'], 'مفعول به منصوب')]),
        ('The same with **أفعل به**', [(['أَحْسِنْ بِالصِّدْقِ!', 'أَحْسِنِ الصِّدْقَ!', 'أَحْسَنَ بِالصِّدْقِ!'], 'أَحْسِنْ بِالصِّدْقِ!'),
            (['اسم ليس مرفوع', 'مفعول به منصوب', 'فاعل مجرور لفظًا مرفوع محلًّا'], 'فاعل مجرور لفظًا مرفوع محلًّا')])]),
]
