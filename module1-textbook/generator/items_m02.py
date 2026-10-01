# Module 2: Verbs as Governing Elements. Auto-checked items; correct answers follow the Module 2 answers file.
from item_kit import M, G, R, ENDA, TF

OBJ = ['فاعل', 'مفعول به أوّل', 'مفعول به ثانٍ', 'مفعول به ثالث']
TREAT = ['إعمال', 'إلغاء', 'تعليق']

ITEMS = {}

L1G3 = ['فاعل مرفوع بالضمة', 'ظرف مكان منصوب بالفتحة، وهو مضاف', 'مضاف إليه مجرور بالكسرة', 'متعلق بجلس، ظرف لغو', 'مفعول به منصوب بالفتحة']
L1I1 = ['فعل ماضٍ مبني على الفتح', 'فاعل مرفوع بالضمة', 'حرف جرّ', 'اسم مجرور بمن بالكسرة', 'متعلق بخرج، ظرف لغو', 'مفعول به منصوب بالفتحة']
L1I3 = ['مفعول به منصوب بالفتحة', 'اسم مجرور بالباء بالكسرة', 'متعلق بذهب: مفعول به غير صريح', 'فاعل مرفوع بالضمة']
L1R = ['حرف نفي وجزم وقلب، يجزم يفتح', 'مضارع مجزوم بلم، وعلامة جزمه السكون', 'فاعل مرفوع بالضمة', 'مفعول به منصوب بالفتحة',
       'مضارع منصوب بلم، وعلامة نصبه الفتحة']

ITEMS['1'] = [
    G('1G-1', 'Match each term with its meaning.', ['Meaning'], R(
        ['verb reaching an object', 'nominative replacement in a passive construction', 'verb not reaching a direct object'],
        [('لازم', 'verb not reaching a direct object'), ('متعدٍّ', 'verb reaching an object'),
         ('نائب الفاعل', 'nominative replacement in a passive construction')])),
    G('1G-2', 'Choose the ending and role: **فُتِحَ البَاب…** “The door was opened.”', ['Ending', 'Role'], [
        ('البَاب…', [(['ـُ', 'ـَ'], 'ـُ'), (['نائب فاعل', 'مفعول به', 'فاعل'], 'نائب فاعل')])]),
    G('1G-3', 'Analyse **جَلَسَ خَالِدٌ أَمَامَ البَابِ**.', ['Analysis'], R(L1G3, [
        ('خالدٌ', 'فاعل مرفوع بالضمة'), ('أمامَ', 'ظرف مكان منصوب بالفتحة، وهو مضاف'), ('البابِ', 'مضاف إليه مجرور بالكسرة'),
        ('أمام الباب', 'متعلق بجلس، ظرف لغو')]) + [
        ('Is **جلس** متعدٍّ here?', [(['No: there is no direct object', 'Yes: **أمامَ** is its مفعول به'], 'No: there is no direct object')])]),
    G('1I-1', 'Analyse **خَرَجَ الضَّيْفُ مِنَ البَيْتِ**, “The guest went out of the house.”', ['Analysis'], R(L1I1, [
        ('خرجَ', 'فعل ماضٍ مبني على الفتح'), ('الضيفُ', 'فاعل مرفوع بالضمة'), ('من', 'حرف جرّ'), ('البيتِ', 'اسم مجرور بمن بالكسرة'),
        ('من البيت', 'متعلق بخرج، ظرف لغو')]) + [
        ('Does the location phrase supply a direct object?', [(['No: **خرج** is لازم in this use', 'Yes: **من البيت** is the مفعول به'], 'No: **خرج** is لازم in this use')])]),
    M('1I-2', 'Why is this claim wrong: “**مُتَأَدِّبًا** in the worked example is a مفعول به because it is accusative”?', [
        '**متأدبًا** is a حال describing the student while sitting; accusative case alone does not make a مفعول به.',
        '**متأدبًا** is a مفعول له giving the reason for the sitting; a noun of purpose after **جلس** is always accusative.',
        '**متأدبًا** is a مفعول به of **جلس**, but because it names the manner of sitting it should really be nominative.',
        '**متأدبًا** is a second خبر describing the student, so its fatḥah comes from **جلس** acting as a ناسخ.',
        ], '**متأدبًا** is a حال describing the student while sitting; accusative case alone does not make a مفعول به.'),
    G('1I-3', 'Compare **أَذْهَبَ اللهُ الخَوْفَ** and **ذَهَبَ اللهُ بِالخَوْفِ**, “Allah removed the fear.”', ['Analysis'], R(L1I3, [
        ('**الخوفَ** in أذهب الله الخوف', 'مفعول به منصوب بالفتحة'), ('**الخوفِ** in ذهب الله بالخوف', 'اسم مجرور بالباء بالكسرة'),
        ('**بالخوف**', 'متعلق بذهب: مفعول به غير صريح'), ('**اللهُ** in both', 'فاعل مرفوع بالضمة')])),
    G('1R', 'In **لَمْ يَفْتَحْ خَالِدٌ البَابَ**, choose the analysis of each word.', ['Analysis'], R(L1R, [
        ('لم', 'حرف نفي وجزم وقلب، يجزم يفتح'), ('يفتحْ', 'مضارع مجزوم بلم، وعلامة جزمه السكون'), ('خالدٌ', 'فاعل مرفوع بالضمة'),
        ('البابَ', 'مفعول به منصوب بالفتحة')])),
    M('1-Read', 'Read: **الفعل اللازم لا يتجاوز أثر فاعله إلى المفعول به.** (**يتجاوز** = passes beyond; **أثر** = effect.) Why does **أمام المعلم** in **جلس الطالب أمام المعلم** not contradict this rule?', [
        '**أمام المعلم** specifies the place of sitting; it is not a direct object, so the rule holds.',
        '**المعلم** receives the sitting directly, so **جلس** is متعدٍّ here and the rule does not apply.',
        '**أمام** is a مفعول به منصوب, but adverbs are exempt from the rule because they name a place.',
        'The rule concerns only مضارع verbs; **جلس** is past, so its subject’s effect may pass on.',
        ], '**أمام المعلم** specifies the place of sitting; it is not a direct object, so the rule holds.'),
]

L2I1 = ['فعل ماضٍ مبني على الفتح', 'تاء التأنيث الساكنة، حرف لا محل له', 'فاعل مرفوع بالضمة', 'مفعول به أوّل منصوب بالفتحة',
        'مفعول به ثانٍ منصوب بالفتحة', 'ضمير متصل في محل رفع فاعل']
L2R = ['فعل ماضٍ مبني على الفتح المقدّر على الألف', 'ضمير متصل في محل نصب مفعول به', 'فاعل مرفوع بالضمة', 'حرف جرّ',
       'اسم مجرور بإلى بالكسرة', 'متعلق بهدى، ظرف لغو', 'ضمير متصل في محل رفع فاعل']

