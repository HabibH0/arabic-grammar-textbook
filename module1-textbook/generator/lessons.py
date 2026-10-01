L = {}

L[1] = dict(title='Words and nouns', ref=[
    ('p', 'A **كَلِمَة** is a single meaningful unit: **قَوْلٌ مُفْرَدٌ**.'),
    ('t', 0),
    ('p', 'Every word belongs to one of three classes: **اِسْم**, a noun or noun-class word; **فِعْل**, a verb, whose form connects its meaning with time; **حَرْف**, a particle, whose grammatical meaning is completed through another word or a sentence.'),
    ('h3', 'Recognising a noun'),
    ('t', 1),
    ('p', 'In the ordinary construction, the first member of an **إضافة** has neither **أل** nor tanwīn: **كِتَابُ الوَلَدِ**, not **كِتَابٌ الوَلَدِ**.'),
    ('h3', 'Classifying nouns by meaning'),
    ('t', 2),
    ('p', '**اِسْم صَرِيح**: an explicit noun, such as **القِرَاءَةُ**. **اِسْم مُؤَوَّل**: a particle with its following clause understood as a noun, as **أَنْ تَقْرَأَ** in **أَنْ تَقْرَأَ نَافِعٌ**.'),
], practice=[
    ('ex', 'R', 'Read: **الكَلِمَةُ ثَلَاثَةُ أَقْسَامٍ: اِسْمٌ وَفِعْلٌ وَحَرْفٌ.** Vocabulary: **أقسام** = divisions; **نحو** = for example; **يدلّ على** = indicates.', []),
    ('set', '1G', 'Guided'),
    ('ex', 1, 'Match **لفظ، قول، مفرد، مركب** with their meanings.', [
        ('match', ['لفظ', 'قول', 'مفرد', 'مركب'], ['meaningful utterance', 'uttered sound', 'single meaningful unit', 'expression with meaningful components'])]),
    ('ex', 2, 'In **بَابُ البَيْتِ**, “the house’s door,” identify the two nouns, the **مضاف**, and the **مضاف إليه**.', [
        ('fill', ['The two nouns', 'مضاف', 'مضاف إليه'], [[None, None, None]], 34)]),
    ('ex', 3, 'Which sign identifies **قَلَمٌ**, “a pen,” as a noun? Circle one.', [('pills', ['tense', 'tanwīn', 'a request'])]),
    ('set', '1I', 'Independent'),
    ('ex', 1, 'Give one noun-sign for each highlighted word.', [
        ('fill', ['Expression', 'Highlighted word', 'Noun-sign'], [
            ['فِي المَسْجِدِ', 'المَسْجِدِ (mosque)', None],
            ['يَا سَعِيدُ', 'سَعِيدُ (Saʿīd)', None],
            ['المَاءُ بَارِدٌ (بارد = cold)', 'المَاءُ (water)', None]], 32)]),
    ('ex', 2, 'Classify each word. Circle one.', [
        ('crows', [('حَجَرٌ (a stone)', ['اسم عين', 'اسم معنى', 'صفة']),
                   ('صَبْرٌ (patience)', ['اسم عين', 'اسم معنى', 'صفة']),
                   ('صَابِرٌ (patient)', ['اسم عين', 'اسم معنى', 'صفة'])])]),
    ('ex', 3, 'In the sentence below, “Your being patient is better,” bracket the **اسم مؤول**. Is **أن** alone that noun-equivalent?', [
        ('disp', 'أَنْ تَصْبِرَ خَيْرٌ'), ('L', 1)]),
    ('ex', 4, 'Correct: “Every noun takes **أل**, so **هو** cannot be a noun.”', [('L', 2)]),
    ('set', '1R', 'Brief review'),
    ('ex', '', 'Explain the difference between a word’s class and the meaning it conveys. Use **عِلْمٌ** and **عَالِمٌ**.', [('L', 3)]),
])

