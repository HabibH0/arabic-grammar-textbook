"""Module 15: each control has one correct choice under the stated conditions."""
from item_kit import M, G
ITEMS = {}
SOLUTIONS = {}
def Q(k,p,a,b,c,why):
    SOLUTIONS[k]=why
    return M(k,p,[a,b,c],a)
def T(k,p,rows,why):
    SOLUTIONS[k]=why
    return G(k,p,['التحليل'],[(lab,[([a,b,c],a)]) for lab,a,b,c in rows])

ITEMS['1']=[
 T('1G-1','Match the role and علامة of **أحمد**, without أل or إضافة.',[
 ('جاء أحمدُ','فاعل مرفوع بالضمة بلا تنوين','فاعل مبني على الضم','مفعول به منصوب'),
 ('رأيت أحمدَ','مفعول به منصوب بالفتحة بلا تنوين','اسم مجرور بالفتحة','فاعل مرفوع'),
 ('مررت بأحمدَ','اسم مجرور بالفتحة نيابة عن الكسرة','مفعول به منصوب بالفتحة','مبني على الفتح')], 'جاء requires فاعل؛ رأيت requires مفعول به؛ الباء gives جر. أحمد is معرب غير منصرف, so جر uses فتحة when neither أل nor إضافة is present.'),
 T('1G-2','Match the terminology.',[
 ('متمكّن أمكن','معرب منصرف','معرب غير منصرف','مبني'),
 ('متمكّن غير أمكن','معرب غير منصرف','مبني','حرف'),
 ('غير متمكّن','مبني','منصرف','غير منصرف معرب')], 'The first two are both معرب. Only غير متمكّن names the مبني category in this classification.'),
 Q('1I-1','Complete **تحدّثتُ معَ أحمد___**. أحمد is مضاف إليه, with no أل and no following إضافة of its own.', 'أحمدَ: مضاف إليه مجرور بالفتحة','أحمدِ: every مضاف إليه must end in كسرة','أحمدًا: مفعول به', 'معَ is مضاف and أحمدَ مضاف إليه. The role requires جر; غير المنصرف uses فتحة for that جر in this setting.'),
 Q('1I-2','Correct: “أحمدَ has the same ending after رأيت and باء, so it must be مبني.”', 'It is معرب; فتحة can mark either نصب or جر here.','Correct: أحمد is always مبني على الفتح.','أحمد cannot occur after حرف جر.', 'جاء أحمدُ displays رفع. رأيت أحمدَ and بأحمدَ have different إعراب despite the shared فتحة. Equality of one visible ending is not proof of بناء.'),
 Q('1R','In **مررتُ بالكتابِ**, why is absence of تنوين insufficient evidence for منع الصرف?', 'أل prevents تنوين; الكتاب remains مجرورًا بالكسرة.','Every word with أل is مبني.','الكتاب is منصوب because it lacks تنوين.', 'Check the construction before classifying. أل removes تنوين from ordinary منصرف أسماء too.'),
 Q('1-Read','**غير المنصرف اسم معرب.** Which follows?', 'بأحمدَ: مجرور بالفتحة، لا مبني على الفتح','بأحمدَ: منصوب بالباء','بأحمدَ: لا محل له كالحروف', 'الباء governs جر. منع الصرف changes the علامة of that جر without changing أحمد into مبني or into a حرف.')]

