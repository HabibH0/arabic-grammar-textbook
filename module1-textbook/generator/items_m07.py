# Module 7: Particles without Government. Auto-checked items; correct answers follow the Module 7 answers file.
from item_kit import M, G, R

ITEMS = {}

ITEMS['1'] = [
    G('1G-1', 'Match each meaning.', ['Meaning'], R(
        ['joining', 'endpoint', 'close succession', 'an interval'], [('جمع', 'joining'), ('تعقيب', 'close succession'), ('تراخٍ', 'an interval'), ('غاية', 'endpoint')])),
    M('1G-2', 'Choose: **رَأَيْتُ خَالِدًا وَسَعِيدٌ / سَعِيدًا / سَعِيدٍ**.', [
        '**سعيدًا**: it follows the object **خالدًا** by coordination.',
        '**سعيدٌ**: after و a new subject begins, so it is nominative.',
        '**سعيدٍ**: و governs like a preposition, so it is genitive.',
        '**سعيدًا**: و itself assigns نصب to the noun after it.',
        ], '**سعيدًا**: it follows the object **خالدًا** by coordination.'),
    M('1G-3', 'Does **جاء خالد وسعيد** prove that Khalid came first?', [
        'No: و only joins; the order needs other evidence, and they may have come together.',
        'Yes: with simple و, the first name mentioned is always the one who arrived first, so Khalid came first.',
        'Yes: و means “then” in a narrative like this, so Khalid came first and Saʿīd after him.',
        'No: with و the second name arrived first.',
        ], 'No: و only joins; the order needs other evidence, and they may have come together.'),
    G('1I-1', '**مررت بخالد وسعيد**, “I passed by Khalid and Saʿīd.”', ['Analysis'], R(
        ['حرف جرّ', 'اسم مجرور بالباء، وهو المعطوف عليه', 'حرف عطف', 'معطوف على خالد مجرور بالكسرة', 'فاعل مرفوع'],
        [('بـ', 'حرف جرّ'), ('خالدٍ', 'اسم مجرور بالباء، وهو المعطوف عليه'), ('و', 'حرف عطف'), ('سعيدٍ', 'معطوف على خالد مجرور بالكسرة')])),
    G('1I-2', 'In **قرأت الكتاب حتى آخرَه**, “I read the book, even its end”:', ['Answer'], [
        ('Why is **آخرَ** accusative?', [(['it is coordinated with the object الكتابَ', 'حتى makes it accusative', 'it is a حال'], 'it is coordinated with the object الكتابَ')]),
        ('Why would **حتى التفاحةَ** fail?', [(['an apple is not part of the book', 'التفاحة is feminine', 'حتى cannot take a definite noun'], 'an apple is not part of the book')])]),
    G('1R', 'Analyse **لَمْ يَقْرَأْ خَالِدٌ الدَّرْسَ وَالمِثَالَ**.', ['Analysis'], R(
        ['حرف نفي وجزم وقلب', 'مضارع مجزوم بلم بالسكون', 'فاعل مرفوع بالضمة', 'مفعول به منصوب بالفتحة', 'معطوف على الدرس منصوب بالفتحة', 'منصوب بالواو'],
        [('لم', 'حرف نفي وجزم وقلب'), ('يقرأْ', 'مضارع مجزوم بلم بالسكون'), ('خالدٌ', 'فاعل مرفوع بالضمة'), ('الدرسَ', 'مفعول به منصوب بالفتحة'), ('المثالَ', 'معطوف على الدرس منصوب بالفتحة')])),
    M('1-Read', 'Read: **المعطوف يتبع المعطوف عليه في الإعراب.** (**يتبع** = follows.) In **أكلت السمكةَ حتى رأسَها**, what gives **رأس** its fatḥah?', [
        'It follows the accusative object **السمكةَ** by coordination.',
        '**حتى** assigns نصب to the noun after it as a preposition.',
        'It is a حال describing the fish at the moment of eating.',
        'It is the object of an omitted verb, **أكلت رأسها**.',
        ], 'It follows the accusative object **السمكةَ** by coordination.'),
]

ITEMS['2'] = [
    G('2G-1', 'Complete for the intended meaning.', ['Particle'], R(
        ['لا', 'لكنْ', 'بل', 'أو'],
        [('جاء خالدٌ ___ سعيدٌ (“Khalid, not Saʿīd, came”)', 'لا'), ('ما جاء خالدٌ ___ سعيدٌ (“Khalid did not come, but Saʿīd did”)', 'لكنْ')])),
    G('2G-2', 'Explain the difference.', ['What بل does'], R(
        ['replaces the affirmative identification of Khalid with Saʿīd', 'keeps the denial about Khalid and affirms seeing Saʿīd'],
        [('رأيت خالدًا بل سعيدًا', 'replaces the affirmative identification of Khalid with Saʿīd'), ('ما رأيت خالدًا بل سعيدًا', 'keeps the denial about Khalid and affirms seeing Saʿīd')])),
    G('2G-3', 'In **ما رأيت خالدًا ولا سعيدًا**:', ['Answer'], [
        ('Which particle coordinates?', [(['و', 'لا', 'ما'], 'و')]),
        ('What does **لا** contribute?', [(['it reinforces the negation for each one (زائدة في الإعراب)', 'it is a second conjunction', 'it governs سعيدًا'], 'it reinforces the negation for each one (زائدة في الإعراب)')])]),
    G('2I-1', '**أقرأت الدرس أم المثال؟**', ['Answer'], [
        ('Vowelled', [(['أَقَرَأْتَ الدَّرْسَ أَمِ المِثَالَ؟', 'أَقَرَأْتَ الدَّرْسُ أَمِ المِثَالُ؟', 'أَقَرَأْتَ الدَّرْسَ أَمِ المِثَالِ؟'], 'أَقَرَأْتَ الدَّرْسَ أَمِ المِثَالَ؟')]),
        ('A suitable answer', [(['قرأتُ المثالَ', 'نعم', 'بلى'], 'قرأتُ المثالَ')])]),
    M('2I-2', 'Correct: “**لا تطع كاذبًا أو ظالمًا** permits obedience to either one, provided that you do not obey both.”', [
        'The prohibition covers either one: obey neither the liar nor the oppressor.',
        'The claim is correct: أو gives a choice, so obeying one of them is allowed.',
        'It forbids obeying both together, but obeying one alone is allowed.',
        'It commands obeying one of them, since أو offers alternatives.',
        ], 'The prohibition covers either one: obey neither the liar nor the oppressor.'),
    G('2R', 'Analyse **ما مررت بخالد لكن سعيد**.', ['Answer'], [
        ('سعيد…', [(['سعيدٍ: معطوف على خالد مجرور', 'سعيدٌ: مبتدأ', 'سعيدًا: منصوب'], 'سعيدٍ: معطوف على خالد مجرور')]),
        ('Why does **لكنْ** meet its conditions?', [(['it follows negation and has no و attached', 'it follows an affirmative statement', 'it has a shaddah'], 'it follows negation and has no و attached')])]),
    M('2-Read', 'Read: **يشترط في لكنْ العاطفة أن يسبقها نفي أو نهي.** (**يشترط** = it is required; **يسبقها** = precedes it.) What does it say?', [
        'Coordinating **لكنْ** requires a preceding negation or prohibition.',
        'Coordinating **لكنْ** requires a preceding affirmative statement.',
        'Coordinating **لكنْ** requires a following و, as in **ولكنْ**.',
        'Coordinating **لكنْ** governs its own اسم and خبر like **لكنّ**.',
        ], 'Coordinating **لكنْ** requires a preceding negation or prohibition.'),
]