ITEMS['2'] = [
    G('2G-1', 'Complete and label the nouns: **مَنَحَ المُعَلِّمـ… الطَّالِبـ… كِتَابـ…**, “The teacher granted the student a book.”', ['Ending', 'Role'], [
        ('المُعَلِّمـ…', [(ENDA, 'ـُ'), (OBJ[:3], 'فاعل')]), ('الطَّالِبـ…', [(ENDA, 'ـَ'), (OBJ[:3], 'مفعول به أوّل')]),
        ('كِتَابـ…', [(ENDA, 'ـًا'), (OBJ[:3], 'مفعول به ثانٍ')])]),
    G('2G-2', 'Divide **مَنَحْتُهُ كِتَابًا**.', ['Part'], R(
        ['فعل ماضٍ', 'فاعل: ضمير متصل في محل رفع', 'مفعول به أوّل: ضمير متصل في محل نصب', 'مفعول به ثانٍ منصوب'],
        [('منحْـ', 'فعل ماضٍ'), ('ـتُ', 'فاعل: ضمير متصل في محل رفع'), ('ـهُ', 'مفعول به أوّل: ضمير متصل في محل نصب'), ('كتابًا', 'مفعول به ثانٍ منصوب')])),
    G('2G-3', 'Compare **هدى خالدٌ الضيفَ الطريقَ** and **هدى خالدٌ الضيفَ إلى الطريقِ**.', ['Answer'], [
        ('**الطريقَ** in the first', [(['مفعول به ثانٍ منصوب', 'اسم مجرور بإلى', 'حال منصوب'], 'مفعول به ثانٍ منصوب')]),
        ('**الطريقِ** in the second', [(['مفعول به ثانٍ منصوب', 'اسم مجرور بإلى', 'حال منصوب'], 'اسم مجرور بإلى')]),
        ('Which sentence has two direct objects?', [(['the first', 'the second', 'both'], 'the first')])]),
    G('2I-1', 'أعرب: **أَلْبَسَتْ هِنْدٌ الطِّفْلَ ثَوْبًا**, “Hind dressed the child in a garment.”', ['Analysis'], R(L2I1, [
        ('ألبسَـ', 'فعل ماضٍ مبني على الفتح'), ('ـتْ', 'تاء التأنيث الساكنة، حرف لا محل له'), ('هندٌ', 'فاعل مرفوع بالضمة'),
        ('الطفلَ', 'مفعول به أوّل منصوب بالفتحة'), ('ثوبًا', 'مفعول به ثانٍ منصوب بالفتحة')])),
    M('2I-2', 'In a conversation about giving a particular child a garment, the speaker says **أَلْبَسْتُ الطِّفْلَ**. Which analysis is correct?', [
        'The second object, **ثوبًا**, is omitted because the context supplies it; **الطفلَ** stays the first object.',
        'The first object is omitted because the context supplies it; **الطفلَ** is now the second object.',
        'The subject is omitted because the context supplies it; **الطفلَ** becomes the فاعل of **ألبس**.',
        'Nothing is omitted: in this use **ألبس** takes one object, and **الطفلَ** is that single object.',
        ], 'The second object, **ثوبًا**, is omitted because the context supplies it; **الطفلَ** stays the first object.'),
    M('2I-3', 'Why is this claim wrong: “In **أعطيته كتابًا**, only **كتابًا** counts as an object because it alone shows fatḥah”?', [
        '**هُ** is also an object, a fixed pronoun in محل نصب مفعول به أوّل; **كتابًا** is the second object.',
        '**هُ** is the subject of **أعطى**, a fixed pronoun in محل رفع; **كتابًا** is its only object.',
        '**هُ** is a مضاف إليه attached to the verb, in محل جرّ; **كتابًا** is its only object.',
        '**هُ** is an object, but **كتابًا** is a حال describing the gift, so there is still one object.',
        ], '**هُ** is also an object, a fixed pronoun in محل نصب مفعول به أوّل; **كتابًا** is the second object.'),
    G('2R', 'Analyse **هَدَانَا خَالِدٌ إِلَى المَسْجِدِ**, “Khalid guided us to the mosque.”', ['Analysis'], R(L2R, [
        ('هدى', 'فعل ماضٍ مبني على الفتح المقدّر على الألف'), ('نا', 'ضمير متصل في محل نصب مفعول به'), ('خالدٌ', 'فاعل مرفوع بالضمة'),
        ('إلى', 'حرف جرّ'), ('المسجدِ', 'اسم مجرور بإلى بالكسرة'), ('إلى المسجد', 'متعلق بهدى، ظرف لغو')])),
    M('2-Read', 'Read: **يجوز حذف المفعول الأوّل أو الثاني أو كليهما.** (**حذف** = omission; **كليهما** = both of them.) What does it say?', [
        'The first object, the second, or both may be omitted.',
        'Only the second object may be omitted; the first must always be expressed.',
        'Neither object may be omitted unless the subject is also omitted.',
        'The subject or the first object may be omitted, but never the second.',
        ], 'The first object, the second, or both may be omitted.'),
]