L[2] = dict(title='Verbs, particles, and the forms you need', ref=[
    ('p', 'A verb brings together **حَدَث** (an event or action), **زَمَان** (time), and a connection to a **فَاعِل** (the subject to whom the action is attributed).'),
    ('t', 0),
    ('h3', 'Recognising verbs'),
    ('t', 1),
    ('p', 'An initial **ي** is not enough to prove that a word is a verb: **يَدٌ**, “a hand,” is a noun.'),
    ('h3', 'Particles and letters'),
    ('p', '**حُرُوف المَبَانِي**: alphabet letters, such as ب، ت، م. **حُرُوف المَعَانِي**: meaningful grammatical particles, such as فِي، هَلْ، بَلْ.'),
    ('p', 'A long-vowel letter (**حَرْف مَدّ**) follows its matching vowel: **قَالَ، يَقُولُ، قِيلَ**. A **لين** letter is silent **وْ** or **يْ** after fatḥah: **خَوْفٌ**, fear; **خَيْرٌ**, good.'),
], practice=[
    ('set', '2G', 'Guided'),
    ('ex', 1, 'Label the forms.', [
        ('fill', ['Form', 'Meaning', 'Term'], [['جَلَسَ', 'sat', None], ['يَجْلِسُ', 'sits', None], ['اِجْلِسْ', 'sit!', None], ['لَا تَجْلِسْ', 'do not sit!', None]], 30)]),
    ('ex', 2, 'Match **لم، لن، سوف، قد** with their uses.', [
        ('match', ['لم', 'لن', 'سوف', 'قد'], ['may precede either past or مضارع', 'negates the future', 'marks future time', 'negates an action in the past using a مضارع'])]),
    ('ex', 3, 'Explain the different uses of **حرف** in “**م** is a حرف” and “**هَلْ** is a حرف.”', [('L', 2)]),
    ('set', '2I', 'Independent'),
    ('ex', 1, 'Classify the words in **سَوْفَ يَخْرُجُ سَعِيدٌ**, “Saʿīd will go out.” Give evidence for the verb and noun.', [
        ('fill', ['Word', 'Class', 'Evidence'], [['سَوْفَ', None, None], ['يَخْرُجُ', None, None], ['سَعِيدٌ', None, None]], 34)]),
    ('ex', 2, 'Choose the sound explanation. Circle one.', [
        ('crows', [('**لَمْ يَفْتَحْ** is', ['(a) a past verb because it means “did not open”', '(b) a مضارع whose past meaning comes from **لم**'])])]),
    ('ex', 3, 'Which is a noun, and why: **نَكْتُبُ** (we write) or **نَهْرٌ** (a river)?', [('L', 2)]),
    ('ex', 4, 'Identify the **حرف مدّ** or **حرف لين**.', [
        ('fill', ['Word', 'The letter', 'حرف مدّ or حرف لين'], [['نُورٌ (light)', None, None], ['بَيْتٌ (house)', None, None]], 30)]),
    ('set', '2R', 'Cumulative review'),
    ('ex', '', 'Classify **عِلْمٌ، عَلِمَ، فِي**. Explain why “it has a meaning” is not enough to distinguish the three classes.', [('L', 3)]),
    ('ex', 'R', 'Read: **الفِعْلُ يَدُلُّ عَلَى مَعْنًى مُقْتَرِنٍ بِزَمَانٍ.** **مقترن بـ** = connected with. Explain why this does not classify **غدًا** as a verb.', [('L', 2)]),
])

L[3] = dict(title='Building a sentence and beginning tarkīb', ref=[
    ('t', 0),
    ('p', 'Both pillars are **عُمْدَة**, structural essentials. Other elements are called **فَضْلَة** or **قَيْد**, qualifications of the basic predication.'),
    ('h3', 'The endings needed now'),
    ('t', 1),
    ('h3', 'Find the subject even when it is not a separate word'),
    ('t', 2),
    ('h3', 'Worked تركيب: كَتَبَ خَالِدٌ الدَّرْسَ.'),
    ('t', 3),
], practice=[
    ('ex', 'R', 'Read: **خَالِدٌ فَاعِلٌ مَرْفُوعٌ، وَالدَّرْسَ مَفْعُولٌ بِهِ مَنْصُوبٌ.**', []),
    ('set', '3G', 'Guided'),
    ('ex', 1, 'For **البَيْتُ وَاسِعٌ**, “The house is spacious,” complete:', [
        ('fill', ['Word', 'Role', 'Pillar'], [['البيت', None, 'مسند إليه'], ['واسع', None, 'مسند']], 30)]),
    ('ex', 2, 'In **فَتَحَ سَعِيدٌ البَابَ**, “Saʿīd opened the door,” identify verb, subject, and object. Explain both noun endings.', [
        ('fill', ['Verb', 'Subject', 'Object'], [[None, None, None]], 32), ('L', 2)]),
    ('ex', 3, 'Supply the understood subject.', [
        ('fill', ['Expression', 'Understood subject'], [['نَكْتُبُ (we write)', None], ['اِجْلِسْ (sit! to one male)', None]], 30)]),
    ('set', '3I', 'Independent'),
    ('ex', 1, 'Choose the endings and give the roles. Meaning: the boy carried the pen.', [
        ('disp', 'حَمَلَ   الوَلَدُ / الوَلَدَ   القَلَمُ / القَلَمَ'), ('L', 2)]),
    ('ex', 2, 'Correct **الكِتَابُ نَافِعًا** if the meaning is “The book is beneficial.”', [('L', 2)]),
    ('ex', 3, 'Compare the subjects. Do not treat all three final tāʾs alike.', [
        ('fill', ['Expression', 'Subject', 'What the final ت is'], [['جَلَسْتُ', None, None], ['جَلَسَتْ', None, None], ['جَلَسَتْ هِنْدٌ', None, None]], 32)]),
    ('ex', 4, 'Analyse **فَتَحْتُ البَابَ**: identify the grammatical components, both pillars, the object, and its ending.', [('grid', 3)]),
    ('set', '3R', 'Cumulative review'),
    ('ex', '', 'Why is **جَالِسٌ** an **اسم** in **خَالِدٌ جَالِسٌ**, while **جَلَسَ** is a **فعل** in **جَلَسَ خَالِدٌ**? What stays the same about Khalid’s relationship to the predication?', [('L', 4)]),
])