ITEMS['2']=[
 T('2G-1','Match the relevant ending.',[
 ('ذكرى','ألف التأنيث المقصورة','ألف التأنيث الممدودة','تاء التأنيث'),
 ('صحراء','ألف التأنيث الممدودة','ألف ثالثة أصلية','تركيب مزجي'),
 ('هدًى','ليست ألفه ألف التأنيث؛ تقع ثالثة','ألف تأنيث رابعة','مجموع منتهى الجموع')], 'ذكرى and صحراء have the two qualifying forms. هدى has an ألف in third position and is not included by this cause.'),
 Q('2G-2','Why does **علماء** qualify here even when it is نكرة?', 'ألف التأنيث الممدودة تكفي وحدها','كل جمع غير منصرف بلا شروط','كل نكرة ممنوعة من الصرف', 'This cause needs neither العلمية nor a particular syntactic role. علماء ends in the qualifying ألف التأنيث الممدودة.'),
 Q('2I-1','Complete **مررتُ بصحراءَ واسع___**.', 'واسعةٍ: نعت مجرور بالكسرة','واسعةَ: must copy the فتحة of صحراء','واسعةٌ: خبر مرفوع', 'واسعة is منصرف, so its جر uses كسرة مع التنوين. It follows صحراء in جر, while the علامة differs.'),
 Q('2I-2','Analyse **بسلمى** in the ordinary عَلَم use.', 'سلمى مجرور بفتحة مقدّرة نيابة عن الكسرة','سلمى مبني على السكون','سلمى منصوب بفتحة ظاهرة', 'سلمى has ألف التأنيث المقصورة. The final ألف prevents the حركة from appearing, so the فتحة of جر is مقدّرة للتعذّر.'),
 Q('2R','Which explains why **ذكرى** and **أحمد** can both lack تنوين?', 'Different qualifying causes: ألف التأنيث in ذكرى; العلمية ووزن الفعل in أحمد.','Both must be مبنيان.','Both must be جمعًا.', 'A shared ending behaviour does not require a shared cause. Both are معربان غير منصرفين in the stated uses.'),
 Q('2-Read','**لا تقع ألف التأنيث الزائدة إلا رابعةً فصاعدًا.** What does this establish about **هدًى**?', 'Its third-position ألف is not ألف التأنيث.','Its ألف prevents الصرف automatically.','Any word ending in ى must be مبني.', 'The position test excludes هدى from this cause. Do not use the visual shape ى alone as a classification.')]

ITEMS['3']=[
 T('3G-1','Apply the structural test to the supplied forms.',[
 ('مَسَاجِد','بعد الألف حرفان','بعد الألف ثلاثة أحرف أوسطها متحرّك','ليس جمعًا'),
 ('مَصَابِيح','بعد الألف ثلاثة أحرف أوسطها ساكن','بعد الألف حرف واحد','ألف التأنيث المقصورة'),
 ('صَوَافّ','بعد الألف حرفان مدغمان','بعد الألف حرف واحد فقط','بعد الألف أربعة أحرف')], 'مساجد has ج د; مصابيح has ب ي ح with ي ساكنة; the شدّة in صوافّ represents ف ف. Count the underlying letters, not just written shapes.'),
 Q('3G-2','Which contrast is correct?', 'مساجد غير منصرف بمنتهى الجموع؛ ملائكة لا يطابق هذا البناء.','Both qualify merely because they contain ألف.','Neither can be جمعًا.', 'منتهى الجموع has a particular structure. ملائكة does not end with the stated two-letter or three-letter pattern after ألف.'),
 Q('3I-1','**مَفَاتِيح** means keys and has ت، ي، ح after its ألف, with ي ساكنة. Complete **بحثتُ عن ___** without أل or إضافة.', 'مفاتيحَ','مفاتيحٍ','مفاتيحًا', 'The supplied structure is منتهى الجموع. عن gives جر, marked here by فتحة without تنوين.'),
 Q('3I-2','Correct: “Every جمع مكسّر is غير منصرف because it is a جمع.”', 'The specified منتهى الجموع pattern qualifies; جمع alone is insufficient.','Correct: all جموع have منع الصرف.','Only أعلام can be غير منصرف.', 'مساجد and مصابيح qualify by their patterns. The label جمع مكسّر is broader, as the contrast with ملائكة shows.'),
 Q('3R','Why do **صحراء** and **مصابيح** need no العلمية to prevent الصرف?', 'Each has a cause that يقوم مقام السببين.','Both secretly function as أعلام in every use.','Both are مبنيان على الفتح.', 'صحراء has ألف التأنيث؛ مصابيح has منتهى الجموع. Each is independently sufficient, and neither makes the word مبنيًا.'),
 Q('3-Read','**الحرفان بعد الألف قد يكونان مدغمين.** Which form illustrates this?', 'صوافّ','مساجد with ج and د distinct','هدًى', 'صوافّ ends with فّ, representing two فاء letters in إدغام. مساجد has two distinct letters, not إدغام.')]

