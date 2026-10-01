# Module 4: Prepositions. Auto-checked items; correct answers follow the Module 4 answers file.
# The answers file has no reading answers, so the reading items carry their own short solutions (SOLMD).
from item_kit import M, G, R, SOLMD

CLASS = ['أصليّ', 'شبيه بالزائد', 'زائد']
ITEMS = {}

ITEMS['1'] = [
    G('1G-1', 'Match each term with its meaning.', ['Meaning'], R(
        ['connection to a governor', 'instrument', 'noun governed in جرّ'],
        [('مجرور', 'noun governed in جرّ'), ('تعلّق', 'connection to a governor'), ('آلة', 'instrument')])),
    M('1G-2', 'Choose: **كتب خالدٌ بالقلمُ / بالقلمِ / بالقلمَ**.', [
        '**بالقلمِ**: genitive by bā; being the instrument does not make it accusative.',
        '**بالقلمَ**: accusative, because the pen is the instrument the writing acts on.',
        '**بالقلمُ**: nominative, because the pen is what actually does the writing.',
        ], '**بالقلمِ**: genitive by bā; being the instrument does not make it accusative.'),
    G('1G-3', 'In **كَتَبَ بِهِ**:', ['Analysis'], R(
        ['ضمير مستتر تقديره هو في محل رفع فاعل', 'ضمير متصل مبني على الكسر في محل جرّ بالباء', 'متعلق بكتب، يدلّ على الآلة', 'ضمير في محل نصب مفعول به'],
        [('Subject of كتب', 'ضمير مستتر تقديره هو في محل رفع فاعل'), ('الهاء', 'ضمير متصل مبني على الكسر في محل جرّ بالباء'),
         ('به', 'متعلق بكتب، يدلّ على الآلة')])),
    G('1I-1', 'Give the attachment and role of **في المسجد** in each.', ['Attachment'], R(
        ['متعلق بجلس: ظرف لغو', 'متعلق بمحذوف عام تقديره كائنٌ: ظرف مستقرّ في محل رفع خبر'],
        [('جَلَسَ الضَّيْفُ فِي المَسْجِدِ', 'متعلق بجلس: ظرف لغو'), ('الضَّيْفُ فِي المَسْجِدِ', 'متعلق بمحذوف عام تقديره كائنٌ: ظرف مستقرّ في محل رفع خبر')])),
    M('1I-2', 'Correct: “Every جارّ ومجرور is a مفعول به, and its noun must therefore be accusative.”', [
        'A phrase can express time, place, cause or instrument; its noun is genitive either way.',
        'The claim is right: every phrase is an object, so its noun should really be accusative.',
        'Every phrase is a حال, so its noun is accusative in position and genitive in form.',
        'The phrase as a whole is accusative, so its noun takes fatḥah after the preposition.',
        ], 'A phrase can express time, place, cause or instrument; its noun is genitive either way.'),
    G('1R', 'Identify both routes to جرّ in **كَتَبَ خَالِدٌ بِقَلَمِ المُعَلِّمِ**.', ['Why genitive?'], R(
        ['مجرور بالباء، وهو مضاف', 'مضاف إليه مجرور', 'مجرور بالباء أيضًا'],
        [('قلمِ', 'مجرور بالباء، وهو مضاف'), ('المعلمِ', 'مضاف إليه مجرور')])),
    M('1-Read', 'Read: **الاسم مجرور، والجارّ والمجرور متعلّق بالفعل.** Which statement concerns a word, and which a relationship?', [
        '**مجرور** describes the noun’s case (a word); **متعلّق** describes the phrase’s link (a relationship).',
        '**مجرور** describes the phrase’s link (a relationship); **متعلّق** describes the noun’s case (a word).',
        'Both describe the noun: **مجرور** its ending and **متعلّق** its position in the sentence.',
        'Both describe the verb: it governs the noun in جرّ and is linked to the preposition.',
        ], '**مجرور** describes the noun’s case (a word); **متعلّق** describes the phrase’s link (a relationship).', sol=SOLMD('“The noun is genitive, and the preposition with its noun is attached to the verb.” **مجرور** describes one word, the noun’s case. **متعلّق** describes the relationship of the whole phrase to its governor.')),
]

ITEMS['2'] = [
    G('2G-1', 'Match each phrase to its relationship.', ['Relationship'], R(
        ['آلة', 'عوض', 'مفعول فيه'],
        [('كتبت **بالقلم**', 'آلة'), ('سافرت **بالليل**', 'مفعول فيه'), ('اشتريت الكتاب **بدرهم**', 'عوض')])),
    G('2G-2', 'In **ذَهَبَ خَالِدٌ بِالطِّفْلِ**:', ['Analysis'], R(
        ['فاعل مرفوع بالضمة', 'اسم مجرور بالباء بالكسرة', 'متعلق بذهب: الباء للتعدية، مفعول به غير صريح', 'مفعول به منصوب'],
        [('خالدٌ', 'فاعل مرفوع بالضمة'), ('الطفلِ', 'اسم مجرور بالباء بالكسرة'), ('بالطفل', 'متعلق بذهب: الباء للتعدية، مفعول به غير صريح')])),
    M('2G-3', 'Why can **بقوة** describe either the action’s manner or the actor’s state?', [
        'Its meaning can describe how the taking was done or the taker’s state; it stays genitive.',
        'Its case changes: accusative when it describes manner, genitive when it describes the actor.',
        'The bā is additional here, so the phrase can attach to either word without changing meaning.',
        'It cannot: a phrase with bā can only describe the actor, never the manner of the action.',
        ], 'Its meaning can describe how the taking was done or the taker’s state; it stays genitive.'),
    G('2I-1', '**كتب المعلم بالقلم. عاقب الطفل بذنبه.** “The teacher wrote with the pen; he punished the child because of his offence.”', ['Analysis'], R(
        ['متعلق بكتب، آلة', 'مفعول به منصوب بالفتحة', 'متعلق بعاقب، سبب: مفعول له غير صريح', 'ضمير في محل جرّ مضاف إليه، يعود على الطفل', 'فاعل مرفوع'],
        [('بالقلم', 'متعلق بكتب، آلة'), ('الطفلَ', 'مفعول به منصوب بالفتحة'), ('بذنبه', 'متعلق بعاقب، سبب: مفعول له غير صريح'),
         ('الهاء in بذنبه', 'ضمير في محل جرّ مضاف إليه، يعود على الطفل')])),
    M('2I-2', 'Correct: “باء التعدية always proves that the agent physically accompanied the object.”', [
        'Accompaniment is a common implication, not a condition: the action can reach its object without it.',
        'The claim is correct: باء التعدية always means the agent physically went along with the object being moved.',
        'باء التعدية never implies accompaniment; it only marks the instrument with which the action is done.',
        'باء التعدية is additional, so it adds no meaning about accompaniment.',
        ], 'Accompaniment is a common implication, not a condition: the action can reach its object without it.'),
    G('2R', 'In **سافرت به بالليل**, “I travelled with him, taking him along, at night”:', ['Analysis'], R(
        ['ضمير متصل في محل رفع فاعل', 'ضمير في محل جرّ بالباء، يعود على المصاحَب', 'mediated object relationship, attached to سافرت', 'time of the travel, attached to سافرت'],
        [('ـتُ', 'ضمير متصل في محل رفع فاعل'), ('الهاء in به', 'ضمير في محل جرّ بالباء، يعود على المصاحَب'),
         ('به', 'mediated object relationship, attached to سافرت'), ('بالليل', 'time of the travel, attached to سافرت')])),
    M('2-Read', 'Read: **تختلف وظيفة شبه الجملة باختلاف المعنى.** (**تختلف** = differs; **باختلاف** = according to the difference in.) What does it say?', [
        'The phrase’s function differs according to the meaning.',
        'The phrase’s case differs according to the meaning.',
        'The phrase’s function stays the same whatever the meaning.',
        'The phrase’s function depends only on which preposition is used.',
        ], 'The phrase’s function differs according to the meaning.', sol=SOLMD('“The function of the phrase differs according to the difference in meaning.” **بالقلم** with writing is an instrument; **بالليل** with travelling gives the time. The noun is genitive in both.')),
]

