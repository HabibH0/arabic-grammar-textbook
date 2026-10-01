"""Module 11: one defensible answer per choice, with explicit analysis constraints."""
from item_kit import M, G
ITEMS = {}
SOLUTIONS = {}
def Q(k, p, a, b, c, why):
    SOLUTIONS[k] = why
    return M(k, p, [a,b,c], a)
def T(k, p, rows, why):
    SOLUTIONS[k] = why
    return G(k, p, ['التحليل'], [(lab,[([a,b,c],a)]) for lab,a,b,c in rows])

ITEMS['1'] = [
 T('1G-1','Match the purpose of المفعول المطلق.',[
 ('سجد سجودًا','للتوكيد','للنوع','للعدد'),
 ('سار سيرًا سريعًا','للنوع','للتوكيد فقط','للعدد'),
 ('سجد سجدتين','للعدد','للنوع فقط','للتوكيد فقط')], 'سجودًا is a bare مصدر؛ سريعًا specifies the نوع of سيرًا؛ سجدتين counts two occurrences and is منصوب بالياء.'),
 Q('1G-2','In **سعيتُ بعضَ السعيِ**, what receives نصب?', 'بعضَ: نائب عن المصدر، وهو مضاف','السعيَ: مفعول به','Both words must be منصوب', 'بعضَ stands in place of the مصدر and is منصوب؛ السعيِ is مضاف إليه مجرور. The two words have different relationships.'),
 Q('1I-1','Complete **ركعَ المصلّي ___** to express exactly two occurrences.', 'ركعتينِ','ركوعًا','ركوعٍ', 'ركعتينِ is مفعول مطلق للعدد منصوب بالياء لأنه مثنى. ركوعًا alone reinforces the action without specifying two.'),
 Q('1I-2','Correct: “Every مصدر منصوب reinforces its فعل without adding information.”', 'It may specify نوع or عدد, or fill a different role according to its عامل.', 'Correct: كل مصدر منصوب للتوكيد.', 'A مصدر cannot be منصوب.', 'سيرًا سريعًا specifies نوع and سجدتين specifies عدد. مصدر is a form; المفعول المطلق is a relationship.'),
 Q('1R','Compare **قرأتُ الكتابَ** and **قرأتُ قراءةً**.', 'الكتابَ مفعول به؛ قراءةً مفعول مطلق','Both are مفعول به','Both are مضاف إليه', 'الكتاب is what was read; قراءة expresses the action itself. Both are منصوب بالفتحة.'),
 Q('1-Read','**قد ينوب عن المصدر ما يدلّ على عدده أو نوعه.** Apply this to **صلّى خمسَ مرّاتٍ**.', 'خمسَ stands in place of the مصدر and indicates عدد.', 'مرّاتٍ must become مرّاتًا.', 'خمسَ is the فاعل of صلّى.', 'خمسَ نائب عن المصدر منصوب، وهو مضاف؛ مرّاتٍ مضاف إليه مجرور. The عدد counts occurrences of prayer.')]

ITEMS['2'] = [
 T('2G-1','Complete the relationships in **أيَّ رسالةٍ كتبتَ؟**.',[
 ('أيَّ','مفعول به مقدّم وجوبًا، وهو مضاف','فاعل مرفوع','حرف استفهام لا محل له'),
 ('رسالةٍ','مضاف إليه مجرور','مفعول مطلق منصوب','خبر مرفوع'),
 ('التاء','ضمير في محل رفع فاعل','ضمير في محل جر','حرف تأنيث')], 'أيَّ اسم استفهام له صدر الكلام، منصوب بكتبت؛ رسالةٍ مضاف إليه. كتبت فعل ماض والتاء فاعل.'),
 Q('2G-2','Why is **إيّاك** in **إيّاك نعبد** in محل نصب?', 'مفعول به مقدّم لنعبد','فاعل لأنّه جاء أولًا','مضاف إليه بلا مضاف', 'إيّاك fills the مفعول به relationship with نعبد. Position before the فعل does not make it فاعلًا.'),
 Q('2I-1','Choose the ending in **حفظتُ القصيدة___**.', 'القصيدةَ: مفعول به','القصيدةُ: فاعل','القصيدةِ: مضاف إليه', 'حفظتُ already contains its فاعل in التاء. القصيدةَ names what was memorised, so it is مفعول به منصوب بالفتحة.'),
 Q('2I-2','In **أحبّ القراءةَ**, identify القراءة.', 'مفعول به، مع كونها مصدرًا','مفعول مطلق لأحبّ لمجرّد كونها مصدرًا','فاعل لأحبّ', 'القراءةَ is what is loved. It is not the مصدر of أحبّ or a فعل with the same meaning, so it is not المفعول المطلق here.'),
 Q('2R','In **أيَّ كتابٍ قرأتَ قراءةً دقيقةً؟**, compare أيّ and قراءة.', 'أيّ مفعول به؛ قراءة مفعول مطلق للنوع','أيّ مفعول مطلق؛ قراءة فاعل','Both are ظرف زمان', 'أيّ identifies what was read and has صدر الكلام؛ قراءةً دقيقةً specifies the kind of reading. كتابٍ remains مضاف إليه.'),
 Q('2-Read','**الأصل في المفعول به أن يكون بعد الفعل والفاعل.** Does this rule forbid **أيَّ كتابٍ قرأتَ؟**?', 'No: الاستفهام requires تقديم أيّ here.','Yes: move أيّ after قرأت in this question.','Yes: أيّ cannot be مفعولًا به.', 'الأصل gives the ordinary order. صدر الكلام is a stated condition requiring a different order.')]