L[4] = dict(title='Sentence structure and sentences inside sentences', ref=[
    ('p', 'Find the underlying construction; do not simply inspect the first printed word.'),
    ('t', 0),
    ('h3', 'A ناسخ enters a nominal construction'),
    ('t', 1),
    ('p', 'Both patterns are **جُمْلَة اِسْمِيَّة مَنْسُوخَة**. **خَالِدٌ صَادِقٌ** is **اسمية غير منسوخة**. **إنّ** is a particle; **كان** is a verb.'),
    ('h3', 'Sentences inside sentences'),
    ('p', 'In **خَالِدٌ يَكْتُبُ**, the outer construction is nominal: **خالدٌ + [يكتبُ]**. Inside **[يكتب]** is a verbal sentence: verb + understood subject **هو**. That entire verbal sentence supplies the outer **خبر**. The containing sentence is **الجُمْلَة الكُبْرَى**; the sentence inside it is **الجُمْلَة الصُّغْرَى**.'),
], practice=[
    ('ex', 'R', 'Read: **الجُمْلَةُ الكُبْرَى تَشْتَمِلُ عَلَى جُمْلَةٍ صُغْرَى.** **تشتمل على** = contains; **تقع موقع** = occupies the position of.', []),
    ('set', '4G', 'Guided'),
    ('ex', 1, 'Classify **إِنَّ العِلْمَ نَافِعٌ**, “Indeed, knowledge is beneficial,” and name the two governed noun roles.', [('L', 2)]),
    ('ex', 2, 'Supply the endings. Meaning: “The house was spacious.”', [('disp', 'كَانَ البَيْتـ___ وَاسِعـ___')]),
    ('ex', 3, 'Bracket the inner sentence in **هِنْدٌ تَكْتُبُ**. Circle its understood subject.', [
        ('disp', 'هِنْدٌ تَكْتُبُ'), ('pills', ['هو', 'هي', 'أنا'])]),
    ('set', '4I', 'Independent'),
    ('ex', 1, 'Classify by structure and justify.', [
        ('fill', ['Sentence', 'Structure', 'Justification'], [['البَابَ فَتَحَ سَعِيدٌ', None, None], ['سَعِيدٌ يَجْلِسُ', None, None], ['كَانَ القَلَمُ جَدِيدًا (جديد = new)', None, None]], 48)]),
    ('ex', 2, 'Correct the reasoning: “**إنّ خالدًا صادقٌ** begins with a particle, so it is neither nominal nor verbal.”', [('L', 2)]),
    ('ex', 3, 'Compare **حَضَرَ الضَّيْفُ** and **الضَّيْفُ حَضَرَ**. Identify every subject or implicit subject and explain the role of **الضيف** in each.', [
        ('fill', ['Sentence', 'Subject or implicit subject', 'Role of الضيف'], [['حَضَرَ الضَّيْفُ', None, None], ['الضَّيْفُ حَضَرَ', None, None]], 48)]),
    ('set', '4R', 'Cumulative review'),
    ('ex', '', 'Analyse **إِنَّ الكِتَابَ نَافِعٌ**: word classes, noun roles, case endings, and structural classification.', [
        ('grid', 3), ('lab', 'Structural classification', 1)]),
])