ITEMS['3'] = [
    M('3G-1', 'Complete: **سرتُ … المسجدِ … البيتِ**, “I walked from the mosque to the house.”', [
        'سِرْتُ مِنَ المَسْجِدِ إِلَى البَيْتِ', 'سِرْتُ إِلَى المَسْجِدِ مِنَ البَيْتِ', 'سِرْتُ مِنَ المَسْجِدِ مِنَ البَيْتِ', 'سِرْتُ إِلَى المَسْجِدِ إِلَى البَيْتِ'],
        'سِرْتُ مِنَ المَسْجِدِ إِلَى البَيْتِ'),
    G('3G-2', 'In **عملت من أول النهار**:', ['Why genitive?'], R(
        ['مجرور بمن، وهو مضاف', 'مضاف إليه مجرور'],
        [('أوّلِ', 'مجرور بمن، وهو مضاف'), ('النهارِ', 'مضاف إليه مجرور')])),
    M('3G-3', 'In the example, what is the function of **من الخوف**?', ['cause', 'place', 'exchange'], 'cause'),
    G('3I-1', '**خرج الضيف من المسجد. سار إلى البيت.**', ['Analysis'], R(
        ['فاعل مرفوع بالضمة', 'متعلق بخرج: the starting place', 'ضمير مستتر تقديره هو، يعود على الضيف', 'متعلق بسار: the destination', 'مفعول به منصوب'],
        [('الضيفُ', 'فاعل مرفوع بالضمة'), ('من المسجد', 'متعلق بخرج: the starting place'), ('Subject of سار', 'ضمير مستتر تقديره هو، يعود على الضيف'),
         ('إلى البيت', 'متعلق بسار: the destination')])),
    M('3I-2', 'Why is **من كل ذنب** attached to **تائب** although **تائب** is not a verb?', [
        '**تائب** is an اسم فاعل meaning “repenting”, a شبه فعل able to govern the phrase.',
        'Every phrase attaches to the nearest noun, so it attaches to **تائب** by position.',
        '**من** is additional here, so the phrase needs no verb to attach to.',
        'The phrase is not attached at all; it stands alone as a حال.',
        ], '**تائب** is an اسم فاعل meaning “repenting”, a شبه فعل able to govern the phrase.'),
    G('3R', 'Why is each noun genitive?', ['Reason'], R(
        ['مجرور بالباء: visible kasrah', 'مجرور بمن: visible kasrah', 'مضاف إليه: visible kasrah', 'مبني على الكسر في محل جرّ بإلى: positional'],
        [('القلمِ in بالقلم', 'مجرور بالباء: visible kasrah'), ('أوّلِ in من أول النهار', 'مجرور بمن: visible kasrah'),
         ('النهارِ in من أول النهار', 'مضاف إليه: visible kasrah'), ('الهاء in إليه', 'مبني على الكسر في محل جرّ بإلى: positional')])),
    M('3-Read', 'Read: **مِن لابتداء الغاية، وإلى لانتهاء الغاية.** What does it say?', [
        '**من** marks the starting point and **إلى** the endpoint.',
        '**من** marks the endpoint and **إلى** the starting point.',
        '**من** and **إلى** both mark the starting point of the extent.',
        '**إلى** marks the endpoint and always includes it.',
        ], '**من** marks the starting point and **إلى** the endpoint.', sol=SOLMD('“**من** is for the beginning of the extent, and **إلى** for its end.” Whether the endpoint itself is included is not settled by **إلى** alone; the expression and context decide.')),
]

ITEMS['4'] = [
    G('4G-1', 'Match each meaning.', ['Meaning'], R(
        ['separation', 'being over', 'obligation'], [('المجاوزة', 'separation'), ('الاستعلاء', 'being over'), ('الإلزام', 'obligation')])),
    G('4G-2', 'Analyse **جلس الطفل على السرير**.', ['Analysis'], R(
        ['فاعل مرفوع بالضمة', 'اسم مجرور بعلى بالكسرة', 'متعلق بجلس: مفعول فيه غير صريح', 'مفعول به منصوب'],
        [('الطفلُ', 'فاعل مرفوع بالضمة'), ('السريرِ', 'اسم مجرور بعلى بالكسرة'), ('على السرير', 'متعلق بجلس: مفعول فيه غير صريح')])),
    M('4G-3', 'Is **عن** a particle or a noun in **من عن يمينه**?', [
        'a noun meaning **جانب**, because it follows **من**; it is مضاف',
        'a preposition, because **عن** keeps its particle class after **من**',
        'an additional particle that adds emphasis to **من**',
        'a noun meaning **جانب**, but it is the مضاف إليه of **من**',
        ], 'a noun meaning **جانب**, because it follows **من**; it is مضاف'),
    G('4I-1', '**نهيت الطفل عن الشر**', ['Analysis'], R(
        ['ضمير في محل رفع فاعل', 'مفعول به منصوب بالفتحة: direct object', 'اسم مجرور بعن بالكسرة', 'متعلق بنهيت: mediated object relationship'],
        [('ـتُ', 'ضمير في محل رفع فاعل'), ('الطفلَ', 'مفعول به منصوب بالفتحة: direct object'), ('الشرِّ', 'اسم مجرور بعن بالكسرة'),
         ('عن الشر', 'متعلق بنهيت: mediated object relationship')])),
    G('4I-2', 'Give the role of **على حبه** for each referent of **ه**.', ['Role'], R(
        ['accompaniment: مفعول معه غير صريح', 'cause: مفعول له غير صريح'],
        [('**ه** refers to the food (giving while loving it)', 'accompaniment: مفعول معه غير صريح'),
         ('**ه** refers to Allah (giving out of love for Him)', 'cause: مفعول له غير صريح')])),
    G('4R', 'In **جئت من عن يمينه**, identify each relation of جرّ.', ['Analysis'], R(
        ['حرف جرّ', 'اسم مبني في محل جرّ بمن، وهو مضاف', 'مضاف إليه مجرور، وهو مضاف', 'ضمير في محل جرّ مضاف إليه', 'حرف جرّ ثانٍ'],
        [('من', 'حرف جرّ'), ('عن', 'اسم مبني في محل جرّ بمن، وهو مضاف'), ('يمينِ', 'مضاف إليه مجرور، وهو مضاف'), ('الهاء', 'ضمير في محل جرّ مضاف إليه')])),
    M('4-Read', 'Read: **تكون عن اسمًا بمعنى جانب إذا سُبقت بمِن.** (**سُبقت** = was preceded.) Which example shows it?', [
        'جئت **من عن** يمينه', 'نهيت الطفل **عن** الشر', 'سألته **عن** الأمر', 'رحلت **عن** البلد'], 'جئت **من عن** يمينه',
        sol=SOLMD('“**عن** is a noun meaning **جانب**, “side”, when it is preceded by **من**.” In **من عن يمينه**, **عن** is a noun in محل جرّ بمن and is مضاف.')),
]

