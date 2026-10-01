# Interactive practice items. Every item has exactly one correct answer per control.
# M = single choice; G = grid of choices (one choice per cell). Answers are given as the option text.

def M(id, prompt, opts, ans, sol=None):
    assert ans in opts, (id, ans)
    return dict(type='mcq', id=id, prompt=prompt, opts=opts, ans=ans, sol=sol)


def G(id, prompt, cols, rows, sol=None):
    for lab, cells in rows:
        assert len(cells) == len(cols), (id, lab)
        for c in cells:
            if c is not None:
                assert c[1] in c[0], (id, lab, c[1])
    return dict(type='grid', id=id, prompt=prompt, cols=cols, rows=rows, sol=sol)


CLS = ['اسم', 'فعل', 'حرف']
CASE = ['مرفوع', 'منصوب', 'مجرور']
SIGN = ['ضمة', 'فتحة', 'كسرة']
END = ['ـُ', 'ـَ', 'ـِ', 'ـٌ', 'ـً', 'ـٍ', 'ـْ']
ENDA = ['ـُ', 'ـَ', 'ـِ', 'ـٌ', 'ـًا', 'ـٍ', 'ـْ']
STRUCT = ['اسمية غير منسوخة', 'اسمية منسوخة', 'فعلية']
IRAB = ['لفظي', 'تقديري', 'محلي']

ITEMS = {}

ITEMS['1'] = [
    G('1G-1', 'Match each term with its meaning.', ['Meaning'], [
        (t, [(['uttered sound', 'meaningful utterance', 'single meaningful unit', 'expression with meaningful components'], a)])
        for t, a in [('لفظ', 'uttered sound'), ('قول', 'meaningful utterance'), ('مفرد', 'single meaningful unit'), ('مركب', 'expression with meaningful components')]]),
    G('1G-2', 'In **بَابُ البَيْتِ**, “the house’s door,” identify the class and the role of each word.', ['Class', 'Role'], [
        ('بَابُ', [(CLS, 'اسم'), (['مضاف', 'مضاف إليه'], 'مضاف')]),
        ('البَيْتِ', [(CLS, 'اسم'), (['مضاف', 'مضاف إليه'], 'مضاف إليه')])]),
    M('1G-3', 'Which sign identifies **قَلَمٌ**, “a pen,” as a اسم?', ['tense', 'تنوين', 'a request'], 'تنوين'),
    G('1I-1', 'Give the علامة that identifies each highlighted word as a اسم.', ['علامة'], [
        ('**المَسْجِدِ** in فِي المَسْجِدِ', [(['جرّ', 'نداء', 'إسناد إليه', 'إضافة'], 'جرّ')]),
        ('**سَعِيدُ** in يَا سَعِيدُ', [(['جرّ', 'نداء', 'إسناد إليه', 'إضافة'], 'نداء')]),
        ('**المَاءُ** in المَاءُ بَارِدٌ', [(['جرّ', 'نداء', 'إسناد إليه', 'إضافة'], 'إسناد إليه')])]),
    G('1I-2', 'Classify each word.', ['Division'], [
        ('حَجَرٌ (a stone)', [(['اسم عين', 'اسم معنى', 'صفة'], 'اسم عين')]),
        ('صَبْرٌ (patience)', [(['اسم عين', 'اسم معنى', 'صفة'], 'اسم معنى')]),
        ('صَابِرٌ (patient)', [(['اسم عين', 'اسم معنى', 'صفة'], 'صفة')])]),
    M('1I-3', 'In **أَنْ تَصْبِرَ خَيْرٌ**, “Your being patient is better,” which part is the **اسم مؤول**?', ['أَنْ', 'تَصْبِرَ', 'أَنْ تَصْبِرَ', 'خَيْرٌ'], 'أَنْ تَصْبِرَ'),
    M('1I-4', 'Why is this claim wrong: “Every اسم takes **أل**, so **هو** cannot be a اسم”?', [
        'A اسم does not have to accept every علامة. **هو** is a ضمير and can be what a statement is made about, as in **هو صالحٌ**.',
        '**هو** does take **أل** in some sentences.',
        '**هو** is a حرف, so the rule does not apply to it.',
        '**هو** is a فعل ماضٍ.'],
        'A اسم does not have to accept every علامة. **هو** is a ضمير and can be what a statement is made about, as in **هو صالحٌ**.'),
    M('1R', 'Which statement about **عِلْمٌ** and **عَالِمٌ** is correct?', [
        'Both are اسم. **علم** is اسم معنى and **عالم** is صفة: word class and the meaning-division answer different questions.',
        '**علم** is a اسم and **عالم** is a فعل.',
        'Both are صفة.',
        '**علم** is اسم عين and **عالم** is اسم معنى.'],
        'Both are اسم. **علم** is اسم معنى and **عالم** is صفة: word class and the meaning-division answer different questions.'),
]

