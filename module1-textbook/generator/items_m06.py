# Module 6: Particles Governing Verbs. Auto-checked items; correct answers follow the Module 6 answers file.
from item_kit import M, G, R

MOOD = ['مرفوع', 'منصوب', 'مجزوم']
ITEMS = {}

ITEMS['1'] = [
    G('1G-1', 'Match each term.', ['Meaning'], R(
        ['a governor of جزم', 'retaining the mood-marking ن', 'a governor of نصب', 'deleting a final weak letter'],
        [('ناصب', 'a governor of نصب'), ('جازم', 'a governor of جزم'), ('ثبوت النون', 'retaining the mood-marking ن'), ('حذف حرف العلة', 'deleting a final weak letter')])),
    G('1G-2', '**لن يفتح… خالدٌ البابَ**', ['Answer'], [
        ('Correct form', [(['يفتحُ', 'يفتحَ', 'يفتحْ'], 'يفتحَ')]),
        ('Governor', [(['لن', 'خالد', 'nothing'], 'لن')]),
        ('خالدٌ', [(['فاعل مرفوع بالضمة', 'مفعول به منصوب'], 'فاعل مرفوع بالضمة')]),
        ('البابَ', [(['مفعول به منصوب بالفتحة', 'فاعل مرفوع'], 'مفعول به منصوب بالفتحة')])]),
    G('1G-3', 'Complete from **تكتبين**.', ['Form'], [
        ('لن ___', [(['تَكْتُبِي', 'تَكْتُبِينَ', 'تَكْتُبْ'], 'تَكْتُبِي')]),
        ('لم ___', [(['تَكْتُبِي', 'تَكْتُبِينَ', 'تَكْتُبْ'], 'تَكْتُبِي')]),
        ('The subject pronoun', [(['ياء المخاطبة', 'التاء', 'النون'], 'ياء المخاطبة')])]),
    G('1I-1', 'Supply the verb forms.', ['لن ___', 'لم ___'], [
        ('يدعو', [(['يدعوَ', 'يدعُ', 'يدعو'], 'يدعوَ'), (['يدعوَ', 'يدعُ', 'يدعو'], 'يدعُ')]),
        ('يرمي', [(['يرميَ', 'يرمِ', 'يرمي'], 'يرميَ'), (['يرميَ', 'يرمِ', 'يرمي'], 'يرمِ')]),
        ('يسعى', [(['يسعى', 'يسعَ', 'يسعيَ'], 'يسعى'), (['يسعى', 'يسعَ', 'يسعيَ'], 'يسعَ')])]),
    M('1I-2', 'Correct: “In **لم يكتبوا**, the subject pronoun was deleted to mark جزم.”', [
        '**نون الإعراب** was deleted; **واو الجماعة** is still the subject, and the alif is not a pronoun.',
        'The claim is correct: **واو الجماعة** was deleted, and the alif now marks the subject.',
        '**نون الإعراب** was deleted, and the written alif is the subject pronoun that replaces it.',
        'Nothing was deleted: **يكتبوا** is the original form, and the alif marks the plural.',
        ], '**نون الإعراب** was deleted; **واو الجماعة** is still the subject, and the alif is not a pronoun.'),
    G('1I-3', 'Analyse **لَنْ نَتْرُكَ العِلْمَ**, “We will not abandon knowledge.”', ['Analysis'], R(
        ['حرف نفي ونصب واستقبال', 'مضارع منصوب بلن بالفتحة؛ فاعله مستتر تقديره نحن', 'مفعول به منصوب بالفتحة', 'مضارع مجزوم بلن'],
        [('لن', 'حرف نفي ونصب واستقبال'), ('نتركَ', 'مضارع منصوب بلن بالفتحة؛ فاعله مستتر تقديره نحن'), ('العلمَ', 'مفعول به منصوب بالفتحة')])),
    M('1R', 'Why can **يكتبوا** be منصوبًا in one sentence and مجزومًا in another?', [
        'Both moods use **حذف النون** in these verbs; only the governor, **لن** or **لم**, tells them apart.',
        'The alif changes: it is written after the واو in the نصب form and dropped in the جزم form of the verb.',
        'The واو changes: it is the subject pronoun in نصب but only a sign of the mood in جزم.',
        'It cannot: **يكتبوا** is always مجزوم, and **لن يكتبوا** is an error.',
        ], 'Both moods use **حذف النون** in these verbs; only the governor, **لن** or **لم**, tells them apart.'),
]