ITEMS['3'] = [
 T('3G-1','Match each expression to its classification here.',[
 ('حينًا','ظرف زمان مبهم','ظرف مكان محدود','مفعول معه'),
 ('يومَ الجمعةِ','ظرف زمان محدود','ظرف مكان مبهم','حال'),
 ('خلفَ البابِ','ظرف مكان مبهم','ظرف زمان محدود','تمييز عدد'),
 ('في المدينةِ','حرف جر واسم مجرور','المدينةَ منصوب بفي','مفعول مطلق')], 'حين names an unspecified time; يوم a defined time unit; خلف a direction. في المدينة has جرّ from the expressed في.'),
 T('3G-2','Analyse **لبثتُ بعضَ يومٍ**.',[
 ('التاء','فاعل في محل رفع','مفعول به في محل نصب','مضاف إليه'),
 ('بعضَ','نائب عن ظرف الزمان منصوب، وهو مضاف','فاعل مرفوع','حرف جر'),
 ('يومٍ','مضاف إليه مجرور','ظرف منصوب بالكسرة','حال مرفوع')], 'بعضَ stands in place of the time expression and is منصوب بالفتحة؛ يومٍ is مجرور بالإضافة. لبثتُ supplies فعل وفاعل.'),
 Q('3I-1','Complete **وقفتُ أمامَ ___** using باب.', 'البابِ','البابَ','البابُ', 'أمامَ ظرف مكان منصوب وهو مضاف؛ البابِ مضاف إليه مجرور بالكسرة. Do not copy the نصب of أمام onto الباب.'),
 Q('3I-2','Which statement correctly applies the مكان محدود rule?', 'نزل المدينةَ is licensed here; this does not license جلستُ المدينةَ by the same rule.', 'Every place اسم after every فعل must be منصوب.', 'مدينة can never occur with نصب.', 'النزول is one of the specified أفعال allowing this analysis. With جلس use an appropriate حرف جر, as in جلست في المدينة.'),
 Q('3R','In **سار ميلًا وسار سيرًا سريعًا**, distinguish ميلًا and سيرًا.', 'ميلًا ظرف مكان؛ سيرًا مفعول مطلق للنوع','Both are مفعول به','ميلًا حال؛ سيرًا مضاف إليه', 'ميل is a distance expression classed with مكان مبهم. سيرًا سريعًا specifies the kind of the action, not the distance.'),
 Q('3-Read','**المفعول فيه ما وقع فيه الفعل من الزمان أو المكان.** Which word fits in **انتظر خالدٌ ساعةً**?', 'ساعةً','خالدٌ','انتظر', 'ساعةً specifies the time occupied by waiting and is ظرف زمان منصوب. خالدٌ is فاعل.')]

ITEMS['4'] = [
 T('4G-1','Match the expression to the condition or relationship.',[
 ('قمتُ إكرامًا للمعلّم','مصدر قلبي مع اتحاد الفاعل والزمن','مفعول معه بعد واو','زمان مختلف بالضرورة'),
 ('سافرتُ للحجّ','لام لأن الحجّ ليس مصدرًا قلبيًّا','حجّ منصوب باللام','الحجّ فاعل سافرت'),
 ('سرتُ والنهرَ','مفعول معه بعد واو المعية','النهر فاعل ثان يسير','مضاف إليه')], 'إكرامًا can express the simultaneous inward motive of the same person. الحجّ is an outward activity, so retain لام. النهرَ accompanies the walking without itself walking.'),
 Q('4G-2','Use **المعية** explicitly in **حضر الأبُ وولد___**.', 'ولدَه: مفعول معه','ولدُه: مفعول معه مرفوع','ولدِه: مجرور بالواو', 'ولدَه is مفعول معه منصوب؛ الهاء مضاف إليه. ولدُه would be valid عطف but is not the specified معية analysis.'),
 Q('4I-1','Why retain لام in **أرحم والدي لرحمته إيّاي صغيرًا** when referring to his earlier kindness?', 'The time of the two actions differs.','رحمة cannot be a مصدر.','لام makes رحمة مرفوعًا.', 'Present kindness and past kindness do not share زمن. This alone prevents applying the direct نصب rule for المفعول له here.'),
 Q('4I-2','Correct: “Every اسم after و is مفعول معه.”', 'المفعول معه requires واو المعية and a preceding جملة with فعل or شبه فعل.', 'Correct: الواو always assigns نصب.', 'المفعول معه must always be معرفة.', 'Compare سرت والنهرَ with كلّ امرئ وشأنُه. Mere adjacency to و does not establish المعية construction.'),
 Q('4R','In **سرتُ ساعةً والنهرَ**, what are the two منصوبان?', 'ساعةً مفعول فيه؛ النهرَ مفعول معه','ساعةً مفعول له؛ النهرَ مفعول مطلق','Both are فاعل', 'ساعةً supplies duration; النهرَ supplies accompaniment after واو المعية. The فاعل is التاء.'),
 Q('4-Read','**يشترط أن تكون قبله جملة فيها فعل أو شبه فعل.** Which مثال meets this for المفعول معه?', 'أنا سائرٌ والنهرَ','كلُّ امرئٍ وشأنُه with مقترنان understood','النهرُ واسعٌ', 'سائرٌ is شبه فعل within أنا سائرٌ. The stated reading of كل امرئ وشأنه has no such expressed governing expression.')]