ITEMS['2'] = [
    G('2G-1', 'Label the forms.', ['Term'], [
        (f, [(['فعل ماضٍ', 'فعل مضارع', 'فعل أمر', 'نهي'], a)]) for f, a in [
            ('جَلَسَ (sat)', 'فعل ماضٍ'), ('يَجْلِسُ (sits)', 'فعل مضارع'), ('اِجْلِسْ (sit!)', 'فعل أمر'), ('لَا تَجْلِسْ (do not sit!)', 'نهي')]]),
    G('2G-2', 'Match each حرف with its use.', ['Use'], [
        (p, [(['may precede either ماضٍ or مضارع', 'negates the future', 'marks future time', 'negates an action in the past using a مضارع'], a)]) for p, a in [
            ('لم', 'negates an action in the past using a مضارع'), ('لن', 'negates the future'), ('سوف', 'marks future time'), ('قد', 'may precede either ماضٍ or مضارع')]]),
    G('2G-3', 'Which use of **حرف** is meant in each statement?', ['Use'], [
        ('“**م** is a حرف”', [(['حروف المباني', 'حروف المعاني'], 'حروف المباني')]),
        ('“**هَلْ** is a حرف”', [(['حروف المباني', 'حروف المعاني'], 'حروف المعاني')])]),
    G('2I-1', 'Classify the words in **سَوْفَ يَخْرُجُ سَعِيدٌ**, “Saʿīd will go out,” and choose the evidence.', ['Class', 'Evidence'], [
        ('سَوْفَ', [(['اسم', 'فعل مضارع', 'حرف'], 'حرف'), None]),
        ('يَخْرُجُ', [(['اسم', 'فعل مضارع', 'حرف'], 'فعل مضارع'),
                     (['it accepts **سوف** and has a حرف مضارعة', 'it ends in ضمة', 'it names an event'], 'it accepts **سوف** and has a حرف مضارعة')]),
        ('سَعِيدٌ', [(['اسم', 'فعل مضارع', 'حرف'], 'اسم'),
                    (['it has تنوين and the going-out is attributed to it', 'it comes last in the جملة', 'it begins with **س**'], 'it has تنوين and the going-out is attributed to it')])]),
    M('2I-2', 'Choose the sound explanation of **لَمْ يَفْتَحْ**.', [
        '(a) a فعل ماضٍ because it means “did not open”', '(b) a مضارع whose past meaning comes from **لم**'], '(b) a مضارع whose past meaning comes from **لم**'),
    M('2I-3', 'Which is a اسم, and why: **نَكْتُبُ** (we write) or **نَهْرٌ** (a river)?', [
        '**نهرٌ**, shown by تنوين', '**نكتبُ**, because it begins with **ن**', '**نهرٌ**, because it begins with **ن**', '**نكتبُ**, because it ends in ضمة'], '**نهرٌ**, shown by تنوين'),
    G('2I-4', 'Identify the حرف مدّ or حرف لين in each word.', ['Letter', 'Type'], [
        ('نُورٌ (light)', [(['ن', 'و', 'ر'], 'و'), (['حرف مدّ', 'حرف لين'], 'حرف مدّ')]),
        ('بَيْتٌ (house)', [(['ب', 'ي', 'ت'], 'ي'), (['حرف مدّ', 'حرف لين'], 'حرف لين')])]),
    G('2R', 'Classify **عِلْمٌ، عَلِمَ، فِي**.', ['Class'], [
        ('عِلْمٌ', [(['اسم', 'فعل ماضٍ', 'حرف'], 'اسم')]), ('عَلِمَ', [(['اسم', 'فعل ماضٍ', 'حرف'], 'فعل ماضٍ')]), ('فِي', [(['اسم', 'فعل ماضٍ', 'حرف'], 'حرف')])]),
    M('2R-b', 'Why is “it has a meaning” not enough to distinguish the three classes?', [
        'All three convey meaning, so meaningfulness alone cannot distinguish them.', 'Only a اسم has meaning.', 'A حرف has no meaning at all.', 'A فعل has no meaning without a ضمير.'],
        'All three convey meaning, so meaningfulness alone cannot distinguish them.', sol='2R'),
    M('2-Read', 'Read: **الفِعْلُ يَدُلُّ عَلَى مَعْنًى مُقْتَرِنٍ بِزَمَانٍ.** (**مقترن بـ** = connected with). Why does this not make **غدًا** a فعل?', [
        '**غدًا** names a time directly; it does not carry tense through a verbal pattern.', '**غدًا** has تنوين, so it is a حرف.', '**غدًا** refers to the past.', '**غدًا** cannot take **أل**.'],
        '**غدًا** names a time directly; it does not carry tense through a verbal pattern.', sol='2R'),
]

ITEMS['3'] = [
    G('3G-1', 'For **البَيْتُ وَاسِعٌ**, “The house is spacious,” give each word’s role.', ['Role', 'Pillar'], [
        ('البيت', [(['مبتدأ', 'خبر', 'فاعل'], 'مبتدأ'), (['مسند إليه', 'مسند'], 'مسند إليه')]),
        ('واسع', [(['مبتدأ', 'خبر', 'فاعل'], 'خبر'), (['مسند إليه', 'مسند'], 'مسند')])]),
    G('3G-2', 'In **فَتَحَ سَعِيدٌ البَابَ**, “Saʿīd opened the door,” identify each role and the noun endings.', ['Role', 'Status', 'Sign'], [
        ('فَتَحَ', [(['فعل ماضٍ', 'فاعل', 'مفعول به'], 'فعل ماضٍ'), None, None]),
        ('سَعِيدٌ', [(['فعل ماضٍ', 'فاعل', 'مفعول به'], 'فاعل'), (CASE, 'مرفوع'), (SIGN, 'ضمة')]),
        ('البَابَ', [(['فعل ماضٍ', 'فاعل', 'مفعول به'], 'مفعول به'), (CASE, 'منصوب'), (SIGN, 'فتحة')])]),
    G('3G-3', 'Supply the understood فاعل.', ['Understood فاعل'], [
        ('نَكْتُبُ (we write)', [(['أنا', 'نحن', 'أنتَ', 'هو'], 'نحن')]),
        ('اِجْلِسْ (sit! to one male)', [(['أنا', 'نحن', 'أنتَ', 'هو'], 'أنتَ')])]),
    G('3I-1', 'Choose the endings and roles. Meaning: the boy carried the pen. **حَمَلَ الوَلَد… القَلَم…**', ['Ending', 'Role'], [
        ('الوَلَد…', [(['ـُ', 'ـَ'], 'ـُ'), (['فاعل', 'مفعول به'], 'فاعل')]),
        ('القَلَم…', [(['ـُ', 'ـَ'], 'ـَ'), (['فاعل', 'مفعول به'], 'مفعول به')])]),
    M('3I-2', 'Correct **الكِتَابُ نَافِعًا** so that it means “The book is beneficial.”', [
        'الكِتَابُ نَافِعٌ', 'الكِتَابَ نَافِعٌ', 'الكِتَابِ نَافِعٍ', 'الكِتَابٌ نَافِعًا'], 'الكِتَابُ نَافِعٌ'),
    G('3I-3', 'Compare the final ت and the فاعل in each.', ['What the final ت is', 'The فاعل'], [
        ('جَلَسْتُ', [(['the فاعل', 'تاء التأنيث'], 'the فاعل'), (['تُ', 'understood هي', 'هِنْدٌ'], 'تُ')]),
        ('جَلَسَتْ', [(['the فاعل', 'تاء التأنيث'], 'تاء التأنيث'), (['تُ', 'understood هي', 'هِنْدٌ'], 'understood هي')]),
        ('جَلَسَتْ هِنْدٌ', [(['the فاعل', 'تاء التأنيث'], 'تاء التأنيث'), (['تُ', 'understood هي', 'هِنْدٌ'], 'هِنْدٌ')])]),
    G('3I-4', 'Analyse **فَتَحْتُ البَابَ**.', ['Role', 'Status'], [
        ('فَتَحْـ', [(['فعل / مسند', 'فاعل / مسند إليه', 'مفعول به / فضلة'], 'فعل / مسند'), None]),
        ('ـتُ', [(['فعل / مسند', 'فاعل / مسند إليه', 'مفعول به / فضلة'], 'فاعل / مسند إليه'), None]),
        ('البَابَ', [(['فعل / مسند', 'فاعل / مسند إليه', 'مفعول به / فضلة'], 'مفعول به / فضلة'), (['منصوب بالفتحة', 'مرفوع بالضمة', 'مجرور بالكسرة'], 'منصوب بالفتحة')])]),
    M('3R', 'Why is **جَالِسٌ** a اسم in **خَالِدٌ جَالِسٌ**, while **جَلَسَ** is a فعل in **جَلَسَ خَالِدٌ**? What stays the same?', [
        '**جالسٌ** is a صفة that accepts تنوين; **جلسَ** is a فعل ماضٍ. Khalid is the مسند إليه in both, but his role changes from مبتدأ to فاعل.',
        'Both are فعل, and Khalid is فاعل in both.',
        '**جالسٌ** is a فعل مضارع, and Khalid is مبتدأ in both.',
        '**جلسَ** is a اسم because it has a meaning, and Khalid is مفعول به.'],
        '**جالسٌ** is a صفة that accepts تنوين; **جلسَ** is a فعل ماضٍ. Khalid is the مسند إليه in both, but his role changes from مبتدأ to فاعل.'),
]