ITEMS['5'] = [
    G('5G-1', 'Classify the lām.', ['Meaning'], R(
        ['ملك (ownership)', 'تعليل (intended purpose)', 'تبليغ (the addressee)', 'عاقبة (unintended outcome)'],
        [('الكتاب لخالد', 'ملك (ownership)'), ('جئت للتعلم', 'تعليل (intended purpose)'), ('قلت له اجلس', 'تبليغ (the addressee)')])),
    G('5G-2', 'In **كتبت كالمعلم**:', ['Answer'], [
        ('Case of **المعلم**', [(['مجرور بالكاف بالكسرة', 'منصوب', 'مرفوع'], 'مجرور بالكاف بالكسرة')]),
        ('The phrase’s contribution', [(['resemblance in the manner of writing, attached to كتبت', 'the instrument of writing', 'the time of writing'],
                                       'resemblance in the manner of writing, attached to كتبت')])]),
    G('5G-3', 'In the outcome example:', ['Answer'], [
        ('Did they intend **عدوًّا وحزنًا**?', [(['No', 'Yes'], 'No')]),
        ('Name of the lām', [(['لام العاقبة / الصيرورة', 'لام التعليل', 'لام الملك'], 'لام العاقبة / الصيرورة')])]),
    G('5I-1', 'Complete with **في، لـ، كـ**.', ['Preposition'], R(
        ['في', 'لـ', 'كـ'], [('جلست … المسجد', 'في'), ('كتبت … المعلم', 'كـ'), ('جئت … التعلم', 'لـ')])),
    G('5I-2', '**أعرب:** **وهبت للطفل كتابا**', ['Analysis'], R(
        ['حرف جرّ أصليّ', 'اسم مجرور باللام بالكسرة', 'متعلق بوهبت: the recipient, مفعول به غير صريح', 'مفعول به منصوب: the gift', 'ضمير في محل رفع فاعل'],
        [('اللام', 'حرف جرّ أصليّ'), ('الطفلِ', 'اسم مجرور باللام بالكسرة'), ('للطفل', 'متعلق بوهبت: the recipient, مفعول به غير صريح'),
         ('كتابًا', 'مفعول به منصوب: the gift'), ('ـتُ', 'ضمير في محل رفع فاعل')])),
    M('5I-3', 'Correct: “A prepositional kāf freely takes the same attached pronouns as باء.”', [
        'Kāf takes an overt noun in this construction; bā’s pronoun permission does not transfer to it.',
        'The claim is correct: kāf and bā both take attached pronouns, as in **كهُ** and **بهِ**.',
        'Kāf takes only attached pronouns; an overt noun after it needs a second preposition.',
        'Kāf takes a pronoun only when it means comparison, and an overt noun otherwise.',
        ], 'Kāf takes an overt noun in this construction; bā’s pronoun permission does not transfer to it.'),
    G('5R', '**جئت إلى المسجد للتعلم. كتبت فيه بالقلم.**', ['Relationship'], R(
        ['destination', 'purpose', 'place of the writing', 'instrument'],
        [('إلى المسجد', 'destination'), ('للتعلم', 'purpose'), ('فيه', 'place of the writing'), ('بالقلم', 'instrument')]) + [
        ('Referent of **ه** in فيه', [(['المسجد', 'القلم', 'the speaker'], 'المسجد')])]),
    M('5-Read', 'Read: **لام التعليل لقصد الفاعل، وقد تكون اللام للعاقبة من غير قصد.** What does it say?', [
        'The lām of purpose expresses what the doer intends; a lām may also express an unintended outcome.',
        'Every lām expresses intended purpose, so even an outcome introduced by lām is always what the doer meant.',
        'The lām of outcome expresses the doer’s intention, while the lām of purpose expresses an unintended result.',
        'The lām never expresses purpose; it expresses only ownership or outcome.',
        ], 'The lām of purpose expresses what the doer intends; a lām may also express an unintended outcome.', sol=SOLMD('“The lām of reason is for the doer’s intention, and the lām may be for the outcome without intention.” **جئت للتعلم** is intended purpose; in the outcome example the result was not intended: **لام العاقبة**.')),
]

ITEMS['6'] = [
    M('6G-1', 'For the intended internal halfway point: **قمت الليل … نصفه**.', ['إلى', 'حتى'], 'إلى'),
    M('6G-2', 'Why does **حتى آخره** not violate the rule **اسم ظاهر**?', [
        'The noun directly governed by **حتى** is overt **آخر**; **ه** depends on it by إضافة.',
        '**حتى** can take any pronoun directly, so the rule does not apply to **آخره**.',
        '**آخره** is not genitive, so **حتى** is not governing it as a preposition.',
        '**حتى** is a conjunction here, so the overt-noun rule does not apply.',
        ], 'The noun directly governed by **حتى** is overt **آخر**; **ه** depends on it by إضافة.'),
    G('6G-3', '**سرنا حتى المسجد…**', ['Answer'], [
        ('Ending', [(['المسجدِ', 'المسجدَ', 'المسجدُ'], 'المسجدِ')]),
        ('Attachment', [(['متعلق بسرنا: the final limit of the journey', 'متعلق بمحذوف: خبر'], 'متعلق بسرنا: the final limit of the journey')])]),
    G('6I-1', 'Explain the difference.', ['Limit'], R(
        ['an internal stopping point', 'the final part of the named period'],
        [('قمت الليل إلى نصفه', 'an internal stopping point'), ('قمت الليل حتى آخره', 'the final part of the named period')])),
    M('6I-2', 'In **مات الناس حتى الأنبياءِ**, what kind of endpoint is intended?', [
        'an extreme of rank (غاية في الرتبة), not a place reached',
        'a physical destination reached by the action',
        'a point in time at which the action ended',
        'an internal halfway point within the group',
        ], 'an extreme of rank (غاية في الرتبة), not a place reached'),
    M('6R', 'Which statement about prepositional **حتى** is correct?', [
        'It takes an overt noun, and its limit must be the end of what precedes; **إلى** can take a pronoun.',
        'It is always interchangeable with **إلى**: both take attached pronouns and can mark any point along the way.',
        'It takes attached pronouns just like **إلى**, and its limit may be any internal point of what precedes.',
        'It takes an overt noun, and its limit must be an internal point, like **إلى نصفه**.',
        ], 'It takes an overt noun, and its limit must be the end of what precedes; **إلى** can take a pronoun.'),
    M('6-Read', 'Read: **لا يكون ما بعد حتى إلا آخرًا لما قبلها أو متّصلًا بآخره.** (**متّصل** = joined to.) Which sentence fits it?', [
        'قمت الليل حتى آخره', 'قمت الليل حتى نصفه', 'سرت حتاه', 'قمت حتى أوله'], 'قمت الليل حتى آخره',
        sol=SOLMD('“What follows **حتى** can only be the last part of what precedes it, or joined to its end.” So **حتى آخره** is correct, while an internal point uses **إلى نصفه**.')),
]