ITEMS['3'] = [
    M('3G-1', 'Begin with **العِلْمُ نَافِعٌ** and add **ظَنَنْتُ**. Which is correct?', [
        'ظَنَنْتُ العِلْمَ نَافِعًا', 'ظَنَنْتُ العِلْمُ نَافِعٌ', 'ظَنَنْتُ العِلْمَ نَافِعٌ', 'ظَنَنْتُ العِلْمُ نَافِعًا'], 'ظَنَنْتُ العِلْمَ نَافِعًا'),
    G('3G-1b', 'Name the roles in **ظَنَنْتُ العِلْمَ نَافِعًا**.', ['Role'], R(OBJ[:3], [
        ('ـتُ', 'فاعل'), ('العلمَ', 'مفعول به أوّل'), ('نافعًا', 'مفعول به ثانٍ')]), sol='3G-1'),
    G('3G-2', 'Match each term with its meaning.', ['Meaning'], R(
        ['in the underlying construction', 'certainty', 'a judgement leaning towards one possibility'],
        [('يقين', 'certainty'), ('رجحان', 'a judgement leaning towards one possibility'), ('في الأصل', 'in the underlying construction')])),
    M('3G-3', 'How does **كتابًا** in **أعطيتُ خالدًا كتابًا** differ from **صادقًا** in **علمتُ خالدًا صادقًا**?', [
        '**كتابًا** names what is given to Khalid; **صادقًا** is the quality attributed to him in a judgement.',
        '**كتابًا** is a second object; **صادقًا** is a حال describing Khalid at the moment of knowing.',
        '**صادقًا** names what Khalid is given; **كتابًا** is the quality attributed to him in a judgement.',
        'Both form a statement about Khalid, **خالدٌ كتابٌ** and **خالدٌ صادقٌ**; only the verbs differ.',
        ], '**كتابًا** names what is given to Khalid; **صادقًا** is the quality attributed to him in a judgement.'),
    G('3I-1', 'Choose the object count from the intended sense.', ['Objects'], R(['one object', 'two objects'], [
        ('**وجدت المفتاح**: I located the key', 'one object'), ('**وجدت الصبر نافعا**: I found patience beneficial', 'two objects')])),
    G('3I-1b', 'Add the noun endings.', ['Ending'], R(ENDA, [
        ('وجدتُ المفتاحـ…', 'ـَ'), ('وجدتُ الصبرـ…', 'ـَ'), ('…نافعـ…', 'ـًا')]), sol='3I-1'),
    G('3I-2', 'أعرب: **حسبت الضيف عند الباب**, “I supposed the guest was by the door.”', ['Analysis'], R(
        ['مفعول به أوّل منصوب بالفتحة', 'ظرف منصوب بالفتحة، وهو مضاف', 'مضاف إليه مجرور بالكسرة', 'ظرف مستقرّ في محل نصب مفعول به ثانٍ',
         'ظرف لغو متعلق بحسب', 'فاعل مرفوع بالضمة'],
        [('الضيفَ', 'مفعول به أوّل منصوب بالفتحة'), ('عندَ', 'ظرف منصوب بالفتحة، وهو مضاف'), ('البابِ', 'مضاف إليه مجرور بالكسرة'),
         ('عند الباب', 'ظرف مستقرّ في محل نصب مفعول به ثانٍ')]) + [
        ('Underlying assertion', [(['الضيفُ عندَ البابِ', 'الضيفَ عندَ البابِ', 'البابُ عندَ الضيفِ'], 'الضيفُ عندَ البابِ')])]),
    M('3I-3', 'Why is this claim wrong: “**رأيت خالدًا** must have a missing second object, because **رأى** appears in the list of أفعال القلوب”?', [
        '**رأى** meaning physical seeing takes one object; no second object is missing.',
        '**رأى** is a فعل قلب here, so the second object is understood from context by اختصار.',
        '**خالدًا** is the second object, and the first object is the omitted pronoun of the speaker.',
        'Every **رأى** takes two objects, so the sentence needs a predicate such as **صادقًا**.',
        ], '**رأى** meaning physical seeing takes one object; no second object is missing.'),
    G('3R', 'Compare **ظَنَنْتُ الطَّالِبَ مُتَأَدِّبًا** with **جَلَسَ الطَّالِبُ مُتَأَدِّبًا**.', ['Role'], R(
        ['مفعول به أوّل', 'مفعول به ثانٍ', 'فاعل', 'حال'],
        [('**الطالبَ** in ظننت الطالب متأدبا', 'مفعول به أوّل'), ('**متأدبًا** in ظننت الطالب متأدبا', 'مفعول به ثانٍ'),
         ('**الطالبُ** in جلس الطالب متأدبا', 'فاعل'), ('**متأدبًا** in جلس الطالب متأدبا', 'حال')])),
    M('3R-b', 'Why does the same ending on **متأدبًا** not imply the same role?', [
        'Both roles require نصب, so the ending alone cannot distinguish them.',
        'Both are objects of their verbs, and objects always share the same ending.',
        'A حال always takes the ending of the noun it describes, so they must match.',
        'The fatḥah on **متأدبًا** comes from the noun before it in both sentences.',
        ], 'Both roles require نصب, so the ending alone cannot distinguish them.', sol='3R'),
    M('3-Read', 'Read: **مفعولا فعل القلب مبتدأ وخبر في الأصل.** Which restatement is correct?', [
        'A cognitive verb’s two objects are originally a مبتدأ and خبر: **علمتُ خالدًا في البيت** comes from **خالدٌ في البيت**.',
        'Any two-object verb has an underlying مبتدأ and خبر: **أعطيتُ خالدًا كتابًا** comes from **خالدٌ كتابٌ**.',
        'A cognitive verb turns its own subject into a مبتدأ: **علمتُ خالدًا** comes from **أنا خالدٌ**.',
        'A cognitive verb’s first object is originally a فاعل: **علمتُ خالدًا في البيت** comes from **جلس خالدٌ**.',
        ], 'A cognitive verb’s two objects are originally a مبتدأ and خبر: **علمتُ خالدًا في البيت** comes from **خالدٌ في البيت**.'),
]

ITEMS['4'] = [
    G('4G-1', 'Supply endings and roles: **صَيَّرَ النَّجَّارـ… الخَشَبـ… بَابـ…**.', ['Ending', 'Role'], [
        ('النَّجَّارـ…', [(ENDA, 'ـُ'), (OBJ[:3], 'فاعل')]), ('الخَشَبـ…', [(ENDA, 'ـَ'), (OBJ[:3], 'مفعول به أوّل')]),
        ('بَابـ…', [(ENDA, 'ـًا'), (OBJ[:3], 'مفعول به ثانٍ')])]),
    M('4G-2', 'In **أريتُ خالدًا الأمرَ سهلًا**, which pair expresses a predication?', [
        'the second and third objects: **الأمرُ سهلٌ**', 'the first and second objects: **خالدٌ الأمرُ**', 'the first and third objects: **خالدٌ سهلٌ**'],
        'the second and third objects: **الأمرُ سهلٌ**'),
    M('4G-3', 'Does “The carpenter made the wood into a door” mean the wood was already a door?', [
        'No. **في الأصل** names the underlying مبتدأ–خبر link; the transformation makes it true as a result.',
        'Yes. **في الأصل** means the wood was already a door before the action began.',
        'Yes. A cognitive verb’s objects always describe a state that existed beforehand.',
        'No. **بابًا** is a حال describing the result, so the two nouns have no underlying link.',
        ], 'No. **في الأصل** names the underlying مبتدأ–خبر link; the transformation makes it true as a result.'),
    G('4I-1', 'أعرب: **اتخذ خالد سعيدا صديقا**, “Khalid took Saʿīd as a friend.”', ['Analysis'], R(
        ['فعل ماضٍ مبني على الفتح', 'فاعل مرفوع بالضمة', 'مفعول به أوّل منصوب بالفتحة', 'مفعول به ثانٍ منصوب بالفتحة', 'حال منصوب بالفتحة'],
        [('اتخذَ', 'فعل ماضٍ مبني على الفتح'), ('خالدٌ', 'فاعل مرفوع بالضمة'), ('سعيدًا', 'مفعول به أوّل منصوب بالفتحة'),
         ('صديقًا', 'مفعول به ثانٍ منصوب بالفتحة')]) + [
        ('Underlying predication', [(['سعيدٌ صديقٌ', 'خالدٌ صديقٌ', 'خالدٌ سعيدٌ'], 'سعيدٌ صديقٌ')])]),
    G('4I-2', 'Analyse **أَرَيْتُ الضَّيْفَ الطَّرِيقَ سَهْلًا**, “I showed the guest that the way was easy.”', ['Role'], R(OBJ, [
        ('ـتُ', 'فاعل'), ('الضيفَ', 'مفعول به أوّل'), ('الطريقَ', 'مفعول به ثانٍ'), ('سهلًا', 'مفعول به ثالث')])),
    M('4I-3', 'Both **وهبت الطفل ثوبا** and **جعلت الخشب بابا** have two objects. What differs?', [
        '**وهبت**: recipient and gift, no assertion. **جعلت**: the second object predicates the first’s result.',
        '**وهبت**: the second object predicates the first. **جعلت**: recipient and gift, no assertion.',
        'Both express an assertion, **الطفلُ ثوبٌ** and **الخشبُ بابٌ**; only the verb meanings differ.',
        '**وهبت** has two objects; **جعلت** has one object and a حال describing the result.',
        ], '**وهبت**: recipient and gift, no assertion. **جعلت**: the second object predicates the first’s result.'),
    G('4R', 'Contrast the three sentences.', ['Objects', 'Sense'], [
        ('رأيتُ البابَ (physical seeing)', [(['one', 'two', 'three'], 'one'), (['physical seeing', 'cognitive judgement', 'cognitive causative'], 'physical seeing')]),
        ('رأيتُ العلمَ نافعًا', [(['one', 'two', 'three'], 'two'), (['physical seeing', 'cognitive judgement', 'cognitive causative'], 'cognitive judgement')]),
        ('أريتُ خالدًا العلمَ نافعًا', [(['one', 'two', 'three'], 'three'), (['physical seeing', 'cognitive judgement', 'cognitive causative'], 'cognitive causative')])]),
    M('4-Read', 'Read: **المفعول الثاني والثالث مبتدأ وخبر في الأصل.** Which verb type does it describe?', [
        'the cognitive three-object construction, as in **أريتُ خالدًا الأمرَ سهلًا**',
        'two-object verbs of giving, as in **أعطيتُ خالدًا كتابًا**',
        'verbs of transformation, as in **جعلتُ الخشبَ بابًا**',
        'cognitive two-object verbs, as in **ظننتُ الأمرَ سهلًا**',
        ], 'the cognitive three-object construction, as in **أريتُ خالدًا الأمرَ سهلًا**'),
]