ITEMS['4'] = [
    G('4G-1', 'Classify **إِنَّ العِلْمَ نَافِعٌ** and name the two governed roles.', ['Role / classification', 'Status'], [
        ('The جملة', [(STRUCT, 'اسمية منسوخة'), None]),
        ('العِلْمَ', [(['اسم إنّ', 'خبر إنّ'], 'اسم إنّ'), (CASE, 'منصوب')]),
        ('نَافِعٌ', [(['اسم إنّ', 'خبر إنّ'], 'خبر إنّ'), (CASE, 'مرفوع')])]),
    G('4G-2', 'Supply the endings. Meaning: “The house was spacious.” **كَانَ البَيْتـ… وَاسِعـ…**', ['Ending'], [
        ('البَيْتـ…', [(ENDA, 'ـُ')]), ('وَاسِعـ…', [(ENDA, 'ـًا')])]),
    G('4G-3', 'In **هِنْدٌ تَكْتُبُ**, find the inner جملة and its understood فاعل.', ['Answer'], [
        ('The inner جملة', [(['هِنْدٌ', 'تَكْتُبُ', 'هِنْدٌ تَكْتُبُ'], 'تَكْتُبُ')]),
        ('Its understood فاعل', [(['هو', 'هي', 'أنا'], 'هي')])]),
    G('4I-1', 'Classify each جملة by structure.', ['Structure'], [
        ('البَابَ فَتَحَ سَعِيدٌ', [(STRUCT, 'فعلية')]), ('سَعِيدٌ يَجْلِسُ', [(STRUCT, 'اسمية غير منسوخة')]),
        ('كَانَ القَلَمُ جَدِيدًا (جديد = new)', [(STRUCT, 'اسمية منسوخة')])]),
    M('4I-2', 'Correct the reasoning: “**إنّ خالدًا صادقٌ** begins with a حرف, so it is neither اسمية nor فعلية.”', [
        'Classification follows the underlying مبتدأ–خبر structure, allowing for the ناسخ: it is اسمية منسوخة.',
        'It is فعلية, because **إنّ** acts like a فعل.',
        'It is اسمية غير منسوخة, because **إنّ** is ignored.',
        'The claim is correct: a جملة beginning with a حرف has no classification.'],
        'Classification follows the underlying مبتدأ–خبر structure, allowing for the ناسخ: it is اسمية منسوخة.'),
    G('4I-3', 'Compare **حَضَرَ الضَّيْفُ** and **الضَّيْفُ حَضَرَ**.', ['Role of الضيف', 'فاعل of حضر'], [
        ('حَضَرَ الضَّيْفُ', [(['فاعل', 'مبتدأ', 'خبر'], 'فاعل'), (['الضيف (expressed)', 'understood هو'], 'الضيف (expressed)')]),
        ('الضَّيْفُ حَضَرَ', [(['فاعل', 'مبتدأ', 'خبر'], 'مبتدأ'), (['الضيف (expressed)', 'understood هو'], 'understood هو')])]),
    G('4R', 'Analyse **إِنَّ الكِتَابَ نَافِعٌ**.', ['Class', 'Role', 'Status'], [
        ('إِنَّ', [(CLS, 'حرف'), None, None]),
        ('الكِتَابَ', [(CLS, 'اسم'), (['اسم إنّ', 'خبر إنّ'], 'اسم إنّ'), (CASE, 'منصوب')]),
        ('نَافِعٌ', [(CLS, 'اسم'), (['اسم إنّ', 'خبر إنّ'], 'خبر إنّ'), (CASE, 'مرفوع')]),
        ('The جملة', [None, (STRUCT, 'اسمية منسوخة'), None])]),
]