ITEMS['7'] = [
    G('7G-1', 'Match each oath particle to its complement restriction.', ['Restriction'], R(
        ['overt noun or pronoun', 'overt noun', 'الله in this construction'],
        [('باء القسم', 'overt noun or pronoun'), ('واو القسم', 'overt noun'), ('تاء القسم', 'الله in this construction')])),
    M('7G-2', 'Complete: **والعصرِ: جارّ ومجرور متعلّق بـ… تقديره …**', [
        'متعلّق بفعل قسم محذوف تقديره أقسم',
        'متعلّق بمحذوف خبر تقديره كائن',
        'متعلّق بفعل محذوف تقديره أكتب',
        'لا متعلّق له لأنه حرف زائد',
        ], 'متعلّق بفعل قسم محذوف تقديره أقسم'),
    M('7G-3', 'Why does the bā in **كتبت بالقلم** not express an oath?', [
        'Meaning and construction decide: it names the writing instrument and attaches to **كتبت**.',
        'Bā never introduces an oath at all; only wāw and tāʾ can introduce one, so this bā must be an instrument.',
        '**القلم** is accusative after the bā here, so the bā cannot be functioning as a preposition of oath.',
        'An oath with bā needs a مضارع such as **أقسم**, and **كتبت** is past.',
        ], 'Meaning and construction decide: it names the writing instrument and attaches to **كتبت**.'),
    G('7I-1', 'Correct each oath while keeping the oath meaning.', ['Correct form'], [
        ('أقسم والله', [(['أُقْسِمُ بِاللهِ', 'أُقْسِمُ وَاللهِ', 'أُقْسِمُ تَاللهِ'], 'أُقْسِمُ بِاللهِ')]),
        ('تالعصر', [(['وَالعَصْرِ', 'تَالعَصْرِ', 'أُقْسِمُ وَالعَصْرِ'], 'وَالعَصْرِ')])]),
    G('7I-2', '**أعرب:** **أقسم بالله**', ['Analysis'], R(
        ['فعل مضارع مرفوع بالضمة؛ فاعله مستتر تقديره أنا', 'حرف جرّ وقسم أصليّ', 'اسم مجرور بالباء بالكسرة', 'متعلق بأقسم', 'لا متعلق له'],
        [('أقسمُ', 'فعل مضارع مرفوع بالضمة؛ فاعله مستتر تقديره أنا'), ('الباء', 'حرف جرّ وقسم أصليّ'), ('اللهِ', 'اسم مجرور بالباء بالكسرة'), ('بالله', 'متعلق بأقسم')]) + [
        ('If the verb is omitted (**باللهِ**)', [(['the same governor **أقسم** is understood', 'the phrase has no governor'], 'the same governor **أقسم** is understood')])]),
    M('7R', 'Which accepts an attached pronoun as its direct complement?', ['بـ', 'كـ', 'حتى', 'واو القسم'], 'بـ'),
    M('7-Read', 'Read: **يجوز ذكر فعل القسم مع الباء وحذفه، ولا يُذكر مع الواو والتاء.** Which is correct?', [
        '**أقسم بالله** and **بالله** are both possible; **والله** and **تالله** go without the verb.',
        '**أقسم والله** and **والله** are both possible; **بالله** goes without the verb.',
        'The oath verb must always be expressed: **أقسم بالله**, **أقسم والله**, **أقسم تالله**.',
        'The oath verb is never expressed: only **بالله**, **والله** and **تالله**.',
        ], '**أقسم بالله** and **بالله** are both possible; **والله** and **تالله** go without the verb.', sol=SOLMD('“The oath verb may be expressed or omitted with bā, and it is not expressed with wāw and tāʾ.” So **أقسم بالله** and **بالله**, but only **والله** and **تالله**.')),
]

ITEMS['8'] = [
    M('8G-1', 'Choose (the intended period is today): **ما رأيته منذ اليوم…**', [
        'منذ اليومِ: جرّ is required for the present period',
        'منذ اليومُ: رفع is required for the present period',
        ], 'منذ اليومِ: جرّ is required for the present period'),
    M('8G-2', 'Which form is preferred for the elapsed past duration: **ما رأيته مذ يومانِ / يومينِ**?', [
        '**مذ يومانِ** is preferred; **مذ يومينِ** is allowed.',
        '**مذ يومينِ** is preferred; **مذ يومانِ** is impossible.',
        '**مذ يومينِ** is required; **مذ يومانِ** is a rare error.',
        '**مذ يومانِ** is required; **مذ يومينِ** is impossible.',
        ], '**مذ يومانِ** is preferred; **مذ يومينِ** is allowed.'),
    M('8G-3', 'What is the sign of جرّ in **منذ يومين**?', [
        'the yāʾ, because it is dual',
        'the kasrah on the nūn',
        'an estimated kasrah on the yāʾ',
        ], 'the yāʾ, because it is dual'),
    G('8I-1', '**ما رأيته منذ يوم الجمعة. نمت منذ نصف الليل.**', ['Ending'], R(
        ['يومِ / نصفِ: مجرور بمنذ، وهو مضاف', 'الجمعةِ / الليلِ: مضاف إليه مجرور', 'منصوب على الظرفية'],
        [('يوم… / نصف…', 'يومِ / نصفِ: مجرور بمنذ، وهو مضاف'), ('الجمعة… / الليل…', 'الجمعةِ / الليلِ: مضاف إليه مجرور')]) + [
        ('Why each action meets the condition', [(['the first is past and negated; the second is past, affirmative and extended', 'both are future actions'],
                                                  'the first is past and negated; the second is past, affirmative and extended')])]),
    G('8I-2', 'In **منذ علمت الغيبة محرمة**:', ['Analysis'], R(
        ['اسم مضاف; the following clause is in محل جرّ بالإضافة', 'حرف جرّ governing the first word', 'مفعول به أوّل منصوب', 'مفعول به ثانٍ منصوب'],
        [('منذ', 'اسم مضاف; the following clause is in محل جرّ بالإضافة'), ('الغيبةَ', 'مفعول به أوّل منصوب'), ('محرّمةً', 'مفعول به ثانٍ منصوب')])),
    M('8I-3', 'Correct: “Every noun after مذ is obligatorily genitive.”', [
        'جرّ is required for the present; for the past **مذ** favours رفع, as in **مذ يومان**.',
        'The claim is correct: every noun after **مذ** is genitive, present or past.',
        'رفع is required for the present; for the past **مذ** favours جرّ.',
        'Every noun after **مذ** is nominative, since **مذ** is always a noun.',
        ], 'جرّ is required for the present; for the past **مذ** favours رفع, as in **مذ يومان**.'),
    G('8R', 'Contrast the relationships.', ['Relationship', 'Noun governed directly'], [
        ('من أول الليل', [(['a beginning', 'an endpoint', 'an elapsed duration'], 'a beginning'), (['أوّل', 'آخر', 'يومين', 'الليل'], 'أوّل')]),
        ('إلى آخر الليل', [(['a beginning', 'an endpoint', 'an elapsed duration'], 'an endpoint'), (['أوّل', 'آخر', 'يومين', 'الليل'], 'آخر')]),
        ('منذ يومين', [(['a beginning', 'an endpoint', 'an elapsed duration'], 'an elapsed duration'), (['أوّل', 'آخر', 'يومين', 'الليل'], 'يومين')])]),
    M('8-Read', 'Read: **يجب الجرّ في الحاضر، ويترجّح بعد منذ في الماضي.** (**يترجّح** = is preferred.) What does it say?', [
        'جرّ is required for the present period and preferred after **منذ** for the past.',
        'جرّ is required for both the present period and the past after **منذ**.',
        'جرّ is preferred for the present period and required after **منذ** for the past.',
        'رفع is required for the present period and preferred after **منذ** for the past.',
        ], 'جرّ is required for the present period and preferred after **منذ** for the past.', sol=SOLMD('“جرّ is obligatory for the present, and preferred after **منذ** for the past.” **منذ اليومِ** must be genitive; **منذ يومِ الجمعةِ** is the preferred form. **يترجّح** does not mean obligatory.')),
]