ITEMS['5'] = [
 T('5G-1','In **رأيتُ خالدًا راكبًا**, take راكبًا as describing Khalid.',[
 ('خالدًا','مفعول به وصاحب الحال','حال وفاعل','مفعول مطلق'),
 ('راكبًا','حال منصوب','نعت مجرور','فاعل مؤخّر'),
 ('عامل الحال','رأيتُ','خالد وحده','الابتداء')], 'خالدًا is the person seen and the صاحب الحال; راكبًا describes his هيئة. Both receive نصب but have different roles.'),
 Q('5G-2','What licenses the نكرة صاحب الحال in **هل صلّى أحدٌ جالسًا؟**?', 'سبق الاستفهام','أحد is always معرفة','جالسًا is مجرور', 'استفهام is a مسوّغ for صاحب الحال to be نكرة. أحدٌ is فاعل وصاحب الحال; جالسًا حال منصوب.'),
 Q('5I-1','In **مررتُ بقريةٍ وهي خاليةٌ**, which stated مسوّغ licenses الحال from قرية?', 'اقتران الحال بالواو','قرية has أل','بقرية is مفعول مطلق', 'قريةٍ is نكرة; وهي خاليةٌ is a جملة حالية joined with واو. هي also links the جملة to قرية.'),
 Q('5I-2','Choose the analysis of **جاء سعيدٌ يبتسمُ**.', 'جملة يبتسم في محل نصب حال؛ يبتسم نفسه مرفوع','يبتسمَ منصوب لأن كل حال له فتحة','سعيدٌ مفعول به', 'يبتسم مضارع مرفوع، فاعله مستتر هو؛ the whole جملة is في محل نصب حال. The ضمير links it to سعيد.'),
 Q('5R','In **جاء خالدٌ صباحًا راكبًا**, distinguish the two descriptions.', 'صباحًا ظرف زمان؛ راكبًا حال من خالد','Both are تمييز','صباحًا حال؛ راكبًا ظرف مكان', 'صباحًا tells when جاء occurred. راكبًا gives هيئة خالد at that time; both are منصوب بالفتحة.'),
 Q('5-Read','**الأصل في الحال أن تكون نكرة، وفي صاحبها أن يكون معرفة.** Choose the ordinary pattern.', 'وصل خالدٌ متعبًا','وصل رجلٌ المتعبَ as the ordinary pattern','وصل خالدًا متعبٌ', 'خالدٌ is معرفة and فاعل؛ متعبًا is نكرة and حال. The roles and endings match the ordinary construction.')]

