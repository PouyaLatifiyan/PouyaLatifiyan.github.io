"""Names, source notes and direct parentage supplied by Pouya Latifiyan."""
from translations import LANGS, TEXT, row


def labels(key, text):
    row(key, *text.split('|'))


labels('familytitle', 'Family tree|شجره‌نامه|شجرة العائلة|家谱|Arbre généalogique')
labels('familyintro', 'Four generations of the Latifiyan and Niktalab families, as recorded by Pouya Latifiyan. Select a name to read the family record.|چهار نسل از خاندان‌های لطیفیان و نیک‌طلب به روایت پویا لطیفیان. برای خواندن سرگذشت هر نفر، نام او را انتخاب کنید.|أربعة أجيال من عائلتي لطيفيان ونيك‌طلب كما رواها بويا لطيفيان. اختر اسماً لقراءة سيرته.|这份家谱由 Pouya Latifiyan 记录，涵盖 Latifiyan 与 Niktalab 两家四代人。选择姓名即可阅读小传。|Quatre générations des familles Latifiyan et Niktalab, retracées par Pouya Latifiyan. Sélectionnez un nom pour lire sa notice.')
labels('art','Art|بخش هنری|الفنون|艺术|Arts')
labels('settings','Settings|تنظیمات|الإعدادات|设置|Réglages')
labels('children','Children|فرزندان|الأبناء|子女|Enfants')
labels('siblings','Siblings|خواهر و برادر|الإخوة والأخوات|兄弟姐妹|Fratrie')
labels('kinparents','Parents|پدر و مادر|الوالدان|父母|Parents')
labels('pbranch','Latifiyan family|خاندان لطیفیان|عائلة لطيفيان|Latifiyan 父系|Famille Latifiyan')
labels('mbranch','Niktalab family|خاندان نیک‌طلب|عائلة نيك‌طلب|Niktalab 母系|Famille Niktalab')
labels('sources','Further reading|منابع زندگی‌نامه|مصادر السيرة|传记资料|Sources biographiques')
labels('familyrecord','Family account · Pouya Latifiyan|روایت خانوادگیِ پویا لطیفیان|رواية عائلية بقلم بويا لطيفيان|家族口述 · Pouya Latifiyan|Témoignage familial de Pouya Latifiyan')
labels('siblingof','Brother of Farrokhondeh|برادر فرخنده|شقيق فرخنده|Farrokhondeh 的兄弟|Frère de Farrokhondeh')
labels('artisttitle','Persian calligraphy & painting|خوشنویسی و نقاشی‌خط|الخط الفارسي والرسم بالحروف|波斯书法与书法绘画|Calligraphie persane et peinture')
labels('artistintro','I practise Persian calligraphy and naqqāshi-khatt, a form of painting that takes the written letter as its subject.|خوشنویسی فارسی و نقاشی‌خط دو شاخهٔ کار هنری من هستند. در نقاشی‌خط، شکل و حرکتِ حروف فارسی موضوع نقاشی‌ام می‌شوند.|أمارس الخط الفارسي والرسم بالحروف، حيث يصبح شكل الحرف وحركته موضوعاً للّوحة.|我创作波斯书法，也从事 naqqāshi-khatt（书法绘画），以字母的形态与运笔的轨迹为绘画主题。|Je pratique la calligraphie persane et le naqqāshi-khatt, une forme de peinture qui prend la lettre et son mouvement pour sujet.')
labels('exhibitions','Exhibitions|نمایشگاه‌ها|المعارض|展览|Expositions')
labels('exhibittext','I have exhibited my work in several galleries. My practice brings together writing, drawing and the composition of the painted page.|آثارم را در چندین گالری به نمایش گذاشته‌ام. در کارم، نوشتن و طراحی از راه ترکیب‌بندیِ حروف روی صفحه به هم می‌رسند.|عرضت أعمالي في عدة صالات فنية. تجمع تجربتي بين الكتابة والرسم وتكوين الحروف على سطح اللوحة.|我的作品曾在多家画廊展出。创作时，我以字形的布局把书写与绘画联系起来。|J’ai exposé mes œuvres dans plusieurs galeries. Mon travail relie écriture et dessin par la composition des lettres sur la page.')
labels('guild','Iranian Calligraphers Association|انجمن خوشنویسان ایران|جمعية الخطاطين الإيرانيين|伊朗书法家协会|Association des calligraphes iraniens')
labels('guildtext','I am a member of the Iranian Calligraphers Association.|عضو انجمن خوشنویسان ایران هستم.|أنا عضو في جمعية الخطاطين الإيرانيين.|我是伊朗书法家协会会员。|Je suis membre de l’Association des calligraphes iraniens.')
labels('museumcredit','Historical reference · Nastaʿliq panel by Sayyid Amir ʿAli, mid-17th century. The Met, 1999.356.|نمونهٔ تاریخی · قطعهٔ نستعلیق سید امیرعلی، میانهٔ سدهٔ هفدهم میلادی. موزهٔ متروپولیتن، ۱۹۹۹٫۳۵۶.|نموذج تاريخي · لوحة نستعليق للسيد أمير علي، منتصف القرن السابع عشر. متحف المتروبوليتان، 1999.356.|历史参照 · 赛义德·阿米尔·阿里，纳斯塔利克体书法，17 世纪中叶。大都会艺术博物馆，1999.356。|Référence historique · Panneau en nastaʿliq de Sayyid Amir ʿAli, milieu du XVIIᵉ siècle. The Met, 1999.356.')
PEOPLE = {}
PARENTS = {'bio':('father','mother'), 'sister':('father','mother'),
           'father':('paternal-grandfather','paternal-grandmother'),
           'mother':('maternal-grandfather','maternal-grandmother'),
           'paternal-grandfather':('heydar-latifiyan',),
           'paternal-grandmother':('hassan-latifiyan','zahra-abdollahi'),
           'maternal-grandmother':('ainollah-mahmoodi','alamtaj-rezaei'),
           'aminollah-rezaei':('ainollah-mahmoodi','alamtaj-rezaei')}