ITEMS['5'] = [
    G('5G-1', 'After **أظننتَ الكتابَ نافعًا؟**, analyse the answer **ظننتُهُ**.', ['Answer'], [
        ('ـتُ', [(['فاعل في محل رفع', 'مفعول به في محل نصب'], 'فاعل في محل رفع')]),
        ('ـهُ', [(['مفعول به أوّل في محل نصب، يعود على الكتاب', 'فاعل في محل رفع', 'مفعول به ثانٍ'], 'مفعول به أوّل في محل نصب، يعود على الكتاب')]),
        ('The omitted object', [(['نافعًا (the second object)', 'الكتابَ (the first object)', 'nothing is omitted'], 'نافعًا (the second object)')]),
        ('Kind of omission', [(['اختصار: the question supplies the evidence', 'اقتصار: omission without evidence'], 'اختصار: the question supplies the evidence')])]),
    M('5G-2', 'Select the sound claim.', [
        '(a) **ظننتُه** always completes “I thought him to be…”', '(b) that intended judgement needs a recoverable predicate'],
        '(b) that intended judgement needs a recoverable predicate'),
    M('5G-3', 'In the special **أرأيتكم**, what is the address kāf?', [
        'a particle of address with no case position',
        'an object pronoun in محل نصب مفعول به',
        'a subject pronoun in محل رفع فاعل',
        ], 'a particle of address with no case position'),
    M('5I-1', 'A speaker says **حسبت الضيف** intending “I supposed the guest was…” but gives no clue to the predicate. What is the problem?', [
        'The judgement lacks its predicate and nothing recovers it (اقتصار); it needs one, e.g. **صادقًا**.',
        'This is acceptable اختصار: the listener can supply any predicate that suits the guest.',
        'The subject is missing; the verb needs an expressed فاعل such as **خالدٌ** before **الضيف**.',
        '**الضيف** should be nominative, because with no predicate it becomes the مبتدأ.',
        ], 'The judgement lacks its predicate and nothing recovers it (اقتصار); it needs one, e.g. **صادقًا**.'),
    G('5I-2', 'في **أرأيت خالدًا أيصدق؟**: عيّن الإعراب.', ['Analysis'], R(
        ['مفعول به أوّل منصوب', 'جملة استفهامية سادّة مسدّ المفعول به الثاني، في محل نصب', 'ضمير مستتر تقديره هو، يعود على خالد', 'مفعول به ثانٍ منصوب', 'فاعل مرفوع'],
        [('خالدًا', 'مفعول به أوّل منصوب'), ('أيصدق؟', 'جملة استفهامية سادّة مسدّ المفعول به الثاني، في محل نصب'),
         ('فاعل **يصدق**', 'ضمير مستتر تقديره هو، يعود على خالد')])),
    M('5I-3', 'Why does the final vowel in **ألم ترَ** not make **ترَ** منصوبًا?', [
        '**ترَ** is مجزوم بلم by deleting the final weak letter; the fatḥah left is not the mood sign.',
        '**ترَ** is منصوب بلم with a visible fatḥah, because **لم** governs like **لن** here.',
        '**ترَ** is مرفوع with an estimated ḍammah; **لم** does not govern verbs ending in alif.',
        '**ترَ** is a past verb fixed on fatḥah, because **لم** turns the meaning to the past.',
        ], '**ترَ** is مجزوم بلم by deleting the final weak letter; the fatḥah left is not the mood sign.'),
    G('5R', 'Give the grammatical explanation of **ظننتُ خالدًا** for each intended meaning.', ['Explanation'], R(
        ['**خالدًا** is the first object; the second object, **صادقًا**, is omitted by اختصار',
         '**خالدًا** is the single object; no second object is required',
         'the second object is omitted without evidence (اقتصار)'],
        [('In a context about truthfulness: “I thought Khalid [truthful]”', '**خالدًا** is the first object; the second object, **صادقًا**, is omitted by اختصار'),
         ('With the meaning “I suspected Khalid”', '**خالدًا** is the single object; no second object is required')])),
    M('5-Read', 'Read: **يجوز الحذف بدليل، ولا يجوز حذف أحد المفعولين بغير دليل في هذا الاستعمال.** Which use is being restricted?', [
        'a cognitive judgement whose two objects are an underlying مبتدأ and خبر',
        'every verb with two objects, including verbs of giving such as **أعطى**',
        'the separate one-object sense “I suspected / accused someone”',
        'verbs of transformation whose objects describe a resulting state',
        ], 'a cognitive judgement whose two objects are an underlying مبتدأ and خبر'),
]

L6 = ['فاعل في محل رفع', 'حرف مصدريّ ونصب', 'اسم أنّ منصوب بالفتحة', 'خبر أنّ مرفوع بالضمة',
      'مصدر مؤوّل في محل نصب سادّ مسدّ المفعولين', 'مفعول به أوّل منصوب', 'مفعول به ثانٍ منصوب']
L6R = ['فاعل في محل رفع', 'حرف مصدريّ ونصب', 'اسم أنّ منصوب بالفتحة', 'اسم مجرور بفي بالكسرة', 'ظرف مستقرّ في محل رفع خبر أنّ',
       'ظرف مستقرّ في محل نصب مفعول به ثانٍ', 'مصدر مؤوّل في محل نصب سادّ مسدّ مفعولي ظنّ']