ITEMS['2'] = [
    G('2G-1', 'Match each particle.', ['Function'], R(
        ['future negation', 'response', 'purpose', 'introducing a verbal noun without itself specifying purpose'],
        [('أن', 'introducing a verbal noun without itself specifying purpose'), ('كي', 'purpose'), ('لن', 'future negation'), ('إذن', 'response')])),
    G('2G-2', '**نقرأ لكي نفهم…**', ['Answer'], [
        ('Correct form', [(['نفهمُ', 'نفهمَ', 'نفهمْ'], 'نفهمَ')]),
        ('Governor of the verb', [(['كي', 'اللام', 'نقرأ'], 'كي')]),
        ('Governor of the مصدر مؤوّل', [(['اللام (in جرّ)', 'كي', 'نقرأ'], 'اللام (in جرّ)')])]),
    M('2G-3', 'In reply to **سأساعدك**, choose and explain.', [
        '**إذن أشكرَكَ**: it begins the reply, the thanking is future, and nothing separates them.',
        '**إذن أشكرُكَ**: إذن never governs, so the verb keeps its ordinary ḍammah.',
        '**إذن أشكرَكَ**: every verb after إذن is منصوب, whatever its time or position.',
        '**إذن أشكرُكَ**: the thanking is already happening, so the present needs رفع.',
        ], '**إذن أشكرَكَ**: it begins the reply, the thanking is future, and nothing separates them.'),
    G('2I-1', 'Supply the ending of **أساعد** (future help in each).', ['Ending'], R(
        ['أساعدُكَ: إذن does not govern', 'أساعدَكَ: إذن governs'],
        [('أنا إذن أساعد…', 'أساعدُكَ: إذن does not govern'), ('إذن والله أساعد…', 'أساعدَكَ: إذن governs'), ('إذن أنا أساعد…', 'أساعدُكَ: إذن does not govern')])),
    G('2I-2', 'Fully analyse **نريد أن يفهم الطلاب الدرس**.', ['Analysis'], R(
        ['مضارع مرفوع بالضمة؛ فاعله مستتر تقديره نحن', 'حرف مصدر ونصب', 'مضارع منصوب بأن بالفتحة', 'فاعل يفهم مرفوع بالضمة', 'مفعول به ليفهم منصوب بالفتحة',
         'مصدر مؤوّل في محل نصب مفعول به لنريد'],
        [('نريدُ', 'مضارع مرفوع بالضمة؛ فاعله مستتر تقديره نحن'), ('أن', 'حرف مصدر ونصب'), ('يفهمَ', 'مضارع منصوب بأن بالفتحة'), ('الطلابُ', 'فاعل يفهم مرفوع بالضمة'),
         ('الدرسَ', 'مفعول به ليفهم منصوب بالفتحة'), ('أن يفهم الطلاب الدرس', 'مصدر مؤوّل في محل نصب مفعول به لنريد')])),
    M('2I-3', 'Correct: “**لن أخرج اليوم** means that I shall never go out at any time.”', [
        'It negates going out today: **لن** is future negation, and **اليومَ** limits the time.',
        'The claim is correct: **لن** always means never, so **اليوم** adds nothing.',
        'It negates going out in the past: **لن** turns the مضارع to the past.',
        'It forbids going out today: **لن** with a first-person verb is a prohibition.',
        ], 'It negates going out today: **لن** is future negation, and **اليومَ** limits the time.'),
    G('2R', '“They want to write the letter”', ['Answer'], [
        ('Sentence', [(['هُمْ يُرِيدُونَ أَنْ يَكْتُبُوا الرِّسَالَةَ', 'هُمْ يُرِيدُوا أَنْ يَكْتُبُونَ الرِّسَالَةَ', 'هُمْ يُرِيدُونَ أَنْ يَكْتُبُونَ الرِّسَالَةَ'], 'هُمْ يُرِيدُونَ أَنْ يَكْتُبُوا الرِّسَالَةَ')]),
        ('يريدون', [(['مرفوع بثبوت النون', 'منصوب بحذف النون'], 'مرفوع بثبوت النون')]),
        ('يكتبوا', [(['مرفوع بثبوت النون', 'منصوب بحذف النون'], 'منصوب بحذف النون')]),
        ('Each واو الجماعة', [(['ضمير في محل رفع فاعل', 'sign of the mood'], 'ضمير في محل رفع فاعل')])]),
]

ITEMS['3'] = [
    M('3G-1', 'Choose: **علمتُ أن سيعودُ / سيعودَ المسافرُ**.', [
        '**سيعودُ**: after a verb of certainty, أن is lightened from أنّ and does not govern the verb.',
        '**سيعودَ**: أن always puts the following مضارع in نصب, and the future سين does not interrupt its government.',
        '**سيعودَ**: the future سين itself requires نصب on the verb it attaches to, whatever comes before it.',
        '**سيعودُ**: a verb placed before its subject stays مرفوع.',
        ], '**سيعودُ**: after a verb of certainty, أن is lightened from أنّ and does not govern the verb.'),
    G('3G-2', 'In **أقرأ لأفهمَ**:', ['Answer'], [
        ('Expanded', [(['أقرأُ لِأَنْ أفهمَ', 'أقرأُ لِكَيْ لا أفهمَ', 'أقرأُ لِمَا أفهمُ'], 'أقرأُ لِأَنْ أفهمَ')]),
        ('Governor of **أفهمَ**', [(['understood أن', 'اللام', 'أقرأ'], 'understood أن')]),
        ('Governor of the مصدر مؤوّل', [(['لام التعليل (in جرّ)', 'understood أن', 'أقرأ'], 'لام التعليل (in جرّ)')])]),
    M('3G-3', 'Correct **أكتبُ لِلا أنسى**, keeping “so as not to forget.”', ['أَكْتُبُ لِئَلَّا أَنْسَى', 'أَكْتُبُ لِلَا أَنْسَ', 'أَكْتُبُ لِأَنْ لَا أَنْسَ', 'أَكْتُبُ لَا أَنْسَى'], 'أَكْتُبُ لِئَلَّا أَنْسَى'),
    G('3I-1', 'Explain both endings.', ['أن is', 'يتأخر is'], [
        ('حسبتُ ألّا يتأخّرَ الضيفُ', [(['مصدرية ناصبة', 'مخفّفة من أنّ'], 'مصدرية ناصبة'), (['منصوب بالفتحة', 'مرفوع بالضمة'], 'منصوب بالفتحة')]),
        ('حسبتُ ألّا يتأخّرُ الضيفُ', [(['مصدرية ناصبة', 'مخفّفة من أنّ'], 'مخفّفة من أنّ'), (['منصوب بالفتحة', 'مرفوع بالضمة'], 'مرفوع بالضمة')])]),
    G('3I-2', 'In **صبرك وتعملَ خيرٌ من الشكوى**:', ['Analysis'], R(
        ['مبتدأ مرفوع (the explicit noun)', 'منصوب بأن مضمرة جوازًا بعد الواو', 'the مصدر مؤوّل أن تعمل, coordinated with صبرك', 'خبر مرفوع'],
        [('صبرُك', 'مبتدأ مرفوع (the explicit noun)'), ('تعملَ', 'منصوب بأن مضمرة جوازًا بعد الواو'), ('What is coordinated with صبرك', 'the مصدر مؤوّل أن تعمل, coordinated with صبرك'),
         ('خيرٌ', 'خبر مرفوع')])),
    M('3I-3', 'Correct: “**لأتعلمَ** contains a preposition, so **أتعلمَ** is مجرور.”', [
        'A verb cannot take جرّ: **أتعلمَ** is منصوب by understood أن; the unit is in محل جرّ.',
        'The claim is correct: the lām is a preposition, so the verb after it is مجرور.',
        '**أتعلمَ** is مجزوم by the lām, as with لام الأمر.',
        'The lām is لام الأمر, so **أتعلمَ** is a command with نصب.',
        ], 'A verb cannot take جرّ: **أتعلمَ** is منصوب by understood أن; the unit is in محل جرّ.'),
    G('3R', 'Analyse **أريد أن أقرأ لأفهم**.', ['Analysis'], R(
        ['منصوب بأن الظاهرة؛ the مصدر مؤوّل is the object of أريد', 'منصوب بأن مضمرة جوازًا؛ purpose attached to أقرأ', 'مرفوع؛ فاعله مستتر تقديره أنا'],
        [('أريدُ', 'مرفوع؛ فاعله مستتر تقديره أنا'), ('أقرأَ', 'منصوب بأن الظاهرة؛ the مصدر مؤوّل is the object of أريد'), ('أفهمَ', 'منصوب بأن مضمرة جوازًا؛ purpose attached to أقرأ')])),
]