ITEMS['6'] = [
 T('6G-1','Match each specified reading to its label.',[
 ('خُلق الإنسان ضعيفًا','حال لازمة','حال مقدّرة بالضرورة','مفعول معه'),
 ('ادخلوها خالدين: permanence lies ahead','حال مقدّرة','حال محكيّة','تمييز مفرد'),
 ('قرآنًا عربيًّا: قرآنًا','حال موطّئة','حرف مصدري','فاعل'),
 ('بدا وجهه قمرًا','حال جامدة مؤوّلة بمشتق للتشبيه','مفعول له قلبي','ظرف زمان')], 'ضعيفًا gives a lasting condition; خالدين looks ahead. قرآنًا prepares for the صفة عربيًّا. قمرًا describes resemblance, not the literal identity of the face.'),
 Q('6G-2','Why can **متنقّلة** and **مؤسِّسة** both describe one حال?', 'They answer different questions: stability and added meaning.','They are opposite labels on the same scale.','A حال can have only one classification.', 'A temporary condition can also add new information. These classifications are not mutually exclusive lists of roles.'),
 Q('6I-1','Take both descriptions of **عاد المسافرُ متعبًا جائعًا** as directly describing المسافر. What are they?', 'حالان مترادفتان','حالان متداخلتان لأنّهما متجاورتان','مفعولان به', 'Both share المسافر as صاحب الحال, so they are مترادفتان. The word here does not mean that متعب and جائع are synonyms.'),
 Q('6I-2','For **لا تعثوا في الأرض مفسدين**, adopt تعثوا بمعنى تفسدوا. Classify مفسدين.', 'حال مؤكّدة','حال موطّئة جامدة','ظرف مكان', 'On the stated meaning, مفسدين reinforces the عامل. The alternative “persist in wrongdoing” can support تأسيس; it is not the reading requested.'),
 Q('6R','Correct: “حال مفرد means a حال describing exactly one person.”', 'مفرد here excludes جملة وشبه جملة; راكبين can be حالًا مفردًا.', 'Correct: راكبين cannot be حالًا.', 'مفرد here means معرفة.', 'Number of people is not the distinction. جاؤوا راكبين contains حال مفرد منصوب بالياء لأنه جمع مذكر سالم.'),
 Q('6-Read','**الحال المتداخلة حال من ضمير في الحال الأولى.** In **خالدين فيها لا يخفّف عنهم العذاب**, what is the specified صاحب of the second حال?', 'الضمير المستتر في خالدين','العذاب باعتباره صاحب الحال الأولى','كلمة فيها باعتبارها فاعلًا', 'The جملة لا يخفّف عنهم العذاب is حال from the ضمير inside خالدين. This nested relationship is تداخل.')]

ITEMS['7'] = [
 T('7G-1','Identify what the تمييز clarifies.',[
 ('لترٌ لبنًا','مفرد: مقدار','نسبة محوّلة عن المبتدأ','هيئة صاحب الحال'),
 ('اشتعل الرأس شيبًا','نسبة: محوّل عن الفاعل','عدد صريح','مفعول معه'),
 ('أنا أكثر منك مالًا','نسبة: محوّل عن المبتدأ','ظرف مكان','مفعول مطلق')], 'لبنًا clarifies the measured material. شيبًا relates to شيب الرأس؛ مالًا to مالي أكثر من مالك.'),
 Q('7G-2','Choose the explanatory reconstruction for **فجّرنا الأرضَ عيونًا**.', 'فجّرنا عيونَ الأرضِ','فجّرت الأرضُ إيّانا','كانت الأرضُ فاعلًا لفجّرنا', 'عيونًا is تمييز محوّل عن المفعول به: عيون الأرض. In the actual wording الأرضَ is مفعول به and عيونًا تمييز.'),
 Q('7I-1','In **سليمٌ أكثرُ من أخيه علمًا**, what is علمًا?', 'تمييز نسبة محوّل عن المبتدأ','حال يصف هيئة سليم عند المجيء','مفعول به لفعل ظاهر', 'The relationship can be explained as علم سليم أكثر من علم أخيه. No فعل of arrival or expressed فعل governing a مفعول به occurs.'),
 Q('7I-2','Correct **خاتمُ فضّةً** to the إضافة form taught here.', 'خاتمُ فضّةٍ','خاتمٌ فضّةٍ with no إضافة or حرف جر','خاتمِ فضّةُ', 'In إضافة, خاتمُ is مضاف without تنوين and فضّةٍ مضاف إليه. خاتمٌ فضّةً would instead use the taught تمييز form, but is not the requested إضافة.'),
 Q('7R','Compare **عاد الطفلُ مسرورًا** and **اشتعل الرأسُ شيبًا**.', 'مسرورًا حال؛ شيبًا تمييز','Both are حال','Both are ظرف', 'مسرورًا describes هيئة الطفل؛ شيبًا clarifies the نسبة of اشتعل to الرأس. Shared نصب does not settle the role.'),
 Q('7-Read','**التمييز يرفع الإبهام.** What does يرفع mean here?', 'يزيل: removes the uncertainty','يجعل التمييز مرفوعًا دائمًا','يحذف العامل من الجملة', 'This is a statement about clarification of meaning, not a rule requiring رفع التمييز.')]