ITEMS['6'] = [
    M('6G-1', 'Change **علمتُ الضيفَ صادقًا** to an **أنّ** construction.', [
        'عَلِمْتُ أَنَّ الضَّيْفَ صَادِقٌ', 'عَلِمْتُ أَنَّ الضَّيْفَ صَادِقًا', 'عَلِمْتُ أَنَّ الضَّيْفُ صَادِقٌ', 'عَلِمْتُ أَنَّ الضَّيْفُ صَادِقًا'],
        'عَلِمْتُ أَنَّ الضَّيْفَ صَادِقٌ'),
    G('6G-1b', 'Analyse **عَلِمْتُ أَنَّ الضَّيْفَ صَادِقٌ**.', ['Analysis'], R(L6, [
        ('الضيفَ', 'اسم أنّ منصوب بالفتحة'), ('صادقٌ', 'خبر أنّ مرفوع بالضمة'), ('أنّ الضيف صادق', 'مصدر مؤوّل في محل نصب سادّ مسدّ المفعولين')]), sol='6G-1'),
    G('6G-2', 'Match each term with its meaning.', ['Meaning'], R(
        ['filled the place of', 'noun-equivalent formed from a particle and its clause'],
        [('سدّ مسدّ', 'filled the place of'), ('المصدر المؤوّل', 'noun-equivalent formed from a particle and its clause')])),
    G('6G-3', '**ظننتُ أنّ الكتابَ نافعٌ / نافعًا**', ['Answer'], [
        ('Correct ending', [(['نافعٌ', 'نافعًا'], 'نافعٌ')]),
        ('Governor of **الكتابَ**', [(['أنّ', 'ظننتُ'], 'أنّ')]),
        ('Governor of **نافعٌ**', [(['أنّ', 'ظننتُ'], 'أنّ')]),
        ('Governor of the whole **أنّ** unit', [(['أنّ', 'ظننتُ'], 'ظننتُ')])]),
    G('6I-1', 'أعرب: **حَسِبْتُ أَنَّ البَابَ مَفْتُوحٌ**, “I supposed that the door was open.”', ['Analysis'], R(L6, [
        ('ـتُ', 'فاعل في محل رفع'), ('أنّ', 'حرف مصدريّ ونصب'), ('البابَ', 'اسم أنّ منصوب بالفتحة'), ('مفتوحٌ', 'خبر أنّ مرفوع بالضمة'),
        ('أنّ الباب مفتوح', 'مصدر مؤوّل في محل نصب سادّ مسدّ المفعولين')])),
    M('6I-2', 'Correct this analysis: “In **علمتُ أنّ خالدًا صادقٌ**, **خالدًا** is the first object of **علم**, and **صادقٌ** is nominative because the whole complement is nominative.”', [
        '**خالدًا** is اسم أنّ, not an object of **علم**; **صادقٌ** is nominative as خبر أنّ.',
        '**خالدًا** is the first object of **علم**; **صادقٌ** should be **صادقًا** as the second.',
        'The whole complement is nominative, so **خالدًا** should be **خالدٌ** as a مبتدأ.',
        '**خالدًا** is اسم أنّ; **صادقٌ** is nominative because it is the second object of **علم**.',
        ], '**خالدًا** is اسم أنّ, not an object of **علم**; **صادقٌ** is nominative as خبر أنّ.'),
    G('6I-3', 'Compare **أنْ يكتبَ** and **أنْ سيكتبُ**.', ['Which أنْ?'], R(
        ['أن المصدرية الناصبة: it puts the مضارع in نصب', 'أن المخفّفة من الثقيلة: the verbal sentence is its خبر'],
        [('أنْ يكتبَ', 'أن المصدرية الناصبة: it puts the مضارع in نصب'), ('أنْ سيكتبُ', 'أن المخفّفة من الثقيلة: the verbal sentence is its خبر')])),
    G('6R', 'Analyse **ظَنَنْتُ أَنَّ الضَّيْفَ فِي البَيْتِ**.', ['Analysis'], R(L6R, [
        ('ـتُ', 'فاعل في محل رفع'), ('أنّ', 'حرف مصدريّ ونصب'), ('الضيفَ', 'اسم أنّ منصوب بالفتحة'), ('البيتِ', 'اسم مجرور بفي بالكسرة'),
        ('في البيت', 'ظرف مستقرّ في محل رفع خبر أنّ'), ('أنّ الضيف في البيت', 'مصدر مؤوّل في محل نصب سادّ مسدّ مفعولي ظنّ')])),
    M('6-Read', 'Read: **المصدر المؤوّل سادّ مسدّ المفعولين، ولكلماته إعرابها داخل التركيب.** Which explains both levels?', [
        'Externally the whole unit fills both object places; internally its words keep their own inflection.',
        'Every word inside the unit is accusative, because the unit fills the object places.',
        'The unit has no position; only its words are analysed, as an ordinary nominal sentence.',
        'Only the first word inside is the object; the remaining words are nominative.',
        ], 'Externally the whole unit fills both object places; internally its words keep their own inflection.'),
]

L7I1 = ['فاعل في محل رفع', 'حرف نفي غير عامل، لا محل له', 'فعل ماضٍ مبني على الفتح', 'فاعل مرفوع بالضمة',
        'جملة في محل نصب سادّة مسدّ مفعولي علم', 'حرف نفي وجزم', 'مفعول به منصوب']
L7I2 = ['اسم استفهام، مفعول به مقدّم منصوب، عامله قرأ', 'مضاف إليه مجرور بالكسرة', 'فاعل قرأ مرفوع بالضمة',
        'جملة استفهامية في محل نصب سادّة مسدّ مفعولي علم', 'مفعول به منصوب، عامله علم']

ITEMS['7'] = [
    G('7G-1', 'In **علمتُ أخالدٌ حاضرٌ**, analyse the complement.', ['Analysis'], R(
        ['مبتدأ مرفوع بالضمة', 'خبر مرفوع بالضمة', 'في محل نصب، سادّة مسدّ مفعولي علم، معلّق عنها العمل', 'مفعول به أوّل منصوب', 'لا محل لها من الإعراب'],
        [('خالدٌ', 'مبتدأ مرفوع بالضمة'), ('حاضرٌ', 'خبر مرفوع بالضمة'), ('أخالدٌ حاضرٌ', 'في محل نصب، سادّة مسدّ مفعولي علم، معلّق عنها العمل')])),
    M('7G-2', 'Choose and explain: **علمتُ أَحَضَرَ الضيفُ / الضيفَ**.', [
        '**الضيفُ**: it is the فاعل of **حضر**; **علم** does not govern it.',
        '**الضيفَ**: it is the first object of **علم**, fronted inside the question.',
        '**الضيفَ**: it is the object of **حضر**, which is متعدٍّ here.',
        '**الضيفُ**: it is the مبتدأ of the outer sentence after **علم**.',
        ], '**الضيفُ**: it is the فاعل of **حضر**; **علم** does not govern it.'),
    G('7G-3', 'Match each particle with its function in the recognition patterns.', ['Function'], R(
        ['negation', 'interrogation', 'emphasis: لام الابتداء'], [('ما', 'negation'), ('أَ', 'interrogation'), ('لَـ', 'emphasis: لام الابتداء')])),
    G('7I-1', 'أعرب: **علمت ما خرج سعيد**, “I knew Saʿīd had not gone out.”', ['Analysis'], R(L7I1, [
        ('ـتُ', 'فاعل في محل رفع'), ('ما', 'حرف نفي غير عامل، لا محل له'), ('خرجَ', 'فعل ماضٍ مبني على الفتح'), ('سعيدٌ', 'فاعل مرفوع بالضمة'),
        ('ما خرج سعيد', 'جملة في محل نصب سادّة مسدّ مفعولي علم')])),
    G('7I-2', 'في **علمت أيّ كتاب قرأ الضيف**: اضبط وأعرب.', ['Analysis'], R(L7I2, [
        ('أيَّ', 'اسم استفهام، مفعول به مقدّم منصوب، عامله قرأ'), ('كتابٍ', 'مضاف إليه مجرور بالكسرة'), ('الضيفُ', 'فاعل قرأ مرفوع بالضمة'),
        ('أيّ كتاب قرأ الضيف', 'جملة استفهامية في محل نصب سادّة مسدّ مفعولي علم')])),
    G('7I-3', 'Does the interrogative clause fill one remaining object place or both?', ['Places filled'], R(
        ['one: the second object (the first is the person asked)', 'both object places'],
        [('سألت خالدًا أحضر الضيف', 'one: the second object (the first is the person asked)'), ('علمت أحضر الضيف', 'both object places')])),
    M('7R', 'Why is **خالد** accusative in **علمتُ أنّ خالدًا صادقٌ** but nominative in **علمتُ أَخالدٌ صادقٌ**?', [
        '**أنّ** governs **خالدًا** as its اسم; interrogative **أَ** suspends government, so **خالدٌ** is a مبتدأ.',
        '**علم** governs **خالدًا** directly in the first; in the second **أَ** makes it a فاعل.',
        'The second is wrong; interrogative **أَ** also governs, so it should be **أخالدًا صادقًا**.',
        '**أنّ** governs **خالدًا** as its اسم; **أَ** governs **خالدٌ** as its own اسم in رفع.',
        ], '**أنّ** governs **خالدًا** as its اسم; interrogative **أَ** suspends government, so **خالدٌ** is a مبتدأ.'),
    M('7-Read', 'Read: **في التعليق يُبطَل العمل اللفظيّ ويبقى العمل المحليّ.** Which example illustrates it?', [
        '**علمتُ أَخالدٌ صادقٌ**: nominal endings inside, but the question still fills the object position.',
        '**علمتُ خالدًا صادقًا**: both objects are accusative, so wording and position agree.',
        '**خالدٌ صادقٌ علمتُ**: nominal endings inside, and no object position remains.',
        '**علمتُ أنّ خالدًا صادقٌ**: أنّ governs inside, and the unit fills the object position.',
        ], '**علمتُ أَخالدٌ صادقٌ**: nominal endings inside, but the question still fills the object position.'),
]