ITEMS['4'] = [
    G('4G-1', 'Classify the understood أن.', ['أن is understood'], R(
        ['جوازًا', 'وجوبًا'], [('لأتعلمَ (purpose)', 'جوازًا'), ('حتى يصلَ الضيفُ (a future arrival)', 'وجوبًا'), ('ما كان ليتركَ الحقَّ', 'وجوبًا')])),
    M('4G-2', 'The brother has not returned: **سأبقى هنا حتى يرجع… أخي**.', [
        '**يرجعَ**: منصوب بأن مضمرة وجوبًا بعد حتى',
        '**يرجعُ**: مرفوع, because the return has not happened',
        '**يرجعْ**: مجزوم بحتى, which governs like لم',
        ], '**يرجعَ**: منصوب بأن مضمرة وجوبًا بعد حتى'),
    M('4G-3', 'Which meanings of **أو** qualify for the نصب pattern?', [
        '**إلى أن** and **إلّا أن**',
        'ordinary “or”',
        '**إلى أن** only',
        '**إلّا أن** only',
        ], '**إلى أن** and **إلّا أن**'),
    M('4I-1', 'In **لَأَسِيرَنَّ أَوْ أَصِلَ**, explain **أصلَ**.', [
        'منصوب بأن مضمرة وجوبًا بعد أو; **أو** means **إلى أن**, so arrival ends the travelling.',
        'منصوب بأو directly; **أو** means “or”, giving travelling or arriving as alternatives.',
        'مجزوم بأو; **أو** means **إلّا أن**, so arriving prevents the travelling.',
        'منصوب بأن مضمرة جوازًا بعد أو; **أو** means “or”, as in ordinary coordination.',
        ], 'منصوب بأن مضمرة وجوبًا بعد أو; **أو** means **إلى أن**, so arrival ends the travelling.'),
    M('4I-2', 'Correct: “In **ما كان الطالب ليكذبَ**, the لام is an ordinary purpose لام, so أن may be expressed.”', [
        'It is **لام الجحود** after negated كان; أن is understood **وجوبًا**.',
        'The claim is correct: it is a purpose lām, so أن may be expressed.',
        'It is لام الأمر, so the verb is a command and أن cannot appear.',
        'It is لام الجحود, and أن is understood **جوازًا**, so it may be expressed.',
        ], 'It is **لام الجحود** after negated كان; أن is understood **وجوبًا**.'),
    G('4I-3', 'Contrast the two.', ['لام', 'أن'], [
        ('جاء ليتعلمَ', [(['purpose لام', 'لام الجحود'], 'purpose لام'), (['مضمرة جوازًا', 'مضمرة وجوبًا'], 'مضمرة جوازًا')]),
        ('ما كان ليكذبَ', [(['purpose لام', 'لام الجحود'], 'لام الجحود'), (['مضمرة جوازًا', 'مضمرة وجوبًا'], 'مضمرة وجوبًا')])]),
    G('4R', 'Why do **لن نسعى** and **لم نسعَ** look different?', ['Mood and sign'], R(
        ['نصب بفتحة مقدّرة على الألف', 'جزم بحذف حرف العلة'], [('لن نسعى', 'نصب بفتحة مقدّرة على الألف'), ('لم نسعَ', 'جزم بحذف حرف العلة')])),
]