ITEMS['9'] = [
    M('9G-1', 'Describe **رجلٍ** in **ربّ رجلٍ كريمٍ لقيته**.', [
        'مجرور لفظًا بربّ، مرفوع محلًّا على الابتداء',
        'مجرور لفظًا ومحلًّا بربّ، لا محل له',
        'مجرور لفظًا، منصوب محلًّا مفعول به للقيت',
        'مجرور لفظًا، مرفوع محلًّا فاعل للقيت',
        ], 'مجرور لفظًا بربّ، مرفوع محلًّا على الابتداء'),
    M('9G-2', 'Choose: **ربّ رجلٍ / الرجلِ كريمٍ لقيته**.', [
        'رُبَّ رَجُلٍ كَرِيمٍ لَقِيتُهُ: its complement must be indefinite',
        'رُبَّ الرَّجُلِ الكَرِيمِ لَقِيتُهُ: its complement must be definite',
        ], 'رُبَّ رَجُلٍ كَرِيمٍ لَقِيتُهُ: its complement must be indefinite'),
    M('9G-3', 'What does **ما الكافّة** change in **ربما يصوم زيد**?', [
        'It stops **ربّ** governing a genitive, so **ربما** can introduce a verbal clause.',
        'It makes **زيد** genitive after **ربما**, as the complement of **ربّ**.',
        'It turns **ربّ** into a negative particle, so the sentence is negated.',
        'It changes nothing: **ربّ** still governs, so **زيد** is genitive in position.',
        ], 'It stops **ربّ** governing a genitive, so **ربما** can introduce a verbal clause.'),
    G('9I-1', '**أعرب:** **رب طالب مجتهد لقيته** (the speaker has met many such students).', ['Analysis'], R(
        ['حرف جرّ شبيه بالزائد للتكثير، لا متعلّق له', 'مجرور لفظًا بربّ، مرفوع محلًّا مبتدأ', 'نعت مجرور بالكسرة', 'ضمير في محل نصب مفعول به، يعود على الطالب',
         'جملة فعلية في محل رفع خبر', 'حرف جرّ أصليّ متعلق بلقيت'],
        [('ربّ', 'حرف جرّ شبيه بالزائد للتكثير، لا متعلّق له'), ('طالبٍ', 'مجرور لفظًا بربّ، مرفوع محلًّا مبتدأ'), ('مجتهدٍ', 'نعت مجرور بالكسرة'),
         ('الهاء in لقيته', 'ضمير في محل نصب مفعول به، يعود على الطالب'), ('لقيته', 'جملة فعلية في محل رفع خبر')])),
    G('9I-2', 'Classify **من**.', ['Class and meaning'], R(
        ['أصلية: beginning in place, attached to the verb', 'شبيهة بالزائد: partitive, no separate attachment'],
        [('خرج من البيت', 'أصلية: beginning in place, attached to the verb'), ('عندي من ماء', 'شبيهة بالزائد: partitive, no separate attachment')])),
    M('9I-3', 'Explain **حاشا العالمِ**.', [
        '**العالمِ** is genitive by **حاشا** (exclusion); “like زائد” means no verb attachment, not no meaning.',
        '**العالمِ** is genitive by إضافة; **حاشا** is a noun meaning “apart”, so it has a meaning.',
        '**العالمِ** is genitive by **حاشا**, which is زائد and therefore adds no meaning.',
        '**العالمِ** is the subject of **حاشا**; its kasrah is for connected pronunciation.',
        ], '**العالمِ** is genitive by **حاشا** (exclusion); “like زائد” means no verb attachment, not no meaning.'),
    G('9R', 'Contrast the uses of **من**.', ['Meaning', 'Class'], [
        ('من للتعليل (من الخوف)', [(['reason', 'kind or substance', '“some of”'], 'reason'), (['أصلية', 'شبيهة بالزائد'], 'أصلية')]),
        ('من للبيان (من الدمع)', [(['reason', 'kind or substance', '“some of”'], 'kind or substance'), (['أصلية', 'شبيهة بالزائد'], 'أصلية')]),
        ('من للتبعيض (من ماء)', [(['reason', 'kind or substance', '“some of”'], '“some of”'), (['أصلية', 'شبيهة بالزائد'], 'شبيهة بالزائد')])]),
    M('9-Read', 'Read: **ربّ للتكثير أو التقليل، والقرينة تعيّن المراد.** (**تعيّن المراد** = determines what is intended.) What does it say?', [
        '**ربّ** expresses many or few; the context decides which.',
        '**ربّ** always expresses a small number, whatever the context.',
        '**ربّ** always expresses a large number, whatever the context.',
        '**ربّ** expresses certainty; the context decides the tense.',
        ], '**ربّ** expresses many or few; the context decides which.', sol=SOLMD('“**ربّ** is for multiplying or reducing, and the context determines what is intended.” **ربّ** does not always mean a small number.')),
]

ITEMS['10'] = [
    M('10G-1', 'Complete: **قائمٍ** in **ليس زيد بقائم** is **مجرور …، منصوب …، وهو … ليس**.', [
        'مجرور لفظًا، منصوب محلًّا، وهو خبر ليس',
        'مجرور محلًّا، منصوب لفظًا، وهو اسم ليس',
        'مجرور لفظًا، مرفوع محلًّا، وهو اسم ليس',
        'مجرور لفظًا، مرفوع محلًّا، وهو خبر ليس',
        ], 'مجرور لفظًا، منصوب محلًّا، وهو خبر ليس'),
    G('10G-2', 'Compare the two bā’s.', ['Bā', 'Instrument relationship?'], [
        ('كتب بالقلم', [(['أصليّ', 'زائد'], 'أصليّ'), (['Yes', 'No'], 'Yes')]),
        ('هل زيد بقائم', [(['أصليّ', 'زائد'], 'زائد'), (['Yes', 'No'], 'No')])]),
    M('10G-3', 'Why does **من** in **هل من مزيد** not need an expressed verb to attach to?', [
        'It is additional: it governs the genitive and widens the question, but forms no dependent phrase.',
        'A verb is always understood, **هل يوجد من مزيد**, so the prepositional phrase attaches to that omitted verb.',
        'It is original and partitive, so the phrase attaches to an omitted general predicate such as **موجود**.',
        '**من** is a noun meaning “some” here, so it needs no attachment.',
        ], 'It is additional: it governs the genitive and widens the question, but forms no dependent phrase.'),
    G('10I-1', 'Give full tarkīb: **ليس الضيف بنائم**, “The guest is not asleep.”', ['Analysis'], R(
        ['فعل ماضٍ ناقص جامد للنفي، مبني على الفتح', 'اسم ليس مرفوع بالضمة', 'حرف جرّ زائد', 'خبر ليس مجرور لفظًا بالباء، منصوب محلًّا', 'اسم مجرور متعلق بليس'],
        [('ليس', 'فعل ماضٍ ناقص جامد للنفي، مبني على الفتح'), ('الضيفُ', 'اسم ليس مرفوع بالضمة'), ('الباء', 'حرف جرّ زائد'), ('نائمٍ', 'خبر ليس مجرور لفظًا بالباء، منصوب محلًّا')])),
    G('10I-2', '**بيّن نوع مِن ومعناها.**', ['Class and meaning'], R(
        ['أصلية، لابتداء الغاية، متعلّقة بسرت', 'شبيهة بالزائد، للتبعيض، لا متعلّق لها', 'زائدة، لتأكيد العموم، لا متعلّق لها'],
        [('سرت من البيت', 'أصلية، لابتداء الغاية، متعلّقة بسرت'), ('عندي من ماء', 'شبيهة بالزائد، للتبعيض، لا متعلّق لها'), ('هل من مزيد؟', 'زائدة، لتأكيد العموم، لا متعلّق لها')])),
    M('10I-3', 'Correct: “If a particle is زائد, its presence has no effect on either meaning or noun ending.”', [
        'It adds emphasis and the genitive form; what it does not add is a place or instrument relationship.',
        'The claim is correct: an additional particle changes neither the meaning nor the ending.',
        'It changes the noun’s position from nominative to genitive, as well as its ending.',
        'It adds an instrument relationship, which is why the noun needs no other attachment.',
        ], 'It adds emphasis and the genitive form; what it does not add is a place or instrument relationship.'),
    G('10R', 'Give the class and the inner/outer analysis.', ['Class', 'Analysis'], [
        ('**قلمٍ** in كتبت بقلمٍ', [(CLASS, 'أصليّ'), (['genitive; the phrase is an instrument attached to the verb', 'genitive in form, nominative مبتدأ in position', 'genitive in form, accusative خبر ليس in position'], 'genitive; the phrase is an instrument attached to the verb')]),
        ('**رجلٍ** after ربّ', [(CLASS, 'شبيه بالزائد'), (['genitive; the phrase is an instrument attached to the verb', 'genitive in form, nominative مبتدأ in position', 'genitive in form, accusative خبر ليس in position'], 'genitive in form, nominative مبتدأ in position')]),
        ('**قائمٍ** in ليس زيد بقائمٍ', [(CLASS, 'زائد'), (['genitive; the phrase is an instrument attached to the verb', 'genitive in form, nominative مبتدأ in position', 'genitive in form, accusative خبر ليس in position'], 'genitive in form, accusative خبر ليس in position')])]),
    M('10-Read', 'Read: **الجرّ لفظيّ، والمحلّ بحسب وظيفة الاسم في الجملة.** (**بحسب** = according to.) Which example shows it?', [
        '**قائمٍ** in **ليس زيد بقائمٍ**: genitive in form, accusative as خبر ليس',
        '**القلمِ** in **كتبت بالقلم**: genitive in form, accusative as an object',
        '**البيتِ** in **إلى البيت**: genitive in form, accusative as a place',
        '**زيدٌ** in **ليس زيد بقائم**: nominative in form, genitive in position',
        ], '**قائمٍ** in **ليس زيد بقائمٍ**: genitive in form, accusative as خبر ليس', sol=SOLMD('“The جرّ is in the wording, and the position follows the noun’s function in the sentence.” After an additional preposition, **قائمٍ** is genitive in form but in an accusative position as خبر ليس.')),
]