ITEMS['3'] = [
    G('3G-1', 'Classify each question.', ['Type'], R(['تصديق', 'تصوّر'], [('هل فهمتَ؟', 'تصديق'), ('أخالدًا رأيتَ أم سعيدًا؟', 'تصوّر')])),
    G('3G-2', 'Reply to **ألم تقرأ الدرس؟**', ['Reply'], R(
        ['بلى، قرأتُ الدرسَ', 'نعم، لم أقرأِ الدرسَ', 'نعم، قرأتُ الدرسَ'],
        [('to assert that you read it', 'بلى، قرأتُ الدرسَ'), ('to confirm that you did not', 'نعم، لم أقرأِ الدرسَ')])),
    M('3G-3', 'Affirming an affirmative question before **واللهِ**:', ['إي واللهِ', 'بلى واللهِ'], 'إي واللهِ'),
    M('3I-1', 'Correct **هل لم يحضر خالد؟**', ['أَلَمْ يَحْضُرْ خَالِدٌ؟', 'هَلْ لَا يَحْضُرُ خَالِدٌ؟', 'أَلَنْ يَحْضُرَ خَالِدٌ؟', 'هَلْ يَحْضُرْ خَالِدٌ؟'], 'أَلَمْ يَحْضُرْ خَالِدٌ؟'),
    M('3I-2', 'In an affirmative response **إنَّهْ**, what is the final هْ?', [
        'هاء السكت: **إنّ** is an answer particle here',
        'an object pronoun in محل نصب, serving as the اسم of **إنّ**',
        'a pronoun in محل رفع, serving as the خبر of **إنّ**',
        'a feminine marker on the answer particle',
        ], 'هاء السكت: **إنّ** is an answer particle here'),
    G('3R', '**أرأيت المعلم أم الطالب؟**', ['Answer'], [
        ('المعلم…', [(['مفعول به منصوب', 'فاعل مرفوع', 'مبتدأ'], 'مفعول به منصوب')]),
        ('الطالب…', [(['معطوف منصوب', 'مبتدأ مرفوع', 'مجرور'], 'معطوف منصوب')]),
        ('Is **نعم** enough?', [(['No: answer, e.g., رأيتُ المعلمَ', 'Yes'], 'No: answer, e.g., رأيتُ المعلمَ')])]),
    M('3-Read', 'Read: **نعم لتصديق الكلام، وبلى لإيجاب المنفي.** To “Did he not travel?”, what do the replies mean?', [
        '**نعم** confirms he did not travel; **بلى** asserts that he travelled.',
        '**نعم** asserts that he travelled; **بلى** confirms he did not.',
        'Both **نعم** and **بلى** assert that he travelled.',
        'Both **نعم** and **بلى** confirm that he did not travel.',
        ], '**نعم** confirms he did not travel; **بلى** asserts that he travelled.'),
]

ITEMS['4'] = [
    G('4G-1', 'Choose the endings.', ['Correct'], [
        ('إنَّ الطالبَ لَحاضر…', [(['لَحاضرٌ', 'لَحاضرًا'], 'لَحاضرٌ')]),
        ('إنَّ الطالبَ لَيكتب…', [(['لَيكتبُ', 'لَيكتبَ'], 'لَيكتبُ')])]),
    G('4G-2', 'In **إنَّ في المسجدِ لَرجلًا**:', ['Role'], R(
        ['اسم إنّ مؤخر منصوب', 'خبر إنّ مقدم، في محل رفع', 'مجرور باللام'],
        [('رجلًا', 'اسم إنّ مؤخر منصوب'), ('في المسجد', 'خبر إنّ مقدم، في محل رفع')])),
    G('4G-3', 'Match each context to the meaning of **قد**.', ['Meaning'], R(
        ['تقليل', 'توقّع', 'تحقيق'], [('rare truth from a liar', 'تقليل'), ('a recovery anticipated', 'توقّع'), ('a past arrival confirmed', 'تحقيق')])),
    G('4I-1', 'Analyse **إن الضيف لفي البيت**.', ['Analysis'], R(
        ['اسم إنّ منصوب بالفتحة', 'اللام المزحلقة', 'اسم مجرور بالكسرة', 'شبه جملة في محل رفع خبر إنّ', 'حرف جرّ'],
        [('الضيفَ', 'اسم إنّ منصوب بالفتحة'), ('لَـ', 'اللام المزحلقة'), ('البيتِ', 'اسم مجرور بالكسرة'), ('في البيت', 'شبه جملة في محل رفع خبر إنّ')])),
    M('4I-2', 'Correct: “The fatḥah in **لأكتبنَّ** proves that نون التوكيد is a حرف نصب.”', [
        'The verb is مبني على الفتح by attachment to the nūn, in محل رفع; the nūn does not govern.',
        'The claim is correct: نون التوكيد puts the verb in نصب, just as **لن** does, which is why the fatḥah appears.',
        'The verb is منصوب by the lām of the oath, and the nūn only adds emphasis to that lām.',
        'The verb is مجزوم; the fatḥah only avoids two vowelless letters.',
        ], 'The verb is مبني على الفتح by attachment to the nūn, in محل رفع; the nūn does not govern.'),
    G('4R', 'In **هل قد وصل الضيف؟**:', ['Answer'], [
        ('هل', [(['asks whether the judgement is true', 'confirms the past occurrence'], 'asks whether the judgement is true')]),
        ('قد', [(['asks whether the judgement is true', 'confirms the past occurrence'], 'confirms the past occurrence')]),
        ('Affirmative reply', [(['نعم، قد وصلَ الضيفُ', 'بلى، قد وصلَ الضيفَ'], 'نعم، قد وصلَ الضيفُ')]),
        ('Why is **الضيف** nominative?', [(['it is the فاعل of وصل', 'هل assigns رفع', 'قد assigns رفع'], 'it is the فاعل of وصل')])]),
    M('4-Read', 'Read: **قد تدخل على الماضي والمضارع، ويتعيّن معناها بالسياق.** (**يتعيّن** = is determined; **السياق** = context.) What does it say?', [
        '**قد** occurs with past and imperfect verbs; context sets its meaning.',
        '**قد** occurs only with past verbs; with an imperfect it is an error.',
        '**قد** with an imperfect always means rarity, whatever the context.',
        '**قد** governs the following verb in نصب, past or imperfect.',
        ], '**قد** occurs with past and imperfect verbs; context sets its meaning.'),
]

