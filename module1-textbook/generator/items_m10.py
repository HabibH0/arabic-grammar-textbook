"""Module 10: one correct answer per control, with explicit analytical scope."""
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
    T('1G-1', 'Match the expression to the stated relationship.', [
        ('قسا القلبُ: القلب', 'فاعل لفعل تام معلوم', 'نائب فاعل لفعل مجهول', 'خبر إنّ'),
        ('أحاضرٌ زيدٌ؟ زيد', 'فاعل لاسم فاعل عامل', 'مضاف إليه لحاضر', 'مفعول به لحاضر'),
        ('إنّ خالدًا حاضرٌ: إنّ', 'عامل غير معمول', 'معمول مرفوع', 'اسم مؤوّل')
    ], '**القلبُ** is فاعل even though no deliberate action is meant. **زيدٌ** is raised by the supported اسم الفاعل حاضر. **إنّ** is عامل in اسمها وخبرها but is itself a حرف لا محل له من الإعراب.'),
    T('1G-2', 'Complete the تركيب of **ما جاء من بشيرٍ**.', [
        ('ما', 'حرف نفي', 'اسم إنّ', 'فعل ماض'),
        ('جاء', 'فعل ماض معلوم', 'اسم فاعل', 'فعل أمر'),
        ('من', 'حرف جر زائد', 'اسم استفهام', 'فاعل'),
        ('بشير', 'فاعل مجرور لفظًا مرفوع محلًّا', 'مفعول به منصوب لفظًا', 'خبر ما منصوب بالكسرة')
    ], '**ما** حرف نفي؛ **جاء** فعل ماض معلوم مبني على الفتح؛ **من** حرف جر زائد؛ **بشيرٍ** فاعل مجرور لفظًا بمن مرفوع محلًّا. The visible كسرة does not erase the فاعل relationship.'),
    Q('1I-1', 'Choose the correct analysis of **ذِكْرُكم آباءَكم**. Focus on the first كم.',
      'كم مضاف إليه للمصدر، وهو فاعله في المعنى.',
      'كم مفعول به للمصدر، وآباء فاعله.',
      'كم حرف جر زائد، وآباء مبتدأ.',
      '**ذكر** مصدر أضيف إلى فاعله: the first **كم** is ضمير في محل جر مضاف إليه and supplies the فاعل meaning. **آباءَ** is مفعول به للمصدر منصوب، وهو مضاف؛ the second كم is مضاف إليه. Keep إضافة and the underlying فاعلية distinct.'),
    T('1I-2', 'Choose the ending and role in **اشتد الحر. حضر الضيف**. اشتدّ = became intense.', [
        ('الحر', 'الحرُّ: فاعل مرفوع', 'الحرَّ: مفعول به', 'الحرِّ: مضاف إليه'),
        ('الضيف', 'الضيفُ: فاعل مرفوع', 'الضيفَ: خبر كان', 'الضيفِ: مجرور بحضر')
    ], '**اشتدَّ الحرُّ. حضرَ الضيفُ.** Both أسماء are فاعل لفعل تام معلوم and مرفوع بالضمة. The definition concerns what the فعل is attributed to, not whether the اسم represents a deliberate action.'),
    Q('1R', 'Compare **الصومُ نافعٌ** and **أن تصوموا خيرٌ لكم**. What occupies the مبتدأ role?',
      'الصوم اسم صريح؛ أن تصوموا اسم مؤوّل في محل رفع مبتدأ.',
      'أن alone is a مرفوع اسم؛ تصوموا is خبرها.',
      'Both expressions are حروف غير معمول.',
      '**الصومُ** is اسم صريح مرفوع مبتدأ. **أن تصوموا** is understood as صومكم: the complete اسم مؤوّل occupies محل رفع مبتدأ. أن remains حرفًا مصدريًّا ناصبًا; تصوموا is منصوب بحذف النون، والواو فاعل.'),
    Q('1-Read', '**الفاعل ما نُسب إليه الفعل التام المعلوم أو ما بمعناه.** Which conclusion follows?',
      'An اسم فاعل meeting its عمل conditions can raise a فاعل.',
      'Only a written فعل can ever raise a فاعل.',
      'Every اسم after a فعل is فاعل regardless of its relationship.',
      '**أو ما بمعناه** includes an عامل اسم with the relevant فعل meaning, such as a supported اسم فاعل. Still establish the conditions and the actual relationship.')
 ],
 '2': [
    T('2G-1', 'Identify the reason for the required order in each stated construction.', [
        ('زار موسى عيسى، بلا قرينة أخرى', 'خوف اللبس؛ موسى فاعل', 'عيسى فاعل لأنّه آخر اسم', 'استفهام له صدر الكلام'),
        ('أكرم خالدًا معلّمُه', 'ضمير في الفاعل يعود إلى المفعول به', 'لا يجوز تأخير أي فاعل', 'خالد مبتدأ مجرور'),
        ('أيَّ كتابٍ قرأتَ؟', 'أيّ مفعول به له صدر الكلام', 'أيّ فاعل مؤخّر', 'كتاب خبر مقدّم')
    ], 'Without a distinguishing قرينة, **موسى** is فاعل and **عيسى** مفعول به. In **أكرم خالدًا معلّمُه** the هاء refers back to خالد, requiring this تقديم المفعول به. **أيَّ** is مفعول به منصوب and اسم استفهام له صدر الكلام؛ كتابٍ مضاف إليه.'),
    T('2G-2', 'Complete the full تركيب: **أكرم خالدًا معلّمُه**.', [
        ('أكرم', 'فعل ماض مبني على الفتح', 'مبتدأ مرفوع', 'حرف نفي'),
        ('خالدًا', 'مفعول به مقدّم منصوب بالفتحة', 'فاعل مرفوع بالفتحة', 'مضاف إليه'),
        ('معلّمُ', 'فاعل مؤخّر مرفوع بالضمة، وهو مضاف', 'خبر منصوب', 'مفعول به ثان'),
        ('الهاء', 'ضمير في محل جر مضاف إليه يعود إلى خالد', 'ضمير في محل رفع نائب فاعل', 'حرف تنبيه')
    ], '**أكرم** فعل ماض؛ **خالدًا** مفعول به مقدّم منصوب؛ **معلّمُ** فاعل مؤخّر مرفوع ومضاف؛ **الهاء** مضاف إليه تعود إلى خالد. The order keeps the referring ضمير after the اسم supplying its reference.'),
    T('2I-1', 'Read without relying on ordinary order. Identify الفاعل and the قرينة.', [
        ('أكل الكمثرى موسى', 'موسى؛ قرينة معنوية', 'الكمثرى؛ لا قرينة للمعنى', 'فاعل محذوف وجوبًا'),
        ('نصرت موسى سلمى، والتاء تاء التأنيث', 'سلمى؛ قرينة لفظية', 'موسى؛ لأنّه أقرب إلى الفعل', 'التاء نفسها فاعل'),
        ('زار سعيدًا حامدٌ', 'حامد؛ الضمة والفتحة تميّزان الدورين', 'سعيد؛ لأنّه قبل حامد', 'كلاهما مفعول به')
    ], '**موسى** is فاعل in the first because the meaning distinguishes Musa from the pears. In the second, **تاء التأنيث** identifies **سلمى** as فاعل؛ موسى مفعول به. In the third, **حامدٌ** is فاعل and **سعيدًا** مفعول به; the expressed endings distinguish them.'),
    Q('2I-2', 'A learner changes **ساعدَهُ خالدٌ** to **ساعدَ خالدٌ إيّاهُ** solely to restore ordinary order. Which correction fits the rule taught here?',
      'Keep ساعدَه خالدٌ: المفعول به is ضمير متصل, so it precedes الفاعل here.',
      'The change is required because الفاعل must always come first.',
      'Change خالدٌ to خالدٍ because a ضمير precedes it.',
      'In the ordinary construction **ساعده خالدٌ**, الهاء is ضمير متصل في محل نصب مفعول به and خالد فاعل. Do not replace الاتصال with الانفصال merely to reverse their order. Compare الفاعل المتصل in ساعدتُ خالدًا.'),
    Q('2R', 'Analyse **سعيدٌ قرأَ** using the usual مبتدأ account.',
      'سعيد مبتدأ؛ قرأ وفاعله المستتر هو جملة في محل رفع خبر.',
      'سعيد مفعول به مقدّم؛ قرأ بلا فاعل.',
      'سعيد اسم كان محذوفة وجوبًا؛ قرأ خبر منصوب.',
      '**سعيدٌ** مبتدأ مرفوع؛ **قرأ** فعل ماض وفاعله ضمير مستتر تقديره هو يعود إلى سعيد؛ الجملة في محل رفع خبر. The question selects this account; it does not deny the alternative account allowing a preceding فاعل.'),
    Q('2-Read', '**يجب تقديم الفاعل عند خوف اللبس.** In **زار موسى عيسى** with no other قرينة, which reading follows?',
      'موسى فاعل وعيسى مفعول به.',
      'عيسى فاعل وموسى مفعول به.',
      'Neither اسم can be assigned a role.',
      'The endings are مقدّرة, and the question excludes another قرينة. The required ordinary order therefore identifies **موسى** as فاعل and **عيسى** as مفعول به.')
 ],
 '3': [
    T('3G-1', 'Match each highlighted relationship.', [
        ('فتح الحارسُ البابَ: الحارس', 'فاعل', 'نائب فاعل', 'خبر'),
        ('فُتح البابُ: الباب', 'نائب فاعل', 'مفعول به', 'مضاف إليه'),
        ('أمفتوحٌ البابُ؟ under المكتفي بمرفوعه: الباب', 'نائب فاعل لاسم مفعول', 'فاعل لفعل ماض معلوم', 'اسم إنّ')
    ], '**فتح** is معلوم and raises الحارس as فاعل. **فُتح** is مجهول and raises الباب as نائب فاعل. **مفتوح** is اسم مفعول عامل supported by استفهام and raises الباب as نائب فاعل سدّ مسدّ الخبر in the selected account.'),
    T('3G-2', 'Use the account making شبه الجملة نائب الفاعل in **جِيءَ بخالدٍ**.', [
        ('جيء', 'فعل ماض مجهول', 'فعل ماض معلوم', 'اسم فاعل'),
        ('الباء', 'حرف جر', 'حرف نصب', 'ضمير في محل رفع'),
        ('خالد', 'اسم مجرور بالباء', 'اسم منصوب بجيء', 'مبتدأ مرفوع لفظًا'),
        ('بخالد', 'شبه جملة في محل رفع نائب فاعل', 'جملة فعلية في محل نصب حال', 'شبه جملة بلا علاقة بالفعل')
    ], '**جيء** فعل ماض مجهول مبني على الفتح؛ **الباء** حرف جر؛ **خالدٍ** اسم مجرور بالكسرة. The whole **بخالد** is شبه جملة في محل رفع نائب فاعل under the stated account. Its internal جر remains unchanged.'),
    Q('3I-1', 'Complete the change to المجهول: **كَتَبَ حامدٌ الخبرَ ← ...**',
      'كُتِبَ الخبرُ.', 'كَتَبَ الخبرُ.', 'كُتِبَ الخبرَ.',
      '**كُتِبَ الخبرُ** omits حامد and makes الخبر نائب فاعل مرفوعًا. The صرف pattern is كَتَبَ ← كُتِبَ. Changing only the اسم ending without changing ضبط الفعل does not produce the intended المجهول construction.'),
    T('3I-2', 'Complete the تركيب of **كُتِبتِ الرسالةُ**.', [
        ('كُتب', 'فعل ماض مجهول مبني على الفتح', 'فعل مضارع منصوب', 'اسم مفعول مجرور'),
        ('التاء', 'تاء التأنيث، ليست فاعلًا', 'ضمير في محل رفع فاعل', 'مفعول به متصل'),
        ('الرسالة', 'نائب فاعل مرفوع بالضمة', 'فاعل لفعل معلوم', 'مفعول به منصوب بالضمة')
    ], '**كُتب** فعل ماض مجهول؛ **التاء** تاء التأنيث الساكنة في الأصل، حُرّكت بالكسر للوصل والتخلّص من التقاء الساكنين؛ **الرسالةُ** نائب فاعل مرفوع. Do not confuse تاء التأنيث with تاء الفاعل in كتبتُ.'),
    Q('3R', 'Compare **حضر الضيفُ** and **أُكرم الضيفُ**. What stays the same and what changes?',
      'الضيف مرفوع in both؛ فاعل in the first and نائب فاعل in the second.',
      'الضيف فاعل in both because both end in ضمة.',
      'الضيف is منصوب in the second because its meaning receives an action.',
      '**حضر** is معلوم: الضيف فاعل. **أُكرم** is مجهول: الضيف نائب فاعل. Both roles have رفع; neither the visible ending alone nor a loose meaning-based label distinguishes them.'),
    Q('3-Read', '**قد يكون نائب الفاعل شبه جملة.** What does this permit in **جِيءَ بكتابٍ**?',
      'بكتاب في محل رفع نائب فاعل، وكتاب مجرور بالباء.',
      'كتاب must become كتابٌ after الباء.',
      'الباء becomes a ضمير فاعل.',
      'The statement concerns the محل of the whole **بكتاب**. Its internal construction remains **باء حرف جر + كتابٍ اسم مجرور**.')
 ],
 '4': [
    T('4G-1', 'Choose the relationships. For the last two rows, use المكتفي بمرفوعه.', [
        ('خالدٌ معلّمٌ: خالد', 'مبتدأ له خبر مستقل', 'فاعل لمعلّم', 'اسم إنّ'),
        ('أقائمٌ خالدٌ؟ قائم', 'مبتدأ عامل', 'فعل أمر', 'مفعول به'),
        ('أقائمٌ خالدٌ؟ خالد', 'فاعل سدّ مسدّ الخبر', 'خبر قائم في التحليل المختار', 'مضاف إليه')
    ], '**خالد معلّم** has an ordinary مبتدأ and separate خبر. In **أقائم خالد؟**, the selected analysis makes **قائم** مبتدأ and عاملًا لاسم بعده; **خالد** is فاعل سدّ مسدّ الخبر. It supplies completion without being an ordinary خبر in that same account.'),
    T('4G-2', 'Distinguish the two لام constructions.', [
        ('لَخالدٌ صادقٌ: اللام', 'لام الابتداء والتوكيد', 'لام الجر', 'لام الأمر الجازمة'),
        ('لِخالدٍ كتابٌ: خالد', 'اسم مجرور باللام', 'مبتدأ مرفوع لفظًا', 'اسم لا منصوب'),
        ('لَخالدٌ صادقٌ: خالد', 'مبتدأ مرفوع', 'اسم مجرور', 'مفعول به')
    ], '**لَـ** adds توكيد without governing جر; خالد remains مبتدأ مرفوعًا. **لِـ** in لخالدٍ is حرف جر, so خالد is مجرور؛ لخالد خبر مقدّم and كتاب مبتدأ مؤخّر. مجرّد عن عامل لفظي does not ban every preceding حرف.'),
    T('4I-1', 'Analyse **ما حاضرٌ أخواك** using المكتفي بمرفوعه.', [
        ('ما', 'حرف نفي', 'فعل ناقص', 'اسم موصول هنا'),
        ('حاضر', 'مبتدأ مرفوع، اسم فاعل اعتمد على النفي', 'خبر ما منصوب في هذا الضبط', 'حرف جر'),
        ('أخوا', 'فاعل سدّ مسدّ الخبر، مرفوع بالألف، وهو مضاف', 'مفعول به منصوب بالألف', 'خبر ثان منصوب'),
        ('الكاف', 'ضمير في محل جر مضاف إليه', 'فاعل في محل رفع', 'حرف استفهام')
    ], '**ما** حرف نفي؛ **حاضرٌ** مبتدأ واسم فاعل عامل اعتمد على النفي؛ **أخوا** فاعل سدّ مسدّ الخبر، مرفوع بالألف لأنه مثنّى، وحذفت النون للإضافة؛ **الكاف** مضاف إليه. No separate خبر is needed.'),
    Q('4I-2', 'In **أراغبٌ أنت؟**, which statement correctly handles the two accounts taught?',
      'أنت may be فاعلًا سدّ مسدّ الخبر, or مبتدأ مؤخّرًا with راغب خبرًا مقدّمًا.',
      'أنت must be مفعولًا به because راغب is an اسم.',
      'Both accounts make أنت simultaneously فاعلًا ومبتدأ in one تركيب.',
      'In the المكتفي account, **راغب** مبتدأ عامل and **أنت** فاعل سدّ مسدّ الخبر. In the other account, **أنت** مبتدأ مؤخّر and **راغب** خبر مقدّم. Each is a complete separate analysis; do not merge them.'),
    Q('4R', 'Analyse **أمفتوحٌ البابُ؟** using المكتفي بمرفوعه.',
      'مفتوح مبتدأ عامل؛ الباب نائب فاعل سدّ مسدّ الخبر.',
      'مفتوح فعل ماض؛ الباب مفعول به.',
      'مفتوح مبتدأ؛ الباب فاعل لاسم فاعل.',
      '**مفتوح** is اسم مفعول, so its مرفوع is **نائب فاعل**, not فاعل. Under the selected account, مفتوح مبتدأ and الباب نائب فاعل سدّ مسدّ الخبر.'),
    Q('4-Read', '**المبتدأ المكتفي بمرفوعه اسم عامل يرفع اسمًا بعد نفي أو استفهام.** What must be identified?',
      'The اسم عامل, its supporting نفي أو استفهام, and the مرفوع completing it.',
      'A separate خبر after every مرفوع, even when the كلام is already complete.',
      'An omitted إنّ before every اسم عامل.',
      'Identify the condition for عمل and the relationship of the مرفوع. The phrase **المكتفي بمرفوعه** means that this مرفوع supplies the needed completion; it does not call for an additional invented خبر.')
 ],
 '5': [
    T('5G-1', 'Match each نكرة مبتدأ to the stated reason it is مفيدة.', [
        ('طالبُ علمٍ حاضرٌ', 'تخصيص بالإضافة لفظًا', 'وقوعها بعد إذا الفجائية', 'دعاء'),
        ('عبدٌ مؤمنٌ خيرٌ من مشرك', 'تخصيص بالوصف لفظًا', 'نفي عام', 'تأخير عن خبر شبه جملة'),
        ('سلامٌ عليكم', 'دعاء', 'إضافة لفظية إلى معرفة', 'وقوعها بعد إذا الفجائية'),
        ('خرجت فإذا رجلٌ قاعدٌ', 'وقوعها بعد إذا الفجائية', 'إضافة رجل إلى قاعد', 'نصب رجل بإنّ')
    ], '**طالب علم** is specified by إضافة; **عبد مؤمن** by وصف. **سلام عليكم** is دعاء. In **فإذا رجل قاعد**, إذا الفجائية introduces the unexpected scene. These are different ways for a نكرة to be مفيدة.'),
    T('5G-2', 'Complete **في البيت رجل**.', [
        ('البيت', 'البيتِ: اسم مجرور', 'البيتُ: فاعل', 'البيتَ: مفعول به'),
        ('في البيت', 'خبر مقدّم، شبه جملة', 'مبتدأ منصوب', 'فعل محذوف لفظًا'),
        ('رجل', 'رجلٌ: مبتدأ مؤخّر', 'رجلًا: حال واجبة', 'رجلٍ: مضاف إليه للبيت')
    ], '**في البيتِ رجلٌ**: في حرف جر؛ البيت اسم مجرور؛ شبه الجملة خبر مقدّم متعلق بمحذوف تقديره كائن؛ رجل مبتدأ مؤخّر مرفوع. The preceding خبر supplies the setting for the نكرة.'),
    T('5I-1', 'Identify the condition without full vowel marks.', [
        ('كلّ يعمل؛ أي كل أحد', 'إضافة مقدّرة', 'إضافة ملفوظة بعد كل', 'إذا الفجائية'),
        ('طائفة قد أهمّتهم أنفسهم؛ أي طائفة منهم', 'وصف مقدّر', 'نعت ملفوظ بين طائفة وقد', 'دعاء'),
        ('ما أحد في البيت', 'عموم بعد النفي', 'تخصيص بالإضافة', 'وقوع بعد أمّا'),
        ('أإله مع الله؟', 'استفهام', 'دعاء', 'إضافة إله إلى مع')
    ], 'In **كلّ** the missing إضافة is understood as **كلّ أحد**. In **طائفة**, the specified account understands **منهم** as وصف. **ما أحد** has generality under نفي; **أإله** is introduced by استفهام. تقدير is a real interpretive distinction from words already expressed.'),
    Q('5I-2', 'Correct the claim: “طالب علم must be معرفة because it is مضاف.”',
      'إضافة طالب إلى النكرة علم specifies it but leaves it نكرة.',
      'Every إضافة makes both words معرفة.',
      'طالب علم cannot ever be مبتدأ because it is نكرة.',
      '**طالبُ علمٍ** is نكرة مخصوصة بالإضافة إلى نكرة. That specification can make it مفيدة as مبتدأ without turning it into معرفة. Do not confuse تخصيص with تعريف.'),
    Q('5R', 'Compare **المعلّم في الفصل** and **في الفصل معلّم**.',
      'المعلّم معرفة مبتدأ مقدّم؛ معلّم نكرة مبتدأ مؤخّر بعد خبر شبه جملة.',
      'في الفصل is فاعل in both.',
      'معلّم must be مضاف إليه because it follows الفصل.',
      'In **المعلّمُ في الفصلِ**, المعلّم معرفة مبتدأ. In **في الفصلِ معلّمٌ**, شبه الجملة is خبر مقدّم and معلّم نكرة مبتدأ مؤخّر. The جار ومجرور remains internally unchanged.'),
    Q('5-Read', '**قد يكون المبتدأ نكرة مفيدة.** What does مفيدة require?',
      'A construction or context making the statement informative.',
      'A word beginning with ال in every case.',
      'نصب المبتدأ whenever it lacks ال.',
      '**مفيدة** concerns the useful meaning supplied by context or construction, such as تخصيص، عموم، دعاء or a preceding خبر شبه جملة. It does not mean the نكرة has secretly become معرفة in every instance.')
 ],
 '6': [
    T('6G-1', 'Match the selected omitted مبتدأ account to its تقدير.', [
        ('من خالد؟ معلّمُنا', 'هو معلّمنا؛ حذف جائز لقرينة', 'معلّمنا هو؛ حذف الخبر واجب', 'يا معلّمنا؛ نداء واجب'),
        ('الحمد لله الحميدُ، مع قطع النعت', 'هو الحميد؛ حذف واجب', 'الحميد مجرور لفظًا هنا', 'إنّ الحميد؛ حذف إنّ واجب'),
        ('في ذمّتي لأقولنّ الصدق', 'في ذمتي عهدٌ؛ المبتدأ محذوف وجوبًا', 'ذمتي فاعل لأقولنّ', 'الصدق مبتدأ محذوف')
    ], 'The reply **معلّمنا** permits هو to be recovered from the question. With **الحميدُ** as النعت المقطوع إلى الرفع, هو is omitted وجوبًا. **في ذمّتي** is خبر مقدّم for an omitted مبتدأ عهدٌ; the following جواب supplies the قرينة القسم.'),
    T('6G-2', 'Analyse **نعم الطالب المجتهد** using المجتهد as خبر لمبتدأ محذوف.', [
        ('نعم', 'فعل ماض جامد للمدح', 'حرف جر', 'اسم إنّ'),
        ('الطالب', 'فاعل مرفوع', 'مفعول به منصوب', 'خبر لمبتدأ محذوف'),
        ('المجتهد', 'مخصوص بالمدح، خبر مرفوع', 'مفعول مطلق منصوب', 'فاعل ثان لنعم'),
        ('المبتدأ المحذوف', 'هو؛ حذفه واجب في التحليل المختار', 'أنا؛ حذفه ممنوع', 'نعم؛ فعل محذوف')
    ], '**نعم** فعل ماض جامد للمدح؛ **الطالب** فاعل؛ **المجتهد** مخصوص بالمدح وخبر لمبتدأ محذوف وجوبًا تقديره هو. The alternative مبتدأ مؤخّر account is valid but is not the one requested.'),
    T('6I-1', 'Recover the omitted مبتدأ in the specified accounts.', [
        ('من عمل صالحًا فلنفسه', 'فعملُه لنفسه', 'فنفسُه مفعول به للعمل', 'فلا مبتدأ ولا خبر هنا'),
        ('قالوا: أساطيرُ الأولين', 'هي أساطير الأولين', 'أساطيرًا مفعول مطلق لقالوا', 'كان أساطيرِ الأولين'),
        ('بئس الطالب الكسولُ، والكسول خبر', 'هو الكسولُ', 'يا الكسولَ', 'إنّ الكسولُ')
    ], 'After فاء الجواب, **فعملُه لنفسه** supplies the مبتدأ appropriate to the statement. After قول, **هي أساطير الأولين** explains the raised أساطير. In the selected ذم account, **الكسول** is خبر for هو محذوف وجوبًا.'),
    Q('6I-2', 'Choose the precise statement about **فصبرٌ جميلٌ**, analysed with صبر as خبر.',
      'The تقدير can be فصبري صبر جميل؛ one account requires حذف and another permits expressing المبتدأ.',
      'صبرٌ must be مفعولًا مطلقًا منصوبًا despite its ضمة.',
      'جميلٌ is always the omitted مبتدأ.',
      '**صبرٌ** is خبر in the selected account, **جميلٌ** نعت له, with a مبتدأ such as صبري understood. The construction presents enduring patience in place of wording like أصبر صبرًا جميلًا. Accounts differ on whether حذف المبتدأ is required; do not turn that difference into an absolute prohibition.'),
    Q('6R', 'What distinguishes **لله الحميدِ** from **الحمد لله الحميدُ** with قطع النعت?',
      'الحميدِ follows in جر؛ الحميدُ is خبر for an omitted هو.',
      'Both must be مجرور لفظًا because لله precedes them.',
      'The ضمة turns الحميد into a فعل.',
      'In the connected expression **لله الحميدِ**, the description follows the earlier مجرور. With **قطع النعت إلى الرفع**, **الحميدُ** belongs to an understood **هو الحميدُ**, and هو is omitted وجوبًا in this account.'),
    Q('6-Read', '**يحذف المبتدأ جوازًا لقرينة، ووجوبًا في مواضع مخصوصة.** Which claim respects the distinction?',
      'Context can permit حذف without requiring it.',
      'Every recoverable مبتدأ must be omitted.',
      'Every omitted مبتدأ is omitted without evidence.',
      '**جوازًا** allows an expressed or omitted مبتدأ when the قرينة supports it. **وجوبًا** belongs to specified constructions and analytical accounts. The presence of a قرينة does not by itself establish وجوب.')
 ],
 '7': [
    T('7G-1', 'Identify the خبر. In the final row use تعدّد الخبر.', [
        ('خالد معلّم', 'معلّم: خبر مفرد', 'خالد: خبر جملة', 'كلاهما حرفان'),
        ('خالد يقرأ', 'يقرأ مع فاعله: جملة في محل رفع خبر', 'يقرأ: اسم مجرور', 'خالد: مفعول به'),
        ('هو الغفور الودود', 'الغفور خبر أول والودود خبر ثان', 'الودود منصوب وجوبًا', 'الغفور والودود مضاف ومضاف إليه')
    ], '**معلّم** is خبر مفرد. **يقرأ** with hidden هو forms خبر جملة. In the specified تعدّد account, **الغفور** and **الودود** are two أخبار of هو. That question does not impose this account on every possible string of descriptions.'),
    T('7G-2', 'Complete the full تركيب of **لنا أعمالنا**.', [
        ('اللام', 'حرف جر', 'لام الابتداء', 'لام جزم'),
        ('نا في لنا', 'ضمير في محل جر باللام', 'مبتدأ في محل رفع', 'حرف لا محل له'),
        ('لنا', 'شبه جملة في محل رفع خبر مقدّم', 'مفعول به مقدّم', 'فعل ماض'),
        ('أعمال', 'مبتدأ مؤخّر مرفوع، وهو مضاف', 'فاعل مجرور', 'خبر إنّ منصوب'),
        ('نا في أعمالنا', 'ضمير في محل جر مضاف إليه', 'ضمير في محل نصب مفعول به', 'توكيد لفظي للام')
    ], '**لنا**: اللام حرف جر ونا ضمير مجرور بها؛ شبه الجملة خبر مقدّم متعلق بمحذوف تقديره كائنة. **أعمالُ** مبتدأ مؤخّر مرفوع ومضاف؛ **نا** مضاف إليه. The two occurrences of نا have different immediate relationships although both are في محل جر.'),
    Q('7I-1', 'Complete with the stated خبر مشتق: **الطالبان ...**',
      'مجتهدانِ', 'مجتهدٌ', 'مجتهدَيْنِ',
      '**الطالبان مجتهدان**: مجتهدان خبر مرفوع بالألف لأنه مثنّى, with a hidden ضمير referring to الطالبان. مجتهدٌ fails the intended مطابقة; مجتهدَين has the wrong إعراب for this خبر.'),
    Q('7I-2', 'A learner changes **نحن فتنةٌ** because نحن refers to several people. Choose the correction.',
      'Keep فتنةٌ: a جامد description can apply to the group without matching its number.',
      'Every خبر must have precisely the same number form as its مبتدأ.',
      'فتنة must be منصوب because نحن is a ضمير.',
      '**نحن** مبتدأ and **فتنةٌ** خبر مرفوع. The جامد فتنة describes the group as a trial, without the hidden ضمير relationship of a خبر مشتق requiring that form of مطابقة.'),
    Q('7R', 'Choose the correct roles and endings in **هذان طالبان**.',
      'هذان مبتدأ وطالبان خبر؛ كلاهما مرفوع بالألف.',
      'هذان فاعل وطالبان مفعول به منصوب بالألف.',
      'هذان خبر إنّ وطالبان اسمها.',
      '**هذان** اسم إشارة مبتدأ مرفوع بالألف, and **طالبان** خبر مرفوع بالألف لأنه مثنّى. The إشارة إلى اثنين and خبر show المطابقة. خبر مفرد in the three-way classification still includes طالبان because it is neither جملة nor شبه جملة.'),
    Q('7-Read', '**الأصل تأخير الخبر، وقد يتقدّم، وقد يتعدّد.** Which statement follows?',
      'A خبر can precede its مبتدأ, and one مبتدأ can have more than one خبر.',
      'The first written expression must always be مبتدأ.',
      'A second مرفوع must always be مضافًا إليه.',
      '**يتقدّم** permits تقديم الخبر, as in لنا أعمالنا. **يتعدّد** permits more than one خبر, as in the specified الغفور والودود analysis. Neither role is assigned solely by position.')
 ],
 '8': [
    T('8G-1', 'Identify the omitted خبر in each selected pattern.', [
        ('لعمرك لأقولنّ الصدق', 'قسمي؛ محذوف وجوبًا', 'عهدٌ؛ مبتدأ محذوف هنا', 'الصدق؛ مفعول به محذوف'),
        ('لولا خالد لرجعنا، مع معنى الوجود العام', 'موجود؛ محذوف وجوبًا', 'لرجعنا؛ خبر مفرد ملفوظ', 'خالد؛ محذوف جوازًا'),
        ('كل رجل وضيعته، والواو صريحة في المعية مع العطف', 'مقرونان؛ محذوف وجوبًا', 'ضيعته؛ مفعول معه منصوب في التحليل المختار', 'رجل؛ خبر منصوب')
    ], '**لعمرك** implies قسمي as خبر; the following جواب shows قسم. After **لولا**, the stated general existence خبر موجود is omitted وجوبًا. With the specified **واو المعية والعطف**, **مقرونان** is omitted وجوبًا because the connection is already conveyed.'),
    T('8G-2', 'Analyse **لولا خالدٌ لرجعنا** with an understood خبر of general existence.', [
        ('لولا', 'حرف امتناع لوجود', 'حرف جر', 'فعل ناقص'),
        ('خالد', 'مبتدأ مرفوع؛ الخبر موجود محذوف وجوبًا', 'فاعل لرجعنا', 'اسم لولا منصوب'),
        ('اللام في لرجعنا', 'واقعة في جواب لولا', 'لام الجر', 'لام الابتداء الداخلة على خالد'),
        ('رجعنا', 'فعل ماض ونا فاعل', 'فعل ماض بلا فاعل', 'مبتدأ وخبر')
    ], '**لولا** حرف امتناع لوجود؛ **خالدٌ** مبتدأ وخبره موجود محذوف وجوبًا. **اللام** في جواب لولا؛ **رجعنا** فعل ماض مبني على السكون ونا فاعل. The جواب is not the خبر for خالد.'),
    T('8I-1', 'Supply only the missing element. Use the stated accounts.', [
        ('من حاضر؟ خالد؛ خالد مبتدأ', 'حاضر: خبر محذوف جوازًا', 'هو: مبتدأ محذوف وجوبًا', 'إنّ: عامل محذوف وجوبًا'),
        ('خرجت فإذا الأسد؛ الأسد مبتدأ', 'موجود: خبر محذوف جوازًا', 'أسدًا: مفعول به محذوف', 'خرج: خبر محذوف وجوبًا'),
        ('خرجت فإذا أسد واقف؛ واقف خبر', 'الخبر ملفوظ؛ لا حاجة إلى تقدير خبر محذوف', 'موجود محذوف وجوبًا رغم وجود واقف', 'إنّ محذوفة وجوبًا')
    ], '**خالدٌ** answers the question with **حاضرٌ** understood as خبر. **فإذا الأسدُ** allows موجود to be supplied. In **فإذا أسدٌ واقفٌ**, واقف is already the خبر; do not invent another required omitted خبر.'),
    Q('8I-2', 'Does **خالد وسعيد حاضران** require حذف الخبر merely because it contains واو?',
      'No؛ it has ordinary عطف and an expressed خبر حاضران.',
      'Yes؛ every واو requires حذف الخبر.',
      'Yes؛ حاضران must instead be مفعولًا معه منصوبًا.',
      '**خالدٌ** مبتدأ، **سعيدٌ** معطوف عليه، **حاضران** خبر مرفوع بالألف. The special حذف pattern requires واو conveying the specified معية relationship, not every ordinary عطف.'),
    Q('8R', 'Compare **في ذمتي لأقولنّ الصدق** and **لعمرك لأقولنّ الصدق** using the accounts taught.',
      'The first omits مبتدأ عهدٌ؛ the second omits خبر قسمي.',
      'Both omit the same مفعول به.',
      'The first omits خبر and the second omits مبتدأ عمر.',
      '**في ذمّتي عهدٌ** has an omitted مبتدأ. **لعمرك قسمي** has an omitted خبر. The قسم meaning alone does not identify which role is missing; inspect the expressed structure.'),
    Q('8-Read', '**يحذف الخبر وجوبًا بعد لولا إذا دلّ على وجود عام.** Which limitation must be retained?',
      'The specified خبر conveys general existence.',
      'Every possible خبر after لولا has exactly this meaning.',
      'لولا is a فعل that makes خالد منصوبًا.',
      'The condition **إذا دلّ على وجود عام** restricts the rule taught. In **لولا خالد لرجعنا**, the understood موجود fits it; do not erase the condition and claim that every conceivable خبر is covered.')
 ],
 '9': [
    T('9G-1', 'Match the فاء construction to its pattern.', [
        ('أمّا خالد فمجتهد', 'فاء جواب أمّا', 'فاء جازمة لمجتهد', 'فاء حرف جر'),
        ('الذي يجتهد فله أجر', 'مبتدأ موصول متضمّن معنى الشرط', 'لا يوجد مبتدأ', 'الذي حرف نصب'),
        ('طالب يجتهد فله أجر، مع المعنى العام المشروط', 'نكرة موصوفة بفعل', 'معرفة باللام', 'قسم بالمصدر'),
        ('كل يتيم فله في قلبي رأفة', 'كل مضافة إلى نكرة', 'مفعول مطلق مقدّم', 'اسم لا لنفي الجنس')
    ], '**أمّا** has its linking فاء. **الذي** is اسم موصول with the intended general معنى الشرط. **طالب يجتهد** is نكرة موصوفة بفعل; **كل يتيم** is كل مضافة إلى نكرة. These conditions explain the link; فاء alone does not govern جزم.'),
    T('9G-2', 'Complete the تركيب of **أمّا خالد فمجتهد**.', [
        ('أمّا', 'حرف شرط وتفصيل وتوكيد', 'فعل ماض ناقص', 'اسم إشارة'),
        ('خالد', 'مبتدأ مرفوع بالضمة', 'اسم أمّا منصوب', 'مفعول به'),
        ('الفاء', 'رابطة لجواب أمّا', 'حرف جر', 'عامل نصب في مجتهد'),
        ('مجتهد', 'خبر مرفوع بالضمة', 'مضارع مجزوم', 'فاعل لأمّا')
    ], '**أمّا** حرف شرط وتفصيل وتوكيد؛ **خالدٌ** مبتدأ؛ **الفاء** رابطة لجواب أمّا؛ **مجتهدٌ** خبر. The فاء connects the statement without changing خبر to a different role.'),
    T('9I-1', 'Read each example with its stated general معنى الشرط. Identify the structure allowing فاء.', [
        ('الطالب الذي يجتهد فله أجر', 'مبتدأ موصوف بموصول صلته فعل', 'لا موصول في الكلام', 'مبتدأ مضاف إلى معرفة'),
        ('طالب في الفصل فله كتاب', 'نكرة موصوفة بظرف', 'نكرة غير موصوفة بلا قرينة', 'فعل مجهول'),
        ('أمّ يتيم يتعلّم فلها عون، ويتعلّم وصف ليتيم', 'مضاف إلى نكرة موصوفة بفعل', 'أمّ مفعول به مقدّم', 'يتيم خبر إنّ')
    ], 'The first has **الطالب** described by **الذي يجتهد**. In the second, **في الفصل** describes طالب before the linked outcome. In the third, **أمّ** is مضاف إلى **يتيمٍ** described by **يتعلّم**. Read each in the general معنى الشرط stipulated, not as a licence for فاء after every ordinary specific اسم.'),
    T('9I-2', 'Analyse **الذي يجتهد فله أجر**. Distinguish the outer and inner relationships.', [
        ('الذي', 'اسم موصول في محل رفع مبتدأ', 'حرف جر', 'خبر مؤخّر'),
        ('يجتهد مع فاعله المستتر', 'صلة الموصول لا محل لها', 'خبر إنّ منصوب', 'مفعول به'),
        ('له داخل له أجر', 'خبر مقدّم', 'فاعل', 'اسم لا'),
        ('أجر داخل له أجر', 'مبتدأ مؤخّر', 'مفعول مطلق', 'مضاف إليه للهاء'),
        ('له أجر كاملة', 'جملة في محل رفع خبر الذي، مرتبطة بالفاء', 'جملة في محل جر مضاف إليه', 'صلة ثانية لا محل لها')
    ], '**الذي** مبتدأ؛ **يجتهد** مضارع مرفوع وفاعله المستتر هو، والجملة صلة الموصول لا محل لها. الفاء تربط الخبر. Within **له أجرٌ**, له خبر مقدّم وأجر مبتدأ مؤخّر؛ the whole جملة is في محل رفع خبر الذي.'),
    Q('9R', 'Correct: “The فاء in **الذي يجتهدُ فله أجرٌ** makes يجتهد مجزومًا.”',
      'يجتهد مرفوع؛ this فاء links the خبر and is not a جازم.',
      'Correct؛ any فاء makes every earlier مضارع مجزومًا.',
      'يجتهد is مجرور because it precedes له.',
      '**يجتهدُ** remains مضارعًا مرفوعًا لخلوّه من ناصب وجازم. The فاء links the خبر in the stated معنى الشرط; it is not a جازم and does not reach back to change the فعل ending.'),
    Q('9-Read', '**قد يتضمّن المبتدأ معنى الشرط فيصحّ دخول الفاء في خبره.** What does فيصحّ mean here?',
      'The stated معنى الشرط permits the linking فاء.',
      'Every مبتدأ always requires فاء.',
      'فاء makes every following اسم منصوبًا.',
      '**فيصحّ** states permissibility under the specified meaning and construction. **قد يتضمّن** does not say that every مبتدأ has معنى الشرط. Retain the actual condition.')
 ],
 '10': [
    T('10G-1', 'Match each مرفوع to its role.', [
        ('كان خالدٌ حاضرًا: خالد', 'اسم فعل ناقص', 'خبر كان', 'مفعول به'),
        ('ما هذا بشرًا: هذا', 'اسم ما المشبهة بليس في محل رفع', 'خبر ما منصوب', 'مفعول مطلق'),
        ('إنّ خالدًا حاضرٌ: حاضر', 'خبر حرف مشبّه بالفعل', 'اسم إنّ', 'فاعل إنّ'),
        ('لا عملَ مراءٍ مقبولٌ: مقبول', 'خبر لا لنفي الجنس', 'اسم لا', 'مضاف إليه')
    ], 'The four remaining مرفوعات are **اسم الأفعال الناقصة، اسم الحروف المشبهة بليس، خبر الحروف المشبهة بالفعل، خبر لا لنفي الجنس**. In ما هذا بشرًا, هذا is مبني في محل رفع اسم ما; it does not acquire a visible ضمة.'),
    T('10G-2', 'Complete the تركيب of **إنّ في ذلك لعبرةً**.', [
        ('إنّ', 'حرف ينصب الاسم ويرفع الخبر', 'حرف يرفع الاسم وينصب الخبر', 'فعل ناقص'),
        ('ذلك', 'اسم إشارة في محل جر بفي', 'اسم إنّ في محل نصب هنا', 'فاعل في محل رفع'),
        ('في ذلك', 'خبر إنّ مقدّم في محل رفع', 'اسم إنّ منصوب لفظًا', 'مفعول مطلق'),
        ('اللام', 'اللام المزحلقة للتوكيد', 'لام الجر', 'لام الأمر'),
        ('عبرة', 'اسم إنّ مؤخّر منصوب بالفتحة', 'خبر إنّ مرفوع بالفتحة', 'مبتدأ مجرور باللام')
    ], '**إنّ** تنصب الاسم وترفع الخبر. **في** حرف جر و**ذلك** اسم إشارة في محل جر؛ شبه الجملة في محل رفع خبر إنّ مقدّم. **اللام** مزحلقة للتوكيد؛ **عبرةً** اسم إنّ مؤخّر منصوب. The لام does not cancel the عمل of إنّ.'),
    T('10I-1', 'Choose the endings with the intended عمل explicitly stated.', [
        ('لا المشبهة بليس: لا شيء... مشابه... لله', 'شيءٌ مشابهًا', 'شيءَ مشابهٌ', 'شيءٍ مشابهٍ'),
        ('لا لنفي الجنس: لا عمل... مراء... مقبول...', 'عملَ مراءٍ مقبولٌ', 'عملُ مراءً مقبولًا', 'عملٍ مراءٌ مقبولٍ'),
        ('إنّ: إنّ خالد... لصادق...', 'خالدًا لصادقٌ', 'خالدٌ لصادقًا', 'خالدٍ لصادقٍ')
    ], '**لا شيءٌ مشابهًا لله** uses عمل ليس: اسم مرفوع وخبر منصوب. **لا عملَ مراءٍ مقبولٌ** uses لا لنفي الجنس: اسمها المضاف منصوب وخبرها مرفوع. **إنّ خالدًا لصادقٌ** retains اسم إنّ منصوبًا وخبرها مرفوعًا despite اللام المزحلقة.'),
    T('10I-2', 'Read **إنّ هذا لهو الحقّ. لا شكّ في ذلك. لا ضير**. Use هو as ضمير فصل and supply a general existence خبر for لا ضير.', [
        ('هو', 'ضمير فصل لا محل له', 'اسم إنّ ثان منصوب', 'خبر إنّ الوحيد في هذا التحليل'),
        ('الحقّ', 'خبر إنّ مرفوع', 'فاعل لهو', 'مفعول به منصوب'),
        ('شكّ', 'اسم لا مبني على الفتح في محل نصب', 'اسم لا مرفوع بالضمة', 'مفعول مطلق'),
        ('في ذلك', 'خبر لا شبه جملة في محل رفع', 'اسم لا في محل جر', 'فاعل مستتر'),
        ('خبر لا ضير', 'محذوف مفهوم؛ تقديره موجود عليكم', 'ضير نفسه خبر لا', 'محذوف وجوبًا في كل تركيب مع لا')
    ], 'In the specified account **هو** is ضمير فصل لا محل له and **الحقُّ** خبر إنّ. **شكَّ** is اسم لا مبني على الفتح في محل نصب, with **في ذلك** as خبرها. **لا ضيرَ** has a contextually understood خبر such as موجود عليكم; such حذف is common, not a blanket requirement after لا.'),
    Q('10R', 'Compare **لا رجلَ في البيت** and **لا طالبَ علمٍ في البيت**.',
      'رجل مبني على الفتح في محل نصب؛ طالب اسم لا منصوب لأنه مضاف، وعلم مضاف إليه.',
      'Both رجل and طالب are مرفوع because خبر لا is مرفوع.',
      'علم مفعول به للا، وطالب مبني على الكسر.',
      '**رجلَ** is the non-added اسم لا: مبني على الفتح في محل نصب. **طالبَ** is مضاف and therefore اسم لا منصوب بالفتحة؛ **علمٍ** مضاف إليه. **في البيت** supplies خبر لا in both.'),
    Q('10-Read', '**اسم الأفعال الناقصة مرفوع، وخبر الحروف المشبهة بالفعل مرفوع.** Apply this to **كان حامدٌ صادقًا. إنّ حامدًا صادقٌ**.',
      'حامد اسم كان مرفوع؛ صادق خبر إنّ مرفوع.',
      'حامد خبر كان وصادق اسم إنّ.',
      'Both عوامل raise their اسم and put their خبر in نصب.',
      '**كان** raises اسمها حامدٌ and assigns نصب to خبرها صادقًا. **إنّ** assigns نصب to اسمها حامدًا and raises خبرها صادقٌ. Name the عامل before assigning the role.')
 ],
 'R': [
    T('A1', 'Identify all eight مرفوعات from their relationships.', [
        ('وصل المسافرُ: المسافر', 'فاعل', 'نائب فاعل', 'خبر'),
        ('فُتح البابُ: الباب', 'نائب فاعل', 'فاعل', 'اسم إنّ'),
        ('المسافرُ متعبٌ: المسافر', 'مبتدأ', 'اسم لا', 'مفعول به'),
        ('المسافر متعبٌ: متعب', 'خبر', 'مبتدأ', 'مضاف إليه'),
        ('كان المسافرُ متعبًا: المسافر', 'اسم فعل ناقص', 'خبر كان', 'نائب فاعل'),
        ('ما هذا بشرًا: هذا', 'اسم حرف مشبّه بليس', 'خبر ما', 'فاعل'),
        ('إنّ المسافر متعبٌ: متعب', 'خبر حرف مشبّه بالفعل', 'اسم إنّ', 'حال'),
        ('لا عملَ مراءٍ مقبولٌ: مقبول', 'خبر لا لنفي الجنس', 'اسم لا', 'مضاف إليه')
    ], 'The roles in order are **فاعل، نائب فاعل، مبتدأ، خبر، اسم فعل ناقص، اسم حرف مشبّه بليس، خبر حرف مشبّه بالفعل، خبر لا لنفي الجنس**. هذا has محل رفع because it is مبني. The others identified here show رفع لفظًا.'),
    Q('A2', 'Which account correctly distinguishes the missing roles in **معلّمنا** as a reply to من خالد؟ and **خالد** as a reply to من حاضر؟ Assume the expressed word is خبر in the first and مبتدأ in the second.',
      'هو معلّمنا: مبتدأ محذوف؛ خالد حاضر: خبر محذوف. Both حذف cases are جائز with context.',
      'Both omit a فاعل وجوبًا.',
      'Both omit إنّ because no written عامل appears.',
      'The first retains خبر **معلّمنا** and recovers مبتدأ **هو**. The second retains مبتدأ **خالد** and recovers خبر **حاضر**. Both rely on قرينة السؤال and permit the omitted expression to be stated.'),
    T('B1', 'Choose the correct endings and relationships.', [
        ('سُلّم الكتاب...؛ الفعل مجهول', 'الكتابُ: نائب فاعل', 'الكتابَ: مفعول به', 'الكتابِ: مضاف إليه'),
        ('إنّ في الصبر لعبر...؛ use عبرة', 'لعبرةً: اسم إنّ مؤخّر', 'لعبرةٌ: مبتدأ تلغيه إنّ', 'لعبرةٍ: مجرور بلام الجر'),
        ('أكرم سعيد... أخو...؛ الهاء تعود إلى سعيد', 'سعيدًا أخوهُ؛ مفعول به ثم فاعل', 'سعيدٌ أخاهُ؛ مع بقاء سعيد مفعولًا به', 'سعيدٍ أخيهِ؛ كلاهما مجرور'),
        ('كل رجل وضيعته؛ عطف مع واو صريحة في المعية', 'ضَيْعَتُهُ معطوف مرفوع؛ الخبر مقرونان محذوف', 'ضَيْعَتَهُ مفعول معه مع إبقاء تحليل العطف نفسه', 'ضَيْعَتِهِ مجرور بالواو')
    ], '**سُلّم الكتابُ** raises نائب الفاعل. **إنّ في الصبر لعبرةً** retains نصب اسم إنّ after اللام المزحلقة. **أكرم سعيدًا أخوه** puts المفعول before الفاعل containing the referring هاء. In the selected **كل رجل وضيعته** account, ضيعتُه معطوف مرفوع and مقرونان خبر محذوف وجوبًا.'),
    Q('B2', 'Choose the only accurate correction of these claims: “Every مبتدأ must be معرفة; every خبر must follow it; every واو requires حذف الخبر.”',
      'A نكرة مفيدة can be مبتدأ; خبر can precede it; the special واو rule requires the specified معنى المعية.',
      'Only the first claim needs correction; the other two are always true.',
      'All three are true without conditions.',
      '**في البيت رجلٌ** has a نكرة مبتدأ after خبر مقدّم. **خالد وسعيد حاضران** has an ordinary واو and an expressed خبر. Each original claim incorrectly removes an important condition or permitted variation.'),
    T('C1', 'اقرأ: **خرجت فإذا رجل واقف. أكرمه حامد. فُتح الباب. أمّا الرجل فمتعب.** اختر التركيب المناسب. In the first جملة, take واقف as the expressed خبر.', [
        ('التاء في خرجتُ', 'ضمير في محل رفع فاعل', 'تاء التأنيث بلا محل', 'مفعول به'),
        ('إذا', 'إذا الفجائية', 'إذا الشرطية للمستقبل هنا', 'حرف جر'),
        ('رجل واقف', 'رجل مبتدأ وواقف خبر؛ النكرة بعد إذا الفجائية', 'رجل فاعل وواقف مفعول به', 'رجل اسم إنّ وواقف خبرها'),
        ('الهاء في أكرمه', 'مفعول به متصل يعود إلى رجل', 'فاعل متصل يعود إلى حامد', 'مضاف إليه لفعل أكرم'),
        ('حامد', 'فاعل مؤخّر مرفوع', 'مبتدأ مؤخّر عن أكرم', 'مفعول به منصوب'),
        ('الباب', 'نائب فاعل مرفوع لفُتح', 'فاعل لفعل معلوم', 'اسم كان محذوفة'),
        ('الرجل بعد أمّا', 'مبتدأ مرفوع', 'اسم أمّا منصوب', 'مضاف إليه'),
        ('فمتعب', 'الفاء رابطة؛ متعب خبر مرفوع', 'الفاء جازمة؛ متعب فعل', 'الفاء حرف جر؛ متعب مجرور')
    ], '**خرجتُ** فعل ماض والتاء فاعل. **إذا** فجائية؛ **رجلٌ** مبتدأ نكرة مفيدة بهذا السياق و**واقفٌ** خبر ملفوظ. **أكرمَه حامدٌ**: الهاء مفعول به متصل، وحامد فاعل مؤخّر. **فُتح البابُ**: فعل مجهول ونائب فاعل. **أمّا الرجلُ فمتعبٌ**: أمّا حرف شرط وتفصيل وتوكيد؛ الرجل مبتدأ؛ الفاء رابطة؛ متعب خبر. The recurring word الرجل keeps its reference while its relationships change.'),
    T('C2', 'التركيب الكامل: **إنّ في البيت لطالبَ علمٍ. كان الطالبُ مجتهدًا.**', [
        ('إنّ', 'حرف مشبّه بالفعل ينصب الاسم ويرفع الخبر', 'فعل ناقص', 'حرف جر'),
        ('في البيت', 'في حرف جر والبيت مجرور؛ شبه الجملة خبر إنّ مقدّم', 'البيت اسم إنّ منصوب', 'شبه الجملة فاعل لإنّ'),
        ('اللام', 'مزحلقة للتوكيد', 'لام جر', 'لام أمر'),
        ('طالبَ', 'اسم إنّ مؤخّر منصوب، وهو مضاف', 'خبر إنّ منصوب', 'فاعل منصوب'),
        ('علمٍ', 'مضاف إليه مجرور', 'نعت مرفوع', 'مفعول به'),
        ('كان', 'فعل ماض ناقص مبني على الفتح', 'حرف مشبّه بالفعل', 'اسم موصول'),
        ('الطالب', 'اسم كان مرفوع بالضمة', 'فاعل كان التامة في هذه الجملة', 'خبر كان مرفوع'),
        ('مجتهدًا', 'خبر كان منصوب بالفتحة', 'مفعول به ثان', 'خبر إنّ مرفوع بالفتحة')
    ], '**إنّ** حرف ينصب الاسم ويرفع الخبر؛ **في البيتِ** جار ومجرور متعلق بمحذوف في محل رفع خبر إنّ مقدّم؛ **اللام** مزحلقة؛ **طالبَ** اسم إنّ مؤخّر منصوب ومضاف؛ **علمٍ** مضاف إليه. **كان** فعل ماض ناقص؛ **الطالبُ** اسمها مرفوع؛ **مجتهدًا** خبرها منصوب. اللام المزحلقة does not remove the نصب of طالب.'),
    T('D1', 'صل العبارة بتطبيقها الصحيح.', [
        ('نكرة مفيدة بتقديم الخبر', 'في الدار ضيفٌ', 'إنّ ضيفًا حاضرٌ', 'حضر الضيفُ'),
        ('مبتدأ مكتفٍ بمرفوعه؛ اختر هذا التحليل', 'أقائمٌ حامدٌ؟ قائم مبتدأ وحامد فاعل سدّ مسدّ الخبر', 'حامد قائم؛ حامد مفعول به', 'إنّ حامدًا قائم؛ قائم اسم إنّ'),
        ('خبر محذوف وجوبًا لدلالته على وجود عام بعد لولا', 'لولا حامد لخرجنا؛ التقدير حامد موجود', 'حامد موجود؛ الخبر محذوف', 'خرج حامد؛ حامد خبر'),
        ('نائب فاعل لاسم مفعول عامل؛ اختر المكتفي بمرفوعه', 'أمكتوبٌ الخبرُ؟ الخبر نائب فاعل', 'كَتب حامد الخبر؛ الخبر نائب فاعل', 'الخبر مكتوب؛ الخبر مفعول به')
    ], '**في الدار ضيفٌ** licenses the نكرة through خبر مقدّم. In the specified accounts, **حامد** completes قائم as فاعل, while **الخبر** completes مكتوب as نائب فاعل. **لولا حامد لخرجنا** has خبر موجود محذوف وجوبًا under the stated general existence condition.'),
    Q('D2', '**لا يلزم من الجرّ في اللفظ انتفاء الفاعلية، ولا من الرفع اتّحاد الموقع الإعرابي.** اختر التطبيق الصحيح.',
      'بشيرٍ في ما جاء من بشيرٍ فاعل؛ خالدٌ في حضر خالد وكان خالد حاضرًا مرفوع مع اختلاف الموقع.',
      'كل مجرور لفظًا مضاف إليه، وكل مرفوع مبتدأ.',
      'حضر خالد وكان خالد حاضرًا لهما التركيب نفسه في جميع الكلمات.',
      '**انتفاء الفاعلية** means absence of the فاعل relationship; **اتّحاد الموقع** means having the same role. بشيرٍ is فاعل despite visible جر after من الزائدة. خالدٌ is فاعل after حضر but اسم كان after كان; shared رفع does not make the roles identical.')
 ]
}