ITEMS['5'] = [
    G('5G-1', 'Classify **هَلْ فَتَحَ خَالِدٌ البَابَ؟** on three axes.', ['Classification'], [
        ('اسمية / فعلية', [(['اسمية', 'فعلية'], 'فعلية')]), ('خبرية / إنشائية', [(['خبرية', 'إنشائية'], 'إنشائية')]),
        ('موجب / غير موجب', [(['موجب', 'غير موجب'], 'غير موجب')])]),
    M('5G-2', 'Which is كلام?', ['بَابُ البَيْتِ', 'اُكْتُبْ', 'إِنْ تَكْتُبْ…'], 'اُكْتُبْ'),
    M('5G-3', 'Is **مَا كَتَبَ خَالِدٌ** a نهي or a negative خبرية?', ['نهي', 'negative خبرية'], 'negative خبرية'),
    G('5I-1', 'Label the use.', ['Use'], [
        ('يَا سَعِيدُ!', [(['نداء', 'نهي', 'تمنٍّ', 'استفهام'], 'نداء')]), ('لَا تَجْلِسْ!', [(['نداء', 'نهي', 'تمنٍّ', 'استفهام'], 'نهي')]),
        ('لَيْتَ البَابَ مَفْتُوحٌ! (If only the door were open!)', [(['نداء', 'نهي', 'تمنٍّ', 'استفهام'], 'تمنٍّ')])]),
    M('5I-2', 'A speaker says **غَفَرَ اللهُ لَكَ** while praying for someone. Why does the past فعل not make this a report about the past?', [
        'As a prayer it asks for forgiveness rather than asserting that forgiveness occurred: its use is إنشاء.',
        'It does report that forgiveness happened in the past.',
        'A فعل ماضٍ is always إنشائية.',
        'It is خبرية because the فعل is ماضٍ.'],
        'As a prayer it asks for forgiveness rather than asserting that forgiveness occurred: its use is إنشاء.'),
    M('5I-3', 'Which is a counterexample to “Every **إنشائية** جملة is **غير موجب**”?', ['اُكْتُبْ', 'لَا تَكْتُبْ', 'هَلْ حَضَرَ خَالِدٌ؟', 'مَا حَضَرَ خَالِدٌ'], 'اُكْتُبْ'),
    G('5R', 'Classify **خَالِدٌ يَكْتُبُ**.', ['Classification'], [
        ('Outer structure', [(['اسمية', 'فعلية'], 'اسمية')]), ('Inner structure', [(['اسمية', 'فعلية'], 'فعلية')]),
        ('Meaning', [(['خبرية', 'إنشائية'], 'خبرية')]), ('موجب / غير موجب', [(['موجب', 'غير موجب'], 'موجب')]),
        ('Is it كلام?', [(['Yes', 'No'], 'Yes')])]),
    M('5-Read', 'Read: **كُلُّ كَلَامٍ جُمْلَةٌ، وَلَيْسَ كُلُّ جُمْلَةٍ كَلَامًا.** Which example is a جملة but not كلام?', [
        'إِنْ تَصْدُقْ…', 'إِنْ تَصْدُقْ تَنْجَحْ', 'صَدَقْتَ', 'اُكْتُبْ'], 'إِنْ تَصْدُقْ…', sol='5R'),
]

ITEMS['6'] = [
    G('6G-1', 'Divide each شبه جملة into its components.', ['First component', 'Second component'], [
        ('إِلَى المَسْجِدِ (to the mosque)', [(['حرف جرّ', 'ظرف'], 'حرف جرّ'), (['مجرور', 'مضاف إليه'], 'مجرور')]),
        ('تَحْتَ الشَّجَرَةِ (under the tree)', [(['حرف جرّ', 'ظرف'], 'ظرف'), (['مجرور', 'مضاف إليه'], 'مضاف إليه')])]),
    M('6G-1b', 'Which of the two begins with a اسم?', ['إِلَى المَسْجِدِ', 'تَحْتَ الشَّجَرَةِ'], 'تَحْتَ الشَّجَرَةِ', sol='6G-1'),
    G('6G-2', 'In **خَرَجَ سَعِيدٌ مِنَ البَيْتِ**, “Saʿīd went out of the house”:', ['Answer'], [
        ('The عامل of البيتِ', [(['مِنْ', 'خَرَجَ', 'سَعِيدٌ'], 'مِنْ')]),
        ('من البيت attaches to', [(['خَرَجَ', 'سَعِيدٌ', 'an omitted general عامل'], 'خَرَجَ')]),
        ('Type', [(['ظرف لغو', 'ظرف مستقرّ'], 'ظرف لغو')])]),
    G('6G-3', 'Complete.', ['ظرف …'], [
        ('An omitted **specific** action gives', [(['لغو', 'مستقرّ'], 'لغو')]),
        ('Omitted **general existence** gives', [(['لغو', 'مستقرّ'], 'مستقرّ')])]),
    G('6I-1', 'Analyse **الكِتَابُ عِنْدَ الوَلَدِ**.', ['Role', 'Status and sign'], [
        ('الكِتَابُ', [(['مبتدأ', 'ظرف', 'مضاف إليه'], 'مبتدأ'), (['مرفوع بالضمة', 'منصوب بالفتحة', 'مجرور بالكسرة'], 'مرفوع بالضمة')]),
        ('عِنْدَ', [(['مبتدأ', 'ظرف', 'مضاف إليه'], 'ظرف'), (['مرفوع بالضمة', 'منصوب بالفتحة', 'مجرور بالكسرة'], 'منصوب بالفتحة')]),
        ('الوَلَدِ', [(['مبتدأ', 'ظرف', 'مضاف إليه'], 'مضاف إليه'), (['مرفوع بالضمة', 'منصوب بالفتحة', 'مجرور بالكسرة'], 'مجرور بالكسرة')]),
        ('عِنْدَ الوَلَدِ', [(['ظرف لغو', 'ظرف مستقرّ'], 'ظرف مستقرّ'), (['في محل رفع خبر', 'في محل نصب خبر كان', 'لا محل له من الإعراب'], 'في محل رفع خبر')])]),
    G('6I-2', 'Name the type of شبه جملة and its attachment.', ['Type', 'Attaches to'], [
        ('جَلَسَ الضَّيْفُ عِنْدَ البَابِ', [(['لغو', 'مستقرّ'], 'لغو'), (['جلس', 'an omitted general عامل such as كائن'], 'جلس')]),
        ('الضَّيْفُ عِنْدَ البَابِ', [(['لغو', 'مستقرّ'], 'مستقرّ'), (['جلس', 'an omitted general عامل such as كائن'], 'an omitted general عامل such as كائن')])]),
    M('6I-3', 'Correct: “**في** and **عند** must both be حرف because both express location.”', [
        '**في** is a حرف governing a مجرور; **عند** is a ظرف, a اسم which can itself be مضاف. Similar meanings do not establish identical classes.',
        'The claim is correct: both are حرف.', 'Both are اسم.', '**في** is a اسم and **عند** is a حرف.'],
        '**في** is a حرف governing a مجرور; **عند** is a ظرف, a اسم which can itself be مضاف. Similar meanings do not establish identical classes.'),
    G('6I-4', '**إِلَى المَسْجِدِ** answers **أَيْنَ ذَهَبَ سَعِيدٌ؟**, “Where did Saʿīd go?”', ['Answer'], [
        ('Understood action', [(['ذهب', 'كائن'], 'ذهب')]), ('Classification', [(['لغو', 'مستقرّ'], 'لغو')])]),
    M('6R', 'Why is **القَلَمُ فَوْقَ الكِتَابِ** كلام although it has no expressed فعل?', [
        'The pen receives a complete خبر through an understood general عامل; **فوق الكتاب** is a ظرف with its مضاف إليه, not an expressed مبتدأ–خبر pair.',
        'It contains a hidden **كان** that must be pronounced.', '**فوق الكتاب** is itself a جملة اسمية.', 'It is not كلام.'],
        'The pen receives a complete خبر through an understood general عامل; **فوق الكتاب** is a ظرف with its مضاف إليه, not an expressed مبتدأ–خبر pair.'),
]