ITEMS['8'] = [
    G('8G-1', 'With the verb between the pair, choose the preferred endings: **خالد… علمتُ صادق…**', ['Answer'], [
        ('خالد…', [(['خالدٌ', 'خالدًا'], 'خالدًا')]), ('صادق…', [(['صادقٌ', 'صادقًا'], 'صادقًا')]), ('Treatment', [(TREAT, 'إعمال')])]),
    G('8G-2', 'With the verb after the pair, choose the preferred endings: **خالد… صادق… علمتُ**', ['Answer'], [
        ('خالد…', [(['خالدٌ', 'خالدًا'], 'خالدٌ')]), ('صادق…', [(['صادقٌ', 'صادقًا'], 'صادقٌ')]), ('Treatment', [(TREAT, 'إلغاء')])]),
    M('8G-3', '“In إلغاء, the verb no longer has a subject.” True or false?', [
        'False: **تُ** remains the فاعل; only government of the object pair is cancelled.',
        'True: إلغاء cancels the verb’s government entirely, including its subject.',
        'True: the verb becomes a parenthetical particle, which cannot have a subject.',
        'False: the subject survives, but it becomes the مبتدأ of the nominal pair.',
        ], 'False: **تُ** remains the فاعل; only government of the object pair is cancelled.'),
    G('8I-1', 'أعرب على وجه الإلغاء: **الكتاب ظننت نافع**.', ['Analysis'], R(
        ['مبتدأ مرفوع بالضمة', 'خبر مرفوع بالضمة', 'جملة فعلية معترضة، لا محل لها', 'مفعول به أوّل منصوب', 'مفعول به ثانٍ منصوب'],
        [('الكتابُ', 'مبتدأ مرفوع بالضمة'), ('نافعٌ', 'خبر مرفوع بالضمة'), ('ظننتُ', 'جملة فعلية معترضة، لا محل لها')]) + [
        ('The same order with **إعمال**', [(['الكِتَابَ ظَنَنْتُ نَافِعًا', 'الكِتَابُ ظَنَنْتُ نَافِعًا', 'الكِتَابَ ظَنَنْتُ نَافِعٌ'], 'الكِتَابَ ظَنَنْتُ نَافِعًا')])]),
    M('8I-2', 'Correct: “Every nominal statement after a cognitive verb is in محل نصب سدّ مسدّ المفعولين, including **الكتابُ نافعٌ ظننتُ** on an إلغاء analysis.”', [
        'On إلغاء, **الكتابُ نافعٌ** has no accusative position: both kinds of government are cancelled.',
        'On إلغاء, **الكتابُ نافعٌ** still keeps محل نصب as the verb’s complement, so the claim is correct as stated.',
        'On إلغاء, the nouns themselves must become accusative, giving **الكتابَ نافعًا ظننتُ**.',
        'On إلغاء, verbal government is cancelled but positional government remains, exactly as in تعليق.',
        ], 'On إلغاء, **الكتابُ نافعٌ** has no accusative position: both kinds of government are cancelled.'),
    G('8I-3', 'Name the treatment and say whether an accusative complement-position remains.', ['Treatment', 'محل نصب remains?'], [
        ('عَلِمْتُ أَحَضَرَ الضَّيْفُ', [(TREAT, 'تعليق'), (['Yes', 'No'], 'Yes')]),
        ('الضَّيْفُ حَاضِرٌ عَلِمْتُ', [(TREAT, 'إلغاء'), (['Yes', 'No'], 'No')])]),
    G('8R', 'Explain **الكتابَ ظننتُ نافعًا**.', ['Answer'], [
        ('**الكتابَ**', [(['مفعول به أوّل مقدّم', 'مبتدأ', 'خبر'], 'مفعول به أوّل مقدّم')]),
        ('**نافعًا**', [(['مفعول به ثانٍ', 'خبر', 'حال'], 'مفعول به ثانٍ')]),
        ('Treatment', [(TREAT, 'إعمال')])]),
    M('8R-b', 'Which تعليق construction means “I knew whether the book was beneficial”?', [
        'عَلِمْتُ هَلِ الكِتَابُ نَافِعٌ', 'عَلِمْتُ هَلِ الكِتَابَ نَافِعًا', 'عَلِمْتُ الكِتَابَ نَافِعًا', 'الكِتَابُ نَافِعٌ عَلِمْتُ'],
        'عَلِمْتُ هَلِ الكِتَابُ نَافِعٌ', sol='8R'),
    M('8-Read', 'Read: **التعليق إبطال العمل لفظًا لا محلًّا، والإلغاء إبطاله لفظًا ومحلًّا.** Which pair illustrates the difference?', [
        '**علمتُ هل الكتابُ نافعٌ** keeps an accusative position; **الكتابُ نافعٌ ظننتُ** keeps none.',
        '**الكتابُ نافعٌ ظننتُ** keeps an accusative position; **علمتُ هل الكتابُ نافعٌ** keeps none.',
        'Both keep an accusative position; they differ only in the endings of the nouns.',
        'Neither keeps an accusative position; they differ only in word order.',
        ], '**علمتُ هل الكتابُ نافعٌ** keeps an accusative position; **الكتابُ نافعٌ ظننتُ** keeps none.'),
]

A1O = ['Cancels object government both verbally and positionally.', 'Expresses a mental judgement.', 'Does not reach a direct object.',
       'Expresses making or rendering something into a state.', 'Retains the complement-position while suspending direct government inside it.',
       'In the two-object pattern studied, its objects do not form an underlying subject–predicate pair.']