ITEMS['4']=[
 T('4G-1','Match the condition to the example.',[
 ('أحمر / حمراء','صفة أفعل لا تقبل التاء','صفة أفعل تقبل التاء','علم مركّب'),
 ('أرمل / أرملة','يقبل التاء فلا يمنع بهذا الباب','غير قابل للتاء','منتهى الجموع'),
 ('غضبان / غضبى','صفة فعلان مؤنثها فعلى','صفة فعلان مؤنثها فعلانة','علم أعجمي'),
 ('ندمان / ندمانة: companion','لا يحقق شرط فعلى','ممنوع لانتهاء كل اسم بان','ألف تأنيث مقصورة')], 'أحمر meets the stated أفعل condition; أرمل permits أرملة. غضبان has غضبى, while the specified ندمان has ندمانة, so the فعلان rule does not apply to it.'),
 Q('4G-2','What does **مثنى** express in **جاء الطلابُ مثنى**?', 'Two at a time; معدول عن ثنتين ثنتين','Exactly one pair with no distributive meaning','An ordinary عَلَم for a student', 'مثنى is a descriptive distributive form. Its منع combines الوصفية والعدل; it does not simply name a total count.'),
 Q('4I-1','**أَصْفَر / صَفْرَاء** means yellow and is أصليّ في الوصف. Complete **بقلمٍ ___**.', 'أصفرَ','أصفرٍ','أصفرٌ', 'أصفر has الوصفية ووزن أفعل and does not take تاء in its مؤنث. It is نعت مجرور بالفتحة نيابة عن الكسرة, without أل or إضافة.'),
 Q('4I-2','Why does **أربع** fail the taught أفعل test, even when used descriptively?', 'It is originally عددًا, not أصلًا في الوصف.','It is necessarily مبني على الكسر.','Every four-letter word is منصرف.', 'Both stated conditions matter. Incidental descriptive use does not supply original الوصفية.'),
 Q('4R','In **برجلٍ غضبانَ**, how can the نعت match its منعوت?', 'Both are مجروران; the علامة is كسرة in رجل and فتحة in غضبان.','The نعت is منصوب and agrees by meaning only.','غضبان must become غضبانٍ in every use.', 'التبعية is in جر here. The noun classes explain the different علامات. غضبان qualifies through الوصفية والألف والنون with غضبى.'),
 Q('4-Read','**مؤنثه فعلى دون فعلانة.** Choose the qualifying pair.', 'غضبان / غضبى','ندمان / ندمانة in the supplied sense','أرمل / أرملة as a فعلان pair', 'غضبان وغضبى meet the exact condition. The other pairs do not establish فعلان/فعلى.')]