ITEMS['7'] = [
    G('7G-1', '**رأيت خالدًا عند الباب**, intended as “I saw Khalid while he was by the door.”', ['Answer'], [
        ('صاحب الحال', [(['خالدًا', 'الباب', 'ـتُ'], 'خالدًا')]), ('Role of the شبه جملة', [(['حال', 'نعت', 'خبر', 'صلة'], 'حال')])]),
    G('7G-2', 'In **جاء الذي في المسجد**:', ['Answer'], [
        ('Suitable general فعل', [(['استقرّ', 'كائن', 'مستقرّ'], 'استقرّ')]),
        ('Why not a صفة alone?', [(['a صلة needs جملة structure', 'a صلة must be منصوب', 'الذي cannot take a شبه جملة'], 'a صلة needs جملة structure')])]),
    G('7G-3', 'In **كان القلم في البيت**:', ['Answer'], [
        ('Position of في البيت', [(['في محل نصب خبر كان', 'في محل رفع خبر', 'لا محل له من الإعراب'], 'في محل نصب خبر كان')]),
        ('Case of البيت', [(CASE, 'مجرور')])]),
    G('7I-1', 'Name the role of each bracketed شبه جملة.', ['Role'], [
        ('الكتاب [على الباب]', [(['خبر', 'حال', 'نعت', 'صلة'], 'خبر')]),
        ('رأيت ولدًا [عند الشجرة] (a boy who was by the tree)', [(['خبر', 'حال', 'نعت', 'صلة'], 'نعت')]),
        ('جاء الذي [في السوق]', [(['خبر', 'حال', 'نعت', 'صلة'], 'صلة')])]),
    G('7I-2', 'Give the two principal analyses of **أعند الباب ضيف؟**, “Is there a guest by the door?”', ['Answer'], [
        ('Analysis 1: ضيفٌ is', [(['فاعل of an understood general فعل', 'مبتدأ مؤخّر', 'خبر مقدّم'], 'فاعل of an understood general فعل')]),
        ('Analysis 2: عند الباب is', [(['فاعل of an understood general فعل', 'مبتدأ مؤخّر', 'خبر مقدّم'], 'خبر مقدّم')]),
        ('Analysis 2: ضيفٌ is', [(['فاعل of an understood general فعل', 'مبتدأ مؤخّر', 'خبر مقدّم'], 'مبتدأ مؤخّر')])]),
    G('7I-3', 'In **خالد عنده قلم**:', ['Answer'], [
        ('ـه refers to', [(['خالد', 'قلم'], 'خالد')]), ('The later اسم مرفوع', [(['خالد', 'قلم'], 'قلم')]),
        ('Context for اعتماد', [(['استفهام', 'نفي', 'موصول', 'صاحب خبر'], 'صاحب خبر')])]),
    G('7I-4', 'Which omitted عامل fits?', ['Omitted عامل'], [
        ('**في البيت** after “Where did Khalid sit?”', [(['جلس', 'كائن', 'استقرّ'], 'جلس')]),
        ('**الذي في المسجد**', [(['جلس', 'كائن', 'استقرّ'], 'استقرّ')])]),
    M('7R', 'How can **في البيت** be لغو or مستقرّ, and how can it fill a رفع position although **البيت** is مجرور?', [
        'With an expressed specific عامل (جلس خالد في البيت) it is لغو; with an omitted general عامل (خالد في البيت) it is مستقرّ. **البيتِ** stays مجرور internally while **في البيت** as a unit supplies the رفع position of the خبر.',
        'It is always مستقرّ, and **البيت** becomes مرفوع when the شبه جملة is a خبر.',
        'لغو means the شبه جملة is meaningless and can be removed.',
        'It is لغو whenever its عامل is omitted.'],
        'With an expressed specific عامل (جلس خالد في البيت) it is لغو; with an omitted general عامل (خالد في البيت) it is مستقرّ. **البيتِ** stays مجرور internally while **في البيت** as a unit supplies the رفع position of the خبر.'),
]

ITEMS['8'] = [
    G('8G-1', 'In **في المسجد**:', ['Answer'], [
        ('عامل', [(['في', 'المسجد'], 'في')]), ('معمول', [(['في', 'المسجد'], 'المسجد')]), ('Status', [(['رفع', 'نصب', 'جرّ', 'جزم'], 'جرّ')])]),
    M('8G-2', 'Choose: **لن ___ سعيدٌ**', ['يخرجُ', 'يخرجَ', 'يخرجْ'], 'يخرجَ'),
    G('8G-3', 'In **لم يكتب خالدٌ**, identify the two relationships.', ['Status required'], [
        ('لم → يكتب', [(['رفع', 'نصب', 'جزم'], 'جزم')]), ('يكتب → خالدٌ', [(['رفع', 'نصب', 'جزم'], 'رفع')]),
        ('Is يكتب both عامل and معمول?', [(['Yes', 'No'], 'Yes')])]),
    G('8I-1', 'Add the ending required by each meaning.', ['Ending'], [
        ('لا تجلسـ… = “Do not sit”', [(['ـُ', 'ـَ', 'ـْ'], 'ـْ')]), ('لا تجلسـ… = “You do not sit”', [(['ـُ', 'ـَ', 'ـْ'], 'ـُ')])]),
    M('8I-2', 'Correct the analysis: “**لن** is **منصوب** because it causes **نصب**.”', [
        '**لن** causes نصب but does not receive it: it is a حرف with لا محل له من الإعراب; the فعل after it is منصوب.',
        '**لن** is مجزوم, not منصوب.', 'The analysis is correct.', '**لن** is a فعل, so it is مرفوع.'],
        '**لن** causes نصب but does not receive it: it is a حرف with لا محل له من الإعراب; the فعل after it is منصوب.'),
    G('8I-3', 'In **ما خرج سعيدٌ من البيت**:', ['Answer'], [
        ('غير عامل', [(['ما', 'من'], 'ما')]), ('Governing حرف', [(['ما', 'من'], 'من')]),
        ('من البيت attaches to', [(['خرج', 'سعيد'], 'خرج')]), ('Role of سعيد', [(['فاعل', 'مبتدأ', 'مفعول به'], 'فاعل')])]),
    M('8I-4', 'Which translation and illustration of **غير العامل ليس هو غير المعمول** is right?', [
        '“A غير عامل is not the same as an ungoverned element.” **لن** governs without being governed; **خالدٌ** in **جلس خالدٌ** is governed without governing.',
        '“Every عامل is also معمول.” **لن** is منصوب.',
        '“A غير عامل is always غير معمول.” **ما** in **ما حضر خالد**.',
        '“A حرف is always معمول.” **في** in **في البيت**.'],
        '“A غير عامل is not the same as an ungoverned element.” **لن** governs without being governed; **خالدٌ** in **جلس خالدٌ** is governed without governing.'),
    G('8R', 'Internal and external government in **خالدٌ في البيت**.', ['Answer'], [
        ('في → البيت', [(['رفع', 'نصب', 'جرّ'], 'جرّ')]),
        ('في البيت attaches to', [(['خالد', 'an omitted general عامل'], 'an omitted general عامل')]),
        ('Role of خالد', [(['مبتدأ', 'فاعل', 'خبر'], 'مبتدأ')]),
        ('The خبر is supplied by', [(['في البيت as a unit', 'البيت alone'], 'في البيت as a unit')])]),
    M('8-Read', 'Read: **العامل يوجب حالة، والمعمول يقبلها.** Which is right for **لن يفتح**?', [
        '**لن** requires نصب and **يفتحَ** receives it.', '**يفتح** requires نصب and **لن** receives it.', 'Both are معمول.', 'Neither is عامل.'],
        '**لن** requires نصب and **يفتحَ** receives it.', sol='8R'),
]