def person(key, latin, persian, biography, *sources):
    PEOPLE[key] = tuple(sources)
    row('name-'+key, latin, persian, persian, latin, latin)
    labels('bio-'+key, biography)


person('father','Ali Latifiyan','علی لطیفیان',
       'Ali Latifiyan is an Iranian writer and researcher. His work examines the role of intellectuals in Iranian history, the Enlightenment and political thought.|علی لطیفیان نویسنده و پژوهشگر ایرانی است. او دربارهٔ نقش روشنفکران در تاریخ ایران، اندیشهٔ روشنگری و تفکر سیاسی نوشته است.|علي لطيفيان كاتب وباحث إيراني تناول دور المثقفين في تاريخ إيران وفكر التنوير والفكر السياسي.|Ali Latifiyan 是伊朗作家和研究者，关注知识分子在伊朗历史中的作用、启蒙思想与政治思想。|Ali Latifiyan est un écrivain et chercheur iranien. Il étudie le rôle des intellectuels dans l’histoire de l’Iran, les Lumières et la pensée politique.',
       ('Wikipedia · Ali Latifiyan','https://en.wikipedia.org/wiki/Ali_Latifiyan'))
person('mother','Poopak Niktalab','پوپک نیک‌طلب',
       'Poopak Niktalab writes and researches literature for young readers. In Sarv-e Samarqand she explores the poetry of Rudaki, bringing a classical Persian poet to a younger audience.|پوپک نیک‌طلب نویسنده و پژوهشگر ادبیات کودک و نوجوان است. در کتاب «سرو سمرقند» خوانندگان نوجوان را با رودکی و شعر او آشنا می‌کند.|پوپك نيك‌طلب كاتبة وباحثة في أدب الأطفال واليافعين. تعرّف القرّاء الشباب بشعر رودكي في كتابها «سرو سمرقند».|Poopak Niktalab 从事儿童与青少年文学的写作和研究。她在《撒马尔罕的柏树》中向年轻读者介绍波斯古典诗人鲁达基的诗歌。|Poopak Niktalab écrit pour la jeunesse et étudie sa littérature. Dans Sarv-e Samarqand, elle fait découvrir aux jeunes lecteurs la poésie classique de Rudaki.',
       ('Wikipedia · Poopak NikTalab','https://en.wikipedia.org/wiki/Poopak_NikTalab'))
