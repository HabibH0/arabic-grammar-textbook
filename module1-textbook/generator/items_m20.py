"""Module 20: explicit الرسم / الوصل / الوقف targets and one answer per control."""
from item_kit import M,G
ITEMS={}
SOLUTIONS={}
def Q(k,p,a,b,c,why):
 SOLUTIONS[k]=why
 return M(k,p,[a,b,c],a)
def T(k,p,rows,why):
 SOLUTIONS[k]=('**الاختيارات الصحيحة:** '+ '؛ '.join('**'+lab+'**: '+a for lab,a,b,c in rows)+'. '+why) if k[0].isdigit() else ('**الاختيارات الصحيحة:**\n\n'+'\n'.join('- **'+lab+'**: '+a for lab,a,b,c in rows)+'\n\n'+why)
 return G(k,p,['التحليل'],[(lab,[([a,b,c],a)]) for lab,a,b,c in rows])

ITEMS['1']=[
 T('1G-1','Match the part of **أطاعوا** to its function.',[
 ('واو أطاعوا','ضمير في محل رفع فاعل','حرف مكتوب لا يلفظ هنا','علامة جر'),
 ('الألف بعد الواو','تكتب ولا تلفظ','ضمير ثان في محل نصب','ألف تنطق بعد الواو دائمًا'),
 ('أطاع مع واو الجماعة','فعل ماض مبني على الضم','فعل مضارع منصوب','اسم منقوص')], 'الواو is the attached فاعل. The following ألف is written but not pronounced and has no محل. Connection with واو الجماعة gives the فعل ماض its بناء على الضم.'),
 Q('1G-2','What does the extra ألف in the spelling **مائة** require in pronunciation?', 'No extra long ألف: read it like مئة.','Always pronounce a long ألف after ميم.','Delete the همزة because كل ألف صامتة.', 'The written ألف in this form does not supply a long sound. This rule does not delete the actual همزة of the word.'),
 Q('1I-1','Choose the appropriate ordinary spelling for “they wrote,” using واو الجماعة.', 'كتبوا','كتبو','كتبواا', 'كتبوا has واو الجماعة followed by its unpronounced ألف. The extra ألف is written once, without an added sound.'),
 Q('1I-2','Correct **هو يدعوا** to the ordinary spelling of “he calls.”', 'هو يدعو','هو يدعواا','هو يدع', 'The واو in يدعو is part of the فعل, not واو الجماعة. Do not add the ألف used after واو الجماعة in كتبوا.'),
 Q('1R','In a رسم of **زدناهم** without a full-sized ألف in نا, what remains true?', 'نا فاعل، وهم مفعول به؛ الرسم لا يحذف هذه العلاقات.','نا is no longer a ضمير.','هم must become فاعل because the ألف is absent.', 'نا is the attached فاعل and هم the مفعول به. The base رسم may omit a full-sized letter while leaving both grammatical relationships intact.'),
 Q('1-Read','**يكتب ولا يلفظ.** Which feature illustrates this?', 'الألف بعد واو الجماعة في أطاعوا','واو الجماعة نفسها في أطاعوا','الباء في بالكتاب', 'The ألف after واو الجماعة is the written but unpronounced feature. The واو still supplies a pronounced ضمير.')]