ITEMS['5']=[
 T('5G-1','Match each عَلَم to the cause added to العلمية.',[
 ('أحمد','وزن الفعل','ألف التأنيث','التركيب المزجي'),
 ('عثمان','الألف والنون الزائدتان','العدل','منتهى الجموع'),
 ('عمر','العدل','تاء التأنيث','العجمة')], 'أحمد has the relevant فعل pattern; عثمان has added ألف ونون; عمر is treated as معدول عن عامر. العلمية is part of each combination.'),
 Q('5G-2','Treat **حسّان** as derived from **الحُسن**, وزن فعّال. Complete **مررتُ بحسّان___**.', 'حسّانٍ','حسّانَ on the الحسّ derivation','حسّانُ', 'Under the stated derivation النون أصلية, so this name has صرف. الباء therefore gives كسرة مع التنوين: بحسّانٍ.'),
 Q('5I-1','Now use **حسّان** from **الحسّ**, وزن فعلان. Complete **كتبتُ إلى حسّان___**.', 'حسّانَ','حسّانٍ on the الحسن derivation','حسّانٌ', 'The stated account makes الألف والنون زائدتين. Combined with العلمية, this gives منع الصرف and جر بالفتحة after إلى.'),
 Q('5I-2','Correct: “يعرب in **حضر يعربُ** is a مضارع because its form resembles one.”', 'It is a عَلَم and فاعل; وزن الفعل helps explain منع الصرف.','Correct: حضر has no فاعل here.','It must be حرفًا لا محل له.', 'Form and use are separate tests. يعرب names the person who arrived, so it is اسم علم، فاعل مرفوع بالضمة بلا تنوين.'),
 Q('5R','Compare **جاء خالدٌ** and **جاء عمرُ**.', 'Both are فاعل وعَلَم; عمر additionally has العدل, so it lacks تنوين.','Every عَلَم must lack تنوين, so خالدٌ is wrong.','عمر is مبني because it lacks تنوين.', 'العلمية alone does not suffice. خالد is منصرف; عمر qualifies through العلمية والعدل.'),
 Q('5-Read','**جاز الصرف والمنع بحسب التقدير.** What makes a single-answer question about حسّان unambiguous?', 'Specifying الحسن or الحسّ as the derivation','Declaring all names ending in ان identical','Ignoring the عامل and both derivations', 'The origin determines whether النون is أصلية or زائدة. The question must fix that account before asking for one ending.')]

ITEMS['6']=[
 T('6G-1','Match the reason or treatment.',[
 ('طلحة, naming a man','علم مؤنث بالتاء؛ يمنع من الصرف','منصرف لأن المسمّى رجل دائمًا','مبني على الكسر'),
 ('مريم','علم مؤنث بالمعنى زائد على ثلاثة أحرف','جمع منتهى الجموع','صفة فعلان'),
 ('هند','يجوز الصرف والمنع؛ المنع أصحّ','يجب البناء على الكسر','يمتنع الصرف في كل استعمال')], 'طلحة qualifies through the form’s تاء with العلمية, regardless of a male referent. مريم meets the length condition. هند has a recognised choice rather than a single obligatory treatment.'),
 Q('6G-2','Use **المنع** for هند in **سلّمتُ على ___**.', 'هندَ','هندٍ with الصرف','هندُ', 'The selected منع gives فتحة نيابة عن الكسرة after على. هندٍ is valid under الصرف but is not the requested treatment.'),
 Q('6I-1','Use **الصرف** for هند in **تحدّثتُ إلى ___**.', 'هندٍ','هندَ with المنع','هندٌ', 'Under الصرف, إلى gives جر بالكسرة with تنوين. The exercise deliberately chooses the permitted alternative to المنع.'),
 Q('6I-2','Analyse **لحذامِ** using the **حجازي** treatment.', 'حذام مبني على الكسر في محل جر باللام','حذام معرب مجرور بالفتحة','حذام منصوب بكسرة ظاهرة', 'The حجازي account is بناء على الكسر. The تميمي account treats this عَلَم as غير منصرف معرب; do not merge the two.'),
 Q('6R','Choose the accurate statement about أسماء القبائل والأماكن.', 'Their recognised usage matters; not all take one uniform treatment.','Every place-name is مبني.','Every tribe-name must be منصرف.', 'The examples include both منع and صرف, and sometimes both are recognised. التأنيث versus التذكير helps explain the stated uses, but guessing a universal geographical rule does not.'),
 Q('6-Read','**يجوز في هند الصرف والمنع، والمنع أصحّ.** Which conclusion follows?', 'هندٍ can be valid when الصرف is selected.','هندٍ is never valid because المنع أصحّ.','هند must be مبنيًا in both accounts.', 'Preference does not cancel permission. The two analyses produce different visible جر endings, so questions name the selected one.')]