ITEMS['8'] = [
 T('8G-1','Choose the supplied عدد with its correctly formed تمييز.',[
 ('ثلاثة','ثلاثةُ كتبٍ','ثلاثةُ كتابًا','ثلاثةُ كتبًا'),
 ('عشرون','عشرون كتابًا','عشرون كتبٍ','عشرون كتابٌ'),
 ('مائة','مائةُ كتابٍ','مائةُ كتابًا','مائةُ كتبًا')], '3–10 take جمعًا مجرورًا بالإضافة؛ 20 takes مفردًا منصوبًا؛ 100 takes مفردًا مجرورًا بالإضافة. The role of the عدد itself depends on its جملة.'),
 Q('8G-2','Ask how many days: **كم ___ لبثتَ؟**', 'يومًا','يومٌ','أيامُ', 'كم الاستفهامية here takes a مفرد منصوب تمييز: يومًا. كم asks for the number; it does not itself mean “many.”'),
 Q('8I-1','Complete the الخبرية meaning “Many a book I have read”: **كم قرأتُ ___**.', 'من كتابٍ','كتابٌ','كتابًا as تمييز كم الخبرية', 'The تمييز is separated from كم, so the taught rule requires من الظاهرة. كتابٍ is مجرور بمن.'),
 Q('8I-2','In **إنّ عدّة الشهور ... اثنا عشر شهرًا**, why can شهرًا be تمييزًا despite الشهور already being mentioned?', 'قد يكون التمييز مؤكّدًا','Every repeated meaning becomes حالًا','شهرًا is فاعل إنّ', 'تمييز can reinforce information rather than remove fresh إبهام. شهرًا still has the number construction’s تمييز role.'),
 Q('8R','In **مكثتُ ثلاثةَ أيامٍ**, distinguish the roles.', 'ثلاثةَ نائب عن ظرف الزمان؛ أيامٍ مضاف إليه وهو تمييز العدد في المعنى','أيامٍ منصوب بكسرة لأنه حال','ثلاثةَ فاعل؛ أيامٍ مفعول به', 'ثلاثةَ states the duration and is مضاف؛ أيامٍ supplies the counted unit and is مجرور بالإضافة. Not all words in the تمييز chapter are منصوب.'),
 Q('8-Read','**قد يكون التمييز مجرورًا.** Select the example.', 'ألفُ سنةٍ: سنةٍ','عشرون يومًا: يومًا','جاء راكبًا: راكبًا', 'سنةٍ is the مفرد مجرور following ألف. يومًا is منصوب, and راكبًا is حال rather than تمييز.')]

ITEMS['9'] = [
 T('9G-1','Identify the أركان in **حضر الطلابُ إلّا خالدًا**.',[
 ('الطلاب','المستثنى منه','أداة الاستثناء','المستثنى'),
 ('إلّا','أداة الاستثناء','المستثنى منه','فاعل'),
 ('خالدًا','المستثنى','مضاف إليه','فاعل حضر')], 'الطلاب is the expressed whole; إلّا introduces exclusion; خالدًا is removed from the حكم of attendance. The construction is تام متصل موجب.'),
 Q('9G-2','Use **البدل** in **ما حضر الطلابُ إلّا خالد___**.', 'خالدٌ','خالدًا','خالدٍ', 'As بدل from الطلابُ, خالدٌ is مرفوع. خالدًا would be valid نصب على الاستثناء, but that is not the selected analysis.'),
 T('9I-1','اختر الإعراب في الاستثناء المفرّغ.',[
 ('ما فاز إلا سليم','سليمٌ: فاعل','سليمًا: مستثنى منصوب وجوبًا','سليمٍ: مضاف إليه'),
 ('ما قابلت إلا سليما','سليمًا: مفعول به','سليمٌ: فاعل','سليمٍ: مجرور بإلّا'),
 ('ما مررت إلا بسليم','سليمٍ: مجرور بالباء','سليمًا: منصوب بإلّا','سليمٌ: خبر')], 'المستثنى منه is absent. إلّا للحصر لا تعمل؛ فاز requires فاعل، قابلت requires مفعول به، and الباء gives جرّ.'),
 Q('9I-2','Complete the specified تام construction with المستثنى مقدّم: **ما جاء إلّا ___ الطلابُ**.', 'خالدًا','خالدٌ على البدل المؤخّر','خالدٍ', 'المستثنى precedes the expressed المستثنى منه, so use نصب. Do not treat this as مفرّغ while ignoring الطلاب.'),
 Q('9R','Which statement about **ما جاء الطلاب إلا خالدٌ** and **ما جاء إلا خالدٌ** is correct?', 'خالدٌ بدل في الأولى وفاعل في الثانية','خالدٌ بدل في كلتيهما','إلّا ترفع خالدًا في كلتيهما', 'The first retains الطلاب as فاعل ومُستثنى منه. The second is مفرّغ, so خالد is directly فاعل جاء.'),
 Q('9-Read','**في الاستثناء المفرّغ لا تعمل إلّا.** What determines رسالةً in **ما كتبتُ إلّا رسالةً**?', 'كتبتُ: رسالةً مفعول به','إلّا: كل ما بعدها منصوب','رسالة is necessarily مفعول مطلق', 'كتب governs رسالة as what was written. إلّا supplies حصر without assigning the ending.')]