ITEMS['5'] = [
    G('5G-1', 'Match each sentence to its meaning.', ['Meaning'], R(
        ['عرض', 'تحضيض', 'تمنٍّ', 'استفهام'],
        [('ألا تزورنا؟', 'عرض'), ('هلّا تجتهد؟', 'تحضيض'), ('ليتك تحضر', 'تمنٍّ'), ('هل تساعدني؟', 'استفهام')])),
    M('5G-2', '“Do not combine speaking and writing”: **لا تتكلمْ وتكتب…**', [
        'لا تتكلمْ وتكتبَ: نصب after واو المعية',
        'لا تتكلمْ وتكتبُ: رفع after واو الاستئناف',
        'لا تتكلمْ وتكتبْ: جزم by coordination',
        ], 'لا تتكلمْ وتكتبَ: نصب after واو المعية'),
    M('5G-3', 'Complete: **تفهمَ** in **اجتهد فتفهمَ** is **منصوب بـ ___ مضمرة ___ بعد ___، والفاعل ___**.', [
        'بأن مضمرة وجوبًا بعد فاء السببية، والفاعل ضمير مستتر تقديره أنت',
        'بأن مضمرة جوازًا بعد فاء العطف، والفاعل ضمير مستتر تقديره هو',
        'بالفاء نفسها مضمرة وجوبًا بعد الأمر، والفاعل ضمير مستتر تقديره أنت',
        ], 'بأن مضمرة وجوبًا بعد فاء السببية، والفاعل ضمير مستتر تقديره أنت'),
    G('5I-1', 'Match each ending of **تلعب** in **لا تقرأ وتلعب** to its meaning.', ['Meaning'], R(
        ['do not combine reading and playing (واو المعية)', 'do neither (جزم by coordination)', 'do not read; the playing is asserted separately (رفع)'],
        [('تلعبَ', 'do not combine reading and playing (واو المعية)'), ('تلعبْ', 'do neither (جزم by coordination)'), ('تلعبُ', 'do not read; the playing is asserted separately (رفع)')])),
    G('5I-2', '**لا تهمل فتندم** (“Do not neglect your duty and consequently regret it”)', ['Analysis'], R(
        ['ناهية جازمة', 'مجزوم بالسكون', 'فاء السببية', 'منصوب بأن مضمرة وجوبًا بالفتحة', 'مجزوم بالعطف'],
        [('لا', 'ناهية جازمة'), ('تهملْ', 'مجزوم بالسكون'), ('فـ', 'فاء السببية'), ('تندمَ', 'منصوب بأن مضمرة وجوبًا بالفتحة')])),
    M('5I-3', 'Why does **يقرأ خالد ويكتب** not require نصب after و?', [
        'It is plain coordination, with no qualifying negation or request, so **يكتبُ** shares رفع.',
        'و never allows نصب on a following verb; only ف can carry an understood أن, so رفع is automatic here.',
        '**خالد** stands between the two verbs, and an intervening subject always blocks an understood أن.',
        'It does require نصب, **ويكتبَ**, as و always implies معية.',
        ], 'It is plain coordination, with no qualifying negation or request, so **يكتبُ** shares رفع.'),
    M('5I-4', 'A learner writes **اِجْلِسْ تَسْتَرِيحَ**, claiming every imperative licenses a following منصوب. What is the error?', [
        'An imperative alone does not license نصب; use **اجلسْ فتستريحَ** or **اجلسْ تسترحْ**.',
        'There is no error: an imperative always licenses a following منصوب verb.',
        'The verb must be مرفوع after any imperative: **اجلسْ تستريحُ**.',
        'The imperative itself must be منصوب to match: **اجلسَ تستريحَ**.',
        ], 'An imperative alone does not license نصب; use **اجلسْ فتستريحَ** or **اجلسْ تسترحْ**.'),
    G('5R', 'Classify أن.', ['أن is'], R(
        ['expressed', 'optionally understood', 'obligatorily understood'],
        [('أريد أن أفهمَ', 'expressed'), ('جئت لأفهمَ', 'optionally understood'), ('انتظر حتى أفهمَ', 'obligatorily understood'), ('اجتهد فتفهمَ', 'obligatorily understood')])),
]

ITEMS['6'] = [
    M('6G-1', '“The traveller has not arrived yet; his arrival is expected”: **___ يصلْ المسافرُ**', ['لمّا', 'لم'], 'لمّا'),
    G('6G-2', 'Distinguish statement and prohibition.', ['Meaning'], R(
        ['negative statement “You do not write” (رفع)', 'prohibition “Do not write” (جزم)'],
        [('لا تكتبُ', 'negative statement “You do not write” (رفع)'), ('لا تكتبْ', 'prohibition “Do not write” (جزم)')])),
    G('6G-3', 'From **تسعين**, write “Do not strive” to one woman.', ['Answer'], [
        ('Form', [(['لَا تَسْعَيْ', 'لَا تَسْعَ', 'لَا تَسْعَيْنَ'], 'لَا تَسْعَيْ')]),
        ('Subject', [(['ياء المخاطبة', 'ضمير مستتر تقديره أنتِ', 'النون'], 'ياء المخاطبة')]),
        ('Sign of جزم', [(['حذف النون', 'حذف حرف العلة', 'السكون'], 'حذف النون')])]),
    G('6I-1', 'Supply endings: **لم يفتح الحارس الباب. لما يرجع الضيف. ليكتب الطالب الجواب.**', ['Mood and governor'], R(
        ['مجزوم بلم بالسكون', 'مجزوم بلمّا بالسكون', 'مجزوم بلام الأمر بالسكون', 'منصوب بالفتحة'],
        [('يفتحْ', 'مجزوم بلم بالسكون'), ('يرجعْ', 'مجزوم بلمّا بالسكون'), ('يكتبْ', 'مجزوم بلام الأمر بالسكون')])),
    M('6I-2', 'Correct **لم يدعو خالدٌ**.', [
        '**لَمْ يَدْعُ خَالِدٌ**: delete the final و and keep the ḍammah; the sign is حذف حرف العلة.',
        '**لَمْ يَدْعُو خَالِدٌ**: it is correct, because the jussive sign is the ḍammah.',
        '**لَمْ يَدْعَ خَالِدٌ**: delete the و and add fatḥah as the jussive sign.',
        '**لَمْ يَدْعُوا خَالِدٌ**: add an alif after the و to mark جزم.',
        ], '**لَمْ يَدْعُ خَالِدٌ**: delete the final و and keep the ḍammah; the sign is حذف حرف العلة.'),
    G('6I-3', 'Compare (the last is feminine plural).', ['Mood or position', 'Subject pronoun'], [
        ('لن تكتبوا', [(['منصوب بحذف النون', 'مجزوم بحذف النون', 'مبني على السكون في محل جزم'], 'منصوب بحذف النون'), (['واو الجماعة', 'نون النسوة'], 'واو الجماعة')]),
        ('لم تكتبوا', [(['منصوب بحذف النون', 'مجزوم بحذف النون', 'مبني على السكون في محل جزم'], 'مجزوم بحذف النون'), (['واو الجماعة', 'نون النسوة'], 'واو الجماعة')]),
        ('لم تكتبْنَ', [(['منصوب بحذف النون', 'مجزوم بحذف النون', 'مبني على السكون في محل جزم'], 'مبني على السكون في محل جزم'), (['واو الجماعة', 'نون النسوة'], 'نون النسوة')])]),
    G('6R', 'Identify the actual governor.', ['Governor'], R(
        ['command لام directly governs جزم', 'understood أن governs نصب; purpose لام governs the مصدر مؤوّل'],
        [('لِيَكْتُبْ خالدٌ', 'command لام directly governs جزم'), ('جاءَ خالدٌ لِيَكْتُبَ', 'understood أن governs نصب; purpose لام governs the مصدر مؤوّل')])),
]