ITEMS['9'] = [
    G('9G-1', 'Choose the kind of إعراب.', ['إعراب'], [
        ('**خالدٌ** as فاعل', [(IRAB, 'لفظي')]), ('**الفتى** as فاعل', [(IRAB, 'تقديري')]),
        ('**هو** as مبتدأ', [(IRAB, 'محلي')]), ('**[يكتب]** as the خبر of خالد', [(IRAB, 'محلي')])]),
    G('9G-2', 'Complete: **الهدى اسم مجرور بكسرة ___، منع من ظهورها ___**', ['Word'], [
        ('First blank', [(['مقدّرة', 'ظاهرة'], 'مقدّرة')]), ('Second blank', [(['التعذّر', 'البناء'], 'التعذّر')])]),
    M('9G-3', 'Does the سكون before **نون النسوة** in **يكتبْنَ** prove جزم?', [
        'No. The فعل is مبني على السكون because of نون النسوة; in **لن يكتبن** it stays fixed but occupies نصب.',
        'Yes. A سكون always shows جزم.', 'Yes. نون النسوة is a جازم.', 'No. The سكون shows نصب.'],
        'No. The فعل is مبني على السكون because of نون النسوة; in **لن يكتبن** it stays fixed but occupies نصب.'),
    G('9I-1', 'أعرب: **هو يجلس**.', ['Analysis', 'إعراب'], [
        ('هو', [(['مبتدأ', 'فاعل'], 'مبتدأ'), (IRAB, 'محلي')]),
        ('يجلسُ', [(['فعل مضارع مرفوع', 'فعل مضارع مجزوم'], 'فعل مضارع مرفوع'), (IRAB, 'لفظي')]),
        ('The فاعل of يجلس', [(['ضمير مستتر تقديره هو', 'the outer هو'], 'ضمير مستتر تقديره هو'), (IRAB, 'محلي')]),
        ('جملة يجلس', [(['في محل رفع خبر', 'لا محل لها من الإعراب'], 'في محل رفع خبر'), (IRAB, 'محلي')])]),
    G('9I-2', 'أعرب: **يسعى الفتى إلى المسجد**.', ['Role', 'Sign'], [
        ('يسعى', [(['فعل مضارع مرفوع', 'فاعل مرفوع', 'حرف جرّ', 'اسم مجرور'], 'فعل مضارع مرفوع'), (['ظاهرة', 'مقدّرة', 'لا محل له'], 'مقدّرة')]),
        ('الفتى', [(['فعل مضارع مرفوع', 'فاعل مرفوع', 'حرف جرّ', 'اسم مجرور'], 'فاعل مرفوع'), (['ظاهرة', 'مقدّرة', 'لا محل له'], 'مقدّرة')]),
        ('إلى', [(['فعل مضارع مرفوع', 'فاعل مرفوع', 'حرف جرّ', 'اسم مجرور'], 'حرف جرّ'), (['ظاهرة', 'مقدّرة', 'لا محل له'], 'لا محل له')]),
        ('المسجدِ', [(['فعل مضارع مرفوع', 'فاعل مرفوع', 'حرف جرّ', 'اسم مجرور'], 'اسم مجرور'), (['ظاهرة', 'مقدّرة', 'لا محل له'], 'ظاهرة')])]),
    M('9I-3', 'صحّح: “**جلسَ** is منصوب because it ends in فتحة.”', [
        '**جلسَ** is a فعل ماضٍ مبني على الفتح; its فتحة marks بناء, not نصب.', 'The claim is correct.', '**جلسَ** is مجزوم.', '**جلسَ** is مرفوع.'],
        '**جلسَ** is a فعل ماضٍ مبني على الفتح; its فتحة marks بناء, not نصب.'),
    G('9I-4', 'Match each description to its kind of إعراب.', ['إعراب'], [
        ('A مرفوع اسم with no printed vowel mark (خالد)', [(IRAB, 'لفظي')]),
        ('A مرفوع اسم ending in alif (الفتى)', [(IRAB, 'تقديري')]),
        ('A ضمير in a رفع position (هو)', [(IRAB, 'محلي')])]),
    G('9R', 'Analyse **لن يكتبن الدرس**.', ['Analysis'], [
        (w, [(['حرف نفي ونصب واستقبال، لا محل له من الإعراب', 'فعل مضارع مبني على السكون في محل نصب', 'ضمير متصل مبني على الفتح في محل رفع فاعل', 'مفعول به منصوب بالفتحة الظاهرة'], a)])
        for w, a in [('لن', 'حرف نفي ونصب واستقبال، لا محل له من الإعراب'), ('يكتبْـ', 'فعل مضارع مبني على السكون في محل نصب'),
                     ('ـنَ (نون النسوة)', 'ضمير متصل مبني على الفتح في محل رفع فاعل'), ('الدرسَ', 'مفعول به منصوب بالفتحة الظاهرة')]]),
]

A1M = ['the recipient of government', 'what is predicated', 'a شبه جملة with an omitted general عامل', 'what something is predicated about',
       'a اسم-equivalent made from a حرف and clause', 'what imposes a grammatical status']