ITEMS['2']=[
 T('2G-1','Match the supplied أصل to its رسم.',[
 ('سعـ: الألف عن ياء، فعل ثلاثي','سعى','سعا','سعي with ياء منطوقة'),
 ('دعـ: الألف عن واو، فعل ثلاثي','دعا','دعى','دعو as the required ماض'),
 ('المصطفـ: the form taught here','المصطفى','المصطفا','المصطفي with ياء منطوقة')], 'Use ى for the stated أصل ياء in سعى, ا for أصل واو in دعا, and the taught longer form المصطفى. The ى in these examples is pronounced ألفًا.'),
 Q('2G-2','What does “تكتب الألف ياءً” mean in **الفتى**?', 'Write the undotted ى while pronouncing ألف.','Pronounce a final ياء after تاء.','The word must be مجرورًا بالياء.', 'This statement concerns رسم. It does not change the sound to ياء or determine the إعراب.'),
 Q('2I-1','Use the supplied origin: **رمـ** is a فعل ثلاثي whose final ألف comes from ياء, as in **رميتُ**. Choose its ماض.', 'رمى','رما','رميْ', 'The supplied related form reveals ياء. The الثلاثي rule therefore gives رمى, with a final ألف sound written ى.'),
 Q('2I-2','Use the supplied origin: **نجـ** is a فعل ثلاثي whose final ألف comes from واو, as in **نجوتُ**. Choose its ماض.', 'نجا','نجى','نجوْ', 'With أصل واو, the stated الثلاثي rule uses ا: نجا. This task supplies the origin rather than asking you to guess it from pronunciation.'),
 Q('2R','In **سعى الفتى**, why is the shared ى not enough to assign one analysis to both words?', 'سعى فعل ماض مبني؛ الفتى فاعل معرب بإعراب تقديري.','Both must be مجرورين بالياء.','Both must be مبنيين على الكسر.', 'The sentence identifies سعى as فعل and الفتى as فاعل. The common written ألف does not erase the difference between بناء الفعل and إعراب الاسم.'),
 Q('2-Read','**إذا كان أصلها ياءً.** What information does this condition require?', 'The origin of the ألف, supplied or shown by a related form.','Only whether a word appears at the end of a sentence.','Whether the preceding word ends in تنوين.', 'The rule concerns the underlying ياء or واو in a ثلاثي. Neither sentence position nor a preceding تنوين supplies that information.')]

ITEMS['3']=[
 T('3G-1','Identify همزة الوصل in the supplied settings.',[
 ('الكتاب','همزة أل','همزة قطع ثابتة في كل وصل','نون تنوين'),
 ('ابن','اسم من الأسماء المذكورة لهمزة الوصل','كل اسم يبدأ بهمزة قطع','فعل أمر'),
 ('اعرفْ','أمر الثلاثي ذو همزة الوصل','مصدر رباعي بهمزة قطع','فعل ماض'),
 ('استغفار','مصدر للماضي المتجاوز أربعة أحرف في هذه الصيغة','اسم لا يقبل وصلًا','ضمير متصل')], 'أل, the established اسم ابن, the supplied أمر اعرف, and المصدر استغفار all illustrate the stated positions. The rule identifies the initial همزة, not the word’s role in every possible sentence.'),
 Q('3G-2','Compare **اِعْمَلْ** at الابتداء and **وَاعْمَلْ** in وصل.', 'The همزة is pronounced in the first and omitted after و in the second.','Both require a new همزة after و.','The written ألف must be erased in واعمل.', 'همزة الوصل تثبت ابتداء وتحذف وصلًا in pronunciation. The written form واعمل remains.'),
 Q('3I-1','Read **واستغفرْ** in وصل from و. What happens to the initial همزة of استغفر?', 'It is omitted in pronunciation; the command remains فعل أمر.','It must be pronounced because the form is long.','The فعل becomes مصدرًا.', 'استغفر is the أمر paired with استغفرَ واستغفار. Dropping همزة الوصل in pronunciation does not change its word class or role.'),
 Q('3I-2','Correct: “Because همزة الوصل drops after و, **وأكرمَ** must also lose its همزة.”', 'أكرم has همزة قطع, which remains in وصل.','Correct: every written همزة drops after و.','و always removes the whole following فعل.', 'The rule is specific to همزة الوصل. The supplied contrast أكرم / وأكرم uses همزة قطع.'),
 Q('3R','In **اعرف ربّك واعبده**, what are ك and ه?', 'الكاف مضاف إليه؛ الهاء مفعول به','Both are فاعل for the preceding أمر','Both are حروف لا محل لها', 'ربّ is مفعول به ومضاف, so ك is في محل جر مضاف إليه. اعبد directly governs ه as مفعول به. The understood فاعل in both commands is أنت.'),
 Q('3-Read','**تثبت ابتداءً وتحذف وصلًا.** Select the accurate تطبيق.', 'Start اِعْرِفْ with its همزة; omit that همزة when joining وَاعْرِفْ.','Erase the ألف from every written اعرف.','Pronounce the همزة only at the end of a word.', 'The contrast is about starting from the word or joining into it. It is not a universal spelling deletion.')]