person('sister','Parnia Latifiyan','پرنیا لطیفیان',
       'Parnia is Pouya’s sister and the daughter of Ali Latifiyan and Poopak Niktalab.|پرنیا خواهر پویا و فرزند علی لطیفیان و پوپک نیک‌طلب است.|پرنيا شقيقة بويا وابنة علي لطيفيان وپوپك نيك‌طلب.|Parnia 是 Pouya 的姐妹，父母为 Ali Latifiyan 和 Poopak Niktalab。|Parnia est la sœur de Pouya et la fille d’Ali Latifiyan et de Poopak Niktalab.')
person('paternal-grandfather','Mohammad Hossein Latifiyan','محمدحسین لطیفیان',
       'Pouya remembers his paternal grandfather as a researcher in the biological sciences at the University of Tehran.|به روایت پویا، پدربزرگ پدری‌اش در دانشگاه تهران پژوهشگر علوم زیست‌شناسی بود.|يذكر بويا أن جدّه لأبيه كان باحثاً في العلوم البيولوجية بجامعة طهران.|据 Pouya 的家族记录，他的祖父曾在德黑兰大学从事生物科学研究。|Selon le témoignage de Pouya, son grand-père paternel a mené des recherches en biologie à l’Université de Téhéran.')
person('paternal-grandmother','Fatemeh Kobra Latifiyan','فاطمه کبری لطیفیان',
       'Fatemeh Kobra is Ali Latifiyan’s mother and the daughter of Hassan Latifiyan and Zahra Abdollahi.|فاطمه کبری، مادر علی لطیفیان و دختر حسن لطیفیان و زهرا عبداللهی است.|فاطمة كبرى والدة علي لطيفيان وابنة حسن لطيفيان وزهراء عبداللهي.|Fatemeh Kobra 是 Ali Latifiyan 的母亲，父母为 Hassan Latifiyan 和 Zahra Abdollahi。|Fatemeh Kobra est la mère d’Ali Latifiyan et la fille de Hassan Latifiyan et de Zahra Abdollahi.')
person('heydar-latifiyan','Heydar Gholi Latifiyan','حیدرقلی لطیفیان',
       'Known as Heydar Latifiyan, he commanded local resistance near Robat Karim during the First World War. He died in the fighting in December 1915. His family remembers him as a national hero.|حیدرقلی، مشهور به حیدر لطیفیان، در جنگ جهانی اول از فرماندهان مقاومت محلی در برابر نیروهای روس در رباط‌کریم بود. او در دی ۱۲۹۴ در این نبرد جان باخت. خانواده از او به‌عنوان قهرمان ملی یاد می‌کند.|قاد حيدر قلي، المعروف بحيدر لطيفيان، المقاومة المحلية قرب رباط كريم أثناء الحرب العالمية الأولى، وقُتل في القتال في ديسمبر 1915. وتذكره أسرته بطلاً وطنياً.|人称 Heydar Latifiyan，一战期间在罗巴特卡里姆一带指挥地方抵抗，于 1915 年 12 月阵亡。家族以民族英雄纪念他。|Connu sous le nom de Heydar Latifiyan, il commanda la résistance locale près de Robat Karim pendant la Première Guerre mondiale. Il y mourut au combat en décembre 1915. Sa famille honore en lui un héros national.',
       ('پیام نفت · نبرد رباط‌کریم','https://www.payamenaft.com/note/1321/نبرد-رباط-کریم-حیدرقلی-خان-لطیفیان-با-ارتش-روس/'))
for key, latin, fa in [('hassan-latifiyan','Hassan Latifiyan','حسن لطیفیان'),('zahra-abdollahi','Zahra Abdollahi','زهرا عبداللهی')]:
    person(key,latin,fa,
           f'The family remembers {latin} for charitable giving. In its account, land belonging to {latin} was used for the construction of Tehran’s Imam Khomeini International Airport.|خانواده از {fa} به نیکی و نیکوکاری یاد می‌کند. بنا بر روایت خانوادگی، بخشی از زمین‌های {fa} برای ساخت فرودگاه بین‌المللی امام خمینی تهران استفاده شد.|تذكر الأسرة أعمال {fa} الخيرية. وبحسب روايتها، استُخدمت أراضٍ كانت ملكاً له أو لها في بناء مطار الإمام الخميني الدولي في طهران.|据家族口述，{latin} 热心公益，其名下的部分土地用于建设德黑兰伊玛目霍梅尼国际机场。|La famille garde le souvenir de la générosité de {latin}. Selon son témoignage, une partie des terres de {latin} a servi à la construction de l’aéroport international Imam-Khomeini de Téhéran.'.replace('له أو لها','له' if key.startswith('hassan') else 'لها'))