A2O = ['علمٌ، صالحٌ، هو', 'الدرسَ كتبَ خالدٌ', 'جلسَ', 'رأيت خالدًا في السوق (Khalid situated in the market)', 'خالدٌ في البيتِ', 'لن']
C1O = ['مبتدأ مرفوع بالضمة الظاهرة', 'حرف جرّ مبني على السكون لا محل له من الإعراب', 'اسم مجرور بفي بالكسرة الظاهرة',
       'متعلق بمحذوف عام تقديره كائنٌ، في محل رفع خبر', 'فعل مضارع مرفوع بالضمة الظاهرة', 'ضمير مستتر تقديره هو في محل رفع فاعل',
       'مفعول به منصوب بالفتحة الظاهرة', 'حرف نفي وجزم وقلب، لا محل له من الإعراب', 'فعل مضارع مجزوم بلم، وعلامة جزمه السكون']
C2O = ['فعل ماضٍ ناقص ناسخ، مبني على الفتح', 'اسم كان مرفوع بالضمة الظاهرة', 'ظرف منصوب بالفتحة وهو مضاف', 'مضاف إليه مجرور بالكسرة الظاهرة',
       'ظرف مستقرّ في محل نصب خبر كان', 'ضمير منفصل مبني على الفتح في محل رفع مبتدأ', 'فعل مضارع مرفوع بالضمة الظاهرة',
       'ضمير مستتر تقديره هو في محل رفع فاعل', 'في محل رفع خبر']
E1O = ['فعل ماضٍ مبني على الفتح لا محل له من الإعراب', 'تاء التأنيث الساكنة، حرف لا محل له من الإعراب', 'فاعل مرفوع بالضمة الظاهرة',
       'مفعول به منصوب بالفتحة الظاهرة', 'حرف جرّ مبني على السكون لا محل له من الإعراب', 'اسم مجرور بفي بالكسرة الظاهرة', 'متعلق بحفظ، ظرف لغو']