L[5] = dict(title='Meaning, complete speech, and independent classifications', ref=[
    ('p', 'A **جُمْلَة خَبَرِيَّة** makes an assertion that can be assessed as true or false. A **جُمْلَة إِنْشَائِيَّة** performs something such as asking, ordering, or wishing. Do not confuse **خبرية** with **خبر**, the predicate of a nominal sentence.'),
    ('t', 0),
    ('p', 'Form and intended use can differ. **غَفَرَ اللهُ لَكَ** uses a past verbal form but, as a prayer, does not report a past event.'),
    ('h3', 'Complete speech'),
    ('p', '**كَلَام** is **قَوْل مُفِيد**: an utterance complete enough for the listener not to need an essential continuation. **إِنْ تَصْدُقْ…** contains a predication but needs its response; **إِنْ تَصْدُقْ تَنْجَحْ** is complete speech.'),
    ('h3', 'Affirmative and non-affirmative speech'),
    ('p', '**كَلَام غَيْر مُوجَب** contains one of **نَفْي، نَهْي، اِسْتِفْهَام**; **كَلَام مُوجَب** contains none of these.'),
    ('t', 1),
], practice=[
    ('set', '5G', 'Guided'),
    ('ex', 1, 'Classify **هَلْ فَتَحَ خَالِدٌ البَابَ؟** on three axes.', [
        ('fill', ['Nominal / verbal', 'Report / performative', 'Affirmative / non-affirmative'], [[None, None, None]], 34)]),
    ('ex', 2, 'Which is complete speech? Circle one, then explain.', [('pills', ['بَابُ البَيْتِ', 'اُكْتُبْ', 'إِنْ تَكْتُبْ…']), ('L', 2)]),
    ('ex', 3, 'Is **مَا كَتَبَ خَالِدٌ** a prohibition or a negative report? Circle one.', [('pills', ['a prohibition', 'a negative report'])]),
    ('set', '5I', 'Independent'),
    ('ex', 1, 'Label the use.', [
        ('fill', ['Utterance', 'Use'], [['يَا سَعِيدُ!', None], ['لَا تَجْلِسْ!', None], ['لَيْتَ البَابَ مَفْتُوحٌ! (If only the door were open!)', None]], 30)]),
    ('ex', 2, 'A speaker says **غَفَرَ اللهُ لَكَ** while praying for someone. Explain why a past verb does not make this a report about the past.', [('L', 3)]),
    ('ex', 3, 'Correct: “Every **إنشائية** sentence is **غير موجب**.” Give a counterexample.', [('L', 2)]),
    ('set', '5R', 'Cumulative review'),
    ('ex', '', 'Classify **خَالِدٌ يَكْتُبُ** by outer structure, inner structure, meaning, and **موجب / غير موجب**. Is it complete speech?', [
        ('fill', ['Outer structure', 'Inner structure', 'Meaning', 'موجب / غير موجب', 'Complete speech?'], [[None, None, None, None, None]], 38)]),
    ('ex', 'R', 'Read without a word-by-word gloss: **كُلُّ كَلَامٍ جُمْلَةٌ، وَلَيْسَ كُلُّ جُمْلَةٍ كَلَامًا.** Explain the distinction with a conditional example.', [('L', 3)]),
])