ITEMS['4']=[
 Q('4G-1','Choose the taught spelling in the connected father-name construction **محمدُ ___ عبدِ اللهِ**.', 'بنُ','إبنُ','بنوا', 'The ألف of ابن is omitted in this stated name construction, giving بن. It remains an اسم with a grammatical role.'),
 T('4G-2','Match each change to the correct level.',[
 ('محمد بن عبد الله: ألف ابن','حذف في الرسم في هذا التركيب','حذف للبدل كله','زيادة ضمير'),
 ('واعرف: همزة اعرف','حذف في النطق وصلًا مع بقاء الألف مكتوبة','حذف الألف من الرسم دائمًا','علامة جزم'),
 ('الاجتناب: لام أل في النطق','لام مكسورة للتوصّل إلى النطق بعد حذف الهمزة الداخلية','كسرة جرّ للمبتدأ','تاء التأنيث')], 'The ابن construction changes spelling. Ordinary همزة الوصل loss in واعرف changes pronunciation. The internal لام movement in الاجتناب is not a final إعراب علامة.'),
 Q('4I-1','At الابتداء with **الاستغفار**, choose the stated pronunciation of its beginning.', 'Initial أَ, then لِسْـ, without a fresh همزة between ل and س.','Initial أَلْ, then a separate إِ before س.','Delete the entire أل and pronounce only غفار.', 'أل precedes another همزة وصل. The inner همزة is omitted and لام takes كسرة. The ordinary spelling الاستغفار is retained.'),
 Q('4I-2','Why should **عبد الله بن أُبَيّ ابن سلول** not be changed mechanically to remove both ألفان?', 'The supplied established form retains the second ألف; a string of names alone is insufficient.','Every ابن must always lose ألف in writing.','Every ابن must become a ضمير.', 'The stated contrast explicitly retains ابن in the second position. Apply the actual construction or the supplied established spelling, not a visual shortcut.'),
 Q('4R','In **الاجتنابُ خيرٌ**, does the pronounced كسرة on لام أل make الاجتناب مجرورًا?', 'No: الاجتناب مبتدأ مرفوع؛ that كسرة is internal pronunciation.','Yes: any كسرة anywhere causes جر.','No: الاجتناب has no إعراب because it begins with أل.', 'الاجتناب is مبتدأ and its final ضمة marks رفع. An internal linking movement is not its final grammatical ending.'),
 Q('4-Read','**كُسرت اللام وحُذفت الهمزة في النطق.** In **الاجتناب**, which همزة is omitted by this statement?', 'The inner همزة of اجتناب after أل.','The همزة of any unrelated following word.','The final باء of اجتناب.', 'When beginning from الاجتناب, the initial همزة of أل is pronounced, while the inner همزة drops and لام takes كسرة. The question specifies that initial reading.')]

ITEMS['5']=[
 T('5G-1','Classify the stated meeting of ساكنين.',[
 ('الرحيمْ عند الوقف: ياء المدّ والميم','على حدّه','على غير حدّه مع وجوب حذف الياء','ليس فيه حرف مد'),
 ('الضالّين: ألف المدّ وأول لّ','على حدّه','يجب حذف الألف في كل نطق','اللام المشددة حرف واحد متحرّك فقط'),
 ('في الصدق عند الوصل','على غير حدّه؛ تحذف ياء في لفظًا','على حدّه كالوقف تمامًا','يجب حذف في من الرسم')], 'وقف and حرف مد before إدغام are the two accepted settings. In في الصدق, the وصل environment instead requires the taught deletion of حرف المد in pronunciation.'),
 Q('5G-2','How should **في** be written after you shorten its sound in **في الصدق**?', 'Retain في in writing.','Replace it permanently with ف.','Replace it with فيي.', 'حذف ياء المد here is لفظي in وصل. It does not create a new written حرف جر or remove the normal spelling.'),
 Q('5I-1','Read **في البيتِ** in وصل. The first meeting letter is ياء المد in في. Choose its treatment.', 'Omit that ياء in pronunciation, leaving a short كسرة on ف.','Give ياء a ضمة as though it were ميم الجمع.','Pronounce a fresh همزة of أل and keep every sound separately.', 'The ياء of في is حرف مد. After همزة الوصل drops, it meets the following ساكن; the taught rule omits the ياء in pronunciation.'),
 Q('5I-2','Correct: “Every meeting of حرف مد with a ساكن requires deleting the حرف مد.”', 'The على حدّه settings, including وقف and a following مدغم, must be excluded.','Correct: delete ألف الضالّين.','Correct: remove every long sound before any pause.', 'The condition على غير حدّه matters. The examples الرحيمْ at وقف and الضالّين retain their حرف المد.'),
 Q('5R','In **النجاةُ في الصدقِ**, which analysis survives shortening في in وصل?', 'في حرف جر؛ الصدق اسم مجرور؛ شبه الجملة خبر.','الصدق becomes مفعولًا به because في lost a sound.','في becomes a فاء عطف.', 'A pronunciation adjustment does not change the عامل. في still governs جر الصدق, and the شبه جملة supplies خبر النجاة.'),
 Q('5-Read','**على غير حدّه.** Why is this phrase essential in the deletion rule?', 'It excludes the accepted meetings where deletion is not required.','It means every وقف is forbidden.','It changes every اسم to فعل.', 'The rule does not apply identically to all ساكنين. First identify the setting, then choose the treatment.')]