ITEMS['5'] = [
    G('5G-1', 'For **لو جاء الضيف لأكرمتُه**:', ['Answer'], [
        ('His arrival', [(['(b) did not occur', '(a) occurred'], '(b) did not occur')]),
        ('Must all honouring of him be denied?', [(['No: he might be honoured for another reason', 'Yes'], 'No: he might be honoured for another reason')])]),
    G('5G-2', '“Without the teacher, the student would have gone astray.”', ['Answer'], [
        ('Sentence', [(['لَوْلَا المُعَلِّمُ لَضَلَّ الطَّالِبُ', 'لَوْلَا المُعَلِّمَ لَضَلَّ الطَّالِبَ', 'لَوْلَا المُعَلِّمِ ضَلَّ الطَّالِبُ'], 'لَوْلَا المُعَلِّمُ لَضَلَّ الطَّالِبُ')]),
        ('المعلمُ', [(['مبتدأ مرفوع، خبره محذوف تقديره موجود', 'فاعل لولا', 'اسم لولا منصوب'], 'مبتدأ مرفوع، خبره محذوف تقديره موجود')])]),
    M('5G-3', 'Supply endings: **أما خالد فصادق، وأما سعيد فكاذب**.', [
        'أَمَّا خَالِدٌ فَصَادِقٌ، وَأَمَّا سَعِيدٌ فَكَاذِبٌ', 'أَمَّا خَالِدًا فَصَادِقًا، وَأَمَّا سَعِيدًا فَكَاذِبًا', 'أَمَّا خَالِدٍ فَصَادِقٍ، وَأَمَّا سَعِيدٍ فَكَاذِبٍ'],
        'أَمَّا خَالِدٌ فَصَادِقٌ، وَأَمَّا سَعِيدٌ فَكَاذِبٌ'),
    G('5I-1', 'Analyse **لو سعيدًا لقيتُه لأكرمتُه**, “Had I met Saʿīd, I would have honoured him.”', ['Analysis'], R(
        ['حرف شرط غير جازم', 'مفعول به لفعل محذوف يفسّره لقيتُه', 'مفعول به، يعود على سعيد', 'مفعول به لـ لو'],
        [('لو', 'حرف شرط غير جازم'), ('سعيدًا', 'مفعول به لفعل محذوف يفسّره لقيتُه'), ('هُ in لقيته', 'مفعول به، يعود على سعيد'), ('هُ in لأكرمته', 'مفعول به، يعود على سعيد')])),
    G('5I-2', 'Explain the different cases (do not assign case to أما).', ['Role'], R(
        ['مبتدأ مرفوع', 'مفعول به مقدم منصوب، عامله تُهِنْ'],
        [('أما الضيفُ فحاضرٌ', 'مبتدأ مرفوع'), ('أما الضيفَ فلا تُهِنْ', 'مفعول به مقدم منصوب، عامله تُهِنْ')])),
    G('5R', 'Compare the two conditionals.', ['Governs جزم?', 'Verbs'], [
        ('إنْ يَحْضُرْ خالدٌ أُكْرِمْهُ', [(['Yes: إنْ', 'No: لو'], 'Yes: إنْ'), (['both مجزوم بالسكون', 'past forms with fixed endings'], 'both مجزوم بالسكون')]),
        ('لو حضر خالدٌ لأكرمتُهُ', [(['Yes: إنْ', 'No: لو'], 'No: لو'), (['both مجزوم بالسكون', 'past forms with fixed endings'], 'past forms with fixed endings')])]),
    M('5-Read', 'Read: **لو غير جازمة، ولولا تدلّ على وجود الشرط.** In **لولا العلم لضل الناس**, what exists and what is prevented?', [
        'Knowledge exists, and it prevents people from going astray.',
        'Knowledge is absent, and that is why people went astray.',
        'Knowledge does not exist, so going astray is only supposed.',
        'Knowledge exists, and it causes people to go astray.',
        ], 'Knowledge exists, and it prevents people from going astray.'),
]