ITEMS['7']=[
 T('7G-1','Match each expression to the selected classification.',[
 ('إبراهيم','علم عجمي زائد على ثلاثة أحرف','علم على وزن فعّال مع نون أصلية','مبني على الكسر'),
 ('بعلبكّ','علم مركّب تركيب مزج غير مختوم بويه','علم مختوم بويه','صفة معدولة'),
 ('سيبويه','مبني على الكسر في التحليل المعتمد','معرب مجرور بالفتحة دائمًا','جمع منتهى الجموع')], 'إبراهيم combines العلمية والعجمة. بعلبكّ meets the تركيب مزجي condition. The ويه ending sends سيبويه to the adopted بناء account.'),
 Q('7G-2','Complete **سافر إبراهيم___ إلى بعلبك___**.', 'إبراهيمُ؛ بعلبكَّ','إبراهيمٌ؛ بعلبكٍّ','إبراهيمَ؛ بعلبكُّ', 'إبراهيم is فاعل مرفوع بالضمة without تنوين. إلى governs بعلبكّ, which takes فتحة for جر because of العلمية والتركيب المزجي.'),
 Q('7I-1','Analyse **قرأتُ لسيبويهِ**.', 'سيبويه مبني على الكسر في محل جر','سيبويه مجرور بكسرة إعراب لأنه منصرف','سيبويه فاعل مرفوع', 'The لام establishes محل جر. The كسر is بناء in this name, not an إعراب ending chosen by the لام.'),
 Q('7I-2','Correct: “Any name made of more than one word is مركّب مزجي and غير منصرف.”', 'عبد الله has إضافة; the مزجي rule requires the specified kind of تركيب.','Correct: عبد الله and بعلبك have identical structure.','Every مركّب is مبني على الكسر.', 'Do not replace تركيب المزج with the broad idea of multiple parts. In عبد الله, عبد is مضاف and الله مضاف إليه.'),
 Q('7R','Compare **ببعلبكَّ** and **لسيبويهِ** in the adopted accounts.', 'بعلبك معرب مجرور بالفتحة؛ سيبويه مبني في محل جر','Both are مبنيان','Both are منصوبان because they lack تنوين', 'Both follow حرف جر, but one expresses جر through إعراب and the other through محل. The ending ويه is a decisive condition here.'),
 Q('7-Read','**غير مختوم بويه.** What must you check?', 'The name must not end in ويه for this منع الصرف rule.','The name must end in ويه to be غير منصرف by this rule.','Every word with و somewhere is excluded.', 'مختوم identifies the end of the word. سيبويه fails this condition and is مبني in the account taught.')]

ITEMS['8']=[
 T('8G-1','Choose the ending and immediate reason.',[
 ('في مساجد, no أل or إضافة','مساجدَ: جر بالفتحة','مساجدٍ: جر بالكسرة والتنوين','مساجدُ: رفع'),
 ('في المساجد','المساجدِ: جر بالكسرة لدخول أل','المساجدَ: أل never affects the علامة','المساجدٍ: أل permits تنوين'),
 ('في مساجد المدينة','مساجدِ: جر بالكسرة لأنه مضاف','مساجدَ: إضافة cannot affect it','مساجدٍ: مضاف منوّن')], 'The bare منتهى الجموع has فتحة in جر. أل or being مضاف restores كسرة, but neither allows تنوين in these constructions.'),
 Q('8G-2','Complete **مررتُ ببعضِ مساجد___**. مساجد has no أل or following مضاف إليه.', 'مساجدَ','مساجدِ because it is مضاف إليه','مساجدٍ', 'بعض is the مضاف; مساجد is only مضاف إليه. That position does not restore كسرة, so it remains مجرورًا بالفتحة.'),
 Q('8I-1','In **لكلّ فرعونٍ موسًى**, the names are used as نكرتين naming types. Why does فرعون have تنوين?', 'The العلمية needed for its منع has been removed.','كلّ always makes every اسم منصرفًا.','فرعون has become مبنيًا.', 'This use removes the particular-name condition. It does not mean that كلّ can override any independent cause of منع الصرف.'),
 Q('8I-2','Correct: “محمد in **بمحمدِ بنِ عبدِ اللهِ** has no تنوين, so it must be غير منصرف.”', 'محمد remains منصرفًا؛ التنوين dropped in the stated ابن construction.','Correct: change it to بمحمدَ.','محمد is مبني على الكسر.', 'The observed كسرة remains جرّ الإعراب. Absence of تنوين can have a construction-specific cause other than منع الصرف.'),
 Q('8R','Does the recognised reading **سلاسلًا وأغلالًا وسعيرًا** permit adding تنوين to any منتهى الجموع in an ordinary exercise?', 'No: it illustrates a specified صرف للتناسب.','Yes: منتهى الجموع never prevents الصرف.','Yes: every مفعول به must have تنوين.', 'A stated special reading is recognised on its own terms. It does not erase the ordinary rule for words such as مصابيح or مساجد.'),
 Q('8-Read','**كونه مضافًا لا مجرّد كونه مضافًا إليه.** Which expression restores كسرة on مساجد through إضافة?', 'بمساجدِ المدينةِ','ببعضِ مساجدَ','بمساجدَ with no following addition', 'In مساجد المدينة, مساجد is itself مضاف. In بعض مساجد, it is the مضاف إليه, which does not supply the required condition.')]