ITEMS['10'] = [
 T('10G-1','Match each stated construction.',[
 ('ما عدا خالدًا','خالدًا مفعول به لعدا','خالدًا مجرور بما','خالدًا اسم عدا الناقصة'),
 ('غيرَ خالدٍ','خالدٍ مضاف إليه','خالدٍ فاعل مجرور','خالدٍ منصوب بإلّا'),
 ('حاشا الأنبياءِ','الأنبياءِ مجرور بحاشا في التحليل المعتمد','الأنبياءَ مفعول مطلق','الأنبياءُ فاعل')], 'ما عدا uses فعل؛ غير uses إضافة؛ حاشا is حرف جر in the account adopted here. Similar exclusion meanings do not give identical تركيب.'),
 Q('10G-2','Complete **حضر الطلابُ غيرَ ___**.', 'سعيدٍ','سعيدًا','سعيدٌ', 'غيرَ receives نصب على الاستثناء؛ سعيدٍ receives جرّ الإضافة. Do not transfer the إعراب of غير to its مضاف إليه.'),
 Q('10I-1','In **ما فاز غيرُ سليمٍ**, identify both roles.', 'غيرُ فاعل وهو مضاف؛ سليمٍ مضاف إليه','غيرُ مستثنى منصوب؛ سليمٍ فاعل','غير حرف جر؛ سليم مفعول به', 'With no expressed المستثنى منه, فاز governs غيرُ as فاعل. The اسم after غير remains مجرورًا بالإضافة.'),
 Q('10I-2','Correct: “خلا and ما خلا must always be حروف جر.”', 'ما خلا فعل؛ خلا permits the verbal account and a حرف جر account.','Correct: ما prevents verbal analysis.','Both must be أسماء مضافة.', 'ما خلا is verbal in the stated classification. Without ما, خلا is predominantly treated as فعل, with a recognised حرف جر alternative.'),
 Q('10R','In the descriptive reading **لو كان فيهما آلهةٌ إلّا اللهُ لفسدتا**, إلّا means:', 'غير، لتقييد آلهة بالصفة','أداة استثناء تام موجب توجب نصب الله','حرف جر يجرّ الله', 'The intended sense is “gods other than Allah.” The stated رفع and meaning support the descriptive account, not ordinary نصب المستثنى in تام موجب.'),
 Q('10-Read','**ما بعد غير مجرور بالإضافة.** Does this force غير itself to be مجرورًا?', 'No: its own role may be فاعل or مستثنى, for example.','Yes: both words always have جرّ.','Yes: غير is itself حرف جر.', 'Separate the outer role of غير from its إضافة relationship. غيرُ in ما جاء غير خالد is فاعل; خالد remains مضاف إليه.')]

ITEMS['11'] = [
 T('11G-1','Match the منصوب to its role.',[
 ('كان خالدٌ حاضرًا: حاضرًا','خبر كان','حال واجبًا','اسم كان'),
 ('إنّ خالدًا حاضرٌ: خالدًا','اسم إنّ','خبر إنّ','مفعول به'),
 ('ما هذا بشرًا: بشرًا','خبر ما المشبهة بليس','اسم ما','تمييز عدد')], 'Each عامل has a distinct pattern of عمل. كان and ما المشبهة بليس have خبر منصوب; إنّ has اسم منصوب.'),
 Q('11G-2','Choose the permitted ترتيب.', 'حاضرًا كان خالدٌ','حاضرًا ما زال خالدٌ under the rule forbidding crossing ما النافية','حاضرًا ما دام خالدٌ under the rule forbidding crossing ما المصدرية', 'خبر كان may precede كان. The specified rule prevents moving it before ما النافية or ما المصدرية in the other two options.'),
 Q('11I-1','Complete **إنّ سليمًا كان ___**.', 'متعبًا','متعبٌ','متعبٍ', 'متعبًا خبر كان منصوب؛ اسم كان ضمير مستتر هو. The whole جملة كان متعبًا is في محل رفع خبر إنّ.'),
 Q('11I-2','Correct the ending in **ما خالدٌ إلّا غائبًا**.', 'غائبٌ: خبر مرفوع بعد انتقاض النفي بإلّا','غائبٍ: مجرور بإلّا','غائبًا must remain خبر ما العاملة', 'إلّا cancels the working negation condition of ما المشبهة بليس. Use خالد مبتدأ وغائب خبر مرفوع in this construction.'),
 Q('11R','Compare **جاء خالدٌ متعبًا** and **كان خالدٌ متعبًا**.', 'متعبًا حال في الأولى وخبر كان في الثانية','متعبًا حال في كلتيهما','متعبًا مفعول به في كلتيهما', 'جاء is فعل تام; متعبًا describes هيئة its فاعل. كان is ناقص and requires its خبر, so the identical word has a different role.'),
 Q('11-Read','**لا يتقدّم الخبر على ما المصدرية أو النافية.** What is the stated boundary?', 'Do not move the خبر to a position before those forms of ما.','No خبر may ever precede any فعل ناقص.','Every ما is a حرف جر.', 'The restriction names ما because of الصدارة. It does not erase the permission exemplified by قائمًا كان زيدٌ.')]