person('maternal-grandfather','Ahmad Niktalab','احمد نیک‌طلب',
       'Ahmad Niktalab wrote poetry under the name Yavar Hamedani, in literary Persian and in the dialect of Hamadan. His collection Sāyesār-e Alvand preserves local verse. His family also recalls his leadership in Iran’s Literary Association.|احمد نیک‌طلب با تخلص «یاور همدانی» به فارسی و گویش همدانی شعر می‌سرود. «سایه‌سار الوند» از مجموعه‌های اوست و بخشی از شعرهای محلی او را در بر دارد. خانواده‌اش از او به‌عنوان یکی از رؤسای انجمن ادبی ایران یاد می‌کند.|كتب أحمد نيك‌طلب الشعر بالفارسية وبلهجة همدان تحت اسم «ياور همداني». يضم ديوانه «سايه‌سار الوند» نماذج من شعره المحلي. وتذكر أسرته تولّيه دوراً قيادياً في الجمعية الأدبية الإيرانية.|Ahmad Niktalab 以 Yavar Hamedani 为笔名，用波斯语和哈马丹方言写诗。诗集《阿尔万德的树荫》收录了他的方言诗。家人还记述了他在伊朗文学协会的领导工作。|Sous le nom de Yavar Hamedani, Ahmad Niktalab écrivait en persan et en dialecte de Hamadan. Son recueil Sāyesār-e Alvand conserve plusieurs poèmes en dialecte. Sa famille évoque aussi ses responsabilités à la direction de l’Association littéraire d’Iran.',
       ('Wikipedia · Ahmad NikTalab','https://en.wikipedia.org/wiki/Ahmad_NikTalab'),('تریبون زمانه · یاور همدانی','https://www.tribunezamaneh.com/archives/291422'))
person('maternal-grandmother','Farrokhondeh Mahmoodi','فرخنده محمودی',
       'Farrokhondeh Mahmoodi is a painter and Poopak Niktalab’s mother. Her brother Aminollah Rezaei also pursued painting.|فرخنده محمودی نقاش و مادر پوپک نیک‌طلب است. برادرش امین‌الله رضایی نیز نقاش بود.|فرخنده محمودي رسامة ووالدة پوپك نيك‌طلب. مارس شقيقها أمين الله رضائي الرسم أيضاً.|Farrokhondeh Mahmoodi 是画家，也是 Poopak Niktalab 的母亲。她的兄弟 Aminollah Rezaei 也从事绘画。|Farrokhondeh Mahmoodi, mère de Poopak Niktalab, est peintre. Son frère Aminollah Rezaei pratiquait également la peinture.')
person('alamtaj-rezaei','Alam-Taj Rezaei','عالم‌تاج رضایی',
       'In the family’s account, Alam-Taj Rezaei was a painter and artist. Her daughter Farrokhondeh and son Aminollah also worked in the visual arts.|عالم‌تاج رضایی در یاد خانواده نقاش و هنرمند بود. دخترش فرخنده و پسرش امین‌الله نیز در هنرهای تجسمی فعالیت داشتند.|تذكر العائلة أن عالم تاج رضائي كانت رسامة وفنانة. وعمل ابناها فرخنده وأمين الله أيضاً في الفنون البصرية.|据家族记载，Alam-Taj Rezaei 是画家和艺术家，女儿 Farrokhondeh 与儿子 Aminollah 也从事视觉艺术。|Selon le récit familial, Alam-Taj Rezaei était peintre et artiste. Sa fille Farrokhondeh et son fils Aminollah se sont également consacrés aux arts visuels.')