ITEMS['7'] = [
    G('7G-1', 'Label the parts of **إن تصبرْ تنجحْ**.', ['Label'], R(
        ['أداة الشرط', 'فعل الشرط', 'جواب الشرط'], [('إن', 'أداة الشرط'), ('تصبرْ', 'فعل الشرط'), ('تنجحْ', 'جواب الشرط')])),
    M('7G-2', 'Complete from **تكتبون، تفهمون**: **إن ___ الدرسَ ___**', [
        'إِنْ تَكْتُبُوا الدَّرْسَ تَفْهَمُوا', 'إِنْ تَكْتُبُونَ الدَّرْسَ تَفْهَمُونَ', 'إِنْ تَكْتُبُوا الدَّرْسَ تَفْهَمُونَ', 'إِنْ تَكْتُبُونَ الدَّرْسَ تَفْهَمُوا'],
        'إِنْ تَكْتُبُوا الدَّرْسَ تَفْهَمُوا'),
    M('7G-3', 'Describe **رجعتَ** in **إن رجعتَ رجعتُ**.', [
        'مبني على السكون في محل جزم',
        'منصوب بالفتحة',
        'مجزوم بحذف النون',
        'مجزوم بالسكون الظاهر',
        ], 'مبني على السكون في محل جزم'),
    G('7I-1', '**إذما تحفظ الدرس تفهم القاعدة**', ['Analysis'], R(
        ['حرف شرط جازم بمعنى إن', 'فعل الشرط مجزوم بالسكون', 'جواب الشرط مجزوم بالسكون', 'مفعول به منصوب'],
        [('إذما', 'حرف شرط جازم بمعنى إن'), ('تحفظْ', 'فعل الشرط مجزوم بالسكون'), ('تفهمْ', 'جواب الشرط مجزوم بالسكون'), ('الدرسَ / القاعدةَ', 'مفعول به منصوب')])),
    M('7I-2', 'In **إن حضرتَ أحضر**, which endings of **أحضر** are permitted?', [
        '**أحضرْ** or **أحضرُ**: after a past-form condition, a مضارع response may take either.',
        'Only **أحضرْ**: every مضارع response after إن must be مجزوم, whatever the form of the condition verb.',
        'Only **أحضرُ**: a past-form condition cannot govern its response, so the مضارع must stay مرفوع.',
        'Only **أحضرَ**: a past-form condition puts its response in نصب.',
        ], '**أحضرْ** or **أحضرُ**: after a past-form condition, a مضارع response may take either.'),
    M('7I-3', 'Why can **إن رجعت رجعت** not be fully analysed until the vowels of both ت are known?', [
        'The verb form is fixed, but **تَ**, **تُ** and **تِ** name different people; the vowels identify them.',
        'The vowels decide the mood of each verb, so the condition cannot be identified without them.',
        'The ت is a feminine marker, and its vowel shows whether the subject is a woman.',
        'The vowels show which verb is the condition, since both verbs look identical.',
        ], 'The verb form is fixed, but **تَ**, **تُ** and **تِ** name different people; the vowels identify them.'),
    G('7I-4', 'Compare the function of ن.', ['Function'], R(
        ['نون الإعراب: the sign of رفع', 'نون النسوة: the subject pronoun', 'نون التوكيد: a particle of emphasis'],
        [('تكتبون', 'نون الإعراب: the sign of رفع'), ('يكتبْنَ', 'نون النسوة: the subject pronoun'), ('تجتهدَنَّ', 'نون التوكيد: a particle of emphasis')])),
    G('7R', 'Explain each verb’s mood and governor.', ['Mood and governor'], R(
        ['مجزوم بالسكون through the conditional construction', 'منصوب بلن بالفتحة'],
        [('تجتهدْ / تنجحْ in إن تجتهدْ تنجحْ', 'مجزوم بالسكون through the conditional construction'), ('تندمَ in لن تندمَ', 'منصوب بلن بالفتحة')])),
]