ITEMS['11'] = [
    G('11G-1', 'Match each lām to its function.', ['Function'], R(
        ['strengthened negation', 'clarification', 'strengthened government'],
        [('الجحود', 'strengthened negation'), ('التبيين', 'clarification'), ('التقوية', 'strengthened government')])),
    G('11G-2', 'In **ليس كمثله شيء**:', ['Analysis'], R(
        ['اسم ليس مؤخّر مرفوع', 'مجرور لفظًا بالكاف الزائدة، منصوب محلًّا خبر ليس مقدّم', 'ضمير في محل جرّ مضاف إليه', 'فاعل مرفوع'],
        [('شيءٌ', 'اسم ليس مؤخّر مرفوع'), ('مثلِ', 'مجرور لفظًا بالكاف الزائدة، منصوب محلًّا خبر ليس مقدّم'), ('الهاء', 'ضمير في محل جرّ مضاف إليه')])),
    M('11G-3', 'Does the name **لام التبيين** by itself prove that the lām is additional?', [
        'No: it names a clarifying use; the lām in **ما أحبّني لرسول الله** is original.',
        'Yes: every clarifying lām is additional, because clarifying adds no new meaning.',
        'Yes: لام التبيين never takes an attachment, which is the mark of an additional lām.',
        'No: لام التبيين is always original, because it introduces the beloved.',
        ], 'No: it names a clarifying use; the lām in **ما أحبّني لرسول الله** is original.'),
    M('11I-1', 'In **إن كنتم للرؤيا تعبرون**, identify the lām.', [
        '**لام التقوية**: the complement precedes **تعبرون**, and the lām strengthens that link.',
        '**لام التعليل**: it gives the reason for interpreting, attached to **تعبرون**.',
        '**لام الملك**: the dream belongs to them, so the phrase is the خبر of **كنتم**.',
        '**لام الجحود**: it follows a negated **كان**, so **تعبرون** should be منصوب.',
        ], '**لام التقوية**: the complement precedes **تعبرون**, and the lām strengthens that link.'),
    G('11I-2', 'Compare the two kāfs.', ['Kāf', 'Separate attachment?'], [
        ('كتبت كالمعلم', [(['أصليّ', 'زائد'], 'أصليّ'), (['Yes: to كتبت', 'No'], 'Yes: to كتبت')]),
        ('ليس كمثله شيء', [(['أصليّ', 'زائد'], 'زائد'), (['Yes: to كتبت', 'No'], 'No')])]),
    M('11R', 'Why can the noun’s visible kasrah alone not distinguish **أصليّ، شبيه بالزائد، زائد**?', [
        'All three produce a genitive form; they differ in meaning, attachment and sentence function.',
        'Only an original preposition produces kasrah; the other two produce fatḥah.',
        'An additional preposition produces fatḥah, so a visible kasrah proves it is original.',
        'The kasrah is always estimated after these particles, so it cannot be seen at all.',
        ], 'All three produce a genitive form; they differ in meaning, attachment and sentence function.'),
    M('11-Read', 'Read: **لام التقوية لتأكيد العمل دون المعنى.** What does it say?', [
        'The strengthening lām reinforces government without adding a reason or destination.',
        'The strengthening lām adds a reason, reinforcing the meaning of the verb.',
        'The strengthening lām cancels the verb’s government over the fronted complement.',
        'The strengthening lām marks the destination, reinforcing the verb’s motion.',
        ], 'The strengthening lām reinforces government without adding a reason or destination.', sol=SOLMD('“The lām of strengthening is for reinforcing the government, not the meaning.” In **للرؤيا تعبرون** it strengthens the link to a governor that comes after its complement; it does not add a new reason or destination.')),
]

ITEMS['12'] = [
    G('12G-1', 'Match each term.', ['Meaning'], R(
        ['a regular construction', 'established usage', 'omission of a genitive governor', 'incorporation of another verb’s meaning'],
        [('قياسًا', 'a regular construction'), ('سماعًا', 'established usage'), ('نزع الخافض', 'omission of a genitive governor'), ('تضمين', 'incorporation of another verb’s meaning')])),
    G('12G-2', 'Contrast the endings and analyses.', ['ربّ is'], R(
        ['منصوب بنزع الخافض بالفتحة', 'مجرور بالباء بالكسرة'],
        [('كفروا ربَّهم', 'منصوب بنزع الخافض بالفتحة'), ('كفروا بربِّهم', 'مجرور بالباء بالكسرة')])),
    M('12G-3', 'Why is **اشهدوا أنّي بريء** not evidence that every noun inside the clause is accusative?', [
        '**أنّي بريءٌ** has its own government: the pronoun is اسم أنّ and **بريءٌ** خبر أنّ مرفوع.',
        '**بريءٌ** is genitive, because the whole clause stands after an omitted preposition.',
        'The clause has no position, so its words keep the endings of an ordinary sentence.',
        'It is evidence: once the bā is omitted, every noun in the clause becomes accusative.',
        ], '**أنّي بريءٌ** has its own government: the pronoun is اسم أنّ and **بريءٌ** خبر أنّ مرفوع.'),
    G('12I-1', 'Explain **إلى أموالكم**.', ['Explanation'], R(
        ['the verb **تأكلوا** incorporates **تضمّوا**, “add”, whose **إلى** it takes', '**إلى** stands with the meaning of **مع**'],
        [('تضمين', 'the verb **تأكلوا** incorporates **تضمّوا**, “add”, whose **إلى** it takes'), ('تناوب', '**إلى** stands with the meaning of **مع**')])),
    M('12I-2', 'Correct: “Once a preposition has been omitted in one expression, I can omit it after any verb with the same English translation.”', [
        'Omission has set environments and fixed exceptions; a similar translation does not license it.',
        'The claim is correct: omission follows the meaning, so the same translation allows it.',
        'Prepositions can never be omitted, so even the original expression is an error.',
        'Omission depends only on the verb’s form, so any verb of the same pattern allows it.',
        ], 'Omission has set environments and fixed exceptions; a similar translation does not license it.'),
    G('12I-3', 'In **يتوارى من القوم من سوء ما بشّر به**:', ['Relationship'], R(
        ['those from whom he hides', 'the cause of hiding'],
        [('من القوم', 'those from whom he hides'), ('من سوء ما بشّر به', 'the cause of hiding')])),
    G('12R', 'Contrast the two descriptions.', ['Example', 'Visible ending'], [
        ('مجرور لفظًا منصوب محلًّا', [(['قائمٍ in ليس زيد بقائمٍ', 'ربَّهم in كفروا ربَّهم'], 'قائمٍ in ليس زيد بقائمٍ'), (['kasrah', 'fatḥah'], 'kasrah')]),
        ('منصوب بنزع الخافض', [(['قائمٍ in ليس زيد بقائمٍ', 'ربَّهم in كفروا ربَّهم'], 'ربَّهم in كفروا ربَّهم'), (['kasrah', 'fatḥah'], 'fatḥah')])]),
    M('12-Read', 'Read: **قد يُضمَّن الفعل معنى فعل آخر، فيتعدّى بحرفه.** What does it say?', [
        'A verb may take on another verb’s meaning and then reach its complement through that verb’s preposition.',
        'A verb may drop its own preposition whenever some other verb with a similar meaning takes no preposition at all.',
        'A preposition may take on the meaning of a verb and then govern the noun after it in place of that verb.',
        'A verb may take on another verb’s subject and so govern two subjects.',
        ], 'A verb may take on another verb’s meaning and then reach its complement through that verb’s preposition.', sol=SOLMD('“A verb may be made to include the meaning of another verb, and so it reaches its complement through that verb’s preposition.” In **ولا تأكلوا أموالهم إلى أموالكم**, **تأكلوا** includes **تضمّوا**, whose preposition is **إلى**.')),
]