L[6] = dict(title='Phrases and what they attach to', ref=[
    ('t', 0),
    ('p', '**عند** is an **اسم**, whereas **في** is a **حرف**. In adverbial uses **فَوْقَ، تَحْتَ، عِنْدَ** are accusative; their following إضافة noun is genitive.'),
    ('p', 'In **جَلَسَ خَالِدٌ فِي البَيْتِ**, **فِي البَيْتِ** is the **مُتَعَلِّق**, the attached phrase; **جَلَسَ** is its **مُتَعَلَّق**, what it attaches to. **في** governs **البيتِ** internally; the whole phrase attaches to **جلس** in the sentence.'),
    ('t', 1),
    ('p', 'Omitted **particular action** gives **لغو**; omitted **general existence** gives **مستقرّ**.'),
    ('h3', 'Worked تركيب: القَلَمُ فَوْقَ الكِتَابِ.'),
    ('ol', ['**القلمُ**: مبتدأ مرفوع بالضمة.', '**فوقَ**: ظرف منصوب بالفتحة، وهو مضاف.', '**الكتابِ**: مضاف إليه مجرور بالكسرة.',
            '**فوق الكتاب**: شبه جملة متعلق بمحذوف عام، تقديره **كائنٌ**. It supplies the predicate position: **في محل رفع خبر**.',
            'The sentence is nominal. The phrase is **ظرف مستقرّ**.']),
], practice=[
    ('set', '6G', 'Guided'),
    ('ex', 1, 'Divide each phrase into its components. Which begins with a noun?', [
        ('fill', ['Phrase', 'First component', 'Second component'], [['إِلَى المَسْجِدِ (to the mosque)', None, None], ['تَحْتَ الشَّجَرَةِ (under the tree)', None, None]], 32),
        ('lab', 'Begins with a noun:', 1)]),
    ('ex', 2, 'In **خَرَجَ سَعِيدٌ مِنَ البَيْتِ**, “Saʿīd went out of the house,” identify the governor of **البيتِ** and the attachment of **من البيت**. The connecting fatḥah in **مِنَ** is part of pronunciation here, not noun case.', [
        ('fill', ['Governor of البيتِ', 'Attachment of من البيت'], [[None, None]], 34)]),
    ('ex', 3, 'Complete: an omitted **specific** action gives ظرف ___; omitted **general existence** gives ظرف ___.', []),
    ('set', '6I', 'Independent'),
    ('ex', 1, 'Analyse **الكِتَابُ عِنْدَ الوَلَدِ** as in the worked example.', [('grid', 4), ('lab', 'The sentence and the phrase', 1)]),
    ('ex', 2, 'Name the phrase-type by its governor and explain its attachment.', [
        ('fill', ['Sentence', 'Phrase-type', 'Attachment'], [['جَلَسَ الضَّيْفُ عِنْدَ البَابِ', None, None], ['الضَّيْفُ عِنْدَ البَابِ', None, None]], 42)]),
    ('ex', 3, 'Correct: “**في** and **عند** must both be particles because both express location.”', [('L', 2)]),
    ('ex', 4, 'A speaker answers **إِلَى المَسْجِدِ** after **أَيْنَ ذَهَبَ سَعِيدٌ؟**, “Where did Saʿīd go?” Identify the understood action and classify the phrase.', [
        ('fill', ['Understood action', 'Classification'], [[None, None]], 34)]),
    ('set', '6R', 'Cumulative review'),
    ('ex', '', 'Explain why **القَلَمُ فَوْقَ الكِتَابِ** is complete speech although it has no expressed verb, and why **فوق الكتاب** is a phrase rather than an independent expressed subject–predicate pair.', [('L', 4)]),
])

L[7] = dict(title='The roles of an implied-predicate phrase', ref=[
    ('p', '**مَعْرِفَة** means definite: here, a personal name or a noun with **أل**. **نَكِرَة** means indefinite, such as **رَجُلٌ**.'),
    ('t', 0),
    ('p', 'For **حال**, learn **ذُو الحَال / صَاحِب الحَال**; for **نعت**, learn **مَنْعُوت / مَوْصُوف**. In a **صلة**, supply a **verb**, such as **استقرّ**. With a **ناسخ**: **إِنَّ الوَلَدَ فِي البَيْتِ** occupies **رفع خبر إنّ**; **كَانَ الوَلَدُ فِي البَيْتِ** occupies **نصب خبر كان**.'),
    ('h3', 'اعتماد: a phrase followed by a nominative noun'),
    ('p', 'In **أَفِي البَيْتِ رَجُلٌ؟**: (1) supply the general verb **استقرّ**, and **رجلٌ** is its **فاعل**; or (2) take **في البيت** as **خبر مقدّم** and **رجلٌ** as **مبتدأ مؤخّر**.'),
    ('t', 1),
], practice=[
    ('set', '7G', 'Guided'),
    ('ex', 1, 'In **رأيت خالدًا عند الباب**, intended as “I saw Khalid while he was by the door,” identify **صاحب الحال** and the phrase’s role.', [
        ('fill', ['صاحب الحال', 'Role of the phrase'], [[None, None]], 34)]),
    ('ex', 2, 'Supply a suitable general **verb** for the relative connection in **جاء الذي في المسجد**. Why is a descriptive noun alone unsuitable?', [('L', 2)]),
    ('ex', 3, 'In **كان القلم في البيت**, distinguish the phrase’s predicate position from the case of **البيت**.', [
        ('fill', ['Position of في البيت', 'Case of البيت'], [[None, None]], 34)]),
    ('set', '7I', 'Independent'),
    ('ex', 1, 'Name the role of each bracketed phrase.', [
        ('fill', ['Expression', 'Role'], [['الكتاب [على الباب]', None], ['رأيت ولدًا [عند الشجرة] (a boy who was by the tree)', None], ['جاء الذي [في السوق]', None]], 30)]),
    ('ex', 2, 'Give the two principal analyses of **أعند الباب ضيف؟**, “Is there a guest by the door?”', [('lab', 'Analysis 1', 2), ('lab', 'Analysis 2', 2)]),
    ('ex', 3, 'In **خالد عنده قلم**, identify what **ـه** refers to and the nominative noun following the phrase. What supplies the context for **اعتماد**?', [
        ('fill', ['ـه refers to', 'Nominative noun', 'Context for اعتماد'], [[None, None, None]], 34)]),
    ('ex', 4, 'Correct: “Whenever a governor is omitted, supply **كائن**.” Use one particular-action example and one relative example.', [('L', 3)]),
    ('set', '7R', 'Cumulative review'),
    ('ex', '', 'Explain how the same words **في البيت** can be **لغو** or **مستقرّ**, and how a phrase containing a genitive noun can occupy a nominative predicate position.', [('L', 4)]),
])