ITEMS['6']=[
 T('6G-1','Choose the linking حركة on the indicated letter.',[
 ('هُمْ الناصحون: ميم الجمع','هُمُ: ضمة','هُمِ: كسرة','هُمَ: فتحة'),
 ('مِنْ النصيحة: النون','مِنَ: فتحة','مِنِ: كسرة','مِنُ: ضمة'),
 ('نصحتْ الأم: تاء التأنيث','نصحتِ: كسرة','نصحتُ: ضمة تاء الفاعل','نصحتَ: فتحة المخاطب'),
 ('دَعَوْا الله: واو لين للجمع','دَعَوُا: ضمة على الواو','حذف الواو كأنها واو مدّ','دَعَوِا: كسرة على الواو')], 'Apply the specific rules: ميم الجمع and واو لين للجمع take ضم؛ نون من takes فتح؛ تاء التأنيث takes كسر. These are adjustments for وصل, not new roles.'),
 Q('6G-2','In **خديجةُ ناصحةٌ الصديقاتِ**, the pronounced نون التنوين takes كسرة. What is ناصحة grammatically?', 'خبر مرفوع؛ the linking كسرة belongs to the نون sound.','اسم مجرور لأن نون التنوين كسرت','فعل أمر مبني على الكسر', 'The ضمة of رفع in ناصحةٌ and the temporary كسرة on the linking نون are different things. خديجة مبتدأ and ناصحة خبر.'),
 Q('6I-1','Join **أوْ** to **الكتابَ** in **اقرأ الدرسَ أوِ الكتابَ**. What describes the واو?', 'واو لين حُرّكت بالكسر؛ أو حرف عطف','واو الجماعة في محل رفع فاعل','واو مدّ يجب حذفها من الرسم', 'The واو in أوْ is preceded by فتحة and is not the special واو الجمع في الفعل. It takes كسرة in the stated وصل setting; أو remains حرف عطف.'),
 Q('6I-2','Complete the analysis of **لم يكتبِ الطالبُ**.', 'يكتب مجزوم بلم؛ الكسرة عارضة للتخلّص من التقاء الساكنين.','يكتب مجرور لأن آخره كسرة','يكتب مرفوع لأن الطالب بعده', 'لم supplies جزم. The original ending is سكون; the final باء takes an incidental كسرة in وصل before أل. Describe the سكون as مقدّر بسبب الحركة العارضة, not the فعل as مجرور.'),
 Q('6R','Compare **قالوا** and **دعَوْا** before a word beginning with همزة وصل. What must be checked?', 'واو المدّ in قالوا differs from واو اللين للجمع in دعَوْا.','Both contain identical حرف مدّ regardless of the preceding حركة.','The written ألف after و must always be pronounced.', 'واو قالوا follows ضمة; واو دعَوْا follows فتحة. The latter takes the special ضم treatment in دعَوُا الله; the former belongs to the حرف مد category.'),
 Q('6-Read','**يُضمّ الأول إن كان ميم جمع.** Choose the application.', 'أَنْتُمُ الناصحون','مِنُ النصيحة','نصحتُ الأمّ as تاء التأنيث', 'The first has ميم الجمع, so ضم applies. مِن uses فتح, and تاء التأنيث uses كسر in the stated linking environment.')]