ITEMS['R'] = [
    G('A1', 'Match each term to its meaning.', ['Meaning'], [
        (t, [(A1M, a)]) for t, a in [('مسند', 'what is predicated'), ('مسند إليه', 'what something is predicated about'), ('عامل', 'what imposes a grammatical status'),
                                     ('معمول', 'the recipient of government'), ('مصدر مؤول', 'a اسم-equivalent made from a حرف and clause'),
                                     ('ظرف مستقرّ', 'a شبه جملة with an omitted general عامل')]]),
    G('A2', 'Each claim fails. Choose the example that shows why.', ['Counterexample'], [
        (c, [(A2O, a)]) for c, a in [('Every اسم names a physical object.', 'علمٌ، صالحٌ، هو'),
                                     ('Every جملة beginning with a written اسم is اسمية.', 'الدرسَ كتبَ خالدٌ'),
                                     ('Every فتحة is a sign of نصب.', 'جلسَ'),
                                     ('A شبه جملة is always governed by the nearest فعل.', 'رأيت خالدًا في السوق (Khalid situated in the market)'),
                                     ('A جملة without an expressed فعل is incomplete.', 'خالدٌ في البيتِ'),
                                     ('غير عامل and غير معمول mean the same thing.', 'لن')]]),
    G('B1', 'Supply the endings.', ['Ending'], [
        ('إنّ العلمـ… (Indeed, knowledge…)', [(ENDA, 'ـَ')]), ('…نافعـ… (…is beneficial)', [(ENDA, 'ـٌ')]),
        ('كان الضيفـ… (The guest was…)', [(ENDA, 'ـُ')]), ('…في البيتـ… (…in the house)', [(ENDA, 'ـِ')]),
        ('لم يفتحـ… (did not open)', [(ENDA, 'ـْ')]), ('سعيدـ… (Saʿīd)', [(ENDA, 'ـٌ')]), ('البابـ… (the door)', [(ENDA, 'ـَ')])]),
    M('B2-1', 'Correct **فَتَحَ الوَلَدَ البَابُ**, intended as “The boy opened the door.”', ['فَتَحَ الوَلَدُ البَابَ', 'فَتَحَ الوَلَدِ البَابَ', 'فَتَحَ الوَلَدَ البَابَ'], 'فَتَحَ الوَلَدُ البَابَ', sol='B2'),
    M('B2-2', 'Correct **لَنْ يَجْلِسْ خَالِدٌ**.', ['لَنْ يَجْلِسَ خَالِدٌ', 'لَنْ يَجْلِسُ خَالِدٌ', 'لَنْ يَجْلِسْ خَالِدًا'], 'لَنْ يَجْلِسَ خَالِدٌ', sol='B2'),
    M('B2-3', 'Correct **كِتَابٌ الوَلَدِ**, intended as “the boy’s book.”', ['كِتَابُ الوَلَدِ', 'كِتَابٌ الوَلَدُ', 'الكِتَابُ الوَلَدِ'], 'كِتَابُ الوَلَدِ', sol='B2'),
    G('B3', 'Complete each with one suitable word.', ['Word'], [
        ('القَلَمُ ___ الكِتَابِ (The pen is above the book.)', [(['فَوْقَ', 'لَا', 'صَادِقٌ'], 'فَوْقَ')]),
        ('___ تَكْذِبْ (Do not lie.)', [(['فَوْقَ', 'لَا', 'صَادِقٌ'], 'لَا')]),
        ('خَالِدٌ ___ (Khalid is truthful.)', [(['فَوْقَ', 'لَا', 'صَادِقٌ'], 'صَادِقٌ')])]),
    G('C1', 'Passage 1: **سَعِيدٌ فِي المَسْجِدِ. يَقْرَأُ الكِتَابَ. لَمْ يَخْرُجْ.** Choose the analysis of each part.', ['Analysis'], [
        (w, [(C1O, a)]) for w, a in [('سعيدٌ', 'مبتدأ مرفوع بالضمة الظاهرة'), ('في', 'حرف جرّ مبني على السكون لا محل له من الإعراب'),
                                     ('المسجدِ', 'اسم مجرور بفي بالكسرة الظاهرة'), ('في المسجد', 'متعلق بمحذوف عام تقديره كائنٌ، في محل رفع خبر'),
                                     ('يقرأُ', 'فعل مضارع مرفوع بالضمة الظاهرة'), ('The فاعل of يقرأ', 'ضمير مستتر تقديره هو في محل رفع فاعل'),
                                     ('الكتابَ', 'مفعول به منصوب بالفتحة الظاهرة'), ('لم', 'حرف نفي وجزم وقلب، لا محل له من الإعراب'),
                                     ('يخرجْ', 'فعل مضارع مجزوم بلم، وعلامة جزمه السكون')]]),
    G('C1-b', 'Passage 1: classify each sentence.', ['Structure', 'موجب / غير موجب'], [
        ('سعيدٌ في المسجدِ', [(STRUCT, 'اسمية غير منسوخة'), (['موجب', 'غير موجب'], 'موجب')]),
        ('يقرأُ الكتابَ', [(STRUCT, 'فعلية'), (['موجب', 'غير موجب'], 'موجب')]),
        ('لم يخرجْ', [(STRUCT, 'فعلية'), (['موجب', 'غير موجب'], 'غير موجب')])], sol='C1'),
    G('C2', 'Passage 2: **كَانَ الضَّيْفُ عِنْدَ البَابِ. … هُوَ يَجْلِسُ.** Choose the analysis of each part of the first and last sentences.', ['Analysis'], [
        (w, [(C2O, a)]) for w, a in [('كانَ', 'فعل ماضٍ ناقص ناسخ، مبني على الفتح'), ('الضيفُ', 'اسم كان مرفوع بالضمة الظاهرة'),
                                     ('عندَ', 'ظرف منصوب بالفتحة وهو مضاف'), ('البابِ', 'مضاف إليه مجرور بالكسرة الظاهرة'),
                                     ('عند الباب', 'ظرف مستقرّ في محل نصب خبر كان'), ('هو', 'ضمير منفصل مبني على الفتح في محل رفع مبتدأ'),
                                     ('يجلسُ', 'فعل مضارع مرفوع بالضمة الظاهرة'), ('The فاعل of يجلس', 'ضمير مستتر تقديره هو في محل رفع فاعل'),
                                     ('جملة يجلس', 'في محل رفع خبر')]]),
    G('C2-b', 'Passage 2: the middle sentences.', ['فاعل', 'مفعول به'], [
        ('فَتَحَ خَالِدٌ البَابَ', [(['خالدٌ', 'البابَ'], 'خالدٌ'), (['خالدٌ', 'البابَ', 'none'], 'البابَ')]),
        ('دَخَلَ الضَّيْفُ', [(['الضيفُ', 'none'], 'الضيفُ'), (['الضيفُ', 'none'], 'none')])], sol='C2'),
    M('C2-c', 'Why does **هُوَ يَجْلِسُ** have both an outer مبتدأ and an inner فاعل?', [
        'One establishes the outer topic and the other is the فاعل required by the inner فعل; their shared reference links the two structures.',
        'The جملة repeats هو for emphasis only.', 'هو is the فاعل of يجلس placed before it.', 'The inner فعل has no فاعل; هو fills both roles.'],
        'One establishes the outer topic and the other is the فاعل required by the inner فعل; their shared reference links the two structures.', sol='C2'),
    M('D1', 'Which sentence does this analysis describe? **خالد مبتدأ مرفوع بالضمة. يكتب فعل مضارع مرفوع بالضمة، والفاعل ضمير مستتر تقديره هو. والجملة الفعلية في محل رفع خبر.**', [
        'خَالِدٌ يَكْتُبُ', 'يَكْتُبُ خَالِدٌ', 'هُوَ يَكْتُبُ', 'خَالِدٌ كَتَبَ'], 'خَالِدٌ يَكْتُبُ'),
    M('D2-1', '**قد يكون العامل مذكورًا أو محذوفًا.** Which pair illustrates it?', [
        '**جلس خالد في البيت** (expressed **جلس**) and **خالد في البيت** (omitted general عامل such as **كائن**)',
        '**لن يكتبَ** and **لم يكتبْ**', '**هو جالسٌ** and **هو يكتبُ**'],
        '**جلس خالد في البيت** (expressed **جلس**) and **خالد في البيت** (omitted general عامل such as **كائن**)', sol='D2'),
    M('D2-2', '**ليس كل مبنيّ بلا محلّ من الإعراب.** Which example illustrates it?', [
        '**هو** in **هو جالسٌ**: مبني على الفتح but في محل رفع مبتدأ', '**جلسَ** in **جلسَ خالدٌ**', '**الفتى** in **يسعى الفتى**'],
        '**هو** in **هو جالسٌ**: مبني على الفتح but في محل رفع مبتدأ', sol='D2'),
    M('D2-3', 'What does **الفعل والحرف لا يكونان مجرورين** mean?', [
        'A فعل and a حرف cannot be مجرور: in **في البيتِ** the جرّ belongs to the اسم.',
        'A فعل becomes مجرور after a حرف جرّ.', 'A حرف جرّ is itself مجرور.'],
        'A فعل and a حرف cannot be مجرور: in **في البيتِ** the جرّ belongs to the اسم.', sol='D2'),
    G('E1', '**حَفِظَتْ هِنْدٌ الدَّرْسَ فِي البَيْتِ.** Hind memorised the lesson in the house. Choose the analysis of each part.', ['Analysis'], [
        (w, [(E1O, a)]) for w, a in [('حفظَ', 'فعل ماضٍ مبني على الفتح لا محل له من الإعراب'), ('ـتْ', 'تاء التأنيث الساكنة، حرف لا محل له من الإعراب'),
                                     ('هندٌ', 'فاعل مرفوع بالضمة الظاهرة'), ('الدرسَ', 'مفعول به منصوب بالفتحة الظاهرة'),
                                     ('في', 'حرف جرّ مبني على السكون لا محل له من الإعراب'), ('البيتِ', 'اسم مجرور بفي بالكسرة الظاهرة'),
                                     ('في البيت', 'متعلق بحفظ، ظرف لغو')]]),
    G('E1-b', 'Classify and identify the إعراب.', ['Answer'], [
        ('إعراب of هندٌ، الدرسَ، البيتِ', [(IRAB, 'لفظي')]), ('Structure', [(STRUCT, 'فعلية')]),
        ('Meaning', [(['خبرية', 'إنشائية'], 'خبرية')]), ('موجب / غير موجب', [(['موجب', 'غير موجب'], 'موجب')])], sol='E1'),
    G('E2', 'Change the first predication to **هِنْدٌ تَحْفَظُ الدَّرْسَ**: “Hind is memorising the lesson.”', ['Answer'], [
        ('Role of هند', [(['مبتدأ', 'فاعل'], 'مبتدأ')]),
        ('فاعل of تحفظ', [(['هند (expressed)', 'ضمير مستتر تقديره هي'], 'ضمير مستتر تقديره هي')]),
        ('Role of تحفظ الدرس', [(['في محل رفع خبر', 'لا محل لها من الإعراب'], 'في محل رفع خبر')])]),
]