PHR = ['instrument', 'oath', 'additional emphasis', 'intended purpose', 'unintended outcome', 'ownership', 'beginning', 'final limit',
       'indefinite frequency', 'starting point', 'partitive meaning', 'reinforced negation', 'exhaustive scope in a question', 'place']

ITEMS['R'] = [
    G('A1', 'Choose the best explanation of each phrase.', ['Explanation'], [
        ('كتبت **بالقلم**', [(['instrument', 'oath', 'additional emphasis'], 'instrument')]),
        ('جئت **للتعلم**', [(['intended purpose', 'unintended outcome', 'ownership'], 'intended purpose')]),
        ('قمت الليل **حتى آخره**', [(['beginning', 'final limit', 'indefinite frequency'], 'final limit')]),
        ('عندي **من ماء**', [(['starting point', 'partitive meaning', 'reinforced negation'], 'partitive meaning')]),
        ('هل **من مزيد**', [(['partitive meaning', 'exhaustive scope in a question', 'place'], 'exhaustive scope in a question')])]),
    G('A2', 'Supply the required or preferred form.', ['Form', 'Strength'], [
        ('ما رأيته منذ اليومـ… (during today)', [(['اليومِ', 'اليومُ'], 'اليومِ'), (['obligatory', 'preferred'], 'obligatory')]),
        ('ما رأيته مذ يومـ… (for two days)', [(['يومانِ', 'يومينِ'], 'يومانِ'), (['obligatory', 'preferred'], 'preferred')]),
        ('ليس الطالب بمجتهد…', [(['بمجتهدٍ', 'بمجتهدًا'], 'بمجتهدٍ'), (['obligatory', 'preferred'], 'obligatory')]),
        ('رب طالب… مجتهد… لقيته', [(['طالبٍ مجتهدٍ', 'طالبًا مجتهدًا', 'طالبٌ مجتهدٌ'], 'طالبٍ مجتهدٍ'), (['obligatory', 'preferred'], 'obligatory')])]),
    M('B1-1', 'Correct: “**البيت** in **سرت إلى البيت** is منصوب because the phrase expresses مفعول فيه.”', [
        '**البيتِ** is genitive by **إلى**; the place relationship does not replace its case.',
        'The claim is correct: **البيتَ** is accusative because the phrase is a مفعول فيه.',
        '**البيتُ** is nominative, because the whole phrase is the خبر of the sentence.',
        '**البيت** has no case, because the phrase as a whole takes the position.',
        ], '**البيتِ** is genitive by **إلى**; the place relationship does not replace its case.', sol='B1'),
    M('B1-2', 'Correct: “**منذ** before a complete clause is a preposition governing its first word.”', [
        'Before a clause **منذ** is a noun (اسم مضاف); the clause is in محل جرّ.',
        'The claim is correct: **منذ** stays a preposition governing the first word.',
        'Before a clause **منذ** is a verb, and the clause is its فاعل.',
        'Before a clause **منذ** governs the last word of the clause in جرّ.',
        ], 'Before a clause **منذ** is a noun (اسم مضاف); the clause is in محل جرّ.', sol='B1'),
    M('B1-3', 'Correct: “**ربّ** always means a small number.”', [
        '**ربّ** can express many or few; the context decides.',
        'The claim is correct: **ربّ** always expresses a small number.',
        '**ربّ** always expresses a large number, not a small one.',
        '**ربّ** expresses no quantity; it only emphasises the noun.',
        ], '**ربّ** can express many or few; the context decides.', sol='B1'),
    M('B1-4', 'Correct: “**بـ** in **هل زيد بقائم** must attach to an omitted verb of writing.”', [
        'The bā is additional before the predicate; there is no writing meaning and no attachment.',
        'The claim is correct: an original bā must attach to an omitted verb of writing.',
        'The bā attaches to **هل**, which is treated as a verb of asking.',
        'The bā attaches to **زيد**, describing him as the instrument.',
        ], 'The bā is additional before the predicate; there is no writing meaning and no attachment.', sol='B1'),
    M('B1-5', 'Correct: “**حتى نصفه** freely replaces **إلى نصفه** when half is an internal point of the stated whole.”', [
        'Use **إلى نصفه**: **حتى** needs the end part or something joined to the end.',
        'The claim is correct: **حتى** and **إلى** are interchangeable for any limit.',
        'Use **من نصفه**: the halfway point is a starting point, not a limit.',
        'Use **في نصفه**: the halfway point is a location, not a limit.',
        ], 'Use **إلى نصفه**: **حتى** needs the end part or something joined to the end.', sol='B1'),
    G('C1', '**خَرَجَ خَالِدٌ مِنَ البَيْتِ. سَارَ إِلَى المَسْجِدِ. جَلَسَ فِيهِ لِلتَّعَلُّمِ. كَتَبَ بِالقَلَمِ. عَادَ إِلَى البَيْتِ بِاللَّيْلِ.** Give each phrase’s meaning and attachment.', ['Meaning', 'Attachment'], [
        ('من البيت', [(['starting point in place', 'endpoint in place', 'location', 'intended purpose', 'instrument', 'time'], 'starting point in place'), (['خرج', 'سار', 'جلس', 'كتب', 'عاد'], 'خرج')]),
        ('إلى المسجد', [(['starting point in place', 'endpoint in place', 'location', 'intended purpose', 'instrument', 'time'], 'endpoint in place'), (['خرج', 'سار', 'جلس', 'كتب', 'عاد'], 'سار')]),
        ('فيه', [(['starting point in place', 'endpoint in place', 'location', 'intended purpose', 'instrument', 'time'], 'location'), (['خرج', 'سار', 'جلس', 'كتب', 'عاد'], 'جلس')]),
        ('للتعلم', [(['starting point in place', 'endpoint in place', 'location', 'intended purpose', 'instrument', 'time'], 'intended purpose'), (['خرج', 'سار', 'جلس', 'كتب', 'عاد'], 'جلس')]),
        ('بالقلم', [(['starting point in place', 'endpoint in place', 'location', 'intended purpose', 'instrument', 'time'], 'instrument'), (['خرج', 'سار', 'جلس', 'كتب', 'عاد'], 'كتب')]),
        ('بالليل', [(['starting point in place', 'endpoint in place', 'location', 'intended purpose', 'instrument', 'time'], 'time'), (['خرج', 'سار', 'جلس', 'كتب', 'عاد'], 'عاد')])]),
    G('C1-b', 'Passage 1: **جلس فيه للتعلم**', ['Analysis'], R(
        ['ضمير مستتر تقديره هو في محل رفع فاعل، يعود إلى خالد', 'ضمير متصل مبني على الكسر في محل جرّ بفي، يعود إلى المسجد', 'اسم مجرور باللام بالكسرة',
         'ضمير في محل نصب مفعول به'],
        [('Subject of جلس', 'ضمير مستتر تقديره هو في محل رفع فاعل، يعود إلى خالد'), ('الهاء in فيه', 'ضمير متصل مبني على الكسر في محل جرّ بفي، يعود إلى المسجد'),
         ('التعلّمِ', 'اسم مجرور باللام بالكسرة')]), sol='C1'),
    G('C2', '**مَا رَأَيْتُ الضَّيْفَ مُنْذُ يَوْمِ الجُمُعَةِ. هَلْ هُوَ بِمَرِيضٍ؟ لَيْسَ الضَّيْفُ بِمَرِيضٍ. رُبَّ رَجُلٍ كَرِيمٍ لَقِيتُهُ، وَالضَّيْفُ كَرِيمٌ.**', ['Analysis'], R(
        ['مفعول به منصوب', 'خبر مجرور لفظًا، مرفوع محلًّا', 'خبر ليس مجرور لفظًا، منصوب محلًّا', 'مبتدأ مجرور لفظًا بربّ، مرفوع محلًّا',
         'ضمير في محل نصب مفعول به، يعود إلى رجل', 'مبتدأ مرفوع بالضمة', 'خبر مرفوع بالضمة'],
        [('الضيفَ (first sentence)', 'مفعول به منصوب'), ('مريضٍ in هل هو بمريض', 'خبر مجرور لفظًا، مرفوع محلًّا'), ('مريضٍ in ليس الضيف بمريض', 'خبر ليس مجرور لفظًا، منصوب محلًّا'),
         ('رجلٍ', 'مبتدأ مجرور لفظًا بربّ، مرفوع محلًّا'), ('الهاء in لقيته', 'ضمير في محل نصب مفعول به، يعود إلى رجل'), ('الضيفُ (last)', 'مبتدأ مرفوع بالضمة'), ('كريمٌ (last)', 'خبر مرفوع بالضمة')])),
    G('D', 'Match each statement to its example.', ['Example'], R(
        ['كتبت كالمعلمِ', 'ليس زيد بقائمٍ', 'عندي من ماءٍ', 'منذ اليومِ / منذ يومِ الجمعةِ', 'كتبت بالقلم / سافرت بالليل'],
        [('لا يكون مجرور كاف التشبيه إلا اسمًا ظاهرًا.', 'كتبت كالمعلمِ'), ('الجارّ الزائد لا يحتاج إلى متعلَّق.', 'ليس زيد بقائمٍ'),
         ('مِن التبعيضيّة تفيد معنى خاصًّا.', 'عندي من ماءٍ'), ('يكون الجرّ بعد منذ واجبًا في الحاضر، راجحًا في الماضي.', 'منذ اليومِ / منذ يومِ الجمعةِ'),
         ('تختلف وظيفة شبه الجملة باختلاف المعنى والقرينة.', 'كتبت بالقلم / سافرت بالليل')])),
    G('E1-1', '**كتب الضيف بقلم المعلم**', ['Analysis'], R(
        ['فاعل مرفوع بالضمة', 'حرف جرّ أصليّ للاستعانة', 'اسم مجرور بالباء، وهو مضاف', 'مضاف إليه مجرور', 'متعلق بكتب، بمعنى الآلة'],
        [('الضيفُ', 'فاعل مرفوع بالضمة'), ('الباء', 'حرف جرّ أصليّ للاستعانة'), ('قلمِ', 'اسم مجرور بالباء، وهو مضاف'), ('المعلمِ', 'مضاف إليه مجرور'),
         ('بقلم المعلم', 'متعلق بكتب، بمعنى الآلة')])),
    G('E1-2', '**سرت من المسجد إلى السوق**', ['Analysis'], R(
        ['ضمير متصل في محل رفع فاعل', 'حرف جرّ أصليّ لابتداء الغاية', 'حرف جرّ أصليّ لانتهاء الغاية', 'اسم مجرور بالكسرة', 'متعلق بسرت'],
        [('ـتُ', 'ضمير متصل في محل رفع فاعل'), ('من', 'حرف جرّ أصليّ لابتداء الغاية'), ('إلى', 'حرف جرّ أصليّ لانتهاء الغاية'),
         ('المسجدِ / السوقِ', 'اسم مجرور بالكسرة'), ('Both phrases', 'متعلق بسرت')])),
    G('E1-3', '**ليس الرجل بقائم**', ['Analysis'], R(
        ['فعل ماضٍ ناقص جامد للنفي', 'اسم ليس مرفوع بالضمة', 'حرف جرّ زائد للتأكيد، لا متعلّق له', 'خبر ليس مجرور لفظًا بالباء، منصوب محلًّا'],
        [('ليس', 'فعل ماضٍ ناقص جامد للنفي'), ('الرجلُ', 'اسم ليس مرفوع بالضمة'), ('الباء', 'حرف جرّ زائد للتأكيد، لا متعلّق له'), ('قائمٍ', 'خبر ليس مجرور لفظًا بالباء، منصوب محلًّا')])),
    G('E1-4', '**رب ضيف كريم لقيته**', ['Analysis'], R(
        ['حرف جرّ شبيه بالزائد، لا متعلّق له', 'مبتدأ مجرور لفظًا بربّ، مرفوع محلًّا', 'نعت مجرور بالكسرة', 'ضمير في محل نصب مفعول به، يعود إلى الضيف', 'جملة فعلية في محل رفع خبر'],
        [('ربّ', 'حرف جرّ شبيه بالزائد، لا متعلّق له'), ('ضيفٍ', 'مبتدأ مجرور لفظًا بربّ، مرفوع محلًّا'), ('كريمٍ', 'نعت مجرور بالكسرة'),
         ('الهاء', 'ضمير في محل نصب مفعول به، يعود إلى الضيف'), ('لقيته', 'جملة فعلية في محل رفع خبر')])),
    G('E1-5', '**ما رأيته منذ يومين**', ['Analysis'], R(
        ['حرف نفي، لا محل له', 'ضمير في محل نصب مفعول به', 'حرف جرّ أصليّ', 'اسم مجرور بمنذ، وعلامة جرّه الياء لأنه مثنّى', 'متعلق برأيت، مفعول فيه غير صريح للزمان'],
        [('ما', 'حرف نفي، لا محل له'), ('الهاء', 'ضمير في محل نصب مفعول به'), ('منذ', 'حرف جرّ أصليّ'), ('يومينِ', 'اسم مجرور بمنذ، وعلامة جرّه الياء لأنه مثنّى'),
         ('منذ يومين', 'متعلق برأيت، مفعول فيه غير صريح للزمان')])),
    G('E2', 'Compare **كَتَبْتُ بِالقَلَمِ** and **لَيْسَ الطِّفْلُ بِنَائِمٍ**.', ['Bā', 'Noun’s role', 'Attachment'], [
        ('كتبت بالقلم', [(['أصليّ', 'زائد'], 'أصليّ'), (['genitive; the phrase is an instrument', 'genitive in form, accusative خبر ليس in position'], 'genitive; the phrase is an instrument'),
                         (['attached to كتبت', 'none'], 'attached to كتبت')]),
        ('ليس الطفل بنائم', [(['أصليّ', 'زائد'], 'زائد'), (['genitive; the phrase is an instrument', 'genitive in form, accusative خبر ليس in position'], 'genitive in form, accusative خبر ليس in position'),
                             (['attached to كتبت', 'none'], 'none')])]),
]