ITEMS['7']=[
 T('7G-1','Match the written ending to the stated وقف pronunciation. Every answer is **نطق فقط**.',[
 ('محمدٌ','مُحَمَّدْ','مُحَمَّدُنْ','مُحَمَّدَا'),
 ('محمدٍ','مُحَمَّدْ','مُحَمَّدِنْ','مُحَمَّدِي'),
 ('محمدًا','مُحَمَّدَا بلا نون','مُحَمَّدَنْ','مُحَمَّدْ وفق قاعدة تنوين الضم'),
 ('رحمةً','رَحْمَهْ','رَحْمَتَا','رَحْمَتَنْ')], 'تنوين ضم وكسر stops with سكون; ordinary تنوين فتح stops with ألف. تاء مربوطة instead stops as هاء ساكنة, so apply its specific rule to رحمةً.'),
 Q('7G-2','In **قرأتُ الكتابَ**, stop on الكتاب. What changes?', 'Pronounce الكتابْ; it remains مفعولًا به منصوبًا.','It becomes اسمًا مجزومًا.','It becomes مبنيًا على السكون in all contexts.', 'The وقف removes the final pronounced حركة. It does not supply a جازم, cancel نصب, or change the word into مبني.'),
 Q('7I-1','Choose the وقف sound for **رأيتُ شجرةً**. The written sentence stays unchanged.', 'نطق فقط: شَجَرَهْ','نطق فقط: شَجَرَتَا','نطق فقط: شَجَرَتَنْ', 'شجرة ends in تاء مربوطة, so وقف uses هاء ساكنة. The general ألف rule for تنوين فتح does not replace this specific rule.'),
 Q('7I-2','You stop on **نرجو** in **رحمةَ اللهِ نرجو**. What happens to its final واو المدّ?', 'It is retained; وقف does not require deleting it.','It becomes a pronounced ألف after واو الجماعة.','It must be deleted because all final letters disappear in وقف.', 'نرجو ends in a retained حرف مد, not a short final حركة to be removed. Its واو is not واو الجماعة.'),
 Q('7R','Both **حضر خالدٌ** and **مررتُ بخالدٍ** end with نطق خالدْ at وقف. How do you identify the role?', 'Use the عامل and the connected form: فاعل first, اسم مجرور second.','The same pause sound makes both فاعلًا.','Both words lose every grammatical relationship.', 'وقف can conceal an ending difference. حضر requires فاعل; الباء governs جر. Recover those relationships rather than guessing from the pause sound.'),
 Q('7-Read','**الوقف على المتحرّك بحذف حركته.** What does حذف remove in **بالكتابِ** at وقف?', 'The final pronounced كسرة; الكتاب remains مجرورًا.','The entire حرف جر باء','The written word الكتاب', 'This describes pronunciation at the stopping point. It does not remove the عامل or the word from the sentence.')]

ITEMS['8']=[
 T('8G-1','Match the specified وقف treatment to its sound.',[
 ('الهدى: المقصور','الهدى مع ثبوت الألف','الهدي مع ياء منطوقة','الهدْ بحذف الألف'),
 ('هادٍ: دون إعادة الياء','هَادْ','هَادِي','هَادِنْ'),
 ('هادٍ: بإعادة الياء','هَادِي','هَادْ','هَادِنْ')], 'المقصور retains ألف. The supplied منقوص منوّن has two permitted وقف treatments; the row tells you which one to use.'),
 Q('8G-2','In **جاءنا هادٍ**, what is the role of هادٍ before any وقف?', 'فاعل مرفوع بضمة مقدّرة على الياء المحذوفة','مضاف إليه مجرور بسبب شكل التنوين','مبني على الكسر', 'جاء requires فاعل, which is هادٍ. It is اسم منقوص with a مقدّرة ضمة; the visible form does not make it مجرورًا.'),
 Q('8I-1','Apply **الوقف بإعادة الياء** to the matching منقوص form **مررتُ بقاضٍ**.', 'نطق فقط: قَاضِي','نطق فقط: قَاضْ under the other permitted treatment','نطق فقط: قَاضِنْ', 'قاضٍ has the same relevant منقوص منوّن form. The question specifies restoring ياء, so قاضي is the required pronunciation; قاضْ would represent the other treatment.'),
 Q('8I-2','In the supplied **لنسفعًا** example, what does the ألف-like وقف replace?', 'نون التوكيد الخفيفة','تنوين اسم فاعل','ميم الجمع', 'The word contains a فعل with نون التوكيد الخفيفة. Its written appearance here must not be mistaken for ordinary تنوين on an اسم.'),
 Q('8R','Under the taught وقف treatment, إذنْ sounds like إذا. What remains true?', 'It remains إذن in grammatical identity, not the separate conditional إذا.','It necessarily becomes أداة شرط.','It loses its whole meaning because نون changes.', 'The نون changes to ألف in the specified وقف. Similarity of the resulting sound does not replace the original word’s function with that of another word.'),
 Q('8-Read','**بالسكون أو بإعادة الياء.** What must a one-answer question about وقف هادٍ specify?', 'Which of the two permitted treatments to use.','That one treatment is always an error.','That هادٍ is a فعل مضارع.', 'Both treatments were allowed for the stated form. Naming the intended treatment makes the answer determinate.')]