ITEMS['12'] = [
 T('12G-1','Use the البناء account for اسم لا غير المضاف ولا الشبيه بالمضاف.',[
 ('لا طالبَ علمٍ غائبٌ: طالب','اسم لا منصوب لأنه مضاف','اسم لا مبني لأنه مضاف','مبتدأ مرفوع'),
 ('لا عاصيًا أمَّه ناجحٌ: عاصيًا','اسم لا منصوب لأنه شبيه بالمضاف','مضاف إليه مجرور','اسم لا مبني بلا تنوين'),
 ('لا طالبَ غائبٌ: طالب','مبني على الفتح في محل نصب','مرفوع بالضمة','مضاف إلى غائب')], 'طالب علم is إضافة؛ عاصيًا governs أمّه and is شبيه بالمضاف؛ طالب in the third is neither. غائبٌ remains خبر لا.'),
 Q('12G-2','Use **بناء الاسمين على الفتح**: **لا حول___ ولا قوّة___**.', 'لا حولَ ولا قوّةَ','لا حولٌ ولا قوّةٌ','لا حولَ ولا قوّةً', 'The selected pattern builds both أسماء على الفتح without تنوين. The other forms are valid under different patterns, not the requested one.'),
 Q('12I-1','اختر التحليل المعتمد في **لا معلّمينَ في البيت**.', 'معلّمينَ: اسم لا مبني على الياء في محل نصب','معلّمينَ: مضاف إليه مجرور','معلّمينَ: خبر لا منصوب', 'معلّمين is جمع مذكر سالم, neither مضاف nor شبيه بالمضاف here. اسم لا is مبني على الياء في محل نصب; في البيت supplies خبر لا.'),
 Q('12I-2','Which pair of endings is absent from the five permitted patterns taught here?', 'رفع الأول ونصب الثاني: لا حولٌ ولا قوّةً','بناء الأول ورفع الثاني: لا حولَ ولا قوّةٌ','رفع الأول وبناء الثاني: لا حولٌ ولا قوّةَ', 'The five patterns include بناء/بناء، بناء/رفع، بناء/نصب، رفع/رفع، رفع/بناء. رفع/نصب is not among them.'),
 Q('12R','In **لا طالبَ علمٍ غائبٌ**, choose the complete set.', 'طالبَ اسم لا منصوب؛ علمٍ مضاف إليه؛ غائبٌ خبر لا','طالبَ حال؛ علمٍ فاعل؛ غائبٌ مفعول به','طالبَ مبني لأنه مضاف؛ علمٍ خبر لا', 'إضافة makes طالبَ معربًا منصوبًا in this account. علمٍ has جرّ الإضافة, and غائبٌ is خبر لا مرفوع.'),
 Q('12-Read','**اسم لا المضاف والشبيه بالمضاف منصوبان لفظًا.** Which expression has اسمًا شبيهًا بالمضاف?', 'لا عاصيًا أباه ناجحٌ','لا رجلَ في البيت','لا طالبَ علمٍ غائبٌ', 'عاصيًا governs أباه as مفعول به, making it شبيهًا بالمضاف. طالب علم is actual إضافة; رجل is neither.')]