ITEMS['8'] = [
    G('8G-1', 'Give the ending of the response word and what is responsible.', ['Ending and reason'], R(
        ['ناجحٌ: خبر مرفوع', 'تندمَ: منصوب بلن', 'تنجحُ: مرفوع; سوف does not govern', 'مجزوم بإن'],
        [('إن تجتهدْ فأنت ناجح…', 'ناجحٌ: خبر مرفوع'), ('إن تجتهدْ فلن تندم…', 'تندمَ: منصوب بلن'), ('إن تجتهدْ فسوف تنجح…', 'تنجحُ: مرفوع; سوف does not govern')])),
    G('8G-2', 'Rewrite **ادخلْ تسترحْ** with explicit إن.', ['Answer'], [
        ('With إن', [(['إِنْ تَدْخُلْ تَسْتَرِحْ', 'إِنْ ادْخُلْ تَسْتَرِحْ', 'إِنْ تَدْخُلُ تَسْتَرِيحُ'], 'إِنْ تَدْخُلْ تَسْتَرِحْ')]),
        ('Is **ادخلْ** مجزوم?', [(['No: it is an imperative مبني على السكون', 'Yes'], 'No: it is an imperative مبني على السكون')])]),
    G('8G-3', 'Distinguish the two ف particles.', ['فـ is'], R(
        ['فاء السببية: the verb is منصوب بأن مضمرة', 'فاء الجواب: لن governs the verb'],
        [('اجتهد فتفهمَ', 'فاء السببية: the verb is منصوب بأن مضمرة'), ('إن تجتهد فلن تندمَ', 'فاء الجواب: لن governs the verb')])),
    G('8I-1', 'أعرب: **إن تفتح الباب فسيدخل الضيف**', ['Analysis'], R(
        ['حرف شرط جازم', 'مضارع مجزوم بإن بالسكون، فعل الشرط', 'رابطة لجواب الشرط', 'حرف استقبال لا يعمل', 'مضارع مرفوع بالضمة', 'جملة في محل جزم جواب الشرط'],
        [('إن', 'حرف شرط جازم'), ('تفتحْ', 'مضارع مجزوم بإن بالسكون، فعل الشرط'), ('فـ', 'رابطة لجواب الشرط'), ('سـ', 'حرف استقبال لا يعمل'),
         ('يدخلُ', 'مضارع مرفوع بالضمة'), ('سيدخل الضيف', 'جملة في محل جزم جواب الشرط')])),
    G('8I-2', 'صحّح وعلّل.', ['Correct form'], [
        ('إن تحضر فأنت ناجحًا', [(['إِنْ تَحْضُرْ فَأَنْتَ نَاجِحٌ', 'إِنْ تَحْضُرْ فَأَنْتَ نَاجِحًا', 'إِنْ تَحْضُرُ فَأَنْتَ نَاجِحٌ'], 'إِنْ تَحْضُرْ فَأَنْتَ نَاجِحٌ')]),
        ('إن تجتهد فلن تندمْ', [(['إِنْ تَجْتَهِدْ فَلَنْ تَنْدَمَ', 'إِنْ تَجْتَهِدْ فَلَنْ تَنْدَمْ', 'إِنْ تَجْتَهِدْ فَلَنْ تَنْدَمُ'], 'إِنْ تَجْتَهِدْ فَلَنْ تَنْدَمَ')])]),
    G('8I-3', 'After **هل تزورنا**, explain each ending.', ['Meaning'], R(
        ['a separate statement “We honour you”; no جازم', 'an intended conditional result: إن تزرْنا نكرمْك'],
        [('نكرمُكَ', 'a separate statement “We honour you”; no جازم'), ('نكرمْكَ', 'an intended conditional result: إن تزرْنا نكرمْك')])),
    G('8I-4', 'Choose the ending.', ['Ending'], [
        ('اجتهد تنجحـ', [(['تنجحْ', 'تنجحَ', 'تنجحُ'], 'تنجحْ')]),
        ('اجتهد فتنجحـ', [(['تنجحْ', 'تنجحَ', 'تنجحُ'], 'تنجحَ')]),
        ('إن اجتهدت فسوف تنجحـ', [(['تنجحْ', 'تنجحَ', 'تنجحُ'], 'تنجحُ')])]),
    G('8R', 'Match each term to its example.', ['Example'], R(
        ['جئتُ لأتعلّمَ', 'اجتهدْ تنجحْ', 'اجتهدْ فتنجحَ', 'إن تجتهدْ فلن تندمَ'],
        [('أن مضمرة', 'جئتُ لأتعلّمَ'), ('إن مقدّرة', 'اجتهدْ تنجحْ'), ('فاء السببية', 'اجتهدْ فتنجحَ'), ('فاء الجواب', 'إن تجتهدْ فلن تندمَ')])),
]