L[8] = dict(title='Governing and being governed', ref=[
    ('ul', ['**عَامِل**: a governing element which requires a grammatical status.',
            '**مَعْمُول**: the element receiving that status.',
            '**إِعْرَاب**: the effect of government at a word’s ending, or in its grammatical position when an ending cannot show it.']),
    ('p', 'All verbs govern. **في، إنّ، لن** are governing particles. In **مَا حَضَرَ خَالِدٌ**, **ما** is **غَيْر عَامِل**, also called **عَاطِل** or **مُهْمَل**. **اِبْتِدَاء** accounts for the رفع of the ordinary مبتدأ and خبر.'),
    ('h3', 'Verb mood'),
    ('t', 0),
    ('p', 'Nouns have **رفع، نصب، جرّ**; inflected verbs have **رفع، نصب، جزم**. Compare **لَا تَكْتُبُ**, “you do not write,” with **لَا تَكْتُبْ**, “do not write.”'),
    ('h3', 'What can receive a grammatical position?'),
    ('t', 1),
], practice=[
    ('set', '8G', 'Guided'),
    ('ex', 1, 'In **في المسجد**, identify the governor, governed noun, and resulting status.', [
        ('fill', ['Governor', 'Governed noun', 'Status'], [[None, None, None]], 34)]),
    ('ex', 2, 'Choose and explain. Circle one.', [('disp', 'لن ___ سعيدٌ'), ('pills', ['يخرجُ', 'يخرجَ', 'يخرجْ']), ('L', 1)]),
    ('ex', 3, 'In **لم يكتب خالدٌ**, can **يكتب** be both **عامل** and **معمول**? Identify the two relationships.', [
        ('fill', ['عامل', 'معمول', 'Status'], [[None, None, None], [None, None, None]], 32)]),
    ('set', '8I', 'Independent'),
    ('ex', 1, 'Add the verb ending required by each meaning.', [
        ('disp', 'لا تجلسـ___ = “Do not sit”'), ('disp', 'لا تجلسـ___ = “You do not sit”')]),
    ('ex', 2, 'Correct the analysis: “**لن** is **منصوب** because it causes **نصب**.”', [('L', 2)]),
    ('ex', 3, 'In **ما خرج سعيدٌ من البيت**, identify one non-governing particle, one governing particle, and the phrase’s attachment. Give the role of **سعيد**.', [
        ('fill', ['Non-governing particle', 'Governing particle', 'Attachment of the phrase', 'Role of سعيد'], [[None, None, None, None]], 38)]),
    ('ex', 4, 'Translate and illustrate: **غير العامل ليس هو غير المعمول**.', [('L', 3)]),
    ('set', '8R', 'Cumulative review'),
    ('ex', '', 'Explain both the internal and external government in **خالدٌ في البيت**. Which part is genitive, and which larger unit supplies the predicate?', [('L', 4)]),
    ('ex', 'R', 'Read: **العامل يوجب حالة، والمعمول يقبلها.** **يوجب** = requires; **يقبل** = receives/accepts; **حالة** = grammatical status. Explain both directions using **لن يفتح**.', [('L', 2)]),
])