person('ainollah-mahmoodi','Ainollah Mahmoodi Hamedani','عین‌الله محمودی همدانی',
       'Ainollah Mahmoodi Hamedani worked in Iran’s telephone and telegraph service. Iranian biographical accounts call him the “father of Iran’s telecommunications industry” for his part in developing the country’s communications infrastructure.|عین‌الله محمودی همدانی در دستگاه تلفن و تلگراف ایران خدمت کرد. در شرح‌حال‌های ایرانی به پاس نقش او در گسترش زیرساخت‌های ارتباطی کشور، از او با عنوان «پدر صنعت مخابرات ایران» یاد شده است.|عمل عين الله محمودي همداني في مرفق الهاتف والبرق الإيراني. وتلقّبه سير إيرانية بـ«أبي صناعة الاتصالات الإيرانية» تقديراً لدوره في تطوير البنية التحتية للاتصالات.|Ainollah Mahmoodi Hamedani 曾在伊朗电话和电报部门任职。伊朗传记资料称他为“伊朗电信业之父”，以纪念他对通信基础设施发展的贡献。|Ainollah Mahmoodi Hamedani a travaillé dans les services iraniens du téléphone et du télégraphe. Des notices iraniennes le surnomment « père de l’industrie iranienne des télécommunications » pour son rôle dans le développement du réseau.',
       ('خبر فارسی · شهر بورس','https://khabarfarsi.com/u/209911854'),('ویکی‌پدیا · عین‌الله محمودی همدانی','https://fa.wikipedia.org/wiki/عین‌الله_محمودی_همدانی'))
person('aminollah-rezaei','Aminollah Rezaei','امین‌الله رضایی',
       'Aminollah Rezaei was an Iranian painter, designer and poet. Scholars of surrealism have compared his use of dream imagery and the unconscious with the work of the Iraqi artist Jamil Hamoudi.|امین‌الله رضایی نقاش، طراح و شاعر ایرانی و از پیشگامان نقاشی سوررئالیستی ایران بود. پژوهشگران شیوهٔ استفادهٔ او از رؤیا و ناخودآگاه را با آثار جمیل حمودی، هنرمند عراقی، مقایسه کرده‌اند.|أمين الله رضائي رسام ومصمم وشاعر إيراني ومن رواد السريالية في إيران. قارن باحثون توظيفه للحلم واللاوعي بأعمال الفنان العراقي جميل حمودي.|Aminollah Rezaei 是伊朗画家、设计师和诗人。研究者曾将他在超现实主义绘画中对梦境和潜意识的表现与伊拉克艺术家 Jamil Hamoudi 的作品进行比较。|Aminollah Rezaei était un peintre, dessinateur et poète iranien. Des chercheurs ont comparé son usage du rêve et de l’inconscient dans la peinture surréaliste avec celui de l’artiste irakien Jamil Hamoudi.',
       ('Journal of Language, Literature, and Arts','https://citeus.um.ac.id/jolla/vol6/iss2/7/'),('Wikipedia · Aminollah Rezaei','https://en.wikipedia.org/wiki/Aminollah_Rezaei'))
labels('sister','My sister|خواهرم|شقيقتي|我的姐妹|Ma sœur')
labels('fatherofpgf','Father of my paternal grandfather|پدرِ پدربزرگ پدری‌ام|والد جدّي لأبي|祖父的父亲|Père de mon grand-père paternel')
labels('fatherofpgm','Father of my paternal grandmother|پدرِ مادربزرگ پدری‌ام|والد جدّتي لأبي|祖母的父亲|Père de ma grand-mère paternelle')
labels('motherofpgm','Mother of my paternal grandmother|مادرِ مادربزرگ پدری‌ام|والدة جدّتي لأبي|祖母的母亲|Mère de ma grand-mère paternelle')
labels('fatherofmgm','Father of my maternal grandmother|پدرِ مادربزرگ مادری‌ام|والد جدّتي لأمّي|外祖母的父亲|Père de ma grand-mère maternelle')
labels('motherofmgm','Mother of my maternal grandmother|مادرِ مادربزرگ مادری‌ام|والدة جدّتي لأمّي|外祖母的母亲|Mère de ma grand-mère maternelle')
labels('mygeneration','My generation|نسل من|جيلي|我的一代|Ma génération')
labels('familychildren','Children of Ali and Poopak|فرزندان علی و پوپک|ابنا علي وپوپك|Ali 与 Poopak 的子女|Enfants d’Ali et de Poopak')
ROLES = {'heydar-latifiyan':'fatherofpgf','hassan-latifiyan':'fatherofpgm','zahra-abdollahi':'motherofpgm','ainollah-mahmoodi':'fatherofmgm','alamtaj-rezaei':'motherofmgm','aminollah-rezaei':'siblingof'}
