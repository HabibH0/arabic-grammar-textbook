"""Module 17: single-answer choices with explicit scope and worked solutions."""
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
    T('1G-1', 'Classify by formation in the three-part division used here.', [
        ('شُكْرٌ', 'مصدر', 'اسم فاعل', 'جامد'),
        ('شاكرٌ', 'مشتق', 'مصدر', 'جامد'),
        ('قلمٌ', 'جامد', 'اسم مفعول', 'مصدر'),
        ('مفتاحٌ', 'مشتق: اسم آلة', 'جامد لمجرد أنه شيء محسوس', 'مصدر')
    ], '**شكر** is مصدر؛ **شاكر** مشتق؛ **قلم** جامد in this division. **مفتاح** is اسم آلة and therefore مشتق, even though it names a physical thing. Do not substitute اسم عين/اسم معنى for the formation classification.'),
    T('1G-2', 'Match the five مشتقات بمعنى الفعل.', [
        ('شاكر', 'اسم فاعل', 'اسم مفعول', 'اسم تفضيل'),
        ('مشكور', 'اسم مفعول', 'اسم فاعل', 'اسم آلة'),
        ('حسن', 'صفة مشبّهة', 'اسم ظرف', 'مصدر'),
        ('شكور', 'اسم مبالغة', 'اسم آلة', 'جامد'),
        ('أفضل', 'اسم تفضيل', 'اسم مفعول', 'مصدر')
    ], 'The forms are **اسم فاعل، اسم مفعول، صفة مشبّهة، اسم مبالغة، اسم تفضيل** respectively. All five are classified as مشتق بمعنى الفعل; actual عمل still requires the relevant construction.'),
    Q('1I-1', 'In **المفتاحُ عندَ خالدٍ**, which account of المفتاح is correct?',
      'مشتق بغير معنى الفعل؛ اسم آلة، وهو مبتدأ هنا.',
      'جامد لأنّه مبتدأ.',
      'مصدر لأنّ الفعل فتح له المعنى نفسه.',
      '**المفتاحُ** is اسم آلة, a مشتق بغير معنى الفعل in this division. It is also معرفة بأل and مبتدأ مرفوع. Formation, identification and sentence role are separate questions.'),
    T('1I-2', 'Analyse **سعيدٌ كاتبٌ رسالةً الآنَ**, with كاتب expressing his current action.', [
        ('كاتبٌ: formation', 'اسم فاعل', 'اسم آلة', 'مصدر'),
        ('كاتبٌ: sentence role', 'خبر مرفوع بالضمة', 'مفعول به منصوب', 'فاعل لسعيد'),
        ('فاعل كاتب', 'ضمير مستتر تقديره هو، يعود إلى سعيد', 'رسالة', 'الآن'),
        ('رسالةً', 'مفعول به لاسم الفاعل منصوب', 'مضاف إليه لكاتب', 'نائب فاعل مرفوع')
    ], '**سعيدٌ** مبتدأ؛ **كاتبٌ** خبر واسم فاعل supported by the مبتدأ and the current meaning. Its فاعل is hidden هو. **رسالةً** مفعول به منصوب. **الآن** ظرف زمان مبني على الفتح في محل نصب. The supplied meaning and construction justify the عمل.'),
    Q('1R', 'In **سائغٌ شرابُه**, شراب has the contextual meaning المشروب. What follows?',
      'A مصدر can express معنى اسم المفعول without taking its visible pattern.',
      'شراب must be changed to مشروب in the original wording.',
      'Every مصدر is an اسم آلة.',
      'A مصدر can be used for مبالغة في الوصف with معنى اسم الفاعل or اسم المفعول. Here **شراب** is understood as **المشروب**; meaning and visible pattern must be distinguished.'),
    Q('1-Read', '**المشتق بغير معنى الفعل** includes which pair?',
      'اسم الظرف واسم الآلة.', 'اسم الفاعل واسم المفعول.', 'الجامد والمصدر.',
      '**مسجد** and **مفتاح** illustrate اسم الظرف and اسم الآلة. They remain مشتقات, although placed in the بغير معنى الفعل group.')
 ],
 '2': [
    T('2G-1', 'Match each expression to the intended قسم المعرفة.', [
        ('هو', 'ضمير', 'علم', 'اسم إشارة'),
        ('خالد، اسم شخص', 'علم', 'ضمير', 'اسم موصول'),
        ('الكتاب', 'معرّف بأل', 'اسم إشارة', 'ضمير'),
        ('هذا', 'اسم إشارة', 'علم', 'نكرة'),
        ('الذي', 'اسم موصول', 'ضمير متصل', 'مصدر'),
        ('كتاب خالد: كتاب في هذه الإضافة', 'مضاف إلى معرفة', 'نكرة محضة', 'ضمير')
    ], 'The six groups are **ضمير، علم، معرّف بأل، اسم إشارة، اسم موصول، مضاف إلى معرفة**. In كتاب خالد, كتاب gains تعريف through ordinary إضافة to the علم خالد.'),
    T('2G-2', 'Choose the محل and role of each ضمير in **أنتَ شكرتَهُ في بيتِهِ**.', [
        ('أنت', 'في محل رفع مبتدأ', 'في محل نصب مفعول به', 'في محل جر'),
        ('التاء في شكرتَه', 'في محل رفع فاعل', 'حرف تأنيث لا محل له', 'في محل جر مضاف إليه'),
        ('الهاء في شكرتَه', 'في محل نصب مفعول به', 'في محل رفع فاعل', 'حرف خطاب'),
        ('الهاء في بيتِه', 'في محل جر مضاف إليه', 'في محل نصب مفعول به', 'في محل رفع خبر')
    ], '**أنت** مبتدأ؛ **التاء** فاعل؛ the first **هاء** is مفعول به; the second is مضاف إليه. The جملة شكرتَه في بيته supplies خبر أنت في محل رفع. All the ضمائر are مبنية.'),
    Q('2I-1', 'A teacher addresses several female students. Complete **___ حفظتنَّ الدرسَ** with the matching منفصل للرفع.',
      'أنتنَّ', 'إيّاكنَّ', 'هنَّ',
      '**أنتنّ حفظتنّ الدرس** addresses مخاطبات. أنتنّ is في محل رفع مبتدأ and the following جملة is خبرها. **إيّاكنّ** is the نصب form; **هنّ** refers to غائبات.'),
    T('2I-2', 'Read **هو شكرني. كتابه عندي.** Identify the highlighted units.', [
        ('النون في شكرني', 'نون الوقاية، حرف لا محل له', 'ضمير في محل رفع فاعل', 'ياء المتكلم'),
        ('الياء في شكرني', 'ضمير في محل نصب مفعول به', 'ضمير في محل جر مضاف إليه', 'حرف مضارعة'),
        ('الهاء في كتابه', 'ضمير في محل جر مضاف إليه', 'ضمير في محل نصب مفعول به', 'فاعل'),
        ('الياء في عندي', 'ضمير في محل جر مضاف إليه', 'ضمير منفصل للنصب', 'حرف جر')
    ], '**شكرني** contains نون الوقاية followed by ياء المتكلّم في محل نصب. In **كتابه** and **عندي**, الهاء والياء are attached to أسماء as مضاف إليه. The same person can be represented in different محال.'),
    Q('2R', 'Which order matches the stated ranking among ضمائر?',
      'المتكلّم ثم المخاطب ثم الغائب.', 'الغائب ثم المخاطب ثم المتكلّم.', 'كل ضمير أقل تعريفًا من كل علم.',
      'Among ضمائر, **المتكلّم أعرف، ثم المخاطب، ثم الغائب**. This order will matter when comparing two ضمائر that are مفعولان.'),
    Q('2-Read', '**الضمير المجرور متصل لا غير.** Which inference is correct?',
      'له and كتابه can contain a مجرور ضمير; إيّاه is not a مجرور منفصل form.',
      'Every هاء attached to a فعل is مجرورة.',
      'A متصل ضمير can never have محل نصب.',
      'The statement classifies forms with محل جر. It does not assign جر to every متصل: **شكره** has هاء في محل نصب, whereas **له** has هاء في محل جر باللام.')
 ],
 '3': [
    T('3G-1', 'Distinguish the تاء and identify the فاعل.', [
        ('شَكَرْتُ', 'التاء ضمير بارز في محل رفع فاعل', 'التاء حرف تأنيث؛ الفاعل هي', 'الفاعل ضمير مستتر أنا'),
        ('شَكَرَتْ، دون اسم ظاهر بعدها', 'التاء حرف تأنيث؛ الفاعل مستتر هي', 'التاء ضمير المتكلّم', 'لا فاعل للفعل'),
        ('شَكَرَتْ هندٌ', 'هند فاعل ظاهر، ولا فاعل مستتر معه', 'التاء فاعل وهند مفعول به', 'فاعل مستتر هي وهند فاعل ثان')
    ], '**شكرتُ** has تاء الفاعل. **شكرتْ** has تاء التأنيث الساكنة, a حرف; the فاعل is hidden هي if no اسم ظاهر supplies it. In **شكرتْ هندٌ**, هند is that فاعل ظاهر.'),
    T('3G-2', 'Identify the hidden ضمير and the حكم الاستتار in these uses.', [
        ('أشكرُ', 'أنا، مستتر وجوبًا', 'هو، مستتر جوازًا', 'التاء، بارز'),
        ('نشكرُ', 'نحن، مستتر وجوبًا', 'نون النسوة، بارز', 'هو، مستتر جوازًا'),
        ('اشكرْ، لمخاطب مفرد مذكّر', 'أنت، مستتر وجوبًا', 'أنا، مستتر جوازًا', 'واو الجماعة، بارز'),
        ('خالدٌ يشكرُ: فاعل يشكر', 'هو، مستتر جوازًا', 'خالد فاعل ظاهر متأخر عن يشكر', 'لا يحتاج يشكر إلى فاعل')
    ], '**أشكر، نشكر، اشكر** contain أنا، نحن، أنت with واجب الاستتار in these forms. In **خالد يشكر** the فعل has hidden هو returning to the مبتدأ خالد. The غائب form also permits a فاعل ظاهر in **يشكر خالد**.'),
    T('3I-1', 'Match the بارز ضمير to its form.', [
        ('الطالبان يشكران: ضمير يشكران', 'ألف الاثنين', 'نون الوقاية', 'ضمير مستتر هما'),
        ('الطلاب يشكرون: ضمير يشكرون', 'واو الجماعة', 'نون النسوة', 'ضمير مستتر هم'),
        ('الطالبات يشكرن: ضمير يشكرن', 'نون النسوة', 'نون الوقاية', 'ألف الاثنين'),
        ('أنتِ تشكرين: ضمير تشكرين', 'ياء المخاطبة', 'ياء المتكلّم', 'ضمير مستتر أنتِ')
    ], 'The فاعل is expressed by **ألف الاثنين، واو الجماعة، نون النسوة، ياء المخاطبة** respectively. Do not add a hidden فاعل alongside these بارز ضمائر.'),
    Q('3I-2', 'In **سعيدٌ مشكورٌ**, use اسم المفعول بمعنى الفعل. What is the internal role of the hidden هو in مشكور?',
      'نائب فاعل يعود إلى سعيد.', 'مفعول به يعود إلى سعيد.', 'فاعل لسعيد لأنه فعل ماض.',
      '**مشكورٌ** is خبر مرفوع and اسم مفعول; its hidden هو is نائب فاعل. The corresponding hidden هو in **سعيد شاكر** would be فاعل of اسم الفاعل.'),
    Q('3R', 'In **تشكرُ** with no other context, what must be established before choosing هي or أنت?',
      'Whether the كلام refers to a غائبة or addresses a مخاطب مذكّر.',
      'Nothing: تـ always means أنت.',
      'Nothing: every مضارع has hidden أنا.',
      '**تشكر** can refer to هي or أنتَ. The حرف المضارعة تـ alone is not enough; the context determines the intended ضمير and whether this استتار is جائز or واجب.'),
    Q('3-Read', '**الضمير المستتر ليس له صورة في اللفظ.** Which example illustrates that?',
      'الفاعل أنت في اشكرْ.', 'التاء في شكرتُ.', 'الواو في شكروا.',
      '**اشكرْ** has a فاعل مستتر تقديره أنت. التاء in شكرتُ and الواو in شكروا are بارزان because they have an expressed form.')
 ],
 '4': [
    T('4G-1', 'Match the structural reason for انفصال.', [
        ('أنت حاضر: أنت', 'مبتدأ', 'مفعول به مقدّم', 'مضاف إليه'),
        ('المسؤول أنت: أنت', 'خبر', 'حرف خطاب', 'فاعل المسؤول'),
        ('إيّاك نشكر: إيّاك', 'مفعول به مقدّم', 'مبتدأ مرفوع', 'توكيد لضمير مذكور'),
        ('لا نعبد إلا إيّاه: إيّاه', 'بعد إلّا', 'مجرور بإلّا', 'اسم إشارة'),
        ('إنّا أو إيّاكم لعلى هدى: إيّاكم', 'معطوف', 'خبر إنّ', 'فاعل أو')
    ], 'The reasons are **ابتداء، خبر، تقديم المفعول به، الوقوع بعد إلّا، عطف**. In the last example إيّاكم is معطوف على اسم إنّ في محل نصب. None of these roles licenses inventing a مجرور منفصل.'),
    Q('4G-2', 'Complete the ordinary statement “I thank him,” without تقديم or a special two-مفعولين construction.',
      'أشكرُهُ.', 'أشكرُ إيّاهُ.', 'أشكرُ هو.',
      '**أشكره** uses the available متصل مفعول به. The ordinary rule does not replace an available متصل with إيّاه; **إيّاه أشكر** would be a different construction involving تقديم.'),
    Q('4I-1', 'You intend the ضمير as خبر كان. Which judgement correctly compares **كنتُه / كنتُ إيّاه**?',
      'Both occur; كنتُ إيّاه is preferred here.',
      'Only كنتُه is permitted; إيّاه can never be خبرًا.',
      'Both are wrong because كان cannot take ضمائر.',
      '**التاء** is اسم كان; **الهاء / إيّاه** is خبرها في محل نصب. Both اتصال and انفصال occur here, with انفصال preferred.'),
    T('4I-2', 'Identify the two مفعولين and the reason for the stated form.', [
        ('يسألكموها: كم then ها', 'مخاطب ثم غائب؛ المتصل أرجح', 'غائب ثم متكلّم؛ المنفصل أرجح', 'كم فاعل وها خبر'),
        ('سألتُه إيّاك: first مفعول به', 'الهاء', 'التاء', 'إيّاك'),
        ('سألتُه إيّاك: why the second is منفصل here', 'المخاطب أعرف من الغائب الذي سبقه', 'التاء هي المفعول الأول', 'كل ضمير بعد سأل يجب فصله')
    ], 'In **يسألكموها**, كم and ها are مفعولان, with مخاطب first, so اتصال is preferred. In **سألتُه إيّاك**, تاء is فاعل, هاء is مفعول أول, and إيّاك is مفعول ثان؛ المخاطب أعرف من الغائب, so this illustrates the separated form.'),
    Q('4R', 'Which claim mistakes preference for necessity?',
      '“If اتصال is preferred, the stated permitted منفصل form must be wrong.”',
      '“كنتُ إيّاه is preferred, while كنتُه also occurs.”',
      '“A مفعول به مقدّم may require a منفصل form.”',
      '**يترجّح** identifies a preference among permitted forms. The exception for خبر كان and the stated two-مفعولين construction must not be collapsed into an absolute ban.'),
    Q('4-Read', '**أوّلهما أعرف من الثاني** in the two-مفعولين rule compares:',
      'ضمير المفعول الأول بضمير المفعول الثاني.', 'ضمير الفاعل بأي اسم بعده.', 'أول حرف بآخر حرف في الفعل.',
      'Locate the two مفعولين first. In **سألتُه إيّاك**, the تاء is excluded from this comparison because it is فاعل.')
 ],
 '5': [
    T('5G-1', 'Match the boundary change before ياء المتكلّم.', [
        ('كتاب + ياء المتكلّم', 'كسرة قبل الياء، والياء ساكنة أو مفتوحة', 'حذف الألف المقصورة', 'قلب الكاف واوًا'),
        ('عصا + ياء المتكلّم', 'تثبت الألف: عصايَ', 'تحذف الألف دائمًا: عصي فقط', 'تضاف نون الوقاية إلى عصا'),
        ('قاضي + ياء المتكلّم', 'إدغام الياء في الياء: قاضيَّ', 'إبقاء ياءين منفصلتين بلا إدغام', 'قلب الياء ألفًا')
    ], 'The صحيح takes كسرة المناسبة before ياء. The مقصور keeps its ألف. An original ياء preceded by كسرة merges with ياء المتكلّم, giving the مشدّدة ياء of **قاضيّ** with فتح on the second ياء.'),
    T('5G-2', 'Analyse **كتابي نافعٌ**.', [
        ('كتاب', 'مبتدأ مرفوع بضمة مقدّرة، وهو مضاف', 'مضاف إليه مجرور لمجرد الكسرة', 'فاعل للياء'),
        ('الياء', 'ضمير في محل جر مضاف إليه', 'فاعل في محل رفع', 'حرف تنبيه'),
        ('الكسرة قبل الياء', 'حركة المناسبة، لا دليل على جر كتاب هنا', 'علامة جر كتاب في كل سياق', 'علامة نصب الياء'),
        ('نافعٌ', 'خبر مرفوع بالضمة', 'مفعول به منصوب', 'نعت للياء')
    ], '**كتاب** مبتدأ مرفوع بضمة مقدّرة منع ظهورها اشتغال المحل بحركة المناسبة؛ الياء مضاف إليه؛ **نافعٌ** خبر. The كسرة before ياء المتكلم does not replace the رفع required by the construction.'),
    Q('5I-1', 'In **قرأتُ كتابي**, what changes from **كتابي نافعٌ**?',
      'كتاب becomes مفعولًا به منصوبًا بفتحة مقدّرة; الياء stays في محل جر.',
      'الياء becomes فاعلًا and كتاب has no إعراب.',
      'كتاب stays مبتدأ because its written form is unchanged.',
      '**قرأتُ** contains فعل وفاعل. **كتاب** is مفعول به منصوب بفتحة مقدّرة قبل ياء المتكلم؛ الياء remains مضافًا إليه. The form كتابي can occur in different roles.'),
    Q('5I-2', 'Start with **مُخْرِجونَ**, remove نون for إضافة, then add ياء المتكلّم in a رفع context. Which explanation gives **مُخْرِجِيَّ**?',
      'الواو تقلب ياء، ويكسر ما قبلها، ثم تدغم في ياء المتكلّم.',
      'The word must become منصوبًا because no واو is visible.',
      'نون الجمع becomes the ياء المتكلّم.',
      'After حذف نون الإضافة, the واو preceded by ضمة becomes ياء, the preceding sound takes كسرة, and the two ياءات merge. The transformation does not itself change a رفع role into نصب.'),
    Q('5R', 'Which generalisation is accurate?',
      'The kind of final letter determines the sound change; the عامل determines the role.',
      'Every اسم before ياء المتكلم is مجرور.',
      'Every original ألف becomes ياء مشدّدة.',
      'Compare **كتابي، عصاي، قاضيّ**. Their sound patterns differ, but the مضاف must still receive the role required by its عامل. The added ياء is مضاف إليه.'),
    Q('5-Read', '**تثبت الألف** gives which completion of **هذه ___** using عصا + ياء المتكلّم?',
      'عصايَ', 'عصِييَ', 'عصانِي',
      '**هذه عصايَ** preserves the original ألف of عصا before the added ياء. This is not the إدغام rule for an original ياء.')
 ],
 '6': [
    T('6G-1', 'Use the توكيد reading explicitly intended here.', [
        ('أكرمتُك أنتَ: أنت', 'في محل نصب توكيد للكاف', 'في محل رفع فاعل جديد', 'في محل جر نعت'),
        ('كتابُك أنتَ نافعٌ: أنت', 'في محل جر توكيد للكاف', 'في محل رفع مبتدأ جديد', 'في محل نصب مفعول به'),
        ('أنت أنت معلّمنا: أنت الثانية', 'توكيد للأولى في محل رفع', 'مفعول به منصوب', 'حرف خطاب'),
        ('إيّاك إيّاك نشكر: إيّاك الثانية', 'توكيد للأولى في محل نصب', 'مبتدأ مرفوع', 'مضاف إليه')
    ], '**أنت** is a مرفوع منفصل form, but its actual محل as توكيد follows the emphasised ضمير: نصب for كاف أكرمتك and جر for كاف كتابك. Repeated **أنت** and **إيّاك** follow their first occurrences in محل.'),
    T('6G-2', 'Match the route to مرجع الضمير.', [
        ('هذا الكتاب قرأتُه: الهاء', 'مرجع مذكور لفظًا: الكتاب', 'مرجع مفهوم من فعل سابق فقط', 'لا مرجع لها'),
        ('اعدلوا هو أقرب للتقوى: هو', 'العدل المفهوم من اعدلوا، معنًى', 'الواو في اعدلوا وحدها', 'اسم ظاهر هو التقوى'),
        ('إذا بلغت التراقي: الفاعل المستتر في السياق المذكور', 'هي، للروح المفهومة حكمًا', 'أنت، للمخاطب حتمًا', 'التاء ضمير متكلّم')
    ], 'The three routes are **لفظًا، معنًى، حكمًا**. In **بلغت** the تاء is للتأنيث and the understood هي refers to الروح established by the situation. In **اعدلوا هو...**, هو refers to the meaning العدل, not to the group commanded.'),
    Q('6I-1', 'Choose the correction meaning “I praised myself”: **مدحتُني**.',
      'مدحتُ نفسي.', 'مدحتَني.', 'مدحني خالدٌ.',
      '**مدحتُ نفسي** gives تاء الفاعل and نفس as مفعول به مضاف إلى ياء المتكلم. **مدحتَني** is grammatical but means “you praised me”; it does not preserve the requested meaning.'),
    T('6I-2', 'Choose the analysis that respects the distinction.', [
        ('من يقول ... وما هم بمؤمنين', 'يقول يراعي اللفظ، وهم تراعي المعنى', 'هم must always be replaced by هو', 'من is plural in its written form'),
        ('إنّي أراني أعصر خمرًا', 'رأى من الاستعمالات المستثناة من منع الضميرين لواحد', 'Every فعل now permits two such ضمائر', 'الياء في أراني فاعل ظاهر'),
        ('أنت مجتهدٌ', 'مجتهد خبر، لا نعت للضمير', 'مجتهد نعت لأنت', 'أنت مضاف ومجتهد مضاف إليه'),
        ('إليك إليك أرغب، على قراءة التوكيد', 'أعيد الجار مع الضمير للتوكيد', 'إلى الثانية فعل', 'الكاف الأولى مفعول به منصوب')
    ], '**من** can be مفردة لفظًا and جمعًا معنًى, allowing both returning forms. **رأى** belongs to the stated exceptions; that does not license مدحتني for “I praised myself.” **مجتهد** is خبر in أنت مجتهد. Repeating **إليك** repeats الجار with its ضمير.'),
    Q('6R', 'Which statement correctly distinguishes **مدحتُ نفسي** and **مدحتَني**?',
      'The first refers both roles to the speaker through نفس; the second has different people in the two roles.',
      'Both are forbidden because two roles appear.',
      'نفسي is always توكيد and never مفعول به.',
      'In **مدحتُ نفسي**, نفسي is مفعول به. In **مدحتَني**, أنت is represented by التاء and أنا by الياء؛ they refer to different people, so the same-person restriction does not apply.'),
    Q('6-Read', '**المضمر لا يوصف ولا يوصف به.** Which analysis agrees?',
      'In أنت حاضرٌ, حاضر is خبر, not نعت of أنت.',
      'In أنت حاضرٌ, أنت is نعت of حاضر.',
      'A ضمير can never be مبتدأ.',
      'The rule excludes the نعت/منعوت relationship for the ضمير. It does not exclude other roles such as مبتدأ or توكيد.')
 ],
 '7': [
    T('7G-1', 'Match the intended kind of علم.', [
        ('خالد، اسم رجل معيّن', 'علم شخصي', 'علم جنسي', 'اسم آلة'),
        ('أسامة، اسم لجنس الأسد هنا', 'علم جنسي', 'علم شخصي في هذا السياق', 'مصدر'),
        ('أبو بكر', 'كنية', 'اسم موصول', 'نكرة محضة'),
        ('الفاروق، عَلَم يفيد المدح', 'لقب', 'حرف خطاب', 'اسم إشارة')
    ], '**خالد** identifies a person. **أسامة** is علم جنسي in the explicitly stated use for the lion-kind. **أبو بكر** is كنية; **الفاروق** is لقب suggesting مدح.'),
    Q('7G-2', 'Complete **جاء هارونُ ___**, explicitly using الرشيد as بدل.',
      'الرشيدُ', 'الرشيدِ', 'الرشيدَ',
      '**الرشيدُ** follows هارون in رفع as بدل. **الرشيدِ** would select the different إضافة analysis, not the requested بدل analysis.'),
    Q('7I-1', 'Analyse **جاء هارونُ الرشيدِ**, explicitly using إضافة.',
      'هارون فاعل مرفوع ومضاف؛ الرشيد مضاف إليه مجرور.',
      'الرشيد بدل مرفوع بالكسرة.',
      'هارون مجرور لأن الرشيد بعده.',
      '**هارونُ** receives رفع from its role as فاعل and also acts as مضاف. **الرشيدِ** is مضاف إليه. إضافة does not require the مضاف itself to have جر.'),
    Q('7I-2', 'A man is personally named أسامة. In **حضر أسامةُ** with that stated meaning, أسامة is:',
      'علم شخصي.', 'علم جنسي حتمًا مهما كان المقصود.', 'نكرة لأنه لا يبدأ بأل.',
      'The context fixes **أسامة** as the personal name of an individual. The same written form can be علم جنسي when used as the name of the lion-kind; spelling alone does not decide.'),
    T('7R', 'Choose the accurate ordering rule.', [
        ('العلم ولقبه في الترتيب المعتاد', 'العلم قبل اللقب', 'اللقب قبل العلم دائمًا', 'لا يجوز اجتماعهما'),
        ('لقب أشهر، مثل المسيح مع عيسى', 'يجوز تقديم اللقب الأشهر', 'يجب حذف اللقب', 'يتحوّل اللقب إلى نكرة'),
        ('الكنية مع الاسم الآخر', 'لا ترتيب واجب بينهما', 'الكنية متأخرة دائمًا', 'الكنية متقدمة دائمًا')
    ], 'Normally the علم precedes its لقب. A better-known لقب can precede, as in **المسيح عيسى**. A كنية has no compulsory precedence relative to the other name.'),
    Q('7-Read', '**اللقب علم يشعر بمدح أو ذم.** What distinguishes لقب here?',
      'It is a علم carrying a suggestion of مدح or ذم.', 'It must begin with أب.', 'It is always a نكرة اسم آلة.',
      'The clue is **يشعر بمدح أو ذم**. Beginning with أب، أم or ابن instead characterises a كنية, though all are being discussed within naming.')
 ],
 '8': [
    T('8G-1', 'Use the context supplied to identify العهد.', [
        ('وجدتُ كتابًا فقرأتُ الكتابَ، وهو الكتاب نفسه', 'عهد ذكري', 'عهد حضوري فقط', 'استغراق حقيقي'),
        ('الكتاب، لكتاب معروف بين المتكلم والسامع لم يذكر من قبل وليس حاضرًا', 'عهد ذهني', 'عهد ذكري', 'جنس دون النظر إلى الأفراد'),
        ('اليوم، بمعنى يوم الكلام نفسه', 'عهد حضوري', 'عهد ذكري لكتاب سابق', 'فرد غير معيّن من الجنس')
    ], '**ذكري** depends on earlier mention; **ذهني** on shared knowledge without that mention; **حضوري** on the current setting. The supplied context rules out guessing from أل alone.'),
    T('8G-2', 'Match the intended use of لام الجنس.', [
        ('الماء، يراد به الجنس دون النظر إلى أفراده', 'الجنس دون النظر إلى الأفراد', 'عهد ذكري', 'علم شخصي'),
        ('كمثل الحمار يحمل أسفارًا، حمار غير معيّن', 'فرد غير معيّن؛ معرفة لفظًا نكرة معنًى', 'عهد لشخص مسمّى', 'استغراق لكل حمار فردًا فردًا'),
        ('إن الإنسان لفي خسر، عموم الجنس قبل الاستثناء', 'استغراق حقيقي', 'عهد حضوري لشخص واحد', 'كنية'),
        ('وجاء السحرة فرعون، يراد جميع السحرة المجتمعين في القصة', 'استغراق عرفي', 'كل ساحر في الوجود بلا تقييد', 'فرد واحد غير معيّن')
    ], 'لام الجنس can present the kind, an unspecified representative, or all individuals. **حقيقي** extends across the kind; **عرفي** is bounded by the relevant situation. The حمار example is معرفة لفظًا but نكرة معنًى.'),
    Q('8I-1', 'Read **رأيتُ طالبًا يحمل كتابًا. ثم سألتُ الطالبَ عن الكتابِ.** Both later أسماء refer to what was just mentioned. What is the use of أل?',
      'عهد ذكري في الطالب والكتاب.', 'عهد حضوري حتمًا في كليهما.', 'استغراق حقيقي لكل الطلاب والكتب.',
      '**الطالب** returns to طالبًا and **الكتاب** to كتابًا. Earlier mention identifies both; their different sentence roles still determine their endings.'),
    Q('8I-2', 'Why can **يحمل أسفارًا** be نعتًا for الحمار in the representative, non-specific use?',
      'الحمار معرفة لفظًا نكرة معنًى في هذا الاستعمال.',
      'Every اسم with أل takes a جملة as نعت.',
      'يحمل is a مجرور اسم.',
      'The specified use puts **الحمار** في حكم النكرة. The جملة carries hidden هو as its عائد. This is not a blanket rule for an ordinary معرفة identifying a particular known individual.'),
    Q('8R', 'Without any context, does the word **الرسول** alone determine ذكري، ذهني or حضوري?',
      'No; the relationship supplied by the كلام must decide.',
      'Yes; every أل is عهد ذكري.',
      'Yes; every أل is استغراق حقيقي.',
      'أل marks a form whose use must be established. Earlier mention, shared knowledge, current presence, and الجنس are different possibilities.'),
    Q('8-Read', '**الاستغراق العرفي** differs from الحقيقي because:',
      'Its all-individuals scope is bounded by the relevant عرف or situation.',
      'It always refers to one unnamed individual only.',
      'It removes أل from the word.',
      'In the سحرة example, all the intended gathered سحرة are meant, not every ساحر in existence. It is still استغراق within that scope.')
 ],
 '9': [
    T('9G-1', 'Complete each expression for the stated group.', [
        ('___ رجلٌ، للقريب', 'هذا', 'هذه', 'هاتان'),
        ('___ امرأةٌ، للقريبة', 'هذه', 'هذان', 'هذا'),
        ('___ رجلانِ، في رفع', 'هذانِ', 'هذينِ', 'هاتانِ'),
        ('___ امرأتانِ، في رفع', 'هاتانِ', 'هذانِ', 'هاتينِ'),
        ('___ نساءٌ، جمع', 'هؤلاء', 'هذا', 'ذلك')
    ], 'Match the indicated group: **هذا** للمذكر المفرد؛ **هذه** للمؤنث المفرد؛ **هذان** للمثنى المذكر في رفع؛ **هاتان** للمثنى المؤنث في رفع؛ **هؤلاء** works with the جمع نساء as well as رجال.'),
    T('9G-2', 'Separate اسم and added حرف.', [
        ('الهاء في هذا', 'هاء التنبيه', 'ضمير في محل جر', 'نون الوقاية'),
        ('اللام في ذلك', 'لام البعد', 'لام جر لكتاب', 'ضمير منصوب'),
        ('الكاف في ذلك', 'حرف خطاب لا محل له', 'ضمير مضاف إليه', 'فاعل'),
        ('الكاف في كتابك', 'ضمير في محل جر مضاف إليه', 'حرف خطاب لا محل له ككاف ذلك', 'لام البعد')
    ], 'In **هذا** the initial هاء is للتنبيه. In **ذلك**, اللام للبعد والكاف للخطاب, both حروف. The كاف in **كتابك** is a different grammatical use: ضمير مجرور بالإضافة.'),
    Q('9I-1', 'Complete **رأيتُ ___** for two indicated men.',
      'هذينِ', 'هذانِ', 'هاتينِ',
      '**هذينِ** matches the مذكّر مثنّى and its نصب as مفعول به. **هذانِ** is the رفع form; **هاتينِ** would indicate two مؤنثين.'),
    Q('9I-2', 'Which account of **تلك** preserves the stated formation?',
      'أصلها تِهِ؛ حذفت الهاء وزيدت لام البعد وكاف الخطاب.',
      'الكاف ضمير مضاف إليه، واللام حرف جر.',
      'أصلها تاء الفاعل مع نون الوقاية.',
      '**تِهِ** is one base form للمؤنث. Its final هاء is removed in **تلك**; اللام والكاف are added. That original هاء is not the prefixed هاء التنبيه of هذا.'),
    T('9R', 'Analyse **رأيتُ ذلكَ** in detail.', [
        ('التاء', 'ضمير في محل رفع فاعل', 'حرف تأنيث ساكن', 'ضمير في محل جر'),
        ('ذا', 'اسم إشارة في محل نصب مفعول به', 'حرف جر', 'ضمير متكلّم'),
        ('اللام والكاف', 'حرفان للبعد والخطاب لا محل لهما', 'ضميران في محل جر', 'مبتدأ وخبر')
    ], '**رأيتُ** contains فعل وفاعل. **ذا** is مبني على السكون في محل نصب مفعول به; اللام للبعد والكاف للخطاب. The short label اسم إشارة for ذلك does not make its كاف a مضاف إليه.'),
    Q('9-Read', '**أولاء لمجموع المذكّر والمؤنّث.** Which pair illustrates the rule?',
      'هؤلاء رجالٌ / هؤلاء نساءٌ.', 'هذا رجلان / هذا امرأتان.', 'ذلك رجال / تلك نساء، لمجرّد الجمع.',
      'The same form **هؤلاء** can indicate the groups رجال and نساء. The stated examples do not require a different spelling of أولاء for each group.')
 ],
 '10': [
    T('10G-1', 'Choose the form for the specified expression.', [
        ('جاء ___ نجحا، رجلان', 'اللذانِ', 'اللتانِ', 'الذين'),
        ('رأيتُ ___ نجحتا، امرأتان', 'اللتينِ', 'اللتانِ', 'اللذينِ'),
        ('أحبُّ ___ يصدقون، رجال', 'الذين', 'الذي', 'التي'),
        ('ماذا تفقدون، على فصل ما الاستفهامية عن ذا', 'ذا موصولة', 'ذا حرف جر', 'ما هنا مصدرية حتمًا')
    ], '**اللذان** has رفع as فاعل and refers to two مذكّرين. **اللتين** has نصب as مفعول به and refers to two مؤنثين. **الذين** matches the stated جمع. In the specified ماذا analysis, ما is استفهامية and ذا موصولة.'),
    T('10G-2', 'Find the عائد, not simply any ضمير in the صلة.', [
        ('أحب الذي يصدق', 'هو المستتر في يصدق', 'أنا المستتر في أحب', 'لا عائد أصلًا'),
        ('أحب الذي خلقه حسن', 'الهاء في خلقه', 'أنا المستتر في أحب', 'حسنٌ'),
        ('أحب الذي عندك', 'ضمير مستتر في المتعلّق العام المحذوف', 'الكاف التي تخاطب السامع', 'عند اسم موصول'),
        ('أحب الذين تحب، أي تحبّهم', 'هم المحذوفة، في محل نصب مفعول به', 'أنت المستتر هو العائد إلى الذين', 'اللام في الذين وحدها')
    ], 'The عائد must return to the موصول. Hidden **هو** does so in يصدق; **هاء** does so in خلقه. In **عندك**, الكاف addresses someone else; the link is in the understood general متعلّق. In **تحبّهم**, هم is the returning مفعول به, while hidden أنت is فاعل.'),
    Q('10I-1', 'Read **قابلتُ التي تحفظ الدرس. شكرتُها.** Identify the two links to the person indicated by التي.',
      'هي المستترة في تحفظ عائد الصلة؛ ها في شكرتها تشير إلى الشخص نفسه.',
      'التاء في قابلت تعود إلى التي؛ الدرس هو العائد.',
      'لا عائد للصلة لأن التي مؤنّث.',
      '**التي** is مفعول به of قابلت. **تحفظ** has hidden هي returning to التي, and الدرسَ is مفعول به. In **شكرتُها**, التاء is the speaker and ها refers to that same person.'),
    Q('10I-2', 'For **الكاتبُ الدرسَ** meaning الذي يكتب الدرس, choose the relevant account of أل.',
      'أل موصولة، والمشتق بمعنى الفعل يتمّ صلتها.',
      'أل استفهامية تنصب كاتب.',
      'كل أل في أي اسم موصولة، حتى أل الكتاب.',
      'This is the stated **أل الموصولة الداخلة على مشتق بمعنى الفعل**. It corresponds to الذي يكتب الدرس, with الدرسَ مفعول به. Do not generalise this account to every أل.'),
    Q('10R', 'Correct: “In أحب الذين تحب, the hidden أنت in تحب is the عائد to الذين.”',
      'أنت is فاعل; the omitted هم in تحبّهم is the عائد.',
      'الذين is the written فاعل of تحب.',
      'There is no need for any عائد in any صلة.',
      '**الذين** refers to a group, while hidden أنت identifies the person doing the loving. **هم المحذوفة** is the مفعول به returning to الذين; the full تقدير is تحبّهم.'),
    Q('10-Read', '**لا بد للصلة من ضمير عائد، وقد يحذف.** Which interpretation is sound?',
      'The relationship is required, while the expression of its ضمير may be omitted in a permitted pattern.',
      'Any ضمير anywhere may be deleted at will.',
      'An omitted عائد makes the موصول نكرة.',
      'The rule distinguishes a required link from whether its form is expressed. The example تحبّهم → تحب does not license arbitrary حذف elsewhere.')
 ],
 '11': [
    T('11G-1', 'Decide whether the stated إضافة gives تعريف or تخصيص.', [
        ('كتاب خالد، إضافة معنوية عادية: كتاب', 'معرفة بالإضافة إلى علم', 'نكرة محضة بلا تخصيص', 'ضمير'),
        ('كتابك، إضافة معنوية عادية: كتاب', 'معرفة بالإضافة إلى ضمير', 'نكرة لأن الكاف ليست أل', 'اسم موصول'),
        ('طالب علم: طالب', 'نكرة غير محضة؛ تخصّص بالإضافة إلى نكرة', 'معرفة حتمًا بكل إضافة', 'حرف جر'),
        ('مؤمنًا سليمَ القلب: سليم في الإضافة اللفظية', 'نكرة؛ لا يكتسب التعريف هنا', 'معرفة بأل الموجودة في القلب حتمًا', 'ضمير مبني')
    ], 'Ordinary إضافة to **خالد** or **الكاف** gives تعريف to كتاب. **طالب علم** gives تخصيص only. **سليم القلب** is إضافة لفظية; سليم remains نكرة, allowing it to describe مؤمنًا.'),
    T('11G-2', 'Classify the نكرة or identifying use precisely.', [
        ('طالب مجتهد', 'نكرة مخصوصة بالوصف، غير محضة', 'معرفة لأنه موصوف', 'ضمير'),
        ('طالب، وحدها بلا سياق إضافي', 'نكرة محضة غير مفيدة في الحالة المذكورة', 'علم شخصي', 'نكرة مخصوصة بالإضافة'),
        ('أطالبٌ حاضرٌ؟: طالب', 'نكرة في سياق استفهام، مفيدة', 'معرفة بأل', 'اسم إشارة'),
        ('يا رجلُ، لشخص مقصود بعينه', 'معرفة بالقصد في النداء', 'نكرة غير مقصودة حتمًا', 'مضاف إلى معرفة')
    ], '**الوصف** gives تخصيص, not تعريف. The isolated **طالب** lacks the supplied conditions, while **أطالب حاضر؟** is useful through استفهام. **يا رجلُ** identifies a particular intended person in the specified نداء.'),
    Q('11I-1', 'Complete **جاء طالبُ ___** so that طالب remains نكرة مخصوصة in an ordinary إضافة معنوية.',
      'علمٍ', 'العلمِ', 'خالدٍ',
      '**طالبُ علمٍ** adds a نكرة and remains نكرة غير محضة. Adding **العلم** or **خالد** in ordinary إضافة معنوية would instead give تعريف.'),
    Q('11I-2', 'In **بيتٍ غيرِ بيتِ اللهِ**, why can غير describe the نكرة بيت?',
      'غير متوغّلة في الإبهام؛ لا تكسب التعريف بهذه الإضافة في الاستعمال المذكور.',
      'Every word preceding لفظ الجلالة must become a ضمير.',
      'غير is a معرفة نعت of any نكرة without conditions.',
      '**غير** remains نكرة in the stated مبهم use despite the إضافة chain. It is نعت مجرور لبيت and also مضاف؛ بيتِ is مضاف إليه ومضاف؛ اللهِ مضاف إليه.'),
    Q('11R', 'In **جاء طالبٌ يقرأُ**, which statement is accurate?',
      'يقرأ مع فاعله جملة في حكم النكرة، في محل رفع نعت لطالب.',
      'يقرأ is itself an اسم نكرة مجرور.',
      'The whole جملة is a معرفة because it contains a ضمير.',
      'The جملة is not classified as a معرفة or نكرة اسم, but is **في حكم النكرة** for this relationship. Its محل is رفع as نعت لطالب, and its hidden هو is the عائد.'),
    Q('11-Read', '**النكرة الموصوفة والمضافة إلى نكرة تسمّى نكرة غير محضة.** What is excluded from this statement?',
      'Ordinary إضافة to a معرفة, which can give تعريف.',
      'طالب علم، لأنه مضاف إلى نكرة.',
      'طالب مجتهد، لأنه موصوف.',
      'The qualification **إلى نكرة** is essential. طالب علم and طالب مجتهد remain نكرتين غير محضتين; كتاب خالد in ordinary إضافة is معرفة.')
 ],
 'R': [
    T('A1', 'Read **دخل طالب يحمل كتابا. قال: أنا طالب علم. ثم فتح الطالب كتابه.** Identify the target under the stated ordinary meanings.', [
        ('طالب مع وصفه يحمل كتابًا', 'نكرة غير محضة بالوصف', 'معرفة بأل', 'ضمير'),
        ('يحمل كتابًا', 'جملة في محل رفع نعت لطالب', 'صلة الموصول لا محل لها', 'جملة في محل جر مضاف إليه'),
        ('أنا', 'ضمير منفصل في محل رفع مبتدأ', 'ضمير منفصل في محل نصب', 'حرف تنبيه'),
        ('طالب علم: طالب', 'خبر مرفوع ونكرة غير محضة', 'خبر مجرور لأن علم بعده', 'معرفة حتمًا'),
        ('الطالب في الجملة الأخيرة', 'معرفة بأل العهد الذكري', 'عهد حضوري بلا سياق', 'اسم موصول'),
        ('الهاء في كتابه', 'ضمير في محل جر يعود إلى الطالب', 'حرف خطاب ككاف ذلك', 'فاعل فتح')
    ], 'The initial **طالبٌ** is introduced as نكرة and then receives **يحمل كتابًا** as نعت جملة؛ its hidden هو is the عائد. **أنا** مبتدأ و**طالبُ** خبر وهو مضاف إلى **علمٍ**, giving تخصيص. The later **الطالب** is identified by prior mention. **كتابَه** is مفعول به منصوب ومضاف؛ الهاء مضاف إليه تعود إلى الطالب.'),
    T('A2', 'Continue **شكرت الطالب. هو شاكر لربه. كتابه عندي.** Use شاكر بمعنى الفعل. Identify the relationships.', [
        ('هو في بدء الجملة الثانية', 'ضمير منفصل في محل رفع مبتدأ', 'حرف استئناف', 'ضمير في محل نصب'),
        ('شاكر', 'اسم فاعل وخبر مرفوع', 'اسم آلة ومفعول به', 'مصدر مجرور'),
        ('الفاعل في شاكر', 'ضمير مستتر هو يعود إلى المبتدأ', 'ربّه فاعل ظاهر', 'لا فاعل له مع معنى الفعل'),
        ('الهاء في ربّه وكتابه', 'تعود إلى الطالب المذكور', 'تعود إلى المتكلّم لأن الياء في عندي', 'حروف لا محل لها'),
        ('الياء في عندي', 'ياء المتكلّم في محل جر مضاف إليه', 'ياء المخاطبة في محل رفع', 'ضمير منفصل')
    ], '**هو** resumes the طالب. **شاكرٌ** is خبر and اسم فاعل; its hidden هو returns to that مبتدأ. **لربّه** is جار ومجرور with ربّ مضاف and الهاء مضاف إليه. In **كتابه عندي**, كتابُه مبتدأ and عندي شبه جملة في محل رفع خبر؛ الياء identifies the speaker, not the طالب.'),
    T('B1', 'Choose the form or ending that preserves the specified meaning.', [
        ('رأيتُ ___، two indicated women', 'هاتينِ', 'هاتانِ', 'هذينِ'),
        ('جاء هارونُ الرشيد، with بدل', 'الرشيدُ', 'الرشيدِ', 'الرشيدَ'),
        ('___ نشكر، مفعول به مقدّم للمخاطب المفرد المذكّر', 'إيّاكَ', 'أنتَ', 'ـكَ alone as a detached word'),
        ('“I praised myself”', 'مدحتُ نفسي', 'مدحتُني', 'مدحتَني'),
        ('جاء طالبُ علم، إضافة to a نكرة', 'علمٍ', 'علمٌ', 'علمًا')
    ], '**هاتين** gives نصب للمثنى المؤنث؛ **الرشيدُ** follows هارون بالبدلية؛ **إيّاك** supplies المفعول المقدّم؛ **نفسي** preserves the intended same-person relationship؛ **علمٍ** is مضاف إليه مجرور and remains نكرة.'),
    Q('B2', 'Which correction separates form from محل?',
      'In أكرمتك أنتَ with توكيد, أنت is a مرفوع منفصل form but في محل نصب توكيد للكاف.',
      'In every occurrence, أنت must be في محل رفع because of its form name.',
      'In كتابي نافع, كتاب must be مجرور because of the كسرة before ياء.',
      'The توكيد follows the emphasised ضمير in محل. Likewise, **كسرة المناسبة** before ياء المتكلّم does not determine the مضاف’s role. The عامل and relationship remain decisive.'),
    T('C1', 'Full تركيب: **أنتَ شكرتَهُ.** Account for the written units, the links and the whole جملة.', [
        ('أنت', 'ضمير منفصل مبني على الفتح في محل رفع مبتدأ', 'ضمير منصوب بفتحة ظاهرة', 'حرف خطاب'),
        ('شكر في شكرت', 'فعل ماض مبني على السكون لاتصاله بتاء الفاعل', 'فعل مضارع منصوب', 'اسم فاعل'),
        ('التاء', 'ضمير متصل مبني على الفتح في محل رفع فاعل', 'حرف تأنيث ساكن لا محل له', 'ضمير مستتر'),
        ('الهاء', 'ضمير متصل في محل نصب مفعول به', 'ضمير في محل رفع فاعل ثان', 'حرف تنبيه'),
        ('شكرتَه', 'جملة فعلية في محل رفع خبر أنت', 'جملة في محل جر نعت', 'صلة لا محل لها'),
        ('الرابط إلى المبتدأ', 'تاء الفاعل المخاطب', 'هاء المفعول به الغائب', 'لا رابط')
    ], '**أنت** مبتدأ مبني في محل رفع. **شكر** ماض مبني على السكون؛ **التاء المفتوحة** فاعل تمثل المخاطب؛ **الهاء** مفعول به تمثل الغائب. **شكرتَه** في محل رفع خبر أنت؛ التاء تربطها بالمبتدأ. The whole opening statement is ابتدائية لا محل لها.'),
    T('C2', 'Full تركيب: **أحبُّ الذي خُلُقُهُ حسنٌ.** Use صلة لا محل لها.', [
        ('أحبّ', 'مضارع مرفوع بالضمة؛ فاعله مستتر أنا وجوبًا', 'ماض مبني على الضم', 'مضارع مجزوم بالذي'),
        ('الذي', 'اسم موصول في محل نصب مفعول به', 'فاعل مرفوع', 'حرف جر'),
        ('خلقُ', 'مبتدأ مرفوع بالضمة وهو مضاف', 'مفعول به منصوب', 'نعت للذي في محل جر'),
        ('الهاء', 'ضمير في محل جر مضاف إليه، وهو العائد', 'ضمير في محل رفع فاعل أحب', 'حرف خطاب'),
        ('حسنٌ', 'خبر مرفوع بالضمة', 'مضاف إليه مجرور', 'مفعول به ثان'),
        ('خلقه حسن', 'جملة اسمية صلة لا محل لها', 'جملة في محل نصب مفعول به ثان', 'جملة في محل جر بالإضافة')
    ], '**أحبُّ** فاعله مستتر أنا؛ **الذي** موصول مبني على السكون في محل نصب مفعول به. **خلقُه حسنٌ** مبتدأ ومضاف إليه وخبر؛ الهاء تعود إلى الذي. This complete inner جملة is صلة لا محل لها; the موصول itself has محل نصب.'),
    T('C3', 'Full تركيب: **قرأتُ كتابي.** Separate the مضاف’s ending from the added ضمير.', [
        ('قرأ في قرأت', 'فعل ماض مبني على السكون', 'مصدر مرفوع', 'اسم مفعول'),
        ('التاء', 'ضمير مبني على الضم في محل رفع فاعل', 'حرف تأنيث', 'ضمير في محل جر'),
        ('كتاب', 'مفعول به منصوب بفتحة مقدّرة وهو مضاف', 'مضاف إليه مجرور بالكسرة الظاهرة', 'مبتدأ مرفوع'),
        ('الياء', 'ضمير متصل في محل جر مضاف إليه', 'ياء مخاطبة في محل رفع فاعل', 'حرف لا محل له'),
        ('كتاب من جهة التعريف', 'معرفة بإضافة معنوية إلى ضمير', 'نكرة محضة لأن أل غير موجودة', 'علم جنسي')
    ], '**قرأ** ماض مبني على السكون لاتصاله بالتاء؛ **التاء** فاعل. **كتاب** مفعول به منصوب بفتحة مقدّرة منع ظهورها اشتغال المحل بحركة المناسبة، وهو مضاف؛ **الياء** مضاف إليه. Ordinary إضافة to this معرفة ضمير makes كتاب معرفة.'),
    Q('D1', '**المضاف إلى النكرة يكتسب التخصيص لا التعريف.** اختر المثال المطابق في الإضافة المعنوية.',
      'طالبُ علمٍ.', 'كتابُ خالدٍ.', 'كتابُكَ.',
      '**علمٍ** نكرة؛ لذا يبقى **طالبُ علمٍ** نكرة غير محضة. خالد علم والكاف ضمير، فالإضافة المعنوية إليهما تفيد التعريف.'),
    Q('D2', '**الجملة ليست بمعرفة ولا نكرة، ولكنها في حكم النكرة.** اختر النتيجة الصحيحة.',
      'يمكن أن تقع نعتًا لنكرة، مثل يقرأ في جاء طالبٌ يقرأ.',
      'كل جملة اسم نكرة يقبل أل.',
      'كل جملة معرفة بسبب وجود الفاعل.',
      '**يقرأ** مع فاعله المستتر جملة في محل رفع نعت لطالب، وفيها العائد هو. هذا حكم في التركيب، لا تحويل الجملة إلى اسم يقبل علامات النكرة.'),
    Q('D3', '**قد يراعى لفظ من وقد يراعى معناها.** اختر التطبيق الموافق.',
      'من يقول ... وما هم بمؤمنين: مفرد في الأول وجمع في الثاني.',
      'كل ضمير يعود إلى من يجب أن يكون جمعًا فقط.',
      'كل ضمير يعود إلى من يجب أن يكون مفردًا فقط.',
      'لفظ **من** مفرد، وقد يكون معناها جمعًا. لذلك يراعى اللفظ في يقول والمعنى في هم؛ والغالب عند الجمع بينهما تقديم مراعاة اللفظ.')
 ]
}