ITEMS['R'] = [
    G('A-1', '**تنصب أن المصدرية الفعل المضارع… وتجزم إن الشرطية فعلين…** Explain the two verbs.', ['Meaning'], R(
        ['governs in نصب', 'governs in جزم', 'governs in رفع'], [('تنصب', 'governs in نصب'), ('تجزم', 'governs in جزم')]), sol='A-1'),
    G('A-2', 'Explain each word from context.', ['Meaning'], R(
        ['is left understood', 'optionally', 'obligatorily', 'was joined or linked to'],
        [('تضمر', 'is left understood'), ('جوازًا', 'optionally'), ('وجوبًا', 'obligatorily'), ('اقترن', 'was joined or linked to')])),
    M('A-3', 'Why does **وإذا اقترن الجواب بالفاء لم تعمل إن في فعل الجواب** allow **إن تجتهد فلن تندمَ**?', [
        'With linking فـ, إن does not set the response verb’s ending: **لن** governs it.',
        'إن governs **تندمَ** in نصب through the فاء, since a linked response takes نصب instead of جزم.',
        'The فاء itself puts **تندمَ** in نصب as فاء السببية, so **لن** adds only the negation.',
        'It does not allow it: the response must be **تندمْ**.',
        ], 'With linking فـ, إن does not set the response verb’s ending: **لن** governs it.'),
    G('A-4', 'Classify each construction.', ['أن may be'], R(
        ['expressed or understood', 'only understood'],
        [('جئت لأتعلّمَ / جئت لأن أتعلّمَ', 'expressed or understood'), ('انتظر حتى يرجعَ خالدٌ (still future)', 'only understood'), ('اجتهد فتنجحَ', 'only understood')])),
    G('B', '**ذَهَبَ خَالِدٌ إِلَى المُعَلِّمِ لِيَتَعَلَّمَ. يُرِيدُ أَنْ يَفْهَمَ الدَّرْسَ، لَكِنَّهُ لَمْ يَكْتُبْ الجَوَابَ. قَالَ المُعَلِّمُ: اِجْتَهِدْ فَتَفْهَمَ، وَلَا تُهْمِلْ فَتَنْدَمَ. إِنْ تَكْتُبْ الجَوَابَ فَسَوْفَ تَفْهَمُ القَاعِدَةَ.** Choose the analysis of each verb.', ['Analysis'], R(
        ['منصوب بأن مضمرة جوازًا بعد لام التعليل', 'مرفوع بالضمة', 'منصوب بأن الظاهرة بالفتحة', 'مجزوم بلم بالسكون', 'أمر مبني على السكون',
         'منصوب بأن مضمرة وجوبًا بعد فاء السببية', 'مجزوم بلا الناهية بالسكون', 'فعل الشرط، مجزوم بإن بالسكون'],
        [('يتعلّمَ', 'منصوب بأن مضمرة جوازًا بعد لام التعليل'), ('يريدُ', 'مرفوع بالضمة'), ('يفهمَ', 'منصوب بأن الظاهرة بالفتحة'), ('يكتبْ', 'مجزوم بلم بالسكون'),
         ('اجتهدْ', 'أمر مبني على السكون'), ('تفهمَ (after اجتهد)', 'منصوب بأن مضمرة وجوبًا بعد فاء السببية'), ('تهملْ', 'مجزوم بلا الناهية بالسكون'),
         ('تندمَ', 'منصوب بأن مضمرة وجوبًا بعد فاء السببية'), ('تكتبْ', 'فعل الشرط، مجزوم بإن بالسكون'), ('تفهمُ (after سوف)', 'مرفوع بالضمة')])),
    G('B-b', 'Passage B: the two types of **فـ**, and the tarkīb of **يريد أن يفهم الدرس**.', ['Analysis'], R(
        ['فاء السببية: introduces a consequence after طلب, with obligatory understood أن', 'رابطة لجواب الشرط: does not impose نصب',
         'مصدر مؤوّل في محل نصب مفعول به ليريد', 'ضمير في محل نصب اسم لكنّ'],
        [('فـ in فتفهمَ / فتندمَ', 'فاء السببية: introduces a consequence after طلب, with obligatory understood أن'), ('فـ before سوف', 'رابطة لجواب الشرط: does not impose نصب'),
         ('أن يفهم الدرس', 'مصدر مؤوّل في محل نصب مفعول به ليريد'), ('ـه in لكنّه', 'ضمير في محل نصب اسم لكنّ')]), sol='B'),
    G('C', '**نُرِيدُ أَنْ نَزُورَ خَالِدًا، لَكِنَّهُ لَمَّا يَرْجِعْ مِنَ السَّفَرِ. لَنْ نَخْرُجَ حَتَّى يَحْضُرَ. إِنْ حَضَرَ خَرَجْنَا. قَالَ أَخِي: هَلْ تَزُورُونَنَا نُكْرِمْكُمْ؟** Choose the analysis of each verb.', ['Analysis'], R(
        ['منصوب بأن بالفتحة', 'مجزوم بلمّا بالسكون', 'منصوب بلن بالفتحة', 'منصوب بأن مضمرة وجوبًا بعد حتى', 'ماضٍ مبني على الفتح في محل جزم، فعل الشرط',
         'ماضٍ مبني على السكون في محل جزم، جواب الشرط', 'مضارع مرفوع بثبوت النون', 'مضارع مجزوم بالسكون، جواب شرط مقدّر'],
        [('نزورَ', 'منصوب بأن بالفتحة'), ('يرجعْ', 'مجزوم بلمّا بالسكون'), ('نخرجَ', 'منصوب بلن بالفتحة'), ('يحضرَ', 'منصوب بأن مضمرة وجوبًا بعد حتى'),
         ('حضرَ', 'ماضٍ مبني على الفتح في محل جزم، فعل الشرط'), ('خرجنا', 'ماضٍ مبني على السكون في محل جزم، جواب الشرط'), ('تزوروننا', 'مضارع مرفوع بثبوت النون'),
         ('نكرمْكم', 'مضارع مجزوم بالسكون، جواب شرط مقدّر')])),
    G('C-b', 'Passage C: time reference and pronouns.', ['Answer'], [
        ('لمّا يرجعْ', [(['not returned up to now, with his return expected', 'he will never return', 'he returned long ago'], 'not returned up to now, with his return expected')]),
        ('إن حضرَ خرجنا', [(['If he comes, we will go out (hypothetical)', 'two completed past events'], 'If he comes, we will go out (hypothetical)')]),
        ('نا in تزوروننا', [(['ضمير في محل نصب مفعول به', 'ضمير في محل رفع فاعل'], 'ضمير في محل نصب مفعول به')]),
        ('Subject of نكرمْ', [(['ضمير مستتر تقديره نحن', 'كم', 'واو الجماعة'], 'ضمير مستتر تقديره نحن')])], sol='C'),
    M('D-1', 'Correct: “In **لن يكتبوا**, واو الجماعة is the sign of نصب.”', [
        'The sign is **حذف النون**; واو الجماعة is the subject pronoun.',
        'The sign is the written alif; واو الجماعة is the subject pronoun.',
        'The sign is fatḥah on the ب; واو الجماعة marks the plural.',
        'The claim is correct: the واو marks نصب and the alif marks the subject.',
        ], 'The sign is **حذف النون**; واو الجماعة is the subject pronoun.'),
    M('D-2', 'Correct: “Every **أن** makes the following verb منصوبًا.”', [
        'Only **أن المصدرية الناصبة** does; lightened **أن** has a خبر clause and leaves the verb alone.',
        'The claim is correct: every أن, lightened or not, makes the following مضارع منصوب by its own government.',
        'No أن governs a verb at all; the نصب after أن always comes from the verb that precedes it.',
        'Every أن makes the verb مجزوم, except after verbs of certainty.',
        ], 'Only **أن المصدرية الناصبة** does; lightened **أن** has a خبر clause and leaves the verb alone.'),
    M('D-3', 'Correct: “Every verb after و or ف takes نصب.”', [
        'Plain coordination conceals no أن; the accompaniment or consequence context must be present.',
        'The claim is correct: و and ف always conceal أن before a مضارع, whatever comes before them.',
        'Every verb after و or ف is مجزوم, because it is coordinated with an implied command.',
        'Verbs after و are منصوب; verbs after ف are مرفوع.',
        ], 'Plain coordination conceals no أن; the accompaniment or consequence context must be present.'),
    M('D-4', 'Correct: “**لم يرمِ** is مجرور because it ends in kasrah.”', [
        'Verbs do not take جرّ: **يرمِ** is مجزوم by deleting the weak letter.',
        'The claim is correct: the kasrah shows the verb is genitive after **لم**.',
        '**يرمِ** is منصوب by **لم**, with kasrah replacing fatḥah.',
        '**يرمِ** is مرفوع with an estimated ḍammah; the kasrah is for pronunciation.',
        ], 'Verbs do not take جرّ: **يرمِ** is مجزوم by deleting the weak letter.'),
    M('D-5', 'Correct: “A fixed past verb cannot have a conditional grammatical position.”', [
        'A past verb stays مبني but can be **في محل جزم** as a condition or response.',
        'The claim is correct: a fixed verb can never have a grammatical position.',
        'A past verb after إن becomes مجزوم with a visible sukūn.',
        'A past verb after إن becomes منصوب, because the condition is hypothetical.',
        ], 'A past verb stays مبني but can be **في محل جزم** as a condition or response.'),
    M('D-6', 'Correct: “The verb in **إن تجتهد فلن تندمَ** must be مجزوم because it is in the response.”', [
        '**تندمَ** is منصوب بلن; the response **لن تندم** as a whole is في محل جزم.',
        'The claim is correct: the response verb is **تندمْ**, مجزوم by إن.',
        '**تندمُ** is مرفوع, because فاء الجواب cancels all government.',
        '**تندمَ** is منصوب by the فاء, which is فاء السببية here.',
        ], '**تندمَ** is منصوب بلن; the response **لن تندم** as a whole is في محل جزم.'),
    M('D-7', 'Correct: “**لن** always means permanent negation, and **إن** always implies doubt.”', [
        '**لن** means permanent negation only with context; **إن** can introduce any kind of condition.',
        'The claim is correct: **لن** always means never, and **إن** always shows the speaker’s doubt about the condition.',
        '**لن** always means never, but **إن** can introduce possible, doubtful, hypothetical or impossible conditions.',
        '**لن** negates the past; **إن** always implies certainty.',
        ], '**لن** means permanent negation only with context; **إن** can introduce any kind of condition.'),
    G('E-1', '**لَنْ يَكْتُبَ الطَّالِبُ الرِّسَالَةَ حَتَّى يَفْهَمَ السُّؤَالَ.**', ['Analysis'], R(
        ['حرف نفي ونصب واستقبال', 'مضارع منصوب بلن بالفتحة', 'فاعل مرفوع بالضمة', 'مفعول به منصوب بالفتحة', 'مضارع منصوب بأن مضمرة وجوبًا بعد حتى',
         'مصدر مؤوّل في محل جرّ بحتى'],
        [('لن', 'حرف نفي ونصب واستقبال'), ('يكتبَ', 'مضارع منصوب بلن بالفتحة'), ('الطالبُ', 'فاعل مرفوع بالضمة'), ('الرسالةَ / السؤالَ', 'مفعول به منصوب بالفتحة'),
         ('يفهمَ', 'مضارع منصوب بأن مضمرة وجوبًا بعد حتى'), ('أن يفهم السؤال', 'مصدر مؤوّل في محل جرّ بحتى')]), sol='E'),
    G('E-2', '**إِنْ تَحْفَظُوا الدَّرْسَ فَلَنْ تَنْسَوُا القَاعِدَةَ.**', ['Analysis'], R(
        ['حرف شرط جازم', 'مضارع مجزوم بإن بحذف النون، فعل الشرط', 'رابطة لجواب الشرط', 'مضارع منصوب بلن بحذف النون', 'جملة في محل جزم جواب الشرط',
         'ضمير في محل رفع فاعل'],
        [('إن', 'حرف شرط جازم'), ('تحفظوا', 'مضارع مجزوم بإن بحذف النون، فعل الشرط'), ('فـ', 'رابطة لجواب الشرط'), ('تنسوا', 'مضارع منصوب بلن بحذف النون'),
         ('لن تنسوا القاعدة', 'جملة في محل جزم جواب الشرط'), ('واو الجماعة (both verbs)', 'ضمير في محل رفع فاعل')]), sol='E'),
    G('E-3', '**اِجْتَهِدْ تَفْهَمْ الدَّرْسَ.** (the second action is a conditional result)', ['Analysis'], R(
        ['فعل أمر مبني على السكون؛ فاعله مستتر تقديره أنت', 'مضارع مجزوم بالسكون، جواب شرط مقدّر', 'مفعول به منصوب بالفتحة', 'مضارع منصوب بأن مضمرة'],
        [('اجتهدْ', 'فعل أمر مبني على السكون؛ فاعله مستتر تقديره أنت'), ('تفهمْ', 'مضارع مجزوم بالسكون، جواب شرط مقدّر'), ('الدرسَ', 'مفعول به منصوب بالفتحة')]), sol='E'),
]