PAT = ['two objects: recipient and gift', 'two objects: a judgement', 'two objects: transformation', 'three objects: cognitive causative']
PAIR = ['none', 'الصبرُ نافعٌ', 'الخشبُ بابٌ', 'الأمرُ سهلٌ']
C1O = ['فعل ماضٍ مبني على الفتح المقدّر على الألف', 'ضمير متصل في محل نصب مفعول به أوّل، يعود على الضيف', 'فاعل مرفوع بالضمة الظاهرة',
       'مفعول به ثانٍ منصوب بالفتحة الظاهرة', 'مفعول به أوّل منصوب بالفتحة الظاهرة', 'ضمير مستتر تقديره هو، يعود على الضيف',
       'ضمير متصل في محل نصب مفعول به، يعود على الكتاب', 'متعلق بقرأ، ظرف لغو']
C2O = ['مفعول به أوّل منصوب بالفتحة', 'مفعول به ثانٍ منصوب بالفتحة', 'حرف مصدريّ ونصب', 'اسم أنّ منصوب بالفتحة', 'خبر أنّ مرفوع بالضمة',
       'مصدر مؤوّل في محل نصب، سادّ مسدّ مفعولي علم', 'جملة استفهامية في محل نصب، سادّة مسدّ المفعول به الثاني لسأل',
       'مفعول به منصوب بالفتحة، عامله فتح', 'فاعل فتح مرفوع بالضمة']
E1O = ['فعل ماضٍ مبني على السكون لاتصاله بتاء الفاعل', 'ضمير متصل في محل رفع فاعل', 'مفعول به أوّل منصوب بالفتحة',
       'مفعول به ثانٍ منصوب بالفتحة', 'مفعول به ثالث منصوب بالفتحة', 'حال منصوب بالفتحة']