ITEMS['R']=[
 T('A1','Match each qualifying use to its سبب أو سببان.',[
 ('صحراء','ألف التأنيث الممدودة','العلمية وحدها','التركيب المزجي'),
 ('مصابيح','مجموع منتهى الجموع','الوصفية والعدل','العلمية والتأنيث'),
 ('أحمر, أصلي في الوصف','الوصفية ووزن أفعل مع عدم قبول التاء','العلمية والعجمة','الجمع'),
 ('عثمان','العلمية والألف والنون الزائدتان','الوصفية والعدل','التأنيث بالتاء'),
 ('بعلبكّ','العلمية والتركيب المزجي','الوصفية وحدها','البناء لوجود ويه')], 'Two causes suffice independently here: ألف التأنيث and منتهى الجموع. The other examples require their stated combinations and conditions.'),
 Q('A2','Which claim wrongly replaces a شرط with a guess?', 'كل اسم آخره ان غير منصرف بلا فحص للأصل أو الاستعمال.','غضبان مؤنثه غضبى فيحقق الشرط المذكور.','حسّان من الحسن نونه أصلية في التحليل المحدّد.', 'Final ان alone does not establish either the descriptive condition or the added-letter condition in a عَلَم. حسّان demonstrates why origin matters.'),
 T('B1','اختر الضبط بحسب الشرط المحدّد.',[
 ('على هند: اختر المنع','على هندَ','على هندٍ','على هندُ'),
 ('إلى حسّان: من الحسن','إلى حسّانٍ','إلى حسّانَ','إلى حسّانُ'),
 ('بمصابيح الغرفة','بمصابيحِ الغرفةِ','بمصابيحَ الغرفةِ','بمصابيحٍ الغرفةِ'),
 ('عن أصفر: صفة بلا أل ولا إضافة','عن أصفرَ','عن أصفرٍ','عن أصفرُ')], 'هند uses the chosen منع. حسّان from الحسن uses صرف. مصابيح is مضاف, restoring كسرة. أصفر meets the وصفية condition and has فتحة for جر in the specified form.'),
 Q('B2','صحّح: **مررتُ برجلٍ غضبانَ؛ غضبان منصوب لأنه مفتوح الآخر.**', 'غضبان نعت مجرور بالفتحة نيابة عن الكسرة.','غضبان فاعل مرفوع.','غضبان مبني على الفتح لأنه نعت.', 'It follows رجل in جر. Its منع الصرف explains the فتحة. A حركة cannot identify the syntactic role independently of the relationship.'),
 T('C1','Read: **سافر إبراهيم إلى بعلبك. مرّ بمساجد قديمة. صلّى في مساجد المدينة.** Restore the indicated endings.',[
 ('إبراهيم','إبراهيمُ: فاعل بلا تنوين','إبراهيمٌ: فاعل منصرف','إبراهيمَ: مفعول به'),
 ('بعلبك','بعلبكَّ: مجرور بالفتحة','بعلبكٍّ: مجرور بالكسرة والتنوين','بعلبكُّ: خبر'),
 ('بمساجد','بمساجدَ: منتهى الجموع بلا أل أو إضافة','بمساجدٍ: كل جمع منصرف','بمساجدُ: مرفوع'),
 ('قديمة','قديمةٍ: نعت مجرور بالكسرة','قديمةَ: يجب نسخ الفتحة','قديمةٌ: فاعل مرّ'),
 ('في مساجد المدينة','مساجدِ لأنه مضاف؛ المدينةِ مضاف إليه','مساجدَ لأن الإضافة تمنع الكسرة','مساجدٍ مع التنوين')], 'Read إبراهيمُ، بعلبكَّ، بمساجدَ قديمةٍ، في مساجدِ المدينةِ. The ضمير المستتر هو in مرّ and صلّى returns to إبراهيم. قديمة is منصرف and takes كسرة despite the فتحة on its منعوت. إضافة in the last جملة restores كسرة on مساجد.'),
 T('C2','Full تركيب: **كتبَ عمرُ إلى عثمانَ.**',[
 ('كتب','فعل ماض مبني على الفتح','اسم مرفوع','مضارع مجزوم'),
 ('عمر','فاعل مرفوع بالضمة؛ غير منصرف للعلمية والعدل','فاعل مبني على الضم','مفعول به منصوب'),
 ('إلى','حرف جر لا محل له','حرف نصب للفعل','اسم في محل رفع'),
 ('عثمان','مجرور بفتحة نيابة عن الكسرة؛ للعلمية والألف والنون الزائدتين','منصوب بإلى','مبني على الفتح'),
 ('إلى عثمان','جار ومجرور متعلقان بكتب','جملة في محل رفع فاعل','مضاف ومضاف إليه بلا حرف جر')], 'The roles come from كتب and إلى. العلمية والعدل explain absence of تنوين on عمر; العلمية والألف والنون explain the special جر علامة on عثمان. Both names remain معربين.'),
 T('C3','حلّل الجملة كاملة: **صلّيتُ في المساجدِ.**',[
 ('صلّيت','فعل ماض مبني على السكون لاتصاله بتاء الفاعل','فعل مضارع منصوب','اسم فعل لا محل له'),
 ('التاء','ضمير مبني على الضم في محل رفع فاعل','تاء تأنيث لا محل لها','ضمير في محل جر'),
 ('في','حرف جر لا محل له','اسم ظرف منصوب','حرف يرفع الاسم'),
 ('المساجد','اسم مجرور بالكسرة لدخول أل','اسم مجرور بالفتحة رغم أل','مبني على الكسر'),
 ('في المساجد','جار ومجرور متعلقان بصلّيت','مفعول مطلق منصوب','جملة فعلية مستقلة')], 'المساجد retains the منتهى الجموع form, but أل restores كسرة in جر. It has no تنوين because of أل. The فعل and attached فاعل form the main structure; في المساجد relates to صلّيت.'),
 Q('D1','**التأنيث بألف زائدة يقوم مقام السببين.** اختر النتيجة.', 'لا تشترط العلمية لمنع صحراء من الصرف.','كل اسم مؤنث المعنى وحده غير منصرف.','ألف هدى الثالثة تمنع الصرف.', 'The statement specifically concerns ألف التأنيث الزائدة. It is sufficient independently; it must not be widened to every kind of تأنيث or every final ألف.'),
 Q('D2','**لا يستلزم سقوط التنوين منع الصرف.** اختر الدليل.', 'محمدِ في بمحمدِ بنِ عبدِ اللهِ','أحمدَ لأنه لا يكون إلا مبنيًا','مصابيحَ لأن كل فتحة علامة نصب', 'محمد is منصرف despite loss of تنوين in this construction, and its كسرة expresses جر. The other choices wrongly equate absence of تنوين with بناء or فتحة with نصب.')]
