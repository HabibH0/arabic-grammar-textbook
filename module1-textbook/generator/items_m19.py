"""Module 19: source-aligned choices, one keyed answer per control."""
from item_kit import M, G

SOLUTIONS = {}

def Q(key, prompt, correct, wrong1, wrong2, why):
    SOLUTIONS[key] = why
    return M(key, prompt, [correct, wrong1, wrong2], correct)

def T(key, prompt, rows, why):
    SOLUTIONS[key] = why
    return G(key, prompt, ['التحليل'], [(label, [([a, b, c], a)]) for label, a, b, c in rows])

ITEMS = {
'1': [
 T('1G-1', 'Match each expression to its meaning.', [
  ('كتب أمس', 'الماضي', 'الحال', 'الأمر'),
  ('يكتب الآن', 'الحال', 'الماضي', 'الأمر'),
  ('سيكتب', 'المستقبل', 'الماضي', 'الأمر')],
  '**كتب أمس** places the action before التكلّم; **يكتب الآن** describes الحال; السين in **سيكتب** specifies المستقبل.'),
 T('1G-2', 'Complete the تركيب of **سيفتحُ سالمٌ البابَ**.', [
  ('السين', 'حرف استقبال', 'حرف نصب', 'ضمير فاعل'),
  ('يفتح', 'مضارع مرفوع بالضمة', 'مضارع منصوب بالفتحة', 'أمر مبني'),
  ('سالم', 'فاعل مرفوع', 'مفعول به منصوب', 'نائب فاعل'),
  ('الباب', 'مفعول به منصوب', 'فاعل مرفوع', 'مضاف إليه')],
  'السين للاستقبال؛ يفتح مضارع مرفوع بالضمة؛ سالم فاعل مرفوع بالضمة؛ الباب مفعول به منصوب بالفتحة. السين changes the time indicated, not the إعراب.'),
 Q('1I-1', 'Which expression both denies entry and places it in المستقبل?', 'لن ندخلَ', 'لَنَدْخُلُ', 'دخلنا',
   '**لن ندخلَ** contains لن الناصبة النافية. **لَنَدْخُلُ** instead has لام التأكيد followed by نَدْخُلُ.'),
 Q('1I-2', 'Read **سوف يقرأ عادل. ثم سيكتب رسالة.** What do the two علامات tell you?', 'Both actions are in المستقبل.', 'Both صيغ are أمر.', 'سوف makes يقرأ مجزومًا.',
   '**سوف** and **السين** each specify المستقبل. يقرأ ويكتب remain مضارعًا; neither حرف governs جزم here.'),
 Q('1R', 'In **نكتبُ الآنَ**, the initial ن is:', 'حرف المضارعة', 'نون النسوة', 'نون التوكيد',
   'The initial ن is one of حروف المضارعة and indicates the نحن form. It is not one of the final نونات.'),
 Q('1-Read', '**المضارع يدلّ على الحال أو المستقبل.** Which inference is sound?', 'Identify context and attached حروف before choosing between الحال والمستقبل.', 'Every مضارع must refer to الحال.', 'Every future meaning requires an أمر.',
   'A مضارع can refer to either الحال or المستقبل. الآن، غدًا and الحروف help determine the intended time.')
],
'2': [
 T('2G-1', 'Form الأمر from these مخاطب forms after جزم.', [
  ('تفتحْ', 'اِفْتَحْ', 'اُفْتَحْ', 'يَفْتَحْ'),
  ('تسجدْ', 'اُسْجُدْ', 'اِسْجُدْ', 'سْجُدْ'),
  ('تُعَلِّمْ', 'عَلِّمْ', 'اِعَلِّمْ', 'تُعَلِّمُ')],
  'Remove حرف المضارعة. **افتح** needs همزة وصل مكسورة because عين الكلمة has فتحة; **اسجد** needs همزة وصل مضمومة because its عين has ضمة. **علّم** already starts with a متحرّك letter.'),
 T('2G-2', 'Analyse **اُكْتُبا الجوابَ**.', [
  ('اكتبا', 'أمر مبني على حذف النون', 'مضارع مرفوع بثبوت النون', 'ماض مجهول'),
  ('الألف', 'ضمير في محل رفع فاعل', 'ألف فاصلة بعد نون النسوة', 'حرف جر'),
  ('الجواب', 'مفعول به منصوب بالفتحة', 'فاعل مرفوع بالألف', 'خبر مرفوع')],
  '**اكتبا** أمر مبني على حذف النون؛ ألف الاثنين فاعل؛ الجواب مفعول به منصوب بالفتحة. The two مخاطبان are expressed by الألف.'),
 Q('2I-1', 'Choose الأمر for أنتَ from **تُكْرِمْ**.', 'أَكْرِمْ، بهمزة قطع', 'اِكْرِمْ، بهمزة وصل', 'يُكْرِمُ، بحرف المضارعة',
   'باب الإفعال gives **أَكْرِمْ** with همزة قطع مفتوحة. Do not apply the ordinary همزة الوصل choice to this pattern.'),
 Q('2I-2', 'Complete the instruction to one woman: **يا هند، ... الجوابَ**.', 'اُكْتُبي', 'اُكْتُبوا', 'اُكْتُبا',
   '**اكتبي** addresses أنتِ. It is أمر مبني على حذف النون, with ياء المخاطبة in محل رفع فاعل.'),
 Q('2R', 'Which two forms both address two people?', 'تكتبانِ / اُكْتُبا', 'يكتبُ / اُكْتُبي', 'نكتبُ / اُكْتُبوا',
   '**تكتبان** and **اكتبا** have ألف الاثنين. The أمر is formed from the مخاطب form after حذف نون الإعراب.'),
 Q('2-Read', '**إن كان أول الباقي ساكنًا زيدت همزة الوصل.** Why does **عَلِّمْ** need no added همزة?', 'Its first remaining letter is متحرّك.', 'Every أمر begins with حرف المضارعة.', 'Its فاعل is always غائب.',
   'After removing ت from **تُعلّمْ**, the remaining ع in **علّمْ** has فتحة, so the stated condition for adding همزة الوصل is absent.')
],
'3': [
 T('3G-1', 'Choose the corresponding مبني للمفعول به form.', [
  ('أَكْرَمَ', 'أُكْرِمَ', 'أَكْرِمْ', 'يُكْرِمُ'),
  ('حَاسَبَ', 'حُوسِبَ', 'حَاسِبْ', 'حُاسَبَ'),
  ('قَالَ', 'قِيلَ', 'قُالَ', 'قَالِ'),
  ('يَكْتُبُ', 'يُكْتَبُ', 'يُكْتِبُ', 'يَكْتَبُ')],
  '**أُكرم** has ضمة then كسرة before the last letter; **حوسب** changes the added ألف to واو; **قيل** is the أجوف pattern; **يُكتب** has ضمة on حرف المضارعة and فتحة before the final letter.'),
 T('3G-2', 'Analyse **لن يُغْلَقَ البابُ**.', [
  ('لن', 'حرف نفي ونصب', 'حرف جزم', 'ضمير'),
  ('يغلق', 'مضارع مبني للمفعول به منصوب بالفتحة', 'ماض مبني على الضم', 'مضارع مجزوم بالسكون'),
  ('الباب', 'نائب فاعل مرفوع بالضمة', 'مفعول به منصوب', 'فاعل لفعل معلوم')],
  'لن تنصب **يُغلقَ**؛ its internal pattern is مبني للمفعول به. **البابُ** fills نائب الفاعل and is مرفوع بالضمة.'),
 Q('3I-1', 'Change **فتحَ الحارسُ البابَ** to المبني للمفعول به, omitting الحارس.', 'فُتِحَ البابُ', 'فُتِحَ البابَ', 'فَتَحَ البابُ',
   '**فُتح البابُ** changes the internal صيغة and gives الباب رفع as نائب الفاعل. Retaining its old نصب would leave the intended relationship unexpressed.'),
 Q('3I-2', 'Someone points to سالم and says **كَتَبَ**. Its فاعل is مستتر هو. Which classification follows?', 'مبني للفاعل', 'مبني للمفعول به because no اسم ظاهر follows', 'جامد because its فاعل is hidden',
   'A ضمير مستتر is still a فاعل. Absence of a following اسم ظاهر does not make **كَتَبَ** مجهولًا.'),
 Q('3R', 'Choose the form for **لم ... الكتابُ** with meaning “the book was not written”.', 'يُكْتَبْ', 'يُكْتَبَ', 'يَكْتُبُ',
   '**لم يُكتبْ الكتابُ** has the مبني للمفعول به internal pattern and سكون from لم. الكتاب نائب فاعل.'),
 Q('3-Read', '**يُضمّ حرف المضارعة ويُفتح ما قبل الآخر.** Which form exemplifies both changes?', 'يُسْتَخْرَجُ', 'يَسْتَخْرِجُ', 'اِسْتَخْرِجْ',
   '**يُستخرَجُ** has ضمة on ي and فتحة on ر, the letter before ج. The last ضمة is its رفع ending in this ungoverned form.')
],
'4': [
 T('4G-1', 'Match each series or use to its classification.', [
  ('أطاع، يطيع، أطع، مطيع', 'تام التصرف', 'جامد', 'حرف جر'),
  ('ما زال / لا يزال في التصنيف المدروس', 'ناقص التصرف', 'تام التصرف بهذه الصيغ وحدها', 'اسم جامد'),
  ('عدا بمعنى الاستثناء في هذا الباب', 'فعل جامد', 'تام التصرف في هذا الاستعمال', 'مضارع منصوب')],
  'The أطاع series illustrates تام التصرف. The pair ما زال / لا يزال illustrates ناقص التصرف. عدا is classified as جامد in the specified استعمال الاستثناء.'),
 T('4G-2', 'Analyse **لستُ حاضرًا**.', [
  ('ليس', 'فعل ماض ناقص جامد', 'مضارع تام التصرف', 'حرف جر'),
  ('التاء', 'ضمير في محل رفع اسم ليس', 'تاء التأنيث لا محل لها', 'مفعول به'),
  ('حاضرًا', 'خبر ليس منصوب', 'فاعل مرفوع', 'مضاف إليه')],
  '**ليس** is جامد but accepts the attached تاء. In this construction التاء is اسم ليس and حاضرًا خبرها منصوب بالفتحة.'),
 Q('4I-1', 'Which conclusion follows from **ليس / لستُ**?', 'Attaching a ضمير does not by itself produce تصرف into مضارع وأمر.', 'ليس must be تام التصرف.', 'لستُ is an أمر.',
   'Changing the attached ضمير is distinct from the range of صيغ used to classify تصرف.'),
 Q('4I-2', 'Select the accurate statement about **نعم وبئس**.', 'They are جامدان and do not accept the attached ضمائر الفاعل discussed here.', 'They have no فاعل in any construction.', 'They are ordinary مضارع forms.',
   '**نعم وبئس** are جامدان. Not accepting these attached ضمائر does not remove their need for a فاعل.'),
 Q('4R', 'Which classification asks about taking اسمًا وخبرًا, rather than the availability of other صيغ?', 'الفعل الناقص', 'ناقص التصرف', 'المبني للمفعول به',
   '**الفعل الناقص** concerns its عمل with اسم وخبر. **ناقص التصرف** concerns its restricted range of صيغ.'),
 Q('4-Read', '**غير المتصرف يسمى فعلًا جامدًا.** Which pair expresses the same classification?', 'غير متصرف / جامد', 'مجهول / ناقص التصرف', 'متصرف / مبني للمفعول به',
   '**غير متصرف** and **جامد** name the same classification here. The other pairs combine separate classifications.')
],
'5': [
 T('5G-1', 'Match the expression to its distinctive meaning.', [
  ('لم يخرجْ', 'نفي مع قلب المعنى ماضيًا', 'طلب الخروج', 'تأكيد حصول الخروج'),
  ('لمّا يخرجْ', 'نفي مع توقّع الحصول', 'ضمان أنه خرج', 'أمر للمخاطب'),
  ('لن يخرجَ', 'تأكيد نفي المستقبل', 'نفي الماضي بلم', 'نهي مجزوم'),
  ('ما يكتبُ الآن', 'نفي الحال', 'طلب الفعل', 'تأكيد الماضي')],
  '**لم** shifts the meaning to الماضي; **لمّا** adds توقّع الحصول; **لن** strengthens نفي المستقبل and governs نصب; **ما** with this مضارع denies الحال.'),
 T('5G-2', 'Choose the analysis of لا in each expression.', [
  ('لا يَكْذِبُ سالمٌ', 'نافية لا تجزم هنا', 'ناهية جازمة', 'حرف جر'),
  ('لا تَكْذِبْ يا سالم', 'ناهية جازمة', 'نافية ناصبة', 'لام التأكيد'),
  ('لا قدّر الله', 'دعاء دخلت فيه لا على الماضي', 'مضارع مجزوم', 'أمر بالصيغة')],
  'In **لا يكذبُ سالم** the statement is نفي with رفع. **لا تكذبْ** requests restraint and has جزم. **لا قدّر الله** is the permitted دعاء use with الماضي.'),
 Q('5I-1', 'Complete: **انتظرنا خالدًا. ... يصلْ، وننتظر وصوله.** Choose the حرف explicitly expressing “not yet”.', 'لمّا', 'لن', 'قد',
   '**لمّا يصلْ** combines نفي with توقّع الحصول. لن would require يصلَ and shift the meaning to المستقبل; قد does not express this نفي.'),
 Q('5I-2', 'In the نفي reading of **فلا اقتحم العقبة**, how is repetition supplied?', 'تقديرًا: فلا فكّ رقبة ولا أطعم يتيمًا أو مسكينًا', 'By changing لا into نون التوكيد', 'By treating اقتحم as مضارع مجزوم',
   'The specified نفي account understands repeated لا through the subsequent explanation. The separate تحضيض reading takes لا بمعنى هلّا; do not mix the two accounts.'),
 Q('5R', 'Correct the ending in **لن يُفْتَحُ البابُ**.', 'لن يُفْتَحَ البابُ', 'لن يُفْتَحْ البابُ', 'لن يُفْتَحَ البابَ',
   'لن governs نصب, so **يُفتحَ** ends in فتحة. الباب remains نائب فاعل مرفوع.'),
 Q('5-Read', '**وقيل: لا للتحضيض بمعنى هلّا.** What is this reading doing?', 'Urging the action strongly.', 'Guaranteeing a future event.', 'Making a فعل into an اسم.',
   '**التحضيض** is strong urging. This is a distinct reading from لا للنفي with repetition understood.')
],
'6': [
 T('6G-1', 'Identify the relevant نون.', [
  ('تكتبونَ: النون الأخيرة', 'نون الإعراب', 'نون النسوة', 'نون التوكيد'),
  ('اكتبْنَ', 'نون النسوة', 'نون الإعراب', 'حرف المضارعة'),
  ('اكتبَنَّ', 'نون التوكيد الثقيلة', 'نون النسوة', 'نون الإعراب'),
  ('اكتبَنْ', 'نون التوكيد الخفيفة', 'نون النسوة', 'نون الإعراب')],
  '**تكتبون** retains نون الإعراب; **اكتبْنَ** has a ضمير فاعل; **اكتبَنَّ / اكتبَنْ** have حرف توكيد. Read the preceding حركة and the نون itself.'),
 T('6G-2', 'Analyse **اُحْفَظَنَّ العهدَ** to one man.', [
  ('احفظنّ', 'أمر مبني على الفتح', 'أمر مبني على الضم', 'ماض منصوب'),
  ('الفاعل', 'مستتر تقديره أنتَ', 'نون التوكيد', 'العهد'),
  ('النون', 'حرف توكيد لا محل له', 'ضمير في محل نصب', 'علامة رفع'),
  ('العهد', 'مفعول به منصوب', 'نائب فاعل مرفوع', 'خبر مرفوع')],
  'The نون directly attaches to الأمر, giving بناء على الفتح. الفاعل مستتر أنتَ؛ العهد مفعول به منصوب بالفتحة؛ نون التوكيد has no محل.'),
 Q('6I-1', 'Choose the correct ending with ألف الاثنين.', 'أَطِيعَانِّ', 'أَطِيعَانَّ', 'أَطِيعَانْ',
   '**أطيعانِّ** uses النون الثقيلة المكسورة with ضمير المثنّى. The خفيفة is not admitted with it here.'),
 Q('6I-2', 'Add the two taught حروف strengthening **فهمنا الدرس**.', 'لقد فهمنا الدرس', 'لم فهمنا الدرس', 'لن فهمنا الدرس',
   '**لقد** combines لام التأكيد and قد before الماضي. لم ولن enter المضارع, not فهمنا in this use.'),
 Q('6R', 'Which instruction contains نهيًا مؤكدًا?', 'لا تَكْذِبَنَّ', 'لا يَكْذِبُ سالمٌ', 'قد كَتَبَ سالمٌ',
   '**لا تكذبنّ** combines لا الناهية with مضارع carrying نون التوكيد. The other expressions are statements.'),
 Q('6-Read', '**لا تدخل الخفيفة مع ضمير المثنّى ونون النسوة.** Which proposed form must be rejected?', 'أَطِعْنَانْ', 'أَطِعْنَانِّ', 'أَطِعَنَّ',
   '**أطعنَانْ** wrongly adds الخفيفة after the separating ألف with نون النسوة. Use الثقيلة المكسورة: **أطعنَانِّ**.')
],
'7': [
 T('7G-1', 'Match the intended ضمير to the emphasised صيغة.', [
  ('هم يكتبون', 'لَيَكْتُبُنَّ', 'لَيَكْتُبَنَّ', 'لَيَكْتُبَانِّ'),
  ('أنتِ تكتبين', 'لَتَكْتُبِنَّ', 'لَتَكْتُبَنَّ', 'لَتَكْتُبَانِّ'),
  ('أنتَ تكتب', 'لَتَكْتُبَنَّ', 'لَتَكْتُبِنَّ', 'لَتَكْتُبُنَّ')],
  'The ضمة before نّ in **ليكتبُنّ** indicates omitted واو الجماعة. The كسرة in **لتكتبِنّ** indicates omitted ياء المخاطبة. The فتحة in **لتكتبَنّ** belongs to the أنتَ form with مستتر فاعل.'),
 T('7G-2', 'Analyse the elements added after أطع in **أَطِعْنَانِّ**.', [
  ('النون الأولى', 'نون النسوة في محل رفع فاعل', 'نون الإعراب', 'نون التوكيد'),
  ('الألف', 'ألف فاصلة', 'ألف الاثنين فاعل', 'علامة نصب'),
  ('النون المشددة', 'نون توكيد ثقيلة مكسورة', 'نون النسوة الثانية', 'نون إعراب مرفوعة')],
  'نون النسوة remains the فاعل; الألف separates it from نون التوكيد الثقيلة المكسورة. Neither the separating ألف nor the last نون introduces another فاعل.'),
 Q('7I-1', 'In **لَيَكْتُبَانِّ**, what happened to the expressed نون of يكتبانِ?', 'نون الإعراب was removed; the visible نّ is نون التوكيد.', 'It became نون النسوة.', 'It remains unchanged and no نون التوكيد was added.',
   'Remove the expressed نون الإعراب when adding نون التوكيد. ألف الاثنين remains فاعل; the final الثقيلة takes كسرة.'),
 Q('7I-2', 'Correct the analysis: “In **لَتَكْتُبِنَّ** addressed to أنتِ, نون التوكيد is the فاعل.”', 'الفاعل ياء المخاطبة المحذوفة، والنون حرف توكيد.', 'الفاعل ألف فاصلة.', 'There is no فاعل once الياء disappears.',
   'The ياء is omitted in expression but remains the intended ضمير فاعل. The preceding كسرة indicates it; نون التوكيد is a حرف.'),
 Q('7R', 'Which pair distinguishes ألف الفاعل from ألف فاصلة after نون النسوة?', 'أَطِيعَانِّ / أَطِعْنَانِّ', 'أَطِعَنَّ / أَطِعَنْ', 'يكتبُ / كتبَ',
   'In **أطيعانِّ**, ألف الاثنين is the فاعل. In **أطعنَانِّ**, نون النسوة is the فاعل and the ألف is فاصلة.'),
 Q('7-Read', '**ويكون الفاعل مقدّرًا.** Applied to **ليكتبُنّ** for هم, what remains understood?', 'واو الجماعة المحذوفة', 'نون النسوة', 'ألف الاثنين',
   '**واو الجماعة** is removed from the expressed form but remains understood in محل رفع فاعل. The ضمة before نون التوكيد points to it.')
],
'8': [
 T('8G-1', 'Classify إلحاق علامة التأنيث in the stated constructions.', [
  ('خرجت هند: فاعل ظاهر مؤنث حقيقي بلا فاصل', 'واجب', 'ممتنع', 'جائز فقط'),
  ('الشمس طلعت: الفاعل ضمير هي', 'واجب', 'ممتنع', 'جائز فقط'),
  ('حضر المعلمون: جمع مذكر سالم', 'ممتنع', 'واجب', 'جائز دائمًا')],
  'An adjacent ظاهر مؤنث حقيقي and a ضمير returning to مؤنث each require التأنيث. The ظاهر جمع المذكر السالم here excludes it.'),
 T('8G-2', 'Complete **هندٌ خرجَتْ**.', [
  ('هند', 'مبتدأ مرفوع', 'مفعول به منصوب', 'حرف تأنيث'),
  ('التاء', 'علامة التأنيث لا محل لها', 'ضمير فاعل', 'مفعول به'),
  ('فاعل خرجت', 'مستتر تقديره هي', 'التاء الساكنة', 'هند فاعل مقدّم في هذا التحليل'),
  ('خرجت مع فاعلها', 'جملة في محل رفع خبر', 'جملة في محل نصب مفعول به', 'شبه جملة مجرور')],
  'هند مبتدأ؛ خرجت فعل ماض مبني على الفتح، تاؤه للتأنيث؛ الفاعل مستتر هي؛ الجملة خبر. The تاء is a علامة, not the فاعل.'),
 Q('8I-1', 'Complete with the form required by the ordinary adjacent فاعل: **... مريمُ**.', 'حَضَرَتْ', 'حَضَرَ', 'حَضَرُوا',
   '**حضرت مريم** requires تأنيث because مريم is اسم ظاهر مؤنث حقيقي with no separating expression.'),
 Q('8I-2', 'Which explanation matches **ما صامَ إلّا فاطمةُ** in the account taught here?', 'The understood basis is ما صام أحد إلا فاطمة.', 'فاطمة is classified as مذكر.', 'صام is an أمر addressed to فاطمة.',
   'The stated تذكير is explained by **ما صام أحد إلا فاطمة**. This does not reclassify فاطمة as مذكر or صام as أمر.'),
 Q('8R', 'In **أنتَ تكتبُ**, does the initial ت prove that the مخاطب is مؤنث?', 'No; ت is also used for the أنتَ form.', 'Yes; every initial ت requires هي.', 'Yes; ت is always تاء الفاعل.',
   '**تكتب** can address أنتَ. Identify the ضمير from the construction rather than treating every initial ت as دليل التأنيث.'),
 Q('8-Read', '**اسمًا ظاهرًا مؤنثًا حقيقيًّا متصلًا بالفعل.** What does متصلًا mean in this condition?', 'No expression intervenes between the فعل and its ظاهر فاعل.', 'The فاعل must be a ضمير متصل.', 'The اسم has become part of the جذر.',
   'Here اتصال concerns adjacency: **خرجت هند**. The condition explicitly describes an اسم ظاهر, not a ضمير متصل.')
],
'9': [
 T('9G-1', 'Choose the permitted pair in each specified context.', [
  ('ظاهر الشمس after the فعل', 'طلع الشمس / طلعت الشمس', 'طلعوا الشمس / طلعتا الشمس', 'الشمس طلع / الشمس طلعوا'),
  ('خالدًا separates هند from the فعل', 'أكرم خالدًا هند / أكرمت خالدًا هند', 'أكرموا خالدًا هند / أكرمتا خالدًا هند', 'أكرم خالدٌ هندًا / أكرمت خالدٌ هندًا'),
  ('نعم with الأم', 'نعم الأم / نعمت الأم', 'نعموا الأم / نعمتا الأم', 'نعمن الأم / نعموا الأم')],
  'The permitted pairs show جائز التأنيث: ظاهر مؤنث غير حقيقي; a separating مفعول به before the مؤنث فاعل; and نعم with ظاهر مؤنث حقيقي. Each pair preserves the specified relationship.'),
 T('9G-2', 'Analyse **أكرمَ خالدًا هندٌ**.', [
  ('أكرم', 'فعل ماض مبني على الفتح', 'أمر بهمزة قطع هنا', 'مضارع منصوب'),
  ('خالدًا', 'مفعول به مقدّم منصوب', 'فاعل مرفوع', 'نائب فاعل'),
  ('هند', 'فاعل مؤخّر مرفوع', 'مفعول به منصوب', 'خبر ليس'),
  ('ترك تاء التأنيث', 'جائز لوجود الفاصل', 'واجب لأن هند مذكر', 'خطأ في كل حال')],
  'أكرم فعل ماض؛ خالدًا مفعول به مقدّم بالفتحة؛ هند فاعل مؤخّر بالضمة. The separator allows تذكير although هند is مؤنث حقيقي.'),
 Q('9I-1', 'Which statement accurately explains **الرجال صلّت / الرجال صلّوا**?', 'The first allows a جماعة reading; the second follows أفراد الجمع.', 'The first treats الرجال as one named woman.', 'Both use نون النسوة.',
   'For this جمع مكسّر, **صلّت** returns a ضمير to the جماعة reading; **صلّوا** uses واو الجماعة referring to the أفراد. This is the specific allowance being practised.'),
 Q('9I-2', 'Choose the form where الجار والمجرور stands مقام نائب الفاعل: **... بجهنّمَ**.', 'جِيءَ', 'جِيئَتْ because جهنم is مؤنث', 'جاؤوا',
   '**جيء بجهنم** has the جار ومجرور in the نائب الفاعل position in this account. The علامة التأنيث is dropped; جهنم inside it does not trigger جيئت.'),
 Q('9R', 'Which pair correctly distinguishes the two الشمس constructions?', 'الشمس طلعت: واجب؛ طلع الشمس / طلعت الشمس: جائز', 'Both always forbid التأنيث.', 'الشمس طلع is required because الشمس is سماعي.',
   'With **الشمس طلعت**, the فاعل is مستتر هي, so التأنيث is واجب. With following ظاهر الشمس, التأنيث غير الحقيقي admits both forms.'),
 Q('9-Read', '**إذا كان الفاعل ضميرًا يعود إلى مجموع مكسّر أو اسم جمع.** What must you identify first?', 'What the ضمير refers back to and whether it is جمع مكسّر or اسم جمع.', 'Only whether the last letter is ة.', 'Whether the فعل has a مفعول به in every case.',
   'This condition concerns the مرجع of the ضمير and its classification. The final spelling alone does not establish it.')
],
'10': [
 T('10G-1', 'Complete using the ordinary analysis with the given word order.', [
  ('... المعلّمان', 'حضرَ', 'حضرَا', 'حضرُوا'),
  ('المعلّمان ...', 'حضرَا', 'حضرَ', 'حضرُوا'),
  ('المعلّمون ...', 'حضرُوا', 'حضرَ', 'حضرَا')],
  'With following ظاهر فاعل, use **حضر المعلّمان**. With initial مبتدأ, the embedded فاعل is a matching ضمير: **المعلّمان حضرا؛ المعلّمون حضروا**.'),
 T('10G-2', 'Analyse **جِيءَ بهم** using شبه الجملة as نائب الفاعل.', [
  ('جيء', 'ماض مبني للمفعول به، مفرد', 'ماض معلوم مع واو الجماعة', 'أمر للمخاطبين'),
  ('الباء', 'حرف جر', 'حرف نصب', 'فاعل'),
  ('هم', 'ضمير في محل جر بالباء', 'ضمير متصل بجيء في محل رفع', 'مفعول به منصوب'),
  ('بهم كله', 'في محل رفع نائب الفاعل', 'مبتدأ مرفوع', 'فاعل لفعل معلوم')],
  '**جيء** stays مفردًا. الباء حرف جر؛ هم في محل جر؛ the whole **بهم** is في محل رفع نائب الفاعل in the specified account. The inner and outer roles are different.'),
 Q('10I-1', 'Rewrite **حضر الحارسان** beginning with الحارسان, using مبتدأ وخبر.', 'الحارسان حضرا', 'الحارسان حضر', 'الحارسان حضروا',
   '**الحارسان حضرا** has مبتدأ مرفوع بالألف and جملة خبر whose فاعل is ألف الاثنين.'),
 Q('10I-2', 'Change only the reference in **جيء به** from one man to two, then several.', 'جيء بهما / جيء بهم', 'جيئا به / جيئوا به', 'جاءا / جاؤوا',
   'When نائب الفاعل is شبه جملة, the مجرور changes: **بهما، بهم**. The فعل stays **جيء**.'),
 Q('10R', 'In **الطالبات كتبْنَ**, identify the فاعل inside the خبر.', 'نون النسوة', 'نون التوكيد', 'الطالبات فاعل مقدّم in this analysis',
   '**الطالبات** is مبتدأ; **كتبن** and its فاعل form the خبر. نون النسوة is ضمير في محل رفع فاعل.'),
 Q('10-Read', '**يوحّد المجرور ويثنّى ويجمع لا ضمير الفعل.** Which sequence illustrates this with نائب الفاعل شبه جملة?', 'جيء به / جيء بهما / جيء بهم', 'حضر / حضرا / حضروا', 'اكتب / اكتبا / اكتبوا',
   'The varying ضمير belongs inside the جار ومجرور: به، بهما، بهم. It is not a matching ضمير attached to جيء.')
],
'11': [
 T('11G-1', 'In **وأسرّوا النجوى الذين ظلموا**, match the specified analysis to the role of الواو in أسرّوا.', [
  ('لغة أكلوني البراغيث', 'علامة جمع لا ضمير فاعل', 'ضمير فاعل والظاهر فاعل ثان', 'مفعول به'),
  ('الذين بدل من الفاعل', 'ضمير في محل رفع فاعل', 'علامة جمع فقط', 'حرف جر'),
  ('الذين مبتدأ مؤخّر', 'ضمير فاعل داخل الخبر المقدّم', 'ضمير مفعول به', 'حرف نصب')],
  'On the special لغة, الواو is علامة جمع and الذين is the ظاهر فاعل. With البدل or مبتدأ مؤخّر, الواو is the فاعل ضمير. Do not combine these alternative roles.'),
 T('11G-2', 'Analyse the excerpt **خُشَّعًا أبصارُهم** in its larger sentence.', [
  ('خشعًا', 'حال منصوب وهو جمع خاشع', 'فعل ماض مبني على الفتح', 'مبتدأ مرفوع'),
  ('أبصار', 'فاعل لخشع مرفوع وهو مضاف', 'مفعول به منصوب', 'بدل من واو الجماعة'),
  ('هم', 'ضمير في محل جر مضاف إليه', 'فاعل ثان لخشع', 'حرف جمع')],
  '**خشعًا** حال منصوب بالفتحة؛ **أبصارُ** فاعل لخشع مرفوع بالضمة ومضاف؛ **هم** مضاف إليه. شبه الفعل here has no internal فاعل ضمير and may be جمعًا.'),
 Q('11I-1', 'Under the البدل analysis of **يتعاقبون فيكم ملائكةٌ**, what is ملائكة?', 'بدل مرفوع من ضمير الفاعل', 'فاعل ثان in addition to الواو', 'مفعول به منصوب',
   'With the stipulated البدل account, الواو is the فاعل; ملائكة is بدل منه مرفوع. Calling it a second فاعل would mix analyses.'),
 Q('11I-2', 'Which ordinary pattern remains correct alongside the special لغة?', 'حضر المعلّمون', 'حضروا المعلّمون with both الواو and المعلّمون independently فاعل', 'حضر المعلّمون with المعلّمون مفعول به',
   'The ordinary pattern is **حضر المعلّمون**, with ظاهر فاعل and a مفرد فعل. The special لغة has its own analysis of الواو as علامة.'),
 Q('11R', 'What condition permits the جمع شبه الفعل illustrated by **خشعًا أبصارهم**?', 'شبه الفعل خالٍ عن ضمير، وفاعله اسم ظاهر.', 'Every فعل before a جمع must be جمعًا.', 'أبصارهم is always مفعول به.',
   'The allowance concerns **شبه الفعل الخالي عن ضمير** with ظاهر فاعل. It does not change the ordinary rule for a فعل with a following ظاهر فاعل.'),
 Q('11-Read', '**أو هو بدل من الفاعل.** What does أو signal here?', 'An alternative analysis to apply separately.', 'An additional فاعل to assign at the same time.', 'That the expression has no possible analysis.',
   '**أو** introduces a different possible account. Choose one coherent analysis rather than giving the same expression incompatible roles at once.')
],
'R': [
 Q('A1', 'Which change preserves الماضي while changing to المبني للمفعول به?', 'أَكْرَمَ → أُكْرِمَ', 'أَكْرَمَ → أَكْرِمْ', 'أَكْرَمَ → يُكْرِمُ',
   '**أُكرمَ** remains ماضيًا and is مبني للمفعول به. أَكرمْ is أمر; يُكرمُ is مضارع معلوم.'),
 Q('A2', 'Choose the correct distinction.', 'ليس جامد؛ اتصال التاء في لستُ لا يجعله تام التصرف.', 'ليس تام التصرف because لستُ exists.', 'نعم has no فاعل because it is جامد.',
   'Attachment of a ضمير and availability of other صيغ are separate matters. ليس remains جامدًا in لستُ; نعم still requires a فاعل.'),
 Q('A3', 'In **أطيعانِّ / أطعنَانِّ**, which element is فاعل respectively?', 'ألف الاثنين / نون النسوة', 'نون التوكيد / الألف الفاصلة', 'نون الإعراب / نون التوكيد',
   '**أطيعانِّ** retains ألف الاثنين as فاعل. **أطعنَانِّ** retains نون النسوة as فاعل and inserts ألف فاصلة.'),
 Q('B1', 'Complete **لن ... البابُ** with المبني للمفعول به.', 'يُكْسَرَ', 'يُكْسَرْ', 'يَكْسِرُ',
   '**لن يُكسرَ البابُ**: لن تنصب؛ يُكسر مبني للمفعول به؛ الباب نائب فاعل مرفوع.'),
 Q('B2', 'To أنتِ, choose the emphasised form corresponding to تكتبين.', 'لَتَكْتُبِنَّ', 'لَتَكْتُبَنَّ', 'لَتَكْتُبَانِّ',
   '**لتكتبِنّ** omits ياء المخاطبة and the expressed نون الإعراب. The كسرة before نّ indicates the omitted ياء.'),
 Q('B3', 'Which correction follows the ordinary مبتدأ وخبر analysis of **المعلّمان حضر**?', 'المعلّمان حضرا', 'المعلّمان حضروا', 'المعلّمان حضرت',
   'The خبر needs its فاعل ضمير to refer to the مثنّى مبتدأ: **حضرا**, with ألف الاثنين.'),
 T('C1', 'Read **حضر الحارسان. فُتِح الباب. لمّا يدخل الضيوف.** Supply the analyses and endings required by the intended statements.', [
  ('الحارسان', 'فاعل مرفوع بالألف', 'نائب فاعل منصوب', 'مبتدأ في الجملة الأولى'),
  ('الباب', 'نائب فاعل مرفوع بالضمة', 'مفعول به منصوب', 'فاعل لفعل معلوم'),
  ('يدخل', 'يَدْخُلْ: مجزوم بلمّا', 'يَدْخُلَ: منصوب بلمّا', 'يَدْخُلُ: مرفوع بلمّا'),
  ('لمّا', 'نفي مع توقّع الدخول', 'تأكيد حصول الدخول', 'طلب الدخول')],
   '**حضر الحارسانِ** keeps حضر مفردًا and raises الحارسان بالألف. **فُتح البابُ** raises نائب الفاعل. **لمّا يدخلْ الضيوفُ** has جزم and means the guests have not entered yet, with expectation of entry.'),
 T('C2', 'Complete a full تركيب of **سَتَكْتُبُ مريمُ رسالةً**.', [
  ('السين', 'حرف استقبال لا محل له', 'حرف نصب', 'ضمير فاعل'),
  ('تكتب', 'مضارع مرفوع بالضمة، والتاء للتأنيث', 'ماض مبني للمفعول به', 'أمر مبني على السكون'),
  ('مريم', 'فاعل مرفوع بالضمة', 'مفعول به منصوب', 'مبتدأ مؤخّر في هذا التحليل'),
  ('رسالة', 'مفعول به منصوب بالفتحة', 'نائب فاعل مرفوع', 'مضاف إليه'),
  ('حكم التأنيث', 'واجب مع هذا الفاعل الظاهر المتصل', 'ممتنع لأن الفاعل ظاهر', 'جائز فقط لأن الفعل مستقبل')],
   'السين للاستقبال؛ تكتب مضارع مرفوع بالضمة وتاؤه للتأنيث؛ مريم فاعل مرفوع بالضمة؛ رسالة مفعول به منصوب بالفتحة. التأنيث واجب with adjacent ظاهر مؤنث حقيقي.'),
 T('C3', 'Read **الشمس طلعت. حضر المعلمون. جيء بهم.** Apply the ordinary analyses and the شبه جملة account for the last sentence.', [
  ('فاعل طلعت', 'مستتر تقديره هي', 'التاء الساكنة', 'الشمس فاعل مقدّم هنا'),
  ('فاعل حضر', 'المعلمون، مرفوع بالواو', 'واو محذوفة مع نون التوكيد', 'مستتر هم مع ظاهر فاعل ثان'),
  ('بهم', 'شبه جملة في محل رفع نائب الفاعل', 'ضمير فاعل متصل بجيء', 'مفعول به منصوب')],
   '**الشمس** مبتدأ and طلعت with its مستتر هي is خبر, making التأنيث واجبًا. **حضر** has ظاهر فاعل المعلمون, so it stays مفردًا. **جيء بهم** has شبه الجملة in the نائب الفاعل position, while هم internally is في محل جر.'),
 Q('D1', '**تدخل لا على الماضي إذا تكررت لفظًا أو تقديرًا.** Which expression shows لفظًا?', 'لا صدّق ولا صلّى', 'لم يكتب', 'لقد كتب',
   '**لا صدّق ولا صلّى** repeats لا explicitly. لفظًا contrasts with an understood repetition تقديرًا.'),
 Q('D2', '**إن كان الفاعل اسمًا ظاهرًا وُحّد الفعل.** Choose its ordinary application.', 'دخل الضيوف', 'الضيوف دخل with no matching ضمير', 'دخلوا الضيوف with two simultaneous فاعلان',
   '**دخل الضيوف** has a following ظاهر فاعل and مفرد فعل. Preposing الضيوف as مبتدأ would instead require a matching embedded ضمير, as in الضيوف دخلوا.'),
 Q('D3', '**شبه الفعل خالٍ عن ضمير.** In **خشعًا أبصارهم**, which analysis fits this condition?', 'أبصار فاعل لخشع؛ لا فاعل ضمير إضافي فيه.', 'خشع فعل ماض and هم its attached فاعل.', 'أبصار مفعول به and خشع has two hidden فاعلان.',
   '**خشعًا** is شبه فعل, جمع خاشع. أبصار is its ظاهر فاعل; هم belongs to أبصار as مضاف إليه. No extra فاعل ضمير is assigned inside خشع.')
]
}