L[9] = dict(title='Visible, estimated, and positional iʿrāb', ref=[
    ('p', '**مُعْرَب** means grammatically inflectable. **مَبْنِيّ** means having a fixed form. Fixed form does not mean “no grammatical role.”'),
    ('t', 0),
    ('p', '**الفتى**: فاعل مرفوع بضمة مقدرة على الألف؛ منع من ظهورها التعذر. **هو**: ضمير منفصل مبني على الفتح في محل رفع مبتدأ.'),
    ('h3', 'نون النسوة: a fixed verb in a mood position'),
    ('t', 1),
    ('p', 'Say **لَا مَحَلَّ لَهُ مِنَ الإِعْرَابِ** for a particle, an ordinary past verb not in a governed mood position, an imperative verb, or an independent sentence as a whole.'),
    ('h3', 'A full تركيب method'),
    ('ol', ['Read for meaning; identify words and attached pronouns.', 'Locate the **مسند إليه** and **مسند**, including understood elements.',
            'Identify the sentence’s foundation and any **ناسخ**.', 'Assign roles to the remaining nouns and units.',
            'Find each governing relationship and phrase attachment.', 'Give case/mood and its sign: **ظاهر، مقدّر، في محلّ**; distinguish **بناء**.',
            'State the role of any embedded sentence or phrase, then classify the whole utterance.']),
], practice=[
    ('set', '9G', 'Guided'),
    ('ex', 1, 'Choose **لفظي، تقديري، محلي** for each. Circle one.', [
        ('crows', [('**خالدٌ** as subject', ['لفظي', 'تقديري', 'محلي']), ('**الفتى** as subject', ['لفظي', 'تقديري', 'محلي']),
                   ('**هو** as مبتدأ', ['لفظي', 'تقديري', 'محلي']), ('**[يكتب]** as the خبر of خالد', ['لفظي', 'تقديري', 'محلي'])])]),
    ('ex', 2, 'Complete the reason:', [('disp', 'الهدى اسم مجرور بكسرة ___، منع من ظهورها ___')]),
    ('ex', 3, 'Does the sukūn before **نون النسوة** in **يكتبْنَ** prove jussive mood? Explain using **لن يكتبن**.', [('L', 2)]),
    ('set', '9I', 'Independent'),
    ('ex', 1, 'أعرب: **هو يجلس**. Include the outer and inner structures, the implicit subject, and the position of the inner sentence.', [('grid', 4), ('lab', 'Outer and inner structures', 1)]),
    ('ex', 2, 'أعرب: **يسعى الفتى إلى المسجد**. Do not classify every ending as estimated merely because one is.', [('grid', 5)]),
    ('ex', 3, 'صحّح: “**جلسَ** is منصوب because it ends in fatḥah.”', [('L', 2)]),
    ('ex', 4, 'Explain the difference between “a nominative noun with no printed vowel mark,” “a nominative noun ending in alif,” and “a pronoun in a nominative position.”', [('L', 3)]),
    ('set', '9R', 'Cumulative review'),
    ('ex', '', 'Analyse **لن يكتبن الدرس**. Identify the particle, the verb’s fixed form and mood position, the attached subject, and the object ending.', [('grid', 4)]),
])