ITEMS['R']=[
 T('A1','Match the phenomenon to the level it changes.',[
 ('ألف كتبوا','رسم بحرف لا يلفظ','رفع مفعول به','جزم ضمير'),
 ('همزة اعرف بعد و','نطق في وصل','حذف ألف من الرسم وجوبًا هنا','تحويل الأمر إلى مصدر'),
 ('كسرة تاء قالتِ البنتُ','حركة عارضة للوصل','جرّ فعل ماض','تاء الفاعل للمخاطبة'),
 ('سكون الكتابْ عند الوقف','نطق في وقف','جزم اسم','بناء دائم للاسم')], 'The examples distinguish spelling, linking pronunciation and pause pronunciation. None of these adjustments licenses inventing a new grammatical role.'),
 Q('A2','Which statement preserves the distinction between omission in الرسم and omission in الوصل?', 'A missing full-sized ألف in الرسم العثماني does not mean every corresponding sound is absent in all readings.','Every written letter must always be pronounced.','Every unpronounced letter must be erased from ordinary spelling.', 'The rules operate at different levels. Recognise the stated رسم and then apply the specified reading conditions, rather than assuming a universal one-to-one relation.'),
 T('B1','اختر ضبط الوصل للحرف المذكور.',[
 ('هم الناصحون: الميم','هُمُ','هُمِ','هُمَ'),
 ('من البيت: النون','مِنَ','مِنِ','مِنُ'),
 ('قالت البنت: التاء','قالتِ','قالتُ','قالتَ'),
 ('أو الكتاب: الواو','أَوِ','أَوُ','أَوَ')], 'ميم الجمع تأخذ الضم؛ نون مِن تأخذ الفتح؛ تاء التأنيث والواو في أو تأخذان الكسر في هذه المواضع. These are وصل adjustments.'),
 Q('B2','صحّح: **لم يكتبِ الطالبُ؛ يكتب مجرور بالكسرة.**', 'يكتب مجزوم بلم؛ الكسرة عارضة للتخلّص من التقاء الساكنين.','يكتب منصوب لأن الطالب فاعل.','لم حرف جر يدخل على الأفعال.', 'لم is a جازم, not حرف جر. The باء moves temporarily in وصل; identify the underlying جزم and its سكون المقدّر here.'),
 T('C1','Read: **قالت الأم: اعرف ربك واعبده. هم الناصحون. النجاة في الصدق.** Continue within each sentence. Start afresh at اعرف after the colon.',[
 ('قالت الأم: تاء قالت','تِ في الوصل؛ تاء تأنيث','تُ: ضمير المتكلم','تَ: ضمير المخاطب'),
 ('اعرف at the stated fresh beginning','همزة الوصل تثبت','همزة الوصل تحذف دائمًا','الهمزة تجعل الفعل ماضيًا'),
 ('واعبده: initial همزة of اعبد','تحذف في النطق بعد و','تثبت بعد و وجوبًا','تحذف الهاء بدلها'),
 ('هم الناصحون: الميم','مُ للتخلّص من التقاء الساكنين','مِ لأنها اسم مجرور','مَ لأنها مفعول به'),
 ('في الصدق: ياء في','تحذف لفظًا في الوصل مع بقاء الرسم','تحذف من الكتابة العادية','تصبح ياء مفعول به')], 'The instructions deliberately distinguish a fresh beginning at اعرف from continuous واعبده. Other joins require تِ، هُمُ and shortening في. The written words retain their grammatical identities.'),
 T('C2','Full تركيب: **نصحتِ الأمُّ أولادَها.**',[
 ('نصح','فعل ماض مبني على الفتح','مضارع مجرور','اسم فعل'),
 ('التاء','تاء التأنيث، حُرّكت بالكسر للوصل، لا محل لها','ضمير في محل رفع فاعل','اسم مجرور'),
 ('الأم','فاعل مرفوع بالضمة','مفعول به منصوب','مضاف إليه'),
 ('أولاد','مفعول به منصوب بالفتحة وهو مضاف','فاعل مرفوع','خبر إنّ'),
 ('ها','ضمير في محل جر مضاف إليه','ضمير في محل رفع فاعل','حرف وصل')], 'الأم is the فاعل; تاء التأنيث marks agreement and has no محل. أولادها is the مفعول به expression, with ها داخل إضافة. The linking كسرة does not transfer الفاعلية to التاء.'),
 T('C3','حلّل **مررتُ بخالدٍ**، ثم قف في آخرها.',[
 ('مررت','فعل ماض مبني على السكون','فعل مضارع منصوب','اسم مقصور'),
 ('التاء','ضمير في محل رفع فاعل','تاء تأنيث لا محل لها','ضمير في محل جر'),
 ('الباء','حرف جر','حرف نصب للمضارع','واو المعية'),
 ('خالد في تركيب الجملة','اسم مجرور بالباء وعلامة جرّه الكسرة','اسم مجزوم بسبب الوقف','اسم مبني على السكون دائمًا'),
 ('بخالد','جار ومجرور متعلقان بمررت','جملة في محل رفع خبر إنّ','مفعول مطلق'),
 ('النطق عند الوقف','بِخَالِدْ، مع بقاء الجر في التحليل','بِخَالِدِنْ مع إبقاء التنوين','بِخَالِدَا كمنوّن الفتح')], 'The الباء determines جر خالد before and after the pause in grammatical analysis. وقف removes the final كسرة and تنوين sound; it does not make خالد مجزومًا or مبنيًا.'),
 T('C4','Read: **رأيت زهرة. ثم قرأت كتابا. ثم جاءنا هاد.** Supply the intended forms زهرةً، كتابًا، هادٍ, and stop after each sentence. For هادٍ choose إعادة الياء. Answers are نطق فقط.',[
 ('زهرةً','زَهْرَهْ','زَهْرَتَا','زَهْرَتَنْ'),
 ('كتابًا','كِتَابَا بلا نون','كِتَابَنْ','كِتَابْ وفق تنوين الضم'),
 ('هادٍ with إعادة الياء','هَادِي','هَادْ وفق الوجه الآخر','هَادِنْ')], 'Apply each specific form: تاء مربوطة stops as هاء; ordinary تنوين فتح stops with ألف; the specified منقوص treatment restores ياء. The task supplies the connected forms so the marking concerns وقف, not guessing their roles.'),
 Q('D1','**يحذف الأول إذا كان حرف مدّ، ويُضمّ إذا كان واو لين للجمع في الفعل.** اختر التطبيق.', 'في البيت: حذف ياء المدّ لفظًا؛ دعَوُا الله: ضم واو اللين.','في البيت: ضم الياء؛ دعوا الله: نطق الألف المكتوبة.','كل واو ساكنة حرف مدّ مهما كانت حركة ما قبلها.', 'في contains ياء مد preceded by كسرة. دعَوْا contains واو لين preceded by فتحة and used for الجمع. The two conditions lead to different treatments.'),
 Q('D2','**الوقف لا يغيّر الموقع الإعرابي.** اختر الدليل الصحيح.', 'الكتابَ في قرأت الكتابَ يبقى مفعولًا به وإن سُكّن آخره وقفًا.','كل اسم موقوف عليه يصير مجزومًا.','خالدٌ يصير حرفًا إذا حذف تنوينه في الوقف.', 'The عامل and relationship remain. Pronunciation at a stopping point cannot replace نصب with جزم or change an اسم into a حرف.')]
