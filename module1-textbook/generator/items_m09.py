"""Module 9 questions. One correct choice per control; explanations export to Markdown."""
from item_kit import M, G

SOLUTIONS = {}


def Q(key, prompt, correct, wrong1, wrong2, why):
    SOLUTIONS[key] = why
    return M(key, prompt, [correct, wrong1, wrong2], correct)


def T(key, prompt, rows, why):
    SOLUTIONS[key] = why
    return G(key, prompt, ['التحليل'], [
        (label, [([correct, wrong1, wrong2], correct)])
        for label, correct, wrong1, wrong2 in rows
    ])


ITEMS = {
 '1': [
    T('1G-1', 'Match the عامل معنوي to its عمل. Use الابتداء for both المبتدأ والخبر.', [
        ('الابتداء', 'رفع المبتدأ والخبر', 'نصب الحال', 'جزم المضارع'),
        ('خلوّ المضارع عن ناصب وجازم', 'رفع المضارع', 'نصب المضارع', 'جرّ الاسم'),
        ('معنى الفعل في الاسم أو الحرف', 'نصب الحال', 'رفع كل اسم بعده', 'جزم فعلين')
    ], 'الابتداء يرفع المبتدأ والخبر under the selected account. خلوّ المضارع عن ناصب وجازم explains رفع المضارع. معنى الفعل can govern نصب الحال; it does not give every following word the same ending.'),
    T('1G-2', 'Complete the تركيب of **تلك بيوتهم خاويةً**.', [
        ('تلك', 'اسم إشارة في محل رفع مبتدأ', 'فعل محذوف', 'حرف جرّ'),
        ('بيوتهم', 'بيوتُ خبر مرفوع ومضاف؛ هم مضاف إليه', 'بيوتَ مفعول به؛ هم فاعل', 'بيوتِ مجرور بتلك'),
        ('خاويةً', 'حال منصوب، عامله معنى الإشارة', 'خبر مرفوع بفتحة', 'مضاف إليه لبيوت')
    ], '**تلك** اسم إشارة مبني في محل رفع مبتدأ. **بيوتُ** خبر مرفوع ومضاف؛ **هم** في محل جر مضاف إليه. **خاويةً** حال منصوب يبيّن حالة البيوت، وعامله معنى أُشير في اسم الإشارة. بيوتهم already supplies the خبر.'),
    T('1I-1', 'Supply the endings and reasons in **يقرأ سعيد. سعيد معلم**.', [
        ('يقرأ', 'يقرأُ: مضارع مرفوع لخلوّه من ناصب وجازم', 'يقرأْ: مجزوم بلم محذوفة', 'يقرأَ: منصوب لأن سعيد بعده'),
        ('سعيد after يقرأ', 'سعيدٌ: فاعل مرفوع بالفعل', 'سعيدًا: مفعول به', 'سعيدٍ: مضاف إليه'),
        ('سعيد معلم', 'سعيدٌ مبتدأ ومعلمٌ خبر؛ رفعهما بالابتداء في التحليل المختار', 'سعيدًا ومعلمًا مفعولان', 'سعيدٌ فاعل لمعلمٍ المجرور')
    ], '**يقرأُ سعيدٌ. سعيدٌ معلّمٌ.** يقرأُ is مرفوع because there is no ناصب or جازم; سعيدٌ in the first جملة is فاعل of يقرأ. In the second, سعيدٌ is مبتدأ and معلّمٌ خبر; الابتداء explains both رفع endings under the specified account.'),
    Q('1I-2', 'Correct: “In **كأنّ خالدًا مقبلًا أسدٌ**, مقبلًا is another اسم كأنّ.”',
      'مقبلًا is حال governed by معنى التشبيه; خالدًا is اسم كأنّ and أسدٌ خبرها.',
      'Correct: every منصوب after كأنّ is اسمها.',
      'مقبلًا must be مضاف إليه because it follows خالد.',
      '**خالدًا** اسم كأنّ منصوب؛ **أسدٌ** خبر كأنّ مرفوع؛ **مقبلًا** حال منصوب from خالد, governed by معنى أُشبّه. Its نصب alone does not make it اسم كأنّ.'),
    Q('1R', 'Compare **خالدٌ معلّمٌ** and **إنّ خالدًا معلّمٌ**. What changes?',
      'The first uses الابتداء; the second has إنّ as عامل لفظي in اسمها وخبرها.',
      'Both require a محذوف إنّ before خالد.',
      'معلّم becomes مجرور in the second because إنّ only permits one مرفوع.',
      'In **خالدٌ معلّمٌ**, use الابتداء. In **إنّ خالدًا معلّمٌ**, إنّ is an expressed عامل لفظي: خالدًا اسمها منصوب and معلّمٌ خبرها مرفوع. Do not invent an omitted إنّ in the first.'),
    Q('1-Read', '**يرتفع المضارع لخلوّه من الناصب والجازم.** Which analysis follows this?',
      'أكتبُ is مرفوع when no ناصب or جازم governs it.',
      'Every أكتب must be preceded by a محذوف لم.',
      'A missing ناصب makes أكتب منصوبًا.',
      '**خلوّ** means absence. In the stated setting, أكتبُ is مضارع مرفوع. No omitted ناصب or جازم is being posited.')
 ],
 '2': [
    T('2G-1', 'Identify the relationships in **كتبتُ وقرأتُ الرسالةَ**, using إعمال الثاني.', [
        ('العاملان', 'كتبتُ وقرأتُ', 'الرسالة والتاء', 'الواو والرسالة'),
        ('المعمول المتأخّر', 'الرسالةَ', 'التاء في كتبتُ', 'الواو'),
        ('عامل الرسالةَ المختار', 'قرأتُ', 'كتبتُ وحده مع إعمال الأول', 'الابتداء')
    ], 'كتبتُ and قرأتُ both seek الرسالة in meaning. The expressed معمول follows them. With **إعمال الثاني**, الرسالةَ is مفعول به لقرأت؛ its relation to writing remains understood. This choice does not deny that إعمال الأول is another permitted account.'),
    Q('2G-2', '**ماذا قرأتَ؟ — كتابًا.** Choose the تقدير and role.',
      'قرأتُ كتابًا؛ كتابًا مفعول به لفعل محذوف جوازًا.',
      'هذا كتابٌ؛ كتابًا مبتدأ منصوب.',
      'يا كتابُ؛ كتابًا منادى مبني على الضم.',
      'The question asks what was read, so the matching تقدير is **قرأتُ كتابًا**. كتابًا retains نصب المفعول به. The question is قرينة السياق, making the حذف جائزًا.'),
    Q('2I-1', 'In **أقريبٌ أم بعيدٌ ما تُوعَدون؟**, what shows that التنازع is not confined to أفعال?',
      'قريب and بعيد are اسمان عاملان seeking the following expression.',
      'قريب and بعيد are both أحرف جرّ.',
      'ما must be a third فعل.',
      'The two أسماء عاملة قريب and بعيد seek **ما توعدون**. التنازع may involve أسماء as well as أفعال, and more than two عوامل can occur in the broader pattern.'),
    T('2I-2', 'Read **ماذا كتبتَ؟ قال خالد: رسالةً.** Analyse the final answer.', [
        ('رسالة', 'رسالةً: مفعول به منصوب بالفتحة', 'رسالةٌ: فاعل لقال', 'رسالةٍ: مضاف إليه لخالد'),
        ('تقدير العامل', 'كتبتُ', 'لم أكتبْ', 'يا'),
        ('قرينة الحذف', 'The preceding question about writing', 'The mere presence of تنوين', 'The fact that every answer omits a فعل وجوبًا')
    ], '**رسالةً** answers ماذا كتبتَ, so its عامل is **كتبتُ** understood جوازًا. It is not فاعل لقال: خالدٌ already fills that role. The exact context, not تنوين alone, identifies the omitted action.'),
    Q('2R', 'Which distinction between عامل معنوي and عامل محذوف is accurate?',
      'الابتداء is a relationship; كتبتُ in the answer رسالةً is an unspoken فعل recovered from context.',
      'Both are always omitted forms of كان.',
      'Neither can explain an ending unless printed in the sentence.',
      'An عامل معنوي need not be reconstructed as a separate word. A محذوف عامل has a suitable تقدير grounded in evidence. **الابتداء** and **كتبتُ** are therefore different explanations.'),
    Q('2-Read', '**يجوز إعمال الأول أو الثاني في التنازع.** What must an exercise asking for one selected عامل make clear?',
      'Whether it is using إعمال الأول or إعمال الثاني.',
      'That إعمال الأول is always forbidden.',
      'That both must independently assign different endings to the same word.',
      'Both selections are permissible. A specified choice makes the requested تركيب unambiguous; shared meaning alone does not identify one required عامل.')
 ],
 '3': [
    T('3G-1', 'Match each example to its قياسيّ condition.', [
        ('صبرًا لا جزعًا: لا جزعًا', 'نهي تابع لمصدر يراد به الأمر', 'نداء عَلَم', 'اختصاص بعد ضمير'),
        ('أجرأةً على المعاصي؟', 'استفهام للتوبيخ', 'استغاثة', 'إضافة لفظية'),
        ('فإمّا منًّا بعدُ وإمّا فداءً', 'تفصيل بعد إمّا لمجمل سابق', 'تنوين عوض عن جملة', 'ترخيم'),
        ('أولئك هم المؤمنون حقًّا', 'تأكيد مضمون الجملة', 'مفعول به لاسم فاعل', 'حال سدّت مسدّ الخبر')
    ], 'The four conditions are **نهي تابع لمصدر يراد به الأمر؛ استفهام للتوبيخ؛ تفصيل بعد إمّا؛ تأكيد مضمون الجملة**. The relevant مصدر is مفعول مطلق with عامل محذوف وجوبًا. إمّا itself is not a ناصب.'),
    T('3G-2', 'Analyse **سبحانَ اللهِ**.', [
        ('سبحانَ', 'مفعول مطلق منصوب، وهو مضاف', 'منادى مبني على الضم', 'فاعل مرفوع'),
        ('العامل', 'فعل محذوف وجوبًا بمعنى أسبّح', 'لفظ الجلالة عامل في سبحان', 'حرف جرّ ظاهر'),
        ('اللهِ', 'مضاف إليه مجرور', 'مفعول به منصوب', 'نائب فاعل')
    ], '**سبحانَ** مفعول مطلق منصوب بالفتحة لفعل محذوف وجوبًا، وهو مضاف. **اللهِ** مضاف إليه مجرور بالكسرة. The construction is سماعيّ; its two endings come from different relationships.'),
    Q('3I-1', 'Correct: “لبّيك means exactly two responses, because it has a صيغة مثنّى.”',
      'Its established صيغة مثنّى conveys التكثير, not a literal count of two.',
      'Correct: every صيغة مثنّى must count exactly two actions.',
      'لبّيك is a فعل مضارع مجزوم بحذف النون.',
      '**لبّيك** and its related established مصادر use صيغة مثنّى للتكثير. Here ياء is علامة نصب and نون is removed للإضافة; ك is مضاف إليه. It is not a مضارع.'),
    T('3I-2', 'Supply the roles in **معاذ الله. عجبا لك**.', [
        ('معاذ', 'معاذَ: مفعول مطلق ومضاف', 'معاذُ: خبر مرفوع', 'معاذِ: مجرور بلا عامل'),
        ('الله', 'اللهِ: مضاف إليه', 'اللهَ: مفعول مطلق', 'اللهُ: فاعل لمعاذ'),
        ('عجبا', 'عجبًا: مفعول مطلق بعامل محذوف', 'عجبٌ: منادى', 'عجبٍ: مضاف إليه للكاف'),
        ('لك', 'اللام حرف جرّ؛ الكاف في محل جر', 'اللام حرف نصب؛ الكاف فاعل', 'ك اسم ظاهر منصوب')
    ], '**معاذَ اللهِ** uses مفعول مطلق with a محذوف عامل conveying seeking protection; معاذَ is مضاف and اللهِ مضاف إليه. **عجبًا لك** likewise uses a مصدر with a محذوف عامل; اللام in لك is حرف جرّ and ك في محل جر. These are سماعيّ expressions.'),
    Q('3R', 'Compare **كتبتُ رسالةً** and **سبحانَ اللهِ**. Why is matching فتحة insufficient?',
      'رسالةً is مفعول به; سبحانَ is مفعول مطلق with عامل محذوف.',
      'Both must be مفعول مطلق because they are منصوب.',
      'Both must be مضاف إليه because something follows them.',
      'رسالة names what was written and is مفعول به. سبحان expresses the action through a مصدر and is مفعول مطلق. Both have نصب; their roles and عوامل differ.'),
    Q('3-Read', '**قد يحذف عامل المفعول المطلق وجوبًا، قياسًا أو سماعًا.** Choose the correct application.',
      'أجرأةً على المعاصي؟ meets a قياسيّ condition; سبحان الله is a سماعيّ expression.',
      'كل مصدر منصوب has an omitted عامل وجوبًا.',
      'سماعيّ permits inventing any new expression with the same apparent ending.',
      'استفهام للتوبيخ supplies the قياسيّ condition in أجرأةً. سبحان الله is learned as an established سماعيّ expression. Neither account justifies universal deletion for all مصادر.')
 ],
 '4': [
    T('4G-1', 'A teacher warns a student against envy. Match the أركان.', [
        ('المُحذِّر', 'The teacher speaking', 'The student addressed', 'Envy'),
        ('المُحذَّر', 'The student addressed', 'The teacher speaking', 'Envy'),
        ('المُحذَّر منه', 'Envy', 'The teacher speaking', 'The student addressed'),
        ('فعل التحذير المقدّر', 'احذرْ or a suitable equivalent', 'ابتداء', 'حرف النداء')
    ], '**المحذِّر** gives the warning; **المحذَّر** receives it; **المحذَّر منه** is what should be avoided. The understood فعل such as احذرْ supplies the action. Speaker and addressee are not interchangeable.'),
    T('4G-2', 'Compare the two forms.', [
        ('الحسدَ الحسدَ: first word', 'مفعول به لفعل محذوف تقديره احذر', 'مبتدأ مرفوع', 'تمييز لعدد'),
        ('الحسدَ الحسدَ: second word', 'توكيد لفظي منصوب', 'فاعل لفعل جديد', 'حرف جرّ'),
        ('إيّاك من الحسدِ: الحسد', 'مجرور بمن', 'منصوب بإيّاك', 'مرفوع بالابتداء')
    ], 'In **الحسدَ الحسدَ**, the first is مفعول به لفعل محذوف وجوبًا and the second توكيد لفظي منصوب. In **إيّاك من الحسدِ**, the expressed من gives جرّ to الحسد. The meaning of warning does not force every word into نصب.'),
    T('4I-1', 'أعرب **إياك من المراء**. المراء = contentious disputing.', [
        ('إيّاك', 'ضمير منفصل في محل نصب في التحذير', 'حرف جرّ', 'مبتدأ مرفوع'),
        ('من', 'حرف جرّ', 'اسم شرط', 'فعل أمر'),
        ('المراء', 'المراءِ: اسم مجرور بمن، وهو المحذّر منه', 'المراءَ: منصوب مع وجود من', 'المراءُ: فاعل ظاهر')
    ], '**إيّاك** is a ضمير منفصل في محل نصب, with a محذوف عامل conveying the warning. **من** حرف جرّ; **المراءِ** اسم مجرور بالكسرة، وهو المحذَّر منه. Separate the semantic role المحذَّر منه from its جرّ in this particular form.'),
    Q('4I-2', '**إيّاك أن تحسدَ**: which analysis preserves the two relationships?',
      'أن makes تحسدَ منصوبًا; مِن is understood before the مصدر المؤوّل.',
      'إيّاك is a ناصب للمضارع and أن is a فاعل.',
      'تحسد must become مجزومًا because the meaning is a warning.',
      '**أن** حرف مصدري ونصب؛ **تحسدَ** مضارع منصوب بالفتحة، فاعله مستتر أنت. أن تحسد forms a مصدر مؤوّل before which من is understood in this warning pattern. A warning meaning is not itself a جازم.'),
    Q('4R', 'Correct: “Any sentence giving a warning must have its فعل omitted.”',
      'The shortened constructions use حذف, but warning can also use an expressed فعل such as قُوا.',
      'Correct: قُوا cannot express warning because it is written.',
      'Warning always requires an اسم شرط.',
      'The meaning التحذير also occurs with an expressed فعل: **قوا أنفسكم وأهليكم نارًا**. Distinguish the shortened construction being analysed from every sentence whose purpose is to warn.'),
    Q('4-Read', '**المحذَّر منه ما يحذّر المتكلّم المخاطَب منه.** In **إيّاك والحسدَ**, using the عطف analysis, identify الحسد.',
      'المحذَّر منه؛ معطوف منصوب',
      'المحذِّر؛ فاعل مرفوع',
      'المحذَّر؛ ضمير منفصل',
      '**الحسد** is what the addressee should avoid: المحذَّر منه. With the specified عطف analysis, الحسدَ is معطوف منصوب, while إيّاك names the person addressed through a ضمير.')
 ],
 '5': [
    T('5G-1', 'Distinguish purpose and حذف.', [
        ('الصبرَ الصبرَ', 'إغراء؛ حذف العامل واجب للتكرار', 'تحذير من الصبر', 'نداء نكرة مقصودة'),
        ('العلمَ والحلمَ', 'إغراء؛ حذف العامل واجب مع العطف', 'كلاهما مرفوع بالابتداء', 'إضافة معنوية'),
        ('المُغرَى به', 'The desirable quality or action urged', 'The speaker', 'The person addressed')
    ], 'الصبرَ الصبرَ urges patience and contains تكرار. العلمَ والحلمَ urges two desirable qualities with عطف. Both have عامل محذوف وجوبًا. The **مُغري** speaks, the **مُغرَى** is addressed, and the **مُغرَى به** is what is urged.'),
    T('5G-2', 'Analyse **نحن الطلابَ نطلبُ العلمَ** as اختصاص.', [
        ('نحن', 'ضمير في محل رفع مبتدأ', 'حرف نداء', 'مفعول به'),
        ('الطلابَ', 'مفعول به لفعل محذوف تقديره أخصّ، على الاختصاص', 'خبر نحن منصوب', 'منادى مع يا مكتوبة'),
        ('نطلب العلم', 'جملة في محل رفع خبر', 'جملة في محل جر مضاف إليه', 'توكيد لفظي للطلاب')
    ], 'نحن is مبتدأ. الطلابَ specifies that ضمير through اختصاص, with عامل محذوف وجوبًا تقديره أخصّ. نطلبُ مضارع مرفوع فاعله مستتر نحن؛ العلمَ مفعول به. جملة نطلب العلم supplies the خبر.'),
    Q('5I-1', 'A speaker includes himself: **نحن المعلمينَ نعلّمُ الصغارَ**. Choose the analysis of المعلمين.',
      'اختصاص؛ مفعول به منصوب بالياء لأنه جمع مذكر سالم، بعامل محذوف.',
      'منادى مبني على الواو لأن يا موجودة.',
      'خبر مرفوع بالياء.',
      '**المعلّمينَ** identifies the group meant by نحن: اختصاص, with تقدير أخصّ or أعني. It is منصوب بالياء لأنه جمع مذكر سالم. The speaker is not summoning the teachers; جملة نعلّم الصغار is the خبر. **الصغار** = children.'),
    T('5I-2', 'Choose the correction or تقدير.', [
        ('“Single الصبرَ! meets the repetition condition.”', 'It is unrepeated; that condition is absent.', 'Every إغراء is repeated even when written once.', 'الصبر must be a فعل.'),
        ('مرحبًا، أهلًا وسهلًا: تقدير used here', 'أصبتَ', 'أدعو', 'لم تكتبْ'),
        ('امرأً ونفسَه: تقدير used here', 'دَعْ', 'أخصّ نحن', 'إنّ'),
        ('نحن أيّها الطلاب نطلب العلم', 'اختصاص without يا', 'استغاثة with لام مفتوحة', 'ندبة with وا')
    ], 'A single الصبرَ does not satisfy تكرار or عطف merely by being إغراء. The established greetings use تقدير أصبتَ here; امرأً ونفسه uses دعْ. أيّها can introduce اختصاص without يا: أيّ مبني على الضم في محل نصب، ها للتنبيه، والطلاب وصف مرفوع.'),
    Q('5R', 'Compare **الحسدَ الحسدَ** and **الصبرَ الصبرَ**.',
      'Both begin with مفعول به لفعل محذوف; the first warns away, the second urges toward.',
      'The first is مفعول مطلق, but the second must be مجرور.',
      'Both call named people and are نداء.',
      'The structural pattern includes a منصوب with محذوف عامل and a repeated توكيد. The intended فعل differs: احذر الحسد versus الزم الصبر. Meaning distinguishes التحذير from الإغراء.'),
    Q('5-Read', '**الاختصاص يعيّن المراد من الضمير قبله.** Which detail establishes الاختصاص in **نحن الطلابَ نطلب العلم**?',
      'الطلابَ identifies the group already referred to by نحن.',
      'الطلابَ is being called from a distance by يا.',
      'الطلابَ assigns جزم to نطلب.',
      'Look back to **نحن**. الطلابَ clarifies its intended group with a محذوف أخصّ or أعني. No حرف نداء appears, and the construction does not govern جزم.')
 ],
 '6': [
    T('6G-1', 'Match the أركان in **الكتابَ قرأتُهُ**.', [
        ('المشغول', 'قرأتُ', 'الكتابَ', 'الهاء'),
        ('المشغول به', 'الهاء', 'الكتابَ', 'التاء بوصفها ضمير الكتاب'),
        ('المشغول عنه', 'الكتابَ', 'الهاء', 'قرأتُ')
    ], 'The عامل قرأت is **المشغول**. It already works in **ه**, the **مشغول به** returning to الكتاب. **الكتاب** is the earlier **مشغول عنه**. تاء الفاعل refers to the reader, not the book.'),
    T('6G-2', 'Match each condition to the strength of its حكم.', [
        ('After إذا الفجائية', 'وجوب الرفع', 'وجوب النصب', 'رجحان النصب فقط'),
        ('After هلّا للتحضيض', 'وجوب النصب', 'وجوب الرفع', 'جرّ بالكسرة'),
        ('With a following فعل طلب', 'رجحان النصب', 'وجوب الرفع', 'النصب ممنوع'),
        ('After همزة الاستفهام', 'رجحان النصب', 'وجوب النصب في كل حال', 'جرّ الاسم')
    ], 'إذا الفجائية is خاصة بالاسم, so رفع is واجب. هلّا للتحضيض is خاصة بالفعل in this pattern, so نصب is واجب. فعل طلب and همزة الاستفهام favour نصب without making رفع forbidden. إنْ الشرطية also requires نصب in the stated الاشتغال pattern; a preceding جملة فعلية or ما النافية favours it.'),
    T('6I-1', 'أعرب **الرسالة كتبتها**, taking الرسالة as منصوب on الاشتغال.', [
        ('الرسالة', 'الرسالةَ: مفعول به لفعل محذوف يفسّره المذكور', 'الرسالةُ: مبتدأ in the requested نصب analysis', 'الرسالةِ: مضاف إليه'),
        ('كتبت', 'فعل ماضٍ؛ التاء فاعل', 'فعل أمر؛ التاء مفعول به', 'اسم فاعل'),
        ('ها', 'مفعول به للفعل المذكور، يعود إلى الرسالة', 'فاعل للفعل المذكور', 'مضاف إليه'),
        ('جملة كتبتها', 'تفسيرية لا محل لها في تحليل النصب', 'في محل رفع خبر في تحليل النصب', 'في محل جر بالإضافة')
    ], '**الرسالةَ** مفعول به منصوب لفعل محذوف وجوبًا تقديره كتبتُ، يفسّره المذكور. **كتبتُ** فعل ماضٍ مبني على السكون؛ التاء فاعل. **ها** مفعول به يعود إلى الرسالة. The expressed جملة is تفسيرية in this نصب account. With الرسالةُ instead, it would supply خبر المبتدأ.'),
    Q('6I-2', 'Why not simply estimate **أعدّ الظالمين** in **والظالمين أعدّ لهم عذابًا أليمًا**?',
      'أعدّ connects the people through ل here; estimate a corresponding فعل such as أوعدَ for نصب الظالمين.',
      'Because الظالمين must be مرفوعًا بالواو.',
      'Because أعدّ is a حرف جرّ.',
      'In the expressed construction أعدّ works directly in عذابًا and links the people by **لهم**. A suitable محذوف فعل is **أوعدَ** or **كافأَ**, preserving the relevant meaning and relationship. The alternative with an estimated removed ل is a separate نصب بنزع الخافض account.'),
    Q('6R', 'Compare **كتابًا** answering ماذا قرأتَ؟ with **الكتابَ قرأتُهُ**.',
      'Both have a محذوف عامل; the first uses قرينة السياق and جائز حذف, the second تفسير by the expressed فعل and واجب حذف in the نصب account.',
      'Both have the same written قرأتُ as the direct عامل of الكتاب.',
      'Neither needs any قرينة for its تقدير.',
      'The short answer recovers قرأتُ from the question and permits its expression. In the نصب الاشتغال account, the later قرأتُه explains the unspoken عامل of الكتابَ while working itself in ه. The two kinds of حذف differ.'),
    Q('6-Read', '**المشغول به ضمير عائد على المشغول عنه.** In **الدرسَ حفظتُهُ**, choose the correct relation.',
      'ه is المشغول به and returns to الدرس, the المشغول عنه.',
      'ت is المشغول به and returns to الدرس.',
      'الدرس is a ضمير returning to ه.',
      '**ه** refers to the lesson, so it is المشغول به. **الدرس** is the earlier مشغول عنه. **حفظتُ** is المشغول; ت refers to the person who memorised the lesson.')
 ],
 '7': [
    T('7G-1', 'Match each منادى to its construction.', [
        ('يا عبدَ اللهِ', 'مضاف منصوب لفظًا', 'مفرد مبني على الضم', 'نكرة غير مقصودة بلا إضافة'),
        ('يا غافرًا ذنوبَنا', 'شبيه بالمضاف منصوب لفظًا', 'مضاف مع تنوين على الأول', 'مبني على الواو'),
        ('يا زيدُ', 'عَلَم مبني على الضم في محل نصب', 'فاعل مرفوع', 'مضاف إليه'),
        ('يا رجلُ: one particular man', 'نكرة مقصودة مبنية على الضم في محل نصب', 'نكرة غير مقصودة منصوبة لفظًا', 'خبر مرفوع')
    ], 'مضاف and شبيه بالمضاف take نصب لفظي. A عَلَم such as زيد and a نكرة مقصودة such as رجل addressing a specific man have بناء على ما يرفع به في محل نصب. غافرًا is شبيه بالمضاف because it works in ذنوبَنا; it is not إضافة with تنوين.'),
    T('7G-2', 'Complete the requested نداء.', [
        ('Address two particular men: يا ___', 'رجلانِ: مبني على الألف في محل نصب', 'رجلَيْنِ: منصوب لفظًا لأنه مثنّى دائمًا', 'رجلانِ: فاعل مرفوع ليا'),
        ('Address particular Muslims: يا ___', 'مسلمونَ: مبني على الواو في محل نصب', 'مسلمينَ: مجرور بفي محذوفة', 'مسلمونَ: خبر مرفوع'),
        ('Call without identifying a particular inattentive person', 'يا غافلًا: نكرة غير مقصودة', 'يا غافلُ: نكرة مقصودة by definition', 'يا غافلٍ: مجرور بيا')
    ], 'The intended addressee matters. رجلانِ and مسلمونَ are نكرة مقصودة, with بناء على الألف or الواو and محل نصب. مفرد in this باب excludes إضافة and شبه إضافة; it does not exclude مثنّى or جمع. غير مقصود غافلًا has نصب لفظي.'),
    T('7I-1', 'أعرب **يا طالبا علما اصبر**, using شبيه بالمضاف.', [
        ('يا', 'حرف نداء يقوم مقام أدعو', 'حرف جرّ', 'فعل أمر'),
        ('طالبا', 'طالبًا: منادى شبيه بالمضاف منصوب', 'طالبُ: منادى مبني على الضم with the requested construction', 'طالبِ: مضاف إليه'),
        ('علما', 'علمًا: مفعول به لاسم الفاعل', 'علمِ: مضاف إليه مع بقاء تنوين طالبًا', 'علمٌ: خبر'),
        ('اصبر', 'اصبرْ: فعل أمر، فاعله مستتر أنت', 'اصبرُ: خبر مرفوع', 'اصبرَ: مفعول به لطالب')
    ], '**يا** حرف نداء؛ **طالبًا** منادى شبيه بالمضاف منصوب بالفتحة، وهو اسم فاعل عامل في علمًا، وفاعله مستتر أنت. **علمًا** مفعول به لاسم الفاعل. **اصبرْ** فعل أمر مبني على السكون؛ فاعله مستتر أنت. Compare طالبَ العلمِ, where إضافة instead requires جرّ العلم.'),
    T('7I-2', 'Can the حرف نداء be omitted under the taught conditions?', [
        ('يوسفُ، أعرضْ عن هذا', 'Permitted with a عَلَم in a calling context', 'Forbidden with every عَلَم', 'يوسف must then become مفعولًا به منصوبًا لفظًا'),
        ('عبدَ اللهِ، اصبرْ', 'Permitted with a مضاف in a calling context', 'Forbidden with every مضاف', 'عبد must become مرفوعًا'),
        ('يا رجلُ: a particular man', 'Retain يا with النكرة المقصودة', 'Omit يا freely under the same rule', 'Replace يا with من and keep the analysis')
    ], 'A calling context can license حذف حرف النداء with a عَلَم or مضاف. Under the conditions used here it is retained with النكرة المقصودة and لفظ الجلالة. اللهمّ is a separate compensated form, not ordinary deletion.'),
    Q('7R', 'Why is ضمة زيد in **يا زيدُ** different from ضمة زيد in **جاء زيدٌ**?',
      'يا زيدُ has بناء على الضم في محل نصب; جاء زيدٌ has فاعل مرفوع بالضمة.',
      'Both are فاعل مرفوع because both have ضمة.',
      'Both are مجرور because a word precedes زيد.',
      'In نداء, زيدُ is منادى مبني على الضم في محل نصب. In جاء زيدٌ, زيدٌ is فاعل مرفوع. The visible vowel does not determine whether the ending is بناء or إعراب.'),
    Q('7-Read', '**المنادى المفرد المعرفة مبني على ما يرفع به في محل نصب.** Which interpretation of مفرد fits **يا مسلمونَ**?',
      'Neither مضاف nor شبيه بالمضاف; it may still be جمعًا.',
      'Exactly one Muslim, despite the ending.',
      'A word that cannot be مبنيًّا.',
      'مفرد is a constructional label in this باب. مسلمونَ can therefore be جمع مذكر سالم and still belong to this class of منادى: مبني على الواو في محل نصب.')
 ],
 '8': [
    T('8G-1', 'Identify the form of إضافة to ياء المتكلّم.', [
        ('يا عبادِ', 'حذف الياء والاكتفاء بالكسرة', 'جرّ المنادى بيا', 'حذف نون المثنّى'),
        ('يا عباديْ', 'ثبوت الياء ساكنة', 'الياء علامة تثنية', 'قلب الياء ألفًا'),
        ('يا عباديَ', 'ثبوت الياء مفتوحة', 'حذف الياء', 'جزم الاسم'),
        ('يا حسرتَا', 'قلب الكسرة فتحة والياء ألفًا', 'تنوين النصب', 'ألف المثنّى')
    ], 'These are four established صور of المنادى المضاف إلى ياء المتكلّم. The ياء may be omitted with كسرة retained, remain ساكنة, remain مفتوحة, or be changed to ألف with the preceding كسرة changed to فتحة. None makes يا a حرف جرّ.'),
    T('8G-2', 'Apply the ترخيم conditions taught here.', [
        ('فاطمة', 'Eligible: ends in تاء', 'Ineligible: every مؤنث is excluded', 'Eligible only because it has three letters'),
        ('جعفر', 'Eligible: عَلَم مذكر زائد على ثلاثة أحرف غير مركّب', 'Ineligible: no تاء', 'Eligible because it is مركّب'),
        ('زيد', 'Excluded by the length condition', 'Eligible because three letters are sufficient here', 'Excluded because it ends in تاء'),
        ('عبد الله', 'Excluded because it is مركّب', 'Eligible because it is مضاف', 'Eligible because its final letter can always be removed')
    ], 'The categories used here are المختوم بالتاء and عَلَم مذكر زائد على ثلاثة أحرف غير مركّب. فاطمة meets the first, جعفر the second. زيد fails the length condition; عبد الله is مركّب. زينب does not satisfy the مذكر condition in this treatment.'),
    Q('8I-1', 'From **حارث**, choose the preferred ترخيم retaining الحركة الأصلية.',
      'يا حارِ', 'يا حارُ is the only permitted form', 'يا حارٍ with تنوين الجرّ',
      '**يا حارِ** preserves the كسرة on ر in حارث and is preferred. **يا حارُ** is also permitted, but is not the answer to a request to retain الحركة الأصلية. تنوين الجرّ is not this construction.'),
    T('8I-2', 'Correct the analysis of these forms.', [
        ('“عبادِ in يا عبادِ is مجرور because of كسرة.”', 'It remains منادى مضاف منصوب تقديرًا; كسرة points to omitted ياء.', 'Correct: يا is a حرف جرّ.', 'It is مجزوم لأن الياء حذفت.'),
        ('اللهمّ', 'صيغة نداء؛ الميم المشددة عوض عن يا', 'فعل أمر بمعنى نادى', 'حرف استثناء'),
        ('اللهمّ نعم', 'Expresses certainty in the answer', 'Requires نعم to become حرف نداء', 'Always expresses grief'),
        ('اللهمّ إلا أن يكون كذا', 'Introduces a rare exception', 'Forbids every exception', 'Makes إلا a اسم فاعل')
    ], 'يا عبادِ preserves the كسرة associated with a deleted ياء المتكلّم; the منادى is still منصوب تقديرًا. اللهمّ compensates for يا with ميم مشدّدة. Before نعم it can signal certainty; before إلا it can signal the rarity of the exception.'),
    Q('8R', 'Which distinguishes **يوسفُ، أعرضْ** from **يا حارِ**?',
      'The first omits حرف النداء; the second shortens the منادى itself.',
      'Both omit only the عامل of a مفعول مطلق.',
      'Both are مجرور because of a deleted من.',
      'يوسفُ is the full عَلَم with يا omitted in context. يا حارِ retains يا and removes the end of حارث through ترخيم. Name what is omitted before classifying the حذف.'),
    Q('8-Read', '**الترخيم حذف آخر المنادى للتخفيف.** What was removed in **يا فاطمَ**?',
      'The final تاء of فاطمة', 'The حرف نداء يا', 'A written فعل ماضٍ after فاطمة',
      'فاطمة loses its final تاء in ترخيم. يا remains, and فاطمَ preserves the preceding حركة أصلية. This is deletion within the منادى, not حذف حرف النداء.')
 ],
 '9': [
    T('9G-1', 'Analyse **يا لَلأميرِ لِلمظلومينَ**.', [
        ('يا', 'حرف استغاثة', 'حرف جرّ', 'اسم فعل'),
        ('الأميرِ', 'مستغاث مجرور بلام مفتوحة', 'مستغاث له منصوب', 'فاعل مرفوع'),
        ('المظلومينَ', 'مستغاث له مجرور بلام مكسورة', 'مستغاث منصوب بالفتحة', 'منادى مبني على الضم'),
        ('علامة جرّ المظلومين', 'الياء لأنه جمع مذكر سالم', 'الفتحة على لام الاستغاثة', 'حذف النون')
    ], 'يا is the حرف الاستغاثة. لَ introduces المستغاث الأميرِ; لِ introduces المستغاث له المظلومينَ. Both لام are حروف جرّ. المظلومين is مجرور بالياء لأنه جمع مذكر سالم; its نون remains.'),
    T('9G-2', 'Complete the second ل while keeping the indicated meaning.', [
        ('يا لَلأميرِ ويا ___ المسلمينَ لِلمظلومينَ', 'لَـ: repeated يا before another مستغاث', 'لِـ: يا never affects the pattern', 'لُـ: every مستغاث requires ضمة'),
        ('يا لَلأميرِ و___ المسلمينَ لِلمظلومينَ', 'لِـ: another مستغاث, without repeated يا', 'لَـ: repetition of يا is irrelevant', 'لُـ: جمع requires ضمة')
    ], 'With repeated يا, use **ويا لَلمسلمين**. Without repeated يا, use **ولِلمسلمين**. In both, المسلمين remains a معطوف مستغاث; المظلومين is المستغاث له. The second لِ does not automatically change who is being asked to help.'),
    T('9I-1', 'Distinguish the recognised نداء patterns.', [
        ('يا لَلقرآنِ', 'نداء تعجّب؛ المتعجّب منه في موضع المستغاث', 'Every لام مفتوحة gives نصب للقرآن', 'ترخيم القرآن'),
        ('يا لِلقرآنِ', 'نداء تعجّب؛ المتعجّب منه في موضع المستغاث له مع حذف المستغاث', 'Impossible because every ل after يا must be مفتوحة', 'نداء عادي مع حذف الألف'),
        ('وا عبدَ اللهِ', 'ندبة؛ المنادى المضاف منصوب لفظًا', 'ندبة؛ كل منادى مبني على الضم', 'استغاثة بحرف وا')
    ], 'Both **يا لَلقرآن** and **يا لِلقرآن** are recognised for نداء التعجب, but their structural accounts differ. **وا عبدَ اللهِ** is ندبة; عبدَ is مضاف منصوب لفظًا and اللهِ مضاف إليه. وا is not the حرف الاستغاثة, which is يا only.'),
    Q('9I-2', 'In **وا رأسَاهْ** at وقف, what is the final ه?',
      'هاء السكت after ألف الندبة',
      'ضمير في محل جر meaning “his”',
      'فاعل مستتر written as ه',
      'The final هْ is **هاء السكت**, added at وقف after ألف الندبة. It is not a possessive ضمير. The ألف is likewise part of the ندبة form, not a علامة تثنية.'),
    Q('9R', 'Which comparison is correct?',
      'وا زيدُ keeps بناء على الضم في محل نصب; وا عبدَ اللهِ has نصب لفظي through its type as مضاف.',
      'وا makes every following word مجرورًا.',
      'ندبة removes all the ordinary أحكام المنادى.',
      'The basic أحكام المنادى remain in ندبة. زيد is مفرد عَلَم with بناء في محل نصب. عبد الله is مضاف, so عبد has نصب لفظي. يا may replace وا for ندبة only when confusion with ordinary نداء is avoided.'),
    Q('9-Read', '**تُكسر لام المستغاث المعطوف إذا لم تتكرر يا.** Apply it to **يا لَلأميرِ ولِلمسلمينَ لِلمظلومينَ**.',
      'المسلمين is another مستغاث; its ل is مكسورة because يا was not repeated.',
      'المسلمين must be the only مستغاث له because its ل is مكسورة.',
      'الأمير becomes منصوبًا لأن لامه مفتوحة.',
      'The عطف and absence of repeated يا explain **ولِلمسلمين**. The final **لِلمظلومين** gives المستغاث له. Both أسماء after the لام are مجرورة despite the different roles.')
 ],
 '10': [
    T('10G-1', 'Match each حال to its condition for حذف العامل.', [
        ('دعائي ربّي مستيقنًا', 'حال تسدّ مسدّ الخبر', 'ترخيم عَلَم', 'تمييز عدد'),
        ('تصدّق بدرهم فصاعدًا', 'زيادة بتدريج مع الفاء', 'نداء نكرة مقصودة', 'اختصاص'),
        ('أقاعدًا وقد أقيمت الصلاة؟', 'استفهام للتوبيخ', 'استغاثة', 'إضافة لفظية'),
        ('خالد أبوك عطوفًا', 'تأكيد مضمون الجملة بشروطه', 'مفعول مطلق لأنه مصدر', 'حال بلا أي شرط')
    ], 'The four settings are سدّ مسدّ الخبر, gradual increase/decrease, استفهام للتوبيخ, and تأكيد مضمون الجملة. In the last, meaning must agree and المبتدأ والخبر must be معرفتين جامدتين. مستيقنًا describes the person praying, not the دعاء itself.'),
    T('10G-2', 'Analyse **تصدّقْ بدرهمٍ فصاعدًا**.', [
        ('درهمٍ', 'اسم مجرور بالباء', 'حال منصوب', 'مفعول مطلق'),
        ('صاعدًا', 'حال منصوب بعامل محذوف وجوبًا', 'نعت مجرور لدرهم', 'خبر مرفوع'),
        ('التقدير المناسب', 'فزِدْ صاعدًا', 'يا صاعدُ', 'إنّ درهمًا'),
        ('الفاء أو ثمّ', 'Required accompaniment for this gradual-change pattern', 'Both forbidden with this حال', 'Both always make صاعدًا مفعولًا به')
    ], '**تصدّقْ** فعل أمر فاعله أنت. **بدرهمٍ** جار ومجرور متعلق بتصدّق. **صاعدًا** حال منصوب بالفتحة بعامل محذوف وجوبًا تقديره زِدْ in **فزد صاعدًا**. فـ or ثمّ accompanies this particular gradual-change pattern; فـ is more frequent.'),
    Q('10I-1', 'Correct: “Any حال after any جملة اسمية allows حذف العامل as تأكيد مضمون الجملة.”',
      'The meanings must agree, and المبتدأ والخبر must be معرفتين جامدتين.',
      'Correct: no conditions concern the two أسماء.',
      'The شرط is that both المبتدأ والخبر be نكرتين مشتقتين.',
      'The rule requires agreement between معنى الحال and معنى الجملة, plus **المبتدأ والخبر معرفتان جامدتان**. خالد أبوك عطوفًا is the taught model. A superficially similar sequence does not automatically meet those conditions.'),
    T('10I-2', 'Read **أقاعدا وقد أقيمت الصلاة؟** Supply the key analysis.', [
        ('قاعدا', 'قاعدًا: حال منصوب', 'قاعدٌ: فاعل مرفوع', 'قاعدٍ: مجرور بالهمزة'),
        ('عامله', 'محذوف وجوبًا؛ تقدير مناسب: أبقيتَ قاعدًا؟', 'همزة الاستفهام كحرف نصب', 'الصلاة هي العامل'),
        ('قد أقيمت الصلاة', 'Explains the circumstance making the sitting a توبيخ', 'Makes قاعدًا a مصدر', 'Changes the همزة into حرف جرّ')
    ], '**قاعدًا** حال منصوب بعامل محذوف وجوبًا in استفهام للتوبيخ. A suitable تقدير is **أبقيتَ قاعدًا؟** or **ألبثتَ قاعدًا؟**. **قد أقيمت الصلاة** supplies the circumstance for the rebuke; the همزة does not itself act as a ناصب للحال.'),
    Q('10R', 'Compare **أجرأةً على المعاصي؟** and **أقاعدًا وقد أقيمت الصلاة؟**.',
      'Both express التوبيخ; جرأةً is مفعول مطلق, قاعدًا is حال.',
      'Both are مفعول مطلق because both are منصوب.',
      'Both are حال because every استفهام governs حال.',
      'جرأة is a مصدر used as مفعول مطلق, whereas قاعد describes a state and is حال. The omitted عوامل are understood through different constructions even though both expressions rebuke.'),
    Q('10-Read', '**يشترط في الحال المؤكدة لمضمون الجملة أن يتفق معناها ومعنى الجملة.** Which adds the other required condition?',
      'أن يكون المبتدأ والخبر معرفتين جامدتين',
      'أن يكون المبتدأ والخبر نكرتين',
      'أن يكون الحال مضافًا دائمًا',
      'For this construction, require agreement of meaning **and** المبتدأ والخبر معرفتين جامدتين. Do not transfer that specific condition to every kind of حال.')
 ],
 'R': [
    T('A1', 'Identify the عامل or تقدير in each specified analysis.', [
        ('خالدٌ معلّمٌ: use the main account', 'الابتداء يرفع المبتدأ والخبر', 'إنّ المحذوفة تنصب خالدًا', 'حرف جرّ مقدّر'),
        ('يقرأُ خالدٌ: عامل رفع يقرأ', 'خلوّه من الناصب والجازم', 'خالد يجزمه', 'لم محذوفة'),
        ('ماذا قرأت؟ — كتابًا', 'قرأتُ محذوف جوازًا', 'أدعو محذوف وجوبًا', 'ابتداء ينصب كتابًا'),
        ('الكتابَ قرأتُه', 'فعل محذوف وجوبًا يفسّره المذكور ينصب الكتاب', 'ه تنصب الكتاب', 'قرأت المذكور له مفعولان هما الكتاب وه')
    ], 'The first two are عامل معنوي: الابتداء and خلوّ المضارع. The short answer has a فعل recovered from context جوازًا. The نصب الاشتغال example has an omitted فعل explained by the following قرأتُه, whose ه already fills its مفعول به position.'),
    T('A2', 'Choose the accurate correction for each overgeneralisation.', [
        ('كل نصب بعد استفهام مفعول مطلق', 'أقاعدًا؟ has حال, unlike أجرأةً؟', 'كل استفهام حرف جرّ', 'كل منصوب منادى'),
        ('كل ضمة علامة رفع', 'يا زيدُ has بناء على الضم في محل نصب', 'جاء زيدٌ has no فاعل', 'الضمة لا تأتي في العربية'),
        ('كل حذف واجب', 'كتابًا answering ماذا قرأت؟ has حذف جائز', 'لا يجوز حذف أي فعل', 'الابتداء فعل محذوف دائمًا'),
        ('راجح means واجب', 'A preferred نصب can coexist with a permitted رفع', 'Every راجح is forbidden', 'Every جائز is obligatory')
    ], 'Identify the role, construction, and strength of the rule separately. قاعدًا is حال; يا زيدُ has بناء; the contextual short answer permits expression of its عامل; رجحان does not forbid the alternative.'),
    T('B1', 'Choose the endings for the specified meanings.', [
        ('Call one particular man: يا ___', 'رجلُ', 'رجلًا as نكرة غير مقصودة', 'رجلٍ'),
        ('نحن ___ نطلب العلم: specify نحن', 'الطلابَ: اختصاص', 'الطلابِ: جرّ بنحن', 'الطلابُ: منصوب بالضمة'),
        ('هلّا ___ قرأتَه؟', 'الكتابَ: وجوب النصب في الاشتغال', 'الكتابُ: وجوب الرفع بعد هلّا', 'الكتابِ: جرّ بهلّا'),
        ('أ___ قرأتَه؟: choose the preferred الاشتغال form', 'الكتابَ: رجحان النصب', 'الكتابُ: الرفع وحده جائز', 'الكتابِ: الجرّ واجب'),
        ('يا طالبَ ___', 'العلمِ: مضاف إليه', 'العلمَ: مفعول به مع الإضافة المطلوبة', 'العلمُ: نائب فاعل')
    ], '**يا رجلُ** addresses a particular man. **نحن الطلابَ** uses اختصاص. **هلّا الكتابَ قرأته** requires نصب in this pattern; **أالكتابَ قرأته** prefers it without forbidding رفع. **يا طالبَ العلمِ** uses إضافة, so العلم is مجرور.'),
    T('B2', 'Distinguish the losses or replacements.', [
        ('يا عبادِ', 'ياء المتكلّم محذوفة والكسرة باقية', 'حذف عامل جزم منادى', 'حذف آخر عَلَم للترخيم'),
        ('يا حارِ', 'ترخيم حارث مع إبقاء الحركة الأصلية', 'حذف يا', 'جرّ بمن محذوفة'),
        ('اللهمّ', 'ميم مشدّدة عوض عن حرف النداء', 'ميم علامة جمع', 'حرف نفي'),
        ('يا زيدَاهْ in الاستغاثة', 'ألف عوض عن لام المستغاث، ثم هاء عند الوقف', 'ألف مثنّى ثم ضمير ه', 'تنوين نصب ثم فاعل')
    ], 'يا عبادِ omits ياء المتكلّم, يا حارِ shortens حارث, and اللهمّ compensates for يا with ميم مشدّدة. In the stated الاستغاثة form, ألف replaces لام المستغاث and هاء occurs at وقف. Similar-looking deletions need different explanations.'),
    T('C1', '**يا خالد، الصبر الصبر. نحن الطلاب نطلب العلم. الدرس حفظته.** Use a named addressee, إغراء, اختصاص, and نصب الاشتغال. Complete the تركيب.', [
        ('يا', 'حرف نداء', 'حرف جرّ', 'ضمير'),
        ('خالد', 'خالدُ: منادى مبني على الضم في محل نصب', 'خالدٌ: فاعل ليا', 'خالدًا: نكرة غير مقصودة'),
        ('الصبر الأول', 'الصبرَ: مفعول به لفعل محذوف وجوبًا تقديره الزم', 'الصبرُ: مبتدأ', 'الصبرِ: مضاف إليه لخالد'),
        ('الصبر الثاني', 'الصبرَ: توكيد لفظي منصوب', 'الصبرُ: خبر', 'الصبرِ: مجرور بالواو'),
        ('نحن', 'ضمير في محل رفع مبتدأ', 'حرف اختصاص', 'فاعل ليا'),
        ('الطلاب', 'الطلابَ: مفعول به لأخصّ المحذوف على الاختصاص', 'الطلابُ: منادى', 'الطلابِ: مضاف إليه لنحن'),
        ('نطلب', 'نطلبُ: مضارع مرفوع، فاعله مستتر نحن', 'نطلبْ: مجزوم بنحن', 'نطلبَ: منصوب بالطلاب'),
        ('العلم', 'العلمَ: مفعول به لنطلب', 'العلمُ: فاعل', 'العلمِ: مضاف إليه'),
        ('جملة نطلب العلم', 'في محل رفع خبر نحن', 'تفسيرية لا محل لها', 'في محل جر مضاف إليه'),
        ('الدرس', 'الدرسَ: مفعول به لفعل محذوف يفسّره حفظتُه', 'الدرسُ: مبتدأ in the requested نصب analysis', 'الدرسِ: مجرور'),
        ('حفظت', 'حفظتُ: فعل ماضٍ مبني على السكون، والتاء فاعل', 'حفظتْ: حرف نداء', 'حفظتَ: فعل أمر'),
        ('ه', 'مفعول به يعود إلى الدرس', 'فاعل يعود إلى نحن', 'مضاف إليه لخالد'),
        ('جملة حفظته', 'تفسيرية لا محل لها في هذا التحليل', 'خبر للدرس المنصوب', 'حال من يا')
    ], '**يا خالدُ، الصبرَ الصبرَ. نحنُ الطلابَ نطلبُ العلمَ. الدرسَ حفظتُهُ.**\n\n**يا** حرف نداء؛ **خالدُ** منادى مبني على الضم في محل نصب. **الصبرَ الأول** مفعول به لفعل محذوف وجوبًا تقديره الزم؛ فاعله مستتر أنت. **الثاني** توكيد لفظي منصوب.\n\n**نحن** ضمير في محل رفع مبتدأ. **الطلابَ** منصوب على الاختصاص بفعل محذوف وجوبًا تقديره أخصّ، فاعله مستتر أنا. **نطلبُ** مضارع مرفوع، فاعله مستتر نحن؛ **العلمَ** مفعول به. **جملة نطلب العلم** في محل رفع خبر.\n\n**الدرسَ** مفعول به لفعل محذوف وجوبًا تقديره حفظتُ، يفسّره المذكور. **حفظتُ** فعل ماضٍ مبني على السكون، والتاء ضمير في محل رفع فاعل. **ه** ضمير في محل نصب مفعول به يعود إلى الدرس. **جملة حفظته** تفسيرية لا محل لها. The requested نصب analysis prevents confusing it with الدرسُ حفظته, whose جملة would be خبرًا.'),
    T('C2', '**ماذا قرأت؟ قال سعيد: كتابا. ثم قال: يا لَلأميرِ ولِلمسلمينَ لِلمظلومينَ.** Follow the relationships.', [
        ('كتابا', 'كتابًا: مفعول به لقرأتُ المحذوف جوازًا', 'كتابٌ: فاعل لقال', 'كتابٍ: مضاف إليه لسعيد'),
        ('الأمير', 'مستغاث مجرور بالكسرة بلام مفتوحة', 'مستغاث له منصوب', 'منادى مبني على الضم بلا لام'),
        ('المسلمين', 'معطوف مستغاث؛ اللام مكسورة لعدم تكرار يا', 'مفعول به لقال', 'فاعل لام الاستغاثة'),
        ('المظلومين', 'مستغاث له مجرور بالياء', 'معطوف على سعيد مرفوع', 'تمييز منصوب'),
        ('Replacing ولِلمسلمين with repeated يا', 'ويا لَلمسلمين', 'ويا لِلمسلمين under the same repeated-يا rule', 'ووا لُلمسلمين')
    ], '**كتابًا** answers ماذا قرأتَ, so estimate قرأتُ and analyse مفعول به منصوب with حذف جائز. **يا** introduces الاستغاثة. **الأميرِ** is مستغاث مجرور بالكسرة with لَ. **المسلمينَ** is another مستغاث, معطوف, with لِ because يا is not repeated; its جرّ is بالياء. **المظلومينَ** is المستغاث له مجرور بالياء. Repeating يا restores **ويا لَلمسلمين**.'),
    T('D1', 'Read the Arabic judgements and select the consequence.', [
        ('يجوز إعمال الأول أو الثاني', 'Both accounts are permitted; specify one for a detailed analysis.', 'Only the second exists.', 'The معمول must precede both.'),
        ('يترجّح النصب إذا كان العامل فعل طلب', 'النصب راجح، وليس معنى ذلك امتناع الرفع.', 'النصب واجب والرفع ممتنع.', 'الجرّ أولى من النصب.'),
        ('المنادى مبني على ما يرفع به في محل نصب', 'علامة البناء لا تغيّر محل النصب إلى رفع.', 'كل ضمة هنا علامة رفع.', 'لا محل لأي منادى من الإعراب.')
    ], '**يجوز** expresses permission; **يترجّح** expresses preference; **مبني ... في محل نصب** separates the fixed form from its position. These distinctions prevent false corrections of valid alternatives.'),
    T('D2', 'Choose a complete condition rather than an overgeneralisation.', [
        ('حذف عامل حال الزيادة أو النقص بتدريج', 'تصحبها الفاء أو ثمّ، والفاء أكثر', 'كل حال بعد اسم مقدار لها الحكم نفسه', 'يجب حذف الفاء وثمّ'),
        ('الحال المؤكدة لمضمون الجملة', 'يتفق المعنيان، والمبتدأ والخبر معرفتان جامدتان', 'يكفي وجود أي جملة اسمية', 'المبتدأ والخبر نكرتان دائمًا'),
        ('يا في الندبة', 'تجوز إذا أُمن اللبس بالنداء المحض', 'ممنوعة دائمًا', 'تجوز بلا اعتبار للمعنى'),
        ('معنى الفعل في اسم الإشارة', 'يمكن أن ينصب الحال مع بقاء الكلمة اسم إشارة', 'يحوّل اسم الإشارة إلى فعل ماضٍ', 'يجزم كل فعل بعده')
    ], 'Keep each condition attached to its own rule: فـ/ثمّ for gradual change; agreement of meaning and معرفتان جامدتان for the specified تأكيد الحال; absence of ambiguity for يا in ندبة. معنى الإشارة can govern حال without changing the word type of اسم الإشارة.')
 ]
}