ITEMS['R'] = [
 T('A1','Match each منصوب in the specified examples.',[
 ('حفظتُ الدرسَ','مفعول به','مفعول مطلق','حال'),
 ('اجتهدتُ اجتهادًا','مفعول مطلق','مفعول له','تمييز'),
 ('انتظرتُ ساعةً','مفعول فيه','مفعول معه','اسم إنّ'),
 ('قمتُ احترامًا للمعلّم','مفعول له','خبر كان','مستثنى'),
 ('سرتُ والنهرَ','مفعول معه','مفعول به','مفعول مطلق')], 'Track the questions answered: what was memorised; the action itself; its duration; the motive; and accompaniment. All five have نصب but different relationships.'),
 T('A2','اختر الوصف الصحيح.',[
 ('ما جاء إلا خالدٌ','استثناء مفرّغ؛ خالد فاعل','تام موجب؛ خالد مستثنى منصوب','خالد بدل من مذكور'),
 ('ما جاء الطلاب إلا خالدٌ','تام غير موجب؛ خالد بدل','مفرّغ؛ خالد فاعل جاء','خالد خبر إنّ'),
 ('جاء الطلاب إلا خالدًا','تام متصل موجب؛ نصب المستثنى','مفرّغ؛ خالد فاعل','خالد مضاف إليه')], 'The presence of الطلاب makes the last two تامّين. ما makes the second غير موجب. In the first the عامل seeks خالد directly.'),
 T('B1','أكمل بحسب التحليل المحدّد.',[
 ('قرأت عشرين ___: كتاب','كتابًا: تمييز','كتابٍ: مضاف إليه','كتبًا: جمع منصوب'),
 ('حضرت الدروس غيرَ ___: درس','درسٍ: مضاف إليه','درسًا: مفعول به','درسٌ: فاعل'),
 ('لا طالبَ ___ غائبٌ: علم','علمٍ: مضاف إليه','علمًا: حال','علمٌ: اسم لا')], 'Twenty takes مفردًا منصوبًا. غير and طالب in these examples are مضافان, so درس and علم receive جرّ.'),
 Q('B2','صحّح: **جاء خالدٌ يضحكَ، لأن جملة يضحك حال.**', 'يضحكُ مرفوع، والجملة في محل نصب حال.','يضحكْ مجزوم لأن الحال نكرة.','خالدًا منصوب لأن بعده حال.', 'The محل of a جملة does not replace the internal إعراب of its فعل. No ناصب or جازم precedes يضحك.'),
 T('C1','Read: **وصل سليم صباحا. جلس خلف الباب ساعة. ثم قرأ الدرس قراءة دقيقة.** Match the roles, restoring endings.',[
 ('صباحا','صباحًا: ظرف زمان','صباحٌ: فاعل','صباحٍ: مضاف إليه'),
 ('خلف الباب','خلفَ ظرف مكان؛ البابِ مضاف إليه','خلفُ فاعل؛ البابَ مفعول به','خلفِ مجرور بلا عامل'),
 ('ساعة','ساعةً: ظرف زمان','ساعةٌ: فاعل جلس','ساعةٍ: مجرور بخلف'),
 ('الدرس','الدرسَ: مفعول به','الدرسُ: فاعل قرأ','الدرسِ: مضاف إليه'),
 ('قراءة دقيقة','قراءةً مفعول مطلق للنوع؛ دقيقةً نعت','قراءةٌ فاعل؛ دقيقةٌ خبر','Both are مفعول معه')], 'سليمٌ is فاعل وصل. The later أفعال have مستتر هو returning to him. صباحًا and ساعةً give time; خلفَ gives place; الدرسَ is what he reads; قراءةً دقيقةً specifies the kind of reading.'),
 T('C2','Full تركيب: **إنّ سليمًا قرأ الدرسَ جالسًا.** Take جالسًا as describing the reader.',[
 ('إنّ','حرف مشبّه بالفعل، لا محل له','فعل ناقص','حرف جر'),
 ('سليمًا','اسم إنّ منصوب بالفتحة','فاعل قرأ مقدّم في التحليل المطلوب','خبر إنّ منصوب'),
 ('قرأ','فعل ماض مبني على الفتح','مضارع منصوب','مصدر مرفوع'),
 ('فاعل قرأ','ضمير مستتر هو يعود إلى سليم','الدرس','لا فاعل له'),
 ('الدرسَ','مفعول به منصوب بالفتحة','حال منصوب','اسم إنّ ثان'),
 ('جالسًا','حال منصوب من الضمير المستتر في قرأ','خبر إنّ منصوب','تمييز عدد'),
 ('جملة قرأ الدرس جالسًا','في محل رفع خبر إنّ','في محل نصب اسم إنّ','في محل جر مضاف إليه')], 'إنّ governs سليمًا as اسمها and the جملة as خبرها. Inside that جملة, قرأ has مستتر هو as فاعل؛ الدرس مفعول به؛ جالسًا حال من ذلك الضمير، عامله قرأ. The internal نصب does not change the جملة’s محل رفع.'),
 T('C3','اقرأ: **حضر الطلاب إلا سليما. كان سليم مريضا. لا طالب علم مهمل.** حلّل الجملة الأخيرة كاملة.',[
 ('لا','حرف نفي للجنس يعمل عمل إنّ','لا الناهية تجزم طالب','حرف جر'),
 ('طالب','طالبَ: اسم لا منصوب بالفتحة، وهو مضاف','طالبَ: مبني لأنه مضاف','طالبُ: فاعل'),
 ('علم','علمٍ: مضاف إليه مجرور بالكسرة','علمًا: تمييز','علمٌ: خبر لا'),
 ('مهمل','مهملٌ: خبر لا مرفوع بالضمة','مهملًا: خبر لا منصوب','مهملٍ: مضاف إليه ثان')], 'Read حضر الطلابُ إلّا سليمًا؛ كان سليمٌ مريضًا؛ لا طالبَ علمٍ مهملٌ. The last جملة has اسم لا مضافًا, so طالب is منصوب لفظًا. Its خبر remains مرفوعًا.'),
 Q('D1','**اتحاد الفاعل والزمن من شروط نصب المفعول له بلا لام.** اختر التطبيق.', 'قمتُ إكرامًا للمعلّم: I rose while intending to honour him.','سافرتُ الحجَّ: الحجّ is automatically قلبي.','أرحمه رحمتَه إيّاي صغيرًا: different times never matter.', 'The first has the same person and time for the action and inward motive. الحجّ fails the قلبي condition, and earlier رحمة fails the shared time condition.'),
 Q('D2','**قد يكون التمييز مجرورًا، وقد يكون الحال لازمًا.** اختر المثالين الموافقين.', 'ألفُ سنةٍ؛ خُلق الإنسانُ ضعيفًا','عشرون كتابًا؛ جاء راكبًا as examples of جرّ and لزوم','سرتُ والنهرَ؛ قرأتُ الدرسَ', 'سنةٍ is تمييز العدد مجرور بالإضافة؛ ضعيفًا is حال لازمة. The statement explicitly warns against equating التمييز with نصب in every instance or الحال with change in every instance.')]