ITEMS['R'] = [
    G('A1', 'Match each term to its description.', ['Description'], R(A1O, [
        ('إلغاء', A1O[0]), ('فعل قلب', A1O[1]), ('لازم', A1O[2]), ('فعل تحويل', A1O[3]), ('تعليق', A1O[4]), ('فعل جارحة', A1O[5])])),
    G('A2', 'State each verb’s object pattern and recover a subject–predicate pair only if one exists.', ['Object pattern', 'Underlying pair'], [
        ('منحت الطفل قلما (I granted the child a pen)', [(PAT, PAT[0]), (PAIR, 'none')]),
        ('حسبت الصبر نافعا (I supposed patience beneficial)', [(PAT, PAT[1]), (PAIR, 'الصبرُ نافعٌ')]),
        ('جعل النجار الخشب بابا (The carpenter made the wood into a door)', [(PAT, PAT[2]), (PAIR, 'الخشبُ بابٌ')]),
        ('أريت سعيدا الأمر سهلا (I showed Saʿīd that the matter was easy)', [(PAT, PAT[3]), (PAIR, 'الأمرُ سهلٌ')])]),
    G('B1', 'Choose the correctly vowelled sentence.', ['Correct form'], [
        ('علمت أن الضيف صادق', [(['عَلِمْتُ أَنَّ الضَّيْفَ صَادِقٌ', 'عَلِمْتُ أَنَّ الضَّيْفَ صَادِقًا', 'عَلِمْتُ أَنَّ الضَّيْفُ صَادِقٌ'], 'عَلِمْتُ أَنَّ الضَّيْفَ صَادِقٌ')]),
        ('علمت أَحضر الضيف', [(['عَلِمْتُ أَحَضَرَ الضَّيْفُ', 'عَلِمْتُ أَحَضَرَ الضَّيْفَ', 'عَلِمْتُ أَحَضَرَ الضَّيْفِ'], 'عَلِمْتُ أَحَضَرَ الضَّيْفُ')]),
        ('الضيف علمت صادق (preferred treatment, verb between the pair)', [(['الضَّيْفَ عَلِمْتُ صَادِقًا', 'الضَّيْفُ عَلِمْتُ صَادِقٌ', 'الضَّيْفُ عَلِمْتُ صَادِقًا'], 'الضَّيْفَ عَلِمْتُ صَادِقًا')]),
        ('الضيف صادق علمت (preferred treatment, verb after the pair)', [(['الضَّيْفُ صَادِقٌ عَلِمْتُ', 'الضَّيْفَ صَادِقًا عَلِمْتُ', 'الضَّيْفَ صَادِقٌ عَلِمْتُ'], 'الضَّيْفُ صَادِقٌ عَلِمْتُ')])]),
    M('B2-1', 'Correct **جَلَسَ الطَّالِبَ أَمَامَ المُعَلِّمِ**, intended as “The student sat before the teacher.”', [
        'جَلَسَ الطَّالِبُ أَمَامَ المُعَلِّمِ', 'جَلَسَ الطَّالِبِ أَمَامَ المُعَلِّمِ', 'جَلَسَ الطَّالِبُ أَمَامُ المُعَلِّمُ'], 'جَلَسَ الطَّالِبُ أَمَامَ المُعَلِّمِ', sol='B2'),
    M('B2-2', 'Correct: “**الحزنِ** in **ذهب اللهُ بالحزنِ** must be accusative because it has an object relation.”', [
        '**الحزنِ** stays genitive because of **الباء**; the phrase carries the object relation.',
        '**الحزنَ** must be accusative, since **ذهب** has no other object to govern.',
        '**الحزنِ** is genitive as a مضاف إليه of **الله**, so it has no object relation.',
        '**الحزنِ** is the فاعل in meaning, so it is genitive in form and nominative in position.',
        ], '**الحزنِ** stays genitive because of **الباء**; the phrase carries the object relation.', sol='B2'),
    M('B2-3', 'Correct **ظَنَنْتُ أَنَّ الكِتَابَ نَافِعًا**.', [
        'ظَنَنْتُ أَنَّ الكِتَابَ نَافِعٌ', 'ظَنَنْتُ أَنَّ الكِتَابُ نَافِعٌ', 'ظَنَنْتُ أَنَّ الكِتَابُ نَافِعًا'], 'ظَنَنْتُ أَنَّ الكِتَابَ نَافِعٌ', sol='B2'),
    M('B2-4', 'Correct: “**أيَّ** in **علمتُ أيَّ كتابٍ قرأ خالدٌ** receives its fatḥah from **علم**.”', [
        '**أيَّ** is the fronted object of **قرأ**; **علم** governs the whole clause’s position.',
        '**أيَّ** should be **أيُّ**, because **علم** is suspended and the question is nominal.',
        '**أيَّ** is the first object of **علم**; the rest of the clause is its second object.',
        '**أيَّ** is the subject of **قرأ** fronted; its fatḥah comes from **علم**.',
        ], '**أيَّ** is the fronted object of **قرأ**; **علم** governs the whole clause’s position.', sol='B2'),
    M('B2-5', 'Correct: “**خالدًا** in **خالدًا ظننتُ صادقًا** is an accusative مبتدأ.”', [
        '**خالدًا** is a fronted first object governed by **ظننتُ** (إعمال), not a مبتدأ.',
        '**خالدًا** is a حال describing the person thought about, fronted for emphasis.',
        '**خالدًا** should be **خالدٌ**: a fronted noun before a cognitive verb is a مبتدأ.',
        '**خالدًا** is an accusative مبتدأ, because إلغاء makes the مبتدأ accusative.',
        ], '**خالدًا** is a fronted first object governed by **ظننتُ** (إعمال), not a مبتدأ.', sol='B2'),
    G('C1', 'Passage 1: **دَخَلَ الضَّيْفُ. أَعْطَاهُ خَالِدٌ كِتَابًا. حَسِبَ الضَّيْفُ الكِتَابَ نَافِعًا. قَرَأَهُ فِي البَيْتِ.** Choose the analysis of each part.', ['Analysis'], R(C1O, [
        ('أعطى', 'فعل ماضٍ مبني على الفتح المقدّر على الألف'), ('هُ in أعطاه', 'ضمير متصل في محل نصب مفعول به أوّل، يعود على الضيف'),
        ('خالدٌ', 'فاعل مرفوع بالضمة الظاهرة'), ('كتابًا', 'مفعول به ثانٍ منصوب بالفتحة الظاهرة'),
        ('الكتابَ in حسب الضيف الكتاب نافعا', 'مفعول به أوّل منصوب بالفتحة الظاهرة'), ('نافعًا', 'مفعول به ثانٍ منصوب بالفتحة الظاهرة'),
        ('فاعل قرأ', 'ضمير مستتر تقديره هو، يعود على الضيف'), ('هُ in قرأه', 'ضمير متصل في محل نصب مفعول به، يعود على الكتاب'),
        ('في البيت', 'متعلق بقرأ، ظرف لغو')])),
    M('C1-b', 'Why does the two-object relationship change between the second and third sentences?', [
        'In **أعطاه** the objects are recipient and gift; in **حسب** they keep the statement **الكتابُ نافعٌ**.',
        'In **أعطاه** the objects keep a statement; in **حسب** they are recipient and gift.',
        'In both sentences the objects keep an underlying statement about the first object.',
        'In **أعطاه** there is one object; in **حسب** there are two, so the relationship changes.',
        ], 'In **أعطاه** the objects are recipient and gift; in **حسب** they keep the statement **الكتابُ نافعٌ**.', sol='C1'),
    G('C2', 'Passage 2: **ظَنَنْتُ البَابَ مَفْتُوحًا. عَلِمْتُ أَنَّ البَابَ مُغْلَقٌ. سَأَلْتُ خَالِدًا أَفَتَحَ سَعِيدٌ البَابَ.** Choose the analysis of each part.', ['Analysis'], R(C2O, [
        ('البابَ in ظننت الباب مفتوحا', 'مفعول به أوّل منصوب بالفتحة'), ('مفتوحًا', 'مفعول به ثانٍ منصوب بالفتحة'), ('أنّ', 'حرف مصدريّ ونصب'),
        ('البابَ in علمت أن الباب مغلق', 'اسم أنّ منصوب بالفتحة'), ('مغلقٌ', 'خبر أنّ مرفوع بالضمة'), ('أنّ الباب مغلق', 'مصدر مؤوّل في محل نصب، سادّ مسدّ مفعولي علم'),
        ('خالدًا', 'مفعول به أوّل منصوب بالفتحة'), ('سعيدٌ', 'فاعل فتح مرفوع بالضمة'), ('البابَ (final)', 'مفعول به منصوب بالفتحة، عامله فتح'),
        ('أفتح سعيد الباب', 'جملة استفهامية في محل نصب، سادّة مسدّ المفعول به الثاني لسأل')])),
    G('D1', 'Match each statement to the example that illustrates it.', ['Example'], R(
        ['**جلسَ الطالبُ متأدبًا**: **متأدبًا** is حال', '**ظننتُ** answering **أظننتَ خالدًا صادقًا؟**', '**علمتُ أَحضر خالدٌ**', '**خالدٌ صادقٌ ظننتُ**'],
        [('ليس كل منصوب بعد الفعل مفعولًا به.', '**جلسَ الطالبُ متأدبًا**: **متأدبًا** is حال'),
         ('قد يحذف المفعولان اختصارًا إذا دلّ عليهما دليل.', '**ظننتُ** answering **أظننتَ خالدًا صادقًا؟**'),
         ('الجملة المعلّق عنها العمل اللفظيّ لها محلّ من الإعراب.', '**علمتُ أَحضر خالدٌ**'),
         ('يترجّح الإلغاء إذا تأخّر فعل القلب عن معموليه.', '**خالدٌ صادقٌ ظننتُ**')])),
    G('D2', 'Identify the sentence described and complete the analysis: **التاء في محل رفع فاعل. أنّ حرف مصدريّ ونصب. العلم اسم أنّ منصوب، ونافع خبرها مرفوع. والمصدر المؤوّل …**', ['Answer'], [
        ('Sentence described', [(['علمت أن العلم نافع', 'علمت العلم نافعا', 'العلم نافع علمت'], 'علمت أن العلم نافع')]),
        ('…والمصدر المؤوّل', [(['في محل نصب، سادّ مسدّ مفعولي علم', 'في محل رفع خبر', 'لا محل له من الإعراب'], 'في محل نصب، سادّ مسدّ مفعولي علم')])]),
    G('E1', '**أَرَيْتُ المُسَافِرَ الطَّرِيقَ آمِنًا.** “I showed the traveller that the route was safe.” Choose the analysis of each part.', ['Analysis'], R(E1O, [
        ('أريْـ', 'فعل ماضٍ مبني على السكون لاتصاله بتاء الفاعل'), ('ـتُ', 'ضمير متصل في محل رفع فاعل'), ('المسافرَ', 'مفعول به أوّل منصوب بالفتحة'),
        ('الطريقَ', 'مفعول به ثانٍ منصوب بالفتحة'), ('آمنًا', 'مفعول به ثالث منصوب بالفتحة')])),
    M('E1-b', 'Which pair forms the underlying assertion, and is **آمنًا** a حال?', [
        '**الطريقُ آمنٌ**; **آمنًا** is the third object',
        '**المسافرُ آمنٌ**; **آمنًا** is a حال',
        '**الطريقُ آمنٌ**; **آمنًا** is a حال',
        '**المسافرُ الطريقُ**; **آمنًا** is the third object',
        ], '**الطريقُ آمنٌ**; **آمنًا** is the third object', sol='E1'),
    G('E2', 'Express each meaning in Arabic.', ['Arabic'], [
        ('I knew that the route was safe (use **أنّ**)', [(['عَلِمْتُ أَنَّ الطَّرِيقَ آمِنٌ', 'عَلِمْتُ أَنَّ الطَّرِيقَ آمِنًا', 'عَلِمْتُ أَنَّ الطَّرِيقُ آمِنٌ'], 'عَلِمْتُ أَنَّ الطَّرِيقَ آمِنٌ')]),
        ('I knew whether the route was safe (use **هل**)', [(['عَلِمْتُ هَلِ الطَّرِيقُ آمِنٌ', 'عَلِمْتُ هَلِ الطَّرِيقَ آمِنًا', 'عَلِمْتُ هَلْ الطَّرِيقَ آمِنٌ'], 'عَلِمْتُ هَلِ الطَّرِيقُ آمِنٌ')]),
        ('The route is safe, I thought (**ظننتُ** last, إلغاء)', [(['الطَّرِيقُ آمِنٌ ظَنَنْتُ', 'الطَّرِيقَ آمِنًا ظَنَنْتُ', 'الطَّرِيقَ آمِنٌ ظَنَنْتُ'], 'الطَّرِيقُ آمِنٌ ظَنَنْتُ')])]),
]