ITEMS['6'] = [
    G('6G-1', 'Match each to its force.', ['Force'], R(
        ['توبيخ', 'تحضيض', 'عرض'],
        [('هلا كتبتَ! (after an opportunity was missed)', 'توبيخ'), ('هلا تكتبُ! (an urgent request)', 'تحضيض'), ('ألا تكتبُ؟ (a gentle suggestion)', 'عرض')])),
    G('6G-2', 'Which has a conditional response?', ['Conditional response?'], R(
        ['Yes: فشل الطالب is the response prevented by the teacher’s presence', 'No: it urges help'],
        [('لولا المعلمُ لفشلَ الطالبُ', 'Yes: فشل الطالب is the response prevented by the teacher’s presence'), ('لولا تساعدُ الطالبَ!', 'No: it urges help')])),
    M('6G-3', 'What is **ها** in **هذا** and **ها قد حضر خالدٌ**?', [
        '**ها التنبيه** in both; neither means “her”',
        'a pronoun meaning “her” in both',
        'a pronoun in **هذا**, but **ها التنبيه** in the other',
        '**ها التنبيه** in **هذا**, but a pronoun in the other',
        ], '**ها التنبيه** in both; neither means “her”'),
    G('6I-1', 'Analyse **ألا تجلس عند الباب؟** (a calm invitation).', ['Analysis'], R(
        ['حرف عرض غير عامل', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره أنت', 'ظرف مكان منصوب، وهو مضاف', 'مضاف إليه مجرور', 'مضارع مجزوم'],
        [('ألا', 'حرف عرض غير عامل'), ('تجلسُ', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره أنت'), ('عندَ', 'ظرف مكان منصوب، وهو مضاف'), ('البابِ', 'مضاف إليه مجرور')])),
    M('6I-2', 'Which **ألا** merely introduces an assertion?', [
        '**ألا إن الطالب حاضر**: remove ألا and the statement stays',
        '**ألا تجلس عند الباب؟**: remove ألا and the question stays',
        'both: in each, removing ألا leaves the meaning unchanged',
        'neither: in each, ألا is needed for the sentence to stand',
        ], '**ألا إن الطالب حاضر**: remove ألا and the statement stays'),
    G('6R', 'Analyse **ها قد حضرت هند**.', ['Analysis'], R(
        ['attention particle', 'confirmation particle', 'feminine marker, no position', 'فاعل مرفوع بالضمة', 'ضمير في محل رفع فاعل'],
        [('ها', 'attention particle'), ('قد', 'confirmation particle'), ('تْ', 'feminine marker, no position'), ('هندٌ', 'فاعل مرفوع بالضمة')])),
    M('6-Read', 'Read: **العرض طلب بلين، والتحضيض طلب بشدّة.** (**لين** = gentleness; **شدّة** = forcefulness.) What does it say?', [
        '**عرض** is a gentle request; **تحضيض** is a forceful one.',
        '**عرض** is a forceful request; **تحضيض** is a gentle one.',
        '**عرض** and **تحضيض** are both questions seeking information.',
        '**عرض** and **تحضيض** are both prohibitions of different strength.',
        ], '**عرض** is a gentle request; **تحضيض** is a forceful one.'),
]

ITEMS['7'] = [
    M('7G-1', 'Replace the clause in **فرحت بما نجحتَ** with **نجاح**.', ['فَرِحْتُ بِنَجَاحِكَ', 'فَرِحْتُ بِنَجَاحَكَ', 'فَرِحْتُ نَجَاحَكَ', 'فَرِحْتُ بِنَجَاحُكَ'], 'فَرِحْتُ بِنَجَاحِكَ'),
    G('7G-2', 'In **أذكر الله ما دمت حيًّا**:', ['Analysis'], R(
        ['مصدرية ظرفية', 'ضمير في محل رفع اسم دام', 'خبر دام منصوب', 'نافية'],
        [('ما', 'مصدرية ظرفية'), ('ـتُ', 'ضمير في محل رفع اسم دام'), ('حيًّا', 'خبر دام منصوب')]) + [
        ('Time meaning', [(['for as long as I remain alive', 'after I die', 'never'], 'for as long as I remain alive')])]),
    M('7G-3', 'Does **سواء عليّ أحضرت أم غبت** request the answer “I attended”?', [
        'No: the hamzah of equality and أم present both as equal to the speaker.',
        'Yes: the hamzah and أم ask the listener which of the two happened.',
        'Yes: it is a yes/no question, so “I attended” is a full answer.',
        'No: it is a command telling the listener to attend or stay away.',
        ], 'No: the hamzah of equality and أم present both as equal to the speaker.'),
    G('7I-1', 'Analyse **أودّ لو تقرأُ الكتابَ**.', ['Analysis'], R(
        ['حرف مصدري غير عامل', 'مضارع مرفوع؛ فاعله مستتر تقديره أنت', 'مفعول به لتقرأ منصوب', 'مصدر مؤوّل في محل نصب مفعول به لأودّ', 'حرف شرط'],
        [('لو', 'حرف مصدري غير عامل'), ('تقرأُ', 'مضارع مرفوع؛ فاعله مستتر تقديره أنت'), ('الكتابَ (internal object)', 'مفعول به لتقرأ منصوب'),
         ('لو تقرأ الكتاب (larger object)', 'مصدر مؤوّل في محل نصب مفعول به لأودّ')])),
    M('7I-2', 'Why can **لو تحضرُ** occupy نصب while **تحضرُ** ends with ḍammah?', [
        'The unit has the object position; the verb inside has no ناصب, so it stays مرفوع.',
        '**لو** itself puts the verb in رفع, while **أودّ** puts the whole unit in نصب, so the two levels differ.',
        'It cannot: once the whole unit is in محل نصب, the verb inside should become **تحضرَ**.',
        'The unit is the فاعل of **أودّ**, in رفع.',
        ], 'The unit has the object position; the verb inside has no ناصب, so it stays مرفوع.'),
    G('7R', 'Identify the two uses of **أم**.', ['Purpose'], R(
        ['asks the listener which action occurred', 'treats both as equal for the speaker (همزة التسوية)'],
        [('أقرأتَ أم كتبتَ؟', 'asks the listener which action occurred'), ('سواء عليّ أقرأتَ أم كتبتَ', 'treats both as equal for the speaker (همزة التسوية)')])),
    M('7-Read', 'Read: **المصدر المؤوّل له محلّ، ولا يلزم أن يظهر إعرابه على الفعل الذي فيه.** How does it apply to **لو تحضرُ**?', [
        '**تحضرُ** stays indicative inside **لو تحضر**, though the unit is in محل نصب.',
        '**تحضرُ** becomes **تحضرَ**, because the unit it belongs to is in نصب.',
        'The unit has no position, so **تحضرُ** simply keeps its ending.',
        '**تحضرُ** is مجزوم inside the unit, with the ḍammah for pronunciation.',
        ], '**تحضرُ** stays indicative inside **لو تحضر**, though the unit is in محل نصب.'),
]

ITEMS['8'] = [
    G('8G-1', 'Choose and explain.', ['Correct'], [
        ('“Khalid does not write”: **لا يكتب… خالدٌ**', [(['يكتبُ: لا نافية غير عاملة', 'يكتبْ: لا ناهية'], 'يكتبُ: لا نافية غير عاملة')]),
        ('“Do not write”: **لا تكتب…**', [(['تكتبُ: لا نافية', 'تكتبْ: لا ناهية جازمة'], 'تكتبْ: لا ناهية جازمة')])]),
    G('8G-2', 'Identify **إنْ**.', ['إنْ is'], R(
        ['conditional, governing جزم', 'negative, non-governing (with إلا)', 'additional after negative ما'],
        [('إنْ يصدقْ ينجُ', 'conditional, governing جزم'), ('إنْ هو إلا صادقٌ', 'negative, non-governing (with إلا)'), ('ما إنْ كذبَ', 'additional after negative ما')])),
    M('8G-3', 'Is **ما** in **عمّا قليلٍ** كافّة?', [
        'No: **قليلٍ** stays genitive after **عن**, so ما has not stopped it.',
        'Yes: ما stops **عن**, so **قليل** is genitive only by إضافة.',
        'Yes: **قليل** is nominative after ما, the subject of a new clause.',
        'No: ما is a relative noun here, and **قليلٍ** is its صلة.',
        ], 'No: **قليلٍ** stays genitive after **عن**, so ما has not stopped it.'),
    G('8I-1', 'Explain the difference in negative scope.', ['Scope'], R(
        ['denies both arrivals separately', 'can deny joint attendance, leaving separate attendance possible'],
        [('مَا حَضَرَ الضَّيْفُ وَلَا المُعَلِّمُ', 'denies both arrivals separately'), ('مَا حَضَرَ الضَّيْفُ وَالمُعَلِّمُ', 'can deny joint attendance, leaving separate attendance possible')])),
    G('8I-2', 'In **لمّا أنْ حضرَ الضيفُ فرحتُ**:', ['Answer'], [
        ('أنْ', [(['additional after time لمّا', 'مصدرية ناصبة', 'تفسيرية'], 'additional after time لمّا')]),
        ('Is **حضر** منصوب?', [(['No: it is a past verb fixed on fatḥah', 'Yes'], 'No: it is a past verb fixed on fatḥah')]),
        ('الضيفُ', [(['فاعل مرفوع', 'مفعول به', 'مبتدأ'], 'فاعل مرفوع')])]),
    G('8R', 'Identify **إنْ** in each.', ['إنْ is'], R(
        ['مخففة من الثقيلة, non-governing; the lām is فارقة', 'negative, non-governing, with إلا for restriction'],
        [('إنْ كانَ خالدٌ لَصادقًا', 'مخففة من الثقيلة, non-governing; the lām is فارقة'), ('إنْ خالدٌ إلا صادقٌ', 'negative, non-governing, with إلا for restriction')])),
    M('8-Read', 'Read: **ما الزائدة هنا لا تكفّ العامل عن العمل.** (**تكفّ** = stops.) How does **عمّا قليلٍ** show it?', [
        '**عن** still makes **قليلٍ** genitive despite the added ما.',
        '**قليلٌ** becomes nominative, because ما stops **عن**.',
        'ما stops **عن**, and **قليلٍ** is genitive by إضافة to ما.',
        'ما is a relative noun, and **قليلٍ** is genitive as its صلة.',
        ], '**عن** still makes **قليلٍ** genitive despite the added ما.'),
]

ITEMS['9'] = [
    G('9G-1', 'Match each use of **لو**.', ['Use'], R(
        ['شرط', 'عرض', 'مصدر'], [('لو حضر لأكرمتُه', 'شرط'), ('لو تجلسُ معنا (a gentle proposal)', 'عرض'), ('أودّ لو تجلسُ معنا', 'مصدر')])),
    M('9G-2', 'Choose: **سوف يكتبُ / يكتبَ الطالبُ**.', [
        'سوف يكتبُ: مرفوع; سوف marks the future without governing',
        'سوف يكتبَ: منصوب, because سوف points to the future like لن',
        ], 'سوف يكتبُ: مرفوع; سوف marks the future without governing'),
    M('9G-3', 'Why can a wish introduced by **هل** not always be translated as an ordinary question?', [
        'In a context of longing, هل can present a wished-for possibility, not a request for facts.',
        'هل always expresses a wish in classical usage, so it is never an ordinary question seeking information.',
        'هل is a conditional particle in this use, so the sentence states a condition rather than asking.',
        'هل governs the verb in جزم here.',
        ], 'In a context of longing, هل can present a wished-for possibility, not a request for facts.'),
    G('9I-1', '**سيقرأ الطالب الدرس ثم سيكتب المثال**', ['Analysis'], R(
        ['حرف استقبال', 'مضارع مرفوع بالضمة', 'فاعل مرفوع', 'مفعول به منصوب', 'حرف عطف للترتيب والتراخي', 'مضارع منصوب'],
        [('سـ', 'حرف استقبال'), ('يقرأُ / يكتبُ', 'مضارع مرفوع بالضمة'), ('الطالبُ', 'فاعل مرفوع'), ('الدرسَ / المثالَ', 'مفعول به منصوب'), ('ثم', 'حرف عطف للترتيب والتراخي')])),
    G('9I-2', 'Give the correct endings.', ['Correct'], [
        ('سوف يحضر…', [(['يحضرُ', 'يحضرَ', 'يحضرْ'], 'يحضرُ')]),
        ('لن يحضر…', [(['يحضرُ', 'يحضرَ', 'يحضرْ'], 'يحضرَ')])]),
    G('9R', 'In **أما الضيف فسيحضر**:', ['Analysis'], R(
        ['حرف شرط وتفصيل وتوكيد غير جازم', 'مبتدأ مرفوع', 'رابطة لجواب أما', 'حرف استقبال', 'في محل رفع خبر المبتدأ', 'في محل جزم'],
        [('أما', 'حرف شرط وتفصيل وتوكيد غير جازم'), ('الضيفُ', 'مبتدأ مرفوع'), ('فـ', 'رابطة لجواب أما'), ('سـ', 'حرف استقبال'), ('سيحضر with its subject', 'في محل رفع خبر المبتدأ')])),
    M('9-Read', 'Read: **السين وسوف للاستقبال، ولا تنصبان المضارع.** What does **تنصبان** mean here?', [
        '“the two do not make it subjunctive”: س and سوف mark the future without نصب.',
        '“the two make it subjunctive”: س and سوف put the verb in نصب, like لن.',
        '“the two make it jussive”: س and سوف put the verb in جزم, like لم.',
        '“the two are nouns”: س and سوف are adverbs of future time.',
        ], '“the two do not make it subjunctive”: س and سوف mark the future without نصب.'),
]

ITEMS['10'] = [
    G('10G-1', 'What can each explain?', ['Can explain'], R(
        ['a single expression or a clause', 'a clause only'], [('أيْ', 'a single expression or a clause'), ('أنْ التفسيرية', 'a clause only')])),
    G('10G-2', '**أمرتُه أنْ ...** (with **بأن** understood)', ['Answer'], [
        ('Verb', [(['يكتبَ', 'يكتبُ'], 'يكتبَ')]),
        ('أنْ is', [(['مصدرية ناصبة', 'تفسيرية'], 'مصدرية ناصبة')])]),
    G('10G-3', 'Identify the two أنْ uses in **كتبتُ إليه أنْ اقرأْ، وأردتُ أنْ يقرأَ**.', ['أنْ is'], R(
        ['تفسيرية, followed by an imperative', 'مصدرية ناصبة, followed by a منصوب imperfect'],
        [('كتبتُ إليه أنْ اقرأْ', 'تفسيرية, followed by an imperative'), ('أردتُ أنْ يقرأَ', 'مصدرية ناصبة, followed by a منصوب imperfect')])),
    G('10I-1', 'أعرب **كتبت إليه أن اجلس**.', ['Analysis'], R(
        ['متعلق بكتبت، identifies the recipient', 'حرف تفسير غير عامل', 'فعل أمر مبني على السكون؛ فاعله مستتر تقديره أنت', 'جملة تفسيرية لا محل لها من الإعراب', 'مصدر مؤوّل في محل نصب'],
        [('إليه', 'متعلق بكتبت، identifies the recipient'), ('أنْ', 'حرف تفسير غير عامل'), ('اجلسْ', 'فعل أمر مبني على السكون؛ فاعله مستتر تقديره أنت'),
         ('اجلس with its subject', 'جملة تفسيرية لا محل لها من الإعراب')])),
    M('10I-2', 'Correct: “Every أنْ following a word associated with speech is تفسيرية.” What are the three checks?', [
        'a preceding clause; a sense of saying without the word “say”; no preposition governing أنْ',
        'a following noun; a past verb before it; a preposition before أنْ, stated or implied',
        'a preceding negation; a following imperative; a shaddah on the nūn of أنْ',
        'a preceding clause; the word “say” itself; a preposition before أنْ',
        ], 'a preceding clause; a sense of saying without the word “say”; no preposition governing أنْ'),
    G('10R', 'Classify **أنْ** in **لمّا أن حضر خالدٌ كتبتُ إليه أن اجلسْ**.', ['أنْ is'], R(
        ['additional after time لمّا', 'explanatory after the written communication', 'مصدرية ناصبة'],
        [('first أنْ', 'additional after time لمّا'), ('second أنْ', 'explanatory after the written communication')])),
    M('10-Read', 'Read: **يشترط في أنْ التفسيرية ألّا يسبقها حرف جرّ لفظًا أو تقديرًا.** What does it say?', [
        'Explanatory أنْ requires that no preposition precede it, stated or implied.',
        'Explanatory أنْ requires that a preposition precede it, stated or implied.',
        'Explanatory أنْ is the urging particle **ألّا**, used without a preposition.',
        'Explanatory أنْ puts the following verb in نصب unless a preposition precedes.',
        ], 'Explanatory أنْ requires that no preposition precede it, stated or implied.'),
]

ITEMS['11'] = [
    G('11G-1', 'Identify the subject.', ['Subject'], R(
        ['تُ', 'هندٌ', 'ألف الاثنين', 'تْ'], [('كتبتُ', 'تُ'), ('كتبتْ هندٌ', 'هندٌ'), ('كتبتا', 'ألف الاثنين')])),
    M('11G-2', 'Why is the kasrah in **كتبتِ الطالبةُ** not جرّ?', [
        'It allows connected pronunciation before الـ; the feminine تاء has no position.',
        'The ت is a subject pronoun here, and subject pronouns take kasrah when they refer to a woman.',
        '**الطالبة** is genitive, and the kasrah on the ت anticipates the case of the noun after it.',
        'It is جرّ: the ت acts as a preposition governing the noun after it.',
        ], 'It allows connected pronunciation before الـ; the feminine تاء has no position.'),
    G('11G-3', 'Classify **ف**.', ['ف is'], R(
        ['a conjunction: order and close succession', 'فاء رابطة للجواب'],
        [('حضر خالدٌ فسعيدٌ', 'a conjunction: order and close succession'), ('إنْ يحضرْ خالدٌ فأكرمْهُ', 'فاء رابطة للجواب')])),
    G('11I-1', 'أعرب: **إنْ تحضرْ هندٌ فسوف أكرمُها**', ['Analysis'], R(
        ['حرف شرط جازم', 'مضارع مجزوم بإن، فعل الشرط', 'فاعل مرفوع', 'رابطة للجواب', 'مضارع مرفوع؛ فاعله مستتر تقديره أنا', 'ضمير في محل نصب مفعول به', 'جملة في محل جزم جواب الشرط'],
        [('إنْ', 'حرف شرط جازم'), ('تحضرْ', 'مضارع مجزوم بإن، فعل الشرط'), ('هندٌ', 'فاعل مرفوع'), ('فـ', 'رابطة للجواب'), ('أكرمُ', 'مضارع مرفوع؛ فاعله مستتر تقديره أنا'),
         ('ها', 'ضمير في محل نصب مفعول به'), ('سوف أكرمها', 'جملة في محل جزم جواب الشرط')])),
    G('11I-2', 'Contrast the final ه.', ['ه is'], R(
        ['هاء السكت, no position', 'a pronoun في محل نصب اسم إنّ'],
        [('إنَّهْ (a paused affirmative answer)', 'هاء السكت, no position'), ('إنَّهُ حاضرٌ', 'a pronoun في محل نصب اسم إنّ')])),
    G('11R', '**ما كتبت الطالبة الدرس بل المثال**', ['Analysis'], R(
        ['feminine marker, no position', 'فاعل مرفوع', 'مفعول به منصوب', 'حرف عطف للإضراب', 'معطوف منصوب', 'ضمير في محل رفع فاعل'],
        [('تِ', 'feminine marker, no position'), ('الطالبةُ', 'فاعل مرفوع'), ('الدرسَ', 'مفعول به منصوب'), ('بل', 'حرف عطف للإضراب'), ('المثالَ', 'معطوف منصوب'),
         ('تُ in ما كتبتُ الدرسَ (“I wrote”)', 'ضمير في محل رفع فاعل')])),
    M('11-Read', 'Read: **تاء التأنيث حرف، وتاء الفاعل ضمير.** Which proves the distinction?', [
        '**كتبتْ هندٌ** has a separate subject; **كتبتُ** already contains its subject.',
        'Both **كتبتْ هندٌ** and **كتبتُ** have a separate subject noun after the verb.',
        'Both ت are pronouns: one feminine, one first person, each a فاعل.',
        'Both ت are particles: the subject is understood in each sentence.',
        ], '**كتبتْ هندٌ** has a separate subject; **كتبتُ** already contains its subject.'),
]

ITEMS['12'] = [
    G('12G-1', 'Match each tanwīn type.', ['Type'], R(
        ['تمكين', 'تنكير', 'مقابلة', 'تعويض'], [('رجلٌ', 'تمكين'), ('صهٍ', 'تنكير'), ('مسلماتٌ', 'مقابلة'), ('كلٌّ (complement omitted)', 'تعويض')])),
    G('12G-2', 'What does the compensation replace?', ['Replaces'], R(
        ['a letter', 'a word', 'a clause'], [('غواشٍ', 'a letter'), ('كلٌّ آمن', 'a word'), ('يومئذٍ', 'a clause')])),
    M('12G-3', 'Correct: “خالدٌ must be indefinite because it has tanwīn.”', [
        'خالد is a definite name; its tanwīn is تمكين and does not make it indefinite.',
        'The claim is correct: any noun carrying tanwīn is indefinite, so the name here means “a Khalid”.',
        'خالدٌ has تنوين تنكير, which turns the proper name into an indefinite noun.',
        'خالدٌ has تنوين مقابلة, so it stays indefinite.',
        ], 'خالد is a definite name; its tanwīn is تمكين and does not make it indefinite.'),
    G('12I-1', 'حلّل **حضرت طالباتٌ**.', ['Analysis'], R(
        ['فعل ماضٍ مبني على الفتح', 'تاء التأنيث الساكنة لا محل لها', 'فاعل مرفوع بالضمة؛ جمع مؤنث سالم', 'تنوين مقابلة', 'تنوين تمكين'],
        [('حضرَ', 'فعل ماضٍ مبني على الفتح'), ('تْ', 'تاء التأنيث الساكنة لا محل لها'), ('طالباتٌ', 'فاعل مرفوع بالضمة؛ جمع مؤنث سالم'), ('Its tanwīn', 'تنوين مقابلة')])),
    M('12I-2', 'Why do **صهٍ** and poetic **أصابَنْ** refute “every final n sound marks a declinable noun”?', [
        '**صهٍ** is a fixed اسم فعل with indefinite tanwīn; **أصابَنْ** is a verb with تنوين الترنم.',
        'Both are declinable nouns with ordinary tanwīn, so they support the claim rather than refute it.',
        '**صهٍ** is a declinable noun with تنوين تمكين; **أصابَنْ** is a noun with تنوين مقابلة.',
        'Both are particles, which never end in an n sound in ordinary speech.',
        ], '**صهٍ** is a fixed اسم فعل with indefinite tanwīn; **أصابَنْ** is a verb with تنوين الترنم.'),
    G('12R', 'In **ألا إنَّ في البيتِ لَطالباتٍ**:', ['Analysis'], R(
        ['حرف تنبيه واستفتاح', 'حرف توكيد ونصب', 'اللام المزحلقة', 'اسم إنّ مؤخر منصوب بالكسرة نيابة عن الفتحة', 'في محل رفع خبر إنّ مقدم', 'مجرور باللام'],
        [('ألا', 'حرف تنبيه واستفتاح'), ('إنّ', 'حرف توكيد ونصب'), ('لَـ', 'اللام المزحلقة'), ('طالباتٍ', 'اسم إنّ مؤخر منصوب بالكسرة نيابة عن الفتحة'), ('في البيت', 'في محل رفع خبر إنّ مقدم')]) + [
        ('Type of tanwīn', [(['مقابلة', 'تمكين', 'تنكير'], 'مقابلة')])]),
    M('12-Read', 'Read: **التنوين ليس نوعا واحدا. والحرف يعرف معناه ووظيفته بالسياق.** Which pair of examples illustrates both statements?', [
        'تمكين in **خالدٌ** vs مقابلة in **مسلماتٌ**; **لا يكتبُ** vs **لا تكتبْ**.',
        'تمكين in **خالدٌ** and in **سعيدٌ**; **لا يكتبُ** and **لا يقرأُ**, both non-governing.',
        'تنكير in **خالدٌ** vs تمكين in **رجلٌ**; **كتبتُ** vs **كتبتْ**, two kinds of ت.',
        'مقابلة in **خالدٌ** vs تمكين in **مسلماتٌ**; **لا تكتبْ** vs **لن تكتبَ**.',
        ], 'تمكين in **خالدٌ** vs مقابلة in **مسلماتٌ**; **لا يكتبُ** vs **لا تكتبْ**.'),
]

ITEMS['R'] = [
    G('A-1', '**حَضَرَ خَالِدٌ وَسَعِيدٌ. أَمَّا خَالِدٌ فَقَرَأَ الدَّرْسَ، وَأَمَّا سَعِيدٌ فَكَتَبَ المِثَالَ. مَا قَرَأَ خَالِدٌ المِثَالَ بَلِ الدَّرْسَ. ثُمَّ حَضَرَتْ هِنْدٌ. أَلَا إِنَّ هِنْدًا لَفِي البَيْتِ. سَوْفَ تَقْرَأُ الدَّرْسَ ثُمَّ تَكْتُبُ المِثَالَ.** Identify each particle’s function.', ['Function'], R(
        ['coordinates سعيد with خالد', 'a division with conditional and emphatic force', 'links the response of أما', 'keeps the denial and affirms the second expression',
         'coordinates with order and an interval', 'feminine marker', 'draws attention', 'emphatic, shifted lām', 'marks future time'],
        [('first و', 'coordinates سعيد with خالد'), ('أما', 'a division with conditional and emphatic force'), ('ف after each أما', 'links the response of أما'),
         ('بل', 'keeps the denial and affirms the second expression'), ('ثم', 'coordinates with order and an interval'), ('تْ in حضرت', 'feminine marker'), ('ألا', 'draws attention'),
         ('ل in لفي', 'emphatic, shifted lām'), ('سوف', 'marks future time')])),
    G('A-2', 'Passage A: order of events.', ['Answer'], [
        ('Does the first sentence show whose arrival came first?', [(['No', 'Yes: Khalid', 'Yes: Saʿīd'], 'No')]),
        ('Does **ثم** introduce a later stage?', [(['Yes', 'No'], 'Yes')])]),
    M('A-3', 'In **ما قرأ خالد المثال بل الدرس**, which reading is denied and which affirmed?', [
        'Reading **المثال** is denied; reading **الدرس** is affirmed.',
        'Reading **الدرس** is denied; reading **المثال** is affirmed.',
        'Reading both **المثال** and **الدرس** is denied.',
        'Reading both **المثال** and **الدرس** is affirmed.',
        ], 'Reading **المثال** is denied; reading **الدرس** is affirmed.'),
    G('A-4', 'Give the tarkīb of **أما خالدٌ فقرأَ الدرسَ** and **ألا إنّ هندًا لفي البيتِ**.', ['Analysis'], R(
        ['مبتدأ مرفوع بالضمة', 'في محل رفع خبر خالد', 'اسم إنّ منصوب بالفتحة', 'في محل رفع خبر إنّ', 'فاعل مرفوع'],
        [('خالدٌ', 'مبتدأ مرفوع بالضمة'), ('قرأ الدرس', 'في محل رفع خبر خالد'), ('هندًا', 'اسم إنّ منصوب بالفتحة'), ('في البيت', 'في محل رفع خبر إنّ')])),
    G('A-5', 'Analyse **سوف تقرأُ الدرسَ ثم تكتبُ المثالَ**.', ['Analysis'], R(
        ['indicative imperfect; subject هي (Hind)', 'direct object, منصوب', 'conjunction; assigns no نصب', 'منصوب by سوف'],
        [('تقرأُ / تكتبُ', 'indicative imperfect; subject هي (Hind)'), ('الدرسَ / المثالَ', 'direct object, منصوب'), ('ثم', 'conjunction; assigns no نصب')])),
    G('B-1', '**ألم يحضر الضيف؟ — بلى**', ['Asserts'], R(
        ['that the guest attended', 'that he did not attend'], [('بلى', 'that the guest attended'), ('نعم (in its place)', 'that he did not attend')])),
    G('B-2', 'أعرب **كتبت إلى الضيف أن اجلس**.', ['Analysis'], R(
        ['ضمير في محل رفع فاعل', 'اسم مجرور بالكسرة؛ the phrase attaches to كتبت', 'حرف تفسير غير عامل', 'فعل أمر مبني على السكون؛ فاعله مستتر تقديره أنت',
         'جملة تفسيرية لا محل لها', 'مصدر مؤوّل مجرور بإلى'],
        [('ـتُ', 'ضمير في محل رفع فاعل'), ('الضيفِ', 'اسم مجرور بالكسرة؛ the phrase attaches to كتبت'), ('أنْ', 'حرف تفسير غير عامل'),
         ('اجلسْ', 'فعل أمر مبني على السكون؛ فاعله مستتر تقديره أنت'), ('اجلس with its subject', 'جملة تفسيرية لا محل لها')])),
    G('B-3', '**لولا المعلم لخرج الضيف**', ['Answer'], [
        ('The existing condition', [(['the teacher’s presence', 'the guest’s departure'], 'the teacher’s presence')]),
        ('The prevented response', [(['the guest’s departure', 'the teacher’s presence'], 'the guest’s departure')]),
        ('Omitted predicate', [(['موجودٌ', 'خرجَ', 'الضيفُ'], 'موجودٌ')])]),
    M('B-4', 'What does **لو خرج الضيف لحزنت** establish?', [
        'The departure is unrealised; it does not rule out other causes of sadness.',
        'The guest did leave, and the speaker was saddened by the departure.',
        'The speaker was never sad, for this reason or for any other reason.',
        'The guest will leave later, and the speaker will then be sad.',
        ], 'The departure is unrealised; it does not rule out other causes of sadness.'),
    G('C-1', 'Name the particles’ functions.', ['Function'], R(
        ['لا نافية غير عاملة: تكتبُ indicative', 'لا ناهية: تكتبْ jussive'],
        [('لا تكتبُ هندٌ', 'لا نافية غير عاملة: تكتبُ indicative'), ('لا تكتبْ', 'لا ناهية: تكتبْ jussive')])),
    G('C-2', 'Name the particles’ functions.', ['Function'], R(
        ['أنْ مصدرية ناصبة: أكتبَ subjunctive', 'أنْ تفسيرية: اكتبْ an imperative'],
        [('أريد أنْ أكتبَ', 'أنْ مصدرية ناصبة: أكتبَ subjunctive'), ('كتبتُ إليه أنْ اكتبْ', 'أنْ تفسيرية: اكتبْ an imperative')])),
    G('C-3', 'Name the particles’ functions.', ['Function'], R(
        ['لولا: an existing condition prevents the response', 'لولا: forceful urging; تتعلّمُ indicative'],
        [('لولا العلمُ لضلَّ الناسُ', 'لولا: an existing condition prevents the response'), ('لولا تتعلّمُ!', 'لولا: forceful urging; تتعلّمُ indicative')])),
    G('C-4', 'Name the particles’ functions.', ['Function'], R(
        ['لو مصدرية: the clause is the object of أودّ', 'لو شرطية: an unrealised past condition'],
        [('أودُّ لو تحضرُ', 'لو مصدرية: the clause is the object of أودّ'), ('لو حضرتَ لأكرمتُكَ', 'لو شرطية: an unrealised past condition')])),
    G('C-5', 'Name the particles’ functions.', ['Function'], R(
        ['إنْ شرطية: governs جزم in both verbs', 'إنْ نافية غير عاملة: both nouns nominative'],
        [('إنْ يحضرْ خالدٌ أُكرمْهُ', 'إنْ شرطية: governs جزم in both verbs'), ('إنْ خالدٌ إلا طالبٌ', 'إنْ نافية غير عاملة: both nouns nominative')])),
    G('C-6', 'Name the particles’ functions.', ['Function'], R(
        ['ما negative, إنْ additional', 'إنْ lightened from إنَّ, non-governing; the lām is فارقة'],
        [('ما إنْ كذبَ', 'ما negative, إنْ additional'), ('إنْ كانَ لَصادقًا', 'إنْ lightened from إنَّ, non-governing; the lām is فارقة')])),
    G('D1', '**إِنْ يَحْضُرِ المُعَلِّمُ فَسَوْفَ أَقْرَأُ الدَّرْسَ.**', ['Analysis'], R(
        ['حرف شرط جازم', 'مضارع مجزوم بإن، حُرّك بالكسر لالتقاء الساكنين', 'فاعل مرفوع بالضمة', 'رابطة للجواب', 'مضارع مرفوع؛ فاعله مستتر تقديره أنا',
         'جملة في محل جزم جواب الشرط', 'مضارع مجزوم بالسكون'],
        [('إنْ', 'حرف شرط جازم'), ('يحضرِ', 'مضارع مجزوم بإن، حُرّك بالكسر لالتقاء الساكنين'), ('المعلمُ', 'فاعل مرفوع بالضمة'), ('فـ', 'رابطة للجواب'),
         ('أقرأُ', 'مضارع مرفوع؛ فاعله مستتر تقديره أنا'), ('سوف أقرأ الدرس', 'جملة في محل جزم جواب الشرط')])),
    G('D2', '**مَا رَأَيْتُ المُعَلِّمَ لَكِنْ الطَّالِبَ.**', ['Analysis'], R(
        ['نافية غير عاملة', 'مفعول به منصوب بالفتحة', 'حرف عطف واستدراك', 'معطوف على المعلم منصوب', 'اسم لكنّ منصوب'],
        [('ما', 'نافية غير عاملة'), ('المعلمَ', 'مفعول به منصوب بالفتحة'), ('لكنْ', 'حرف عطف واستدراك'), ('الطالبَ', 'معطوف على المعلم منصوب')])),
    G('D3', '**أَمَّا فِي البَيْتِ فَخَالِدٌ.**', ['Analysis'], R(
        ['حرف شرط وتفصيل وتوكيد غير جازم', 'خبر مقدم، في محل رفع', 'رابطة لجواب أما', 'مبتدأ مؤخر مرفوع بالضمة', 'فاعل مرفوع بأما'],
        [('أما', 'حرف شرط وتفصيل وتوكيد غير جازم'), ('في البيت', 'خبر مقدم، في محل رفع'), ('فـ', 'رابطة لجواب أما'), ('خالدٌ', 'مبتدأ مؤخر مرفوع بالضمة')])),
    G('D4', '**كَتَبَتِ الطَّالِبَةُ الدَّرْسَ وَالمِثَالَ.**', ['Analysis'], R(
        ['فعل ماضٍ مبني على الفتح', 'تاء التأنيث الساكنة، حُرّكت بالكسر، لا محل لها', 'فاعل مرفوع بالضمة', 'مفعول به منصوب بالفتحة', 'معطوف على الدرس منصوب',
         'ضمير متصل في محل رفع فاعل'],
        [('كتبَ', 'فعل ماضٍ مبني على الفتح'), ('تِ', 'تاء التأنيث الساكنة، حُرّكت بالكسر، لا محل لها'), ('الطالبةُ', 'فاعل مرفوع بالضمة'), ('الدرسَ', 'مفعول به منصوب بالفتحة'),
         ('المثالَ', 'معطوف على الدرس منصوب')])),
]