REVIEW = [
    ('p', 'Add the necessary final endings in your answers. In the unvowelled passages, use the stated meaning to choose the reading. Give full internal vowels only where requested or needed to disambiguate a word.'),
    ('h2', 'A. Distinctions'),
    ('ex', 'A1', 'Match the term to its meaning.', [
        ('match', ['مسند', 'مسند إليه', 'عامل', 'معمول', 'مصدر مؤول', 'ظرف مستقرّ'],
         ['the recipient of government', 'what is predicated', 'a phrase with an omitted general governor', 'what something is predicated about',
          'a noun-equivalent made from a particle and clause', 'what imposes a grammatical status'])]),
    ('ex', 'A2', 'Explain why each claim fails:', []),
    ('ex', '1', 'Every noun names a physical object.', [('L', 1)]),
    ('ex', '2', 'Every sentence beginning with a written noun is nominal.', [('L', 1)]),
    ('ex', '3', 'Every fatḥah is a sign of accusative case.', [('L', 1)]),
    ('ex', '4', 'A phrase is always governed by the nearest verb.', [('L', 1)]),
    ('ex', '5', 'A sentence without an expressed verb is incomplete.', [('L', 1)]),
    ('ex', '6', '**غير عامل** and **غير معمول** mean the same thing.', [('L', 1)]),
    ('h2', 'B. Endings, relationships, and corrections'),
    ('ex', 'B1', 'Supply endings and explain their causes:', []),
    ('ex', '1', '“Indeed, knowledge is beneficial.”', [('disp', 'إنّ العلمـ___ نافعـ___'), ('L', 1)]),
    ('ex', '2', '“The guest was in the house.”', [('disp', 'كان الضيفـ___ في البيتـ___'), ('L', 1)]),
    ('ex', '3', '“Saʿīd did not open the door.”', [('disp', 'لم يفتحـ___ سعيدـ___ البابـ___'), ('L', 1)]),
    ('ex', 'B2', 'Correct the grammatical error in each:', []),
    ('ex', '1', '**فَتَحَ الوَلَدَ البَابُ** intended as “The boy opened the door.”', [('L', 1)]),
    ('ex', '2', '**لَنْ يَجْلِسْ خَالِدٌ**.', [('L', 1)]),
    ('ex', '3', '**كِتَابٌ الوَلَدِ** intended as “the boy’s book.”', [('L', 1)]),
    ('ex', 'B3', 'Complete with one suitable word and give its role:', [
        ('fill', ['Sentence', 'Word', 'Role'], [['القَلَمُ ___ الكِتَابِ (The pen is above the book.)', None, None],
                                               ['___ تَكْذِبْ (Do not lie.)', None, None], ['خَالِدٌ ___ (Khalid is truthful.)', None, None]], 34)]),
    ('h2', 'C. Connected reading and full تركيب'),
    ('ex', 'C1', 'Add the grammatical endings and give full تركيب of all three sentences. For every understood subject, state its referent. Give the phrase’s attachment and the outer classification of each sentence. Meaning: Saʿīd is in the mosque. He is reading the book. He did not go out. The reading verb is **يَقْرَأُ**.', [
        ('disp', 'سعيد في المسجد. يقرأ الكتاب. لم يخرج.'), ('grid', 10), ('lab', 'Classifications', 3)]),
    ('ex', 'C2', 'Add endings. Give full تركيب of the first and last sentences. In the middle two, identify verb, subject, and any object. Explain why the final sentence has both an outer مبتدأ and an inner subject. Meaning: The guest was by the door. Khalid opened the door. The guest entered. He is sitting. **دَخَلَ** means “entered”; the final **هو** refers to the guest.', [
        ('disp', 'كان الضيف عند الباب. فتح خالد الباب. دخل الضيف. هو يجلس.'),
        ('lab', 'With endings', 1), ('grid', 8),
        ('fill', ['Sentence', 'Verb', 'Subject', 'Object'], [['فتح خالد الباب', None, None, None], ['دخل الضيف', None, None, None]], 34),
        ('L', 3)]),
    ('h2', 'D. Read Arabic grammatical explanations'),
    ('ex', 'D1', 'Translate the analysis, then identify the sentence it describes:', [
        ('disp', 'خالد مبتدأ مرفوع بالضمة. يكتب فعل مضارع مرفوع بالضمة، والفاعل ضمير مستتر تقديره هو. والجملة الفعلية في محل رفع خبر.'),
        ('L', 4), ('lab', 'The sentence', 1)]),
    ('ex', 'D2', 'Explain in English, using one Arabic example for each:', []),
    ('ex', '1', '**قد يكون العامل مذكورًا أو محذوفًا.**', [('L', 2)]),
    ('ex', '2', '**ليس كل مبنيّ بلا محلّ من الإعراب.**', [('L', 2)]),
    ('ex', '3', '**الفعل والحرف لا يكونان مجرورين.**', [('L', 2)]),
    ('h2', 'E. Final transfer task'),
    ('ex', 'E1', 'Analyse this new sentence, using only the vocabulary help. Intended meaning: Hind memorised the lesson in the house. **حَفِظَ** = memorised. The place qualifies the memorising. Add full vowels. Distinguish the feminine marker from the subject. Identify both pillars, the object, the internal government of the phrase, its external attachment, and the type of إعراب on each noun. Classify the utterance by structure, meaning, and **موجب / غير موجب**.', [
        ('disp', 'حفظت هند الدرس في البيت.'), ('lab', 'Fully vowelled', 1), ('grid', 7), ('lab', 'Classification', 2)]),
    ('ex', 'E2', 'Change the first predication to **هِنْدٌ تَحْفَظُ الدَّرْسَ**: “Hind is memorising the lesson.” Explain what changed in the تركيب of **هند**, where the verb’s subject is now, and what role the inner sentence occupies.', [('L', 4)]),
    ('h2', 'Ready to continue?'),
    ('p', 'You are ready when you can explain a choice of ending from the grammatical relationship, distinguish a word’s class from its role, find implicit subjects, and identify a phrase’s attachment without guessing from word order alone. Use the answer explanations to repair the reasoning behind any mistake, then redo that item before continuing.'),
]
