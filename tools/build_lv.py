"""Build lv/index.html from index.html by translating its text.
Run from the repo root after changing the English homepage: python3 tools/build_lv.py
Each phrase must exist in index.html, otherwise the script stops and names it."""
import re,sys
src=open('index.html').read()
i=src.index('<!-- MODALS -->'); j=src.index('<script>',i)
A,M,B=src[:i],src[i:j],src[j:]

def R(part,en,lv,min_count=1):
    n=part.count(en)
    if n<min_count: sys.exit('MISSING: '+en[:70])
    return part.replace(en,lv)

# ---------- head / body ----------
pairs_A=[
('<html lang="en">','<html lang="lv">'),
('<title>Web Design & Development in Riga, Latvia — Erewhile Digital</title>','<title>Mājaslapu izstrāde un dizains Rīgā — Erewhile Digital</title>'),
('content="Web design studio in Riga, Latvia. Business websites from €1 200 and landing pages from €250 for companies, NGOs and Erasmus+ projects across the Baltics and the EU."',
 'content="Mājaslapu dizaina studija Rīgā. Uzņēmumu mājaslapas no €1 200 un vienas lapas mājaslapas no €250 uzņēmumiem, NVO un Erasmus+ projektiem Baltijā un ES."'),
('<link rel="canonical" href="https://erewhile.digital/"/>','<link rel="canonical" href="https://erewhile.digital/lv/"/>'),
('<meta property="og:url" content="https://erewhile.digital/"/>','<meta property="og:url" content="https://erewhile.digital/lv/"/>'),
('content="Erewhile Digital — Web Design & Development in Riga"','content="Erewhile Digital — mājaslapu izstrāde Rīgā"'),
('content="Business websites and landing pages for companies, NGOs and Erasmus+ projects across the Baltics and the EU."','content="Mājaslapas uzņēmumiem, NVO un Erasmus+ projektiem Baltijā un ES."'),
('content="en_GB"','content="lv_LV"'),
('"url": "https://erewhile.digital/", "inLanguage": "en"','"url": "https://erewhile.digital/lv/", "inLanguage": "lv"'),
# nav
('<a href="#ew-websites" class="active">Websites</a>','<a href="#ew-websites" class="active">Mājaslapas</a>'),
('<a href="/portfolio">Portfolio</a>','<a href="/portfolio">Portfolio</a>'),
('<a href="#ew-faq">FAQ</a>','<a href="#ew-faq">BUJ</a>'),
('<a href="#ew-contact">Contact</a>','<a href="#ew-contact">Kontakti</a>'),
('<a href="/lv/" hreflang="lv" lang="lv">LV</a>','<a href="/" hreflang="en" lang="en">EN</a>'),
('<a href="#ew-websites" onclick="closeMobileNav()">Websites</a>','<a href="#ew-websites" onclick="closeMobileNav()">Mājaslapas</a>'),
('<a href="#ew-faq" onclick="closeMobileNav()">FAQ</a>','<a href="#ew-faq" onclick="closeMobileNav()">BUJ</a>'),
('<a href="#ew-contact" onclick="closeMobileNav()">Contact</a>','<a href="#ew-contact" onclick="closeMobileNav()">Kontakti</a>'),
('<a href="/lv/" hreflang="lv" lang="lv">Latviski</a>','<a href="/" hreflang="en" lang="en">English</a>'),
('<a class="btn btn-teal btn-sm" href="#ew-contact">Get a quote</a>','<a class="btn btn-teal btn-sm" href="#ew-contact">Piedāvājums</a>'),
('aria-label="Open menu"','aria-label="Atvērt izvēlni"'),
# hero
('Web design studio · Riga, Latvia','Mājaslapu dizaina studija · Rīga'),
('<h1>Websites that <span class="g">bring you</span> new clients</h1>','<h1>Mājaslapas, kas <span class="g">atved jums</span> jaunus klientus</h1>'),
('We design and build websites and landing pages for businesses, personal brands, NGOs and Erasmus+ projects in the Baltics and across the EU. Landing pages from €250, business websites from €1 200.',
 'Izstrādājam mājaslapas uzņēmumiem, personīgajiem zīmoliem, NVO un Erasmus+ projektiem Baltijā un visā ES. Vienas lapas mājaslapa no €250, uzņēmuma mājaslapa no €1 200.'),
('>Discuss your project<','>Apspriest projektu<'),
('>See our work →<','>Skatīt mūsu darbus →<'),
('aria-label="Animated examples of client websites we built"','aria-label="Animēti mūsu izstrādāto mājaslapu piemēri"'),
('>View portfolio →<','>Skatīt portfolio →<'),
# services
('Services <span class="g">and prices</span>','Pakalpojumi <span class="g">un cenas</span>'),
('>Full business website<','>Uzņēmuma mājaslapa<'),
('Multi-page site with strategy, information architecture, UI/UX design and SEO foundations. Built for long-term growth.','Vairāku lapu mājaslapa ar stratēģiju, informācijas arhitektūru, UI/UX dizainu un SEO pamatiem. Veidota ilgtermiņa izaugsmei.'),
('>From €1 200<','>No €1 200<'),
('<div class="svc-title">Landing page</div>','<div class="svc-title">Vienas lapas mājaslapa</div>'),
('One focused page that explains what you do and captures leads. Fast turnaround, clean design, tested CTA.','Viena mērķtiecīga lapa, kas skaidro, ko jūs darāt, un piesaista pieteikumus. Ātra izstrāde, tīrs dizains, pārbaudīta darbības poga.'),
('>From €250<','>No €250<'),
('>Tools & integrations<','>Rīki un integrācijas<'),
('Forms connected to your CRM, booking flows, mini-dashboards and automations that make your site work for you.','Formas, kas savienotas ar jūsu CRM, rezervāciju sistēmas, mini paneļi un automatizācijas, lai mājaslapa strādātu jūsu labā.'),
('>Priced per project<','>Cena pēc projekta<'),
# work
('Recent <span class="g">work</span>','Jaunākie <span class="g">darbi</span>'),
('>Clothing brand · Estonia<','>Apģērbu zīmols · Igaunija<'),
('Kondo — brand website with online ordering','Kondo — zīmola mājaslapa ar tiešsaistes pasūtījumiem'),
('>Digital infopack<','>Digitālā infopaka<'),
('>Digital tool<','>Digitāls rīks<'),
('>Restaurant<','>Restorāns<'),
('Digital Menu — QR-accessible, no app','Digitālā ēdienkarte — atveras ar QR kodu, bez lietotnes'),
('>Request details →<','>Uzzināt vairāk →<'),
('>Local shop<','>Vietējais veikals<'),
('<div class="bcard-kicker">Flower shop</div>','<div class="bcard-kicker">Ziedu veikals</div>'),
('Razalija — catalogue & online order','Razalija — katalogs un tiešsaistes pasūtījumi'),
('>View all projects<','>Visi projekti<'),
('>10+ websites, tools & apps<','>10+ mājaslapas, rīki un lietotnes<'),
# statement
("Let's get your business <span class=\"g\">where you</span> want it to be","Aizvedīsim jūsu biznesu <span class=\"g\">tur, kur jūs</span> to vēlaties redzēt"),
('Website, content and integrations built to work as one system, from the first call to launch and beyond.','Mājaslapa, saturs un integrācijas, kas strādā kā viena sistēma, no pirmās sarunas līdz palaišanai un tālāk.'),
('>Start a project<','>Sākt projektu<'),
# pricing
('What will your <span class="g">project cost?</span>','Cik maksās <span class="g">jūsu projekts?</span>'),
('>Based on your answers<','>Pēc jūsu atbildēm<'),
('>Get a precise quote →<','>Saņemt precīzu piedāvājumu →<'),
(">Start over<",">Sākt no jauna<"),
('Final price depends on content, integrations and scope. No surprises after we agree.','Galīgā cena ir atkarīga no satura, integrācijām un apjoma. Pēc vienošanās nekādu pārsteigumu.'),
# process
('How a project <span class="g">runs</span>','Kā notiek <span class="g">projekts</span>'),
('>Discovery call<','>Iepazīšanās saruna<'),
('We talk through your goal, audience and what success looks like. 30 minutes, no pressure.','Pārrunājam jūsu mērķi, auditoriju un to, kā izskatās veiksme. 30 minūtes, bez spiediena.'),
('>Proposal & scope<','>Piedāvājums un apjoms<'),
('You get a written plan: structure, timeline, price. We agree on scope before anything starts.','Jūs saņemat rakstisku plānu: struktūru, termiņus, cenu. Apjomu saskaņojam pirms darba sākuma.'),
('>Design & build<','>Dizains un izstrāde<'),
('We design, develop and test. You review and give feedback. Two rounds of revisions included.','Mēs veidojam dizainu, izstrādājam un testējam. Jūs pārskatāt un sniedzat atsauksmes. Iekļautas divas labojumu kārtas.'),
('>Launch & handoff<','>Palaišana un nodošana<'),
('We launch, connect analytics and hand over everything. You own the site completely.','Palaižam mājaslapu, pieslēdzam analītiku un nododam visu jums. Mājaslapa pilnībā pieder jums.'),
# faq heading
('Questions <span class="g">clients ask</span>','Biežāk uzdotie <span class="g">jautājumi</span>'),
# form
('Request <span class="g">a quote</span>','Saņemt <span class="g">piedāvājumu</span>'),
("Tell us your niche and goal — we'll reply with a plan, timeline and estimate within 24 hours.",'Pastāstiet par savu nozari un mērķi, un 24 stundu laikā atsūtīsim plānu, termiņus un izmaksu tāmi.'),
('New request — erewhile.digital (EN)','New request — erewhile.digital (LV)'),
('<label>Name</label>','<label>Vārds</label>'),
('<label>Email</label>','<label>E-pasts</label>'),
('<label>What do you need?</label>','<label>Kas jums nepieciešams?</label>'),
('>Consultation (project discovery)<','>Konsultācija (projekta izpēte)<'),
('>Website (custom)<','>Mājaslapa (individuāla)<'),
('>Landing page from €250<','>Vienas lapas mājaslapa no €250<'),
('>Content / video<','>Saturs / video<'),
('>Integrations / analytics<','>Integrācijas / analītika<'),
('>Other<','>Cits<'),
('<label>Message</label>','<label>Ziņa</label>'),
('placeholder="How should we address you?"','placeholder="Kā pie jums vērsties?"'),
('placeholder="you@company.com"','placeholder="jus@uznemums.lv"'),
('placeholder="Briefly: niche, goal, what you sell/offer, deadline, references (if any)"','placeholder="Īsi: nozare, mērķis, ko piedāvājat, termiņš, piemēri (ja ir)"'),
('I agree to the <a','Piekrītu <a'),
('My email will only be used to respond to this inquiry.','Mans e-pasts tiks izmantots tikai atbildei uz šo pieprasījumu. Noteikumi pieejami angļu valodā.'),
('>Send request<','>Nosūtīt pieprasījumu<'),
('We reply within 24 hours. Urgent? Add your deadline in the message.','Atbildam 24 stundu laikā. Steidzami? Norādiet termiņu ziņā.'),
('>Terms & Conditions</a>,','>noteikumiem</a>,'),
('>Privacy Policy</a> and','>privātuma politikai</a> un'),
('>Cookie Policy</a>.','>sīkdatņu politikai</a>.'),
]
for en,lv in pairs_A: A=R(A,en,lv)

FAQ=[
("How much does a website cost?","Cik maksā mājaslapa?",
 "A one-page landing page in one language costs €250, a business website with up to five pages starts at €1 200, and an online store at €2 200. Extra pages, language versions, copywriting and integrations are added as clear modules, and custom tools are estimated in working days. The calculator above gives a realistic range, and we confirm a fixed price in writing before work starts.",
 "Vienas lapas mājaslapa vienā valodā maksā €250, uzņēmuma mājaslapa līdz piecām lapām no €1 200, interneta veikals no €2 200. Papildu lapas, valodu versijas, teksti un integrācijas tiek pievienotas kā skaidri moduļi, bet individuāli rīki tiek novērtēti darba dienās. Kalkulators augstāk parāda reālu cenu diapazonu, un fiksētu cenu rakstiski apstiprinām pirms darba sākuma."),
("How long does it take to build a website?","Cik ilgi tiek izstrādāta mājaslapa?",
 "A landing page typically takes 1–2 weeks and a business website 2–4 weeks. Rush delivery in under two weeks is possible at a higher rate. Most of the timeline depends on how quickly content and feedback come in.",
 "Vienas lapas mājaslapa parasti aizņem 1–2 nedēļas, uzņēmuma mājaslapa 2–4 nedēļas. Steidzama izstrāde ātrāk par divām nedēļām ir iespējama par augstāku cenu. Termiņš lielā mērā atkarīgs no tā, cik ātri saņemam saturu un atsauksmes."),
("Do you work with clients outside Latvia?","Vai strādājat ar klientiem ārpus Latvijas?",
 "Yes. We are based in Riga and work with clients across the Baltics and the EU, for example Kondo in Estonia. Everything can be done remotely, and we communicate in English, Latvian or Russian.",
 "Jā. Atrodamies Rīgā un strādājam ar klientiem visā Baltijā un ES, piemēram, ar Kondo Igaunijā. Visu var izdarīt attālināti, un sazināmies latviešu, angļu vai krievu valodā."),
("Do you build websites for NGOs and Erasmus+ projects?","Vai izstrādājat mājaslapas NVO un Erasmus+ projektiem?",
 "Yes. We have built websites and digital infopacks for NGOs and Erasmus+ projects, such as From Thinking to Speaking for UNTU. We know what these projects need: clear structure, partner and result pages, and materials that stay online after the project ends.",
 "Jā. Esam izstrādājuši mājaslapas un digitālās infopakas NVO un Erasmus+ projektiem, piemēram, From Thinking to Speaking organizācijai UNTU. Zinām, kas šādiem projektiem vajadzīgs: skaidra struktūra, partneru un rezultātu lapas un materiāli, kas paliek tiešsaistē arī pēc projekta beigām."),
("Will my website be optimised for Google?","Vai mājaslapa būs optimizēta Google?",
 "Every site gets SEO foundations: a clean page structure, meta titles and descriptions, structured data, a sitemap, fast loading and correct language versions. For competitive markets we can also plan landing pages and content around the searches your clients make.",
 "Katra mājaslapa saņem SEO pamatus: tīru lapu struktūru, meta virsrakstus un aprakstus, strukturētos datus, vietnes karti, ātru ielādi un pareizas valodu versijas. Konkurētspējīgos tirgos varam arī plānot lapas un saturu atbilstoši tam, ko meklē jūsu klienti."),
("What do I need to prepare before we start?","Kas jāsagatavo pirms darba sākuma?",
 "A short description of your business and goal, your logo if you have one, and any texts or photos you already have. If you are starting from zero, we can help with structure, copy and visuals.",
 "Īss apraksts par jūsu biznesu un mērķi, logotips, ja tāds ir, un esošie teksti vai foto. Ja sākat no nulles, palīdzēsim ar struktūru, tekstiem un vizuālo materiālu."),
("Can you connect the website to my CRM or booking system?","Vai varat savienot mājaslapu ar manu CRM vai rezervāciju sistēmu?",
 "Yes. We connect forms to CRMs such as HubSpot or Pipedrive, set up booking flows and email notifications, and configure analytics so you can see where your leads come from.",
 "Jā. Savienojam formas ar CRM sistēmām, piemēram, HubSpot vai Pipedrive, iestatām rezervācijas un e-pasta paziņojumus un konfigurējam analītiku, lai jūs redzētu, no kurienes nāk pieteikumi."),
("Who owns the website after the project?","Kam pieder mājaslapa pēc projekta?",
 "You do. After launch we hand over the site, the accounts and access, and you own everything completely. Two rounds of revisions are included in every project.",
 "Jums. Pēc palaišanas nododam mājaslapu, kontus un piekļuves, un viss pilnībā pieder jums. Katrā projektā iekļautas divas labojumu kārtas."),
]
for qe,ql,ae,al in FAQ:
    A=R(A,qe,ql,2); A=R(A,ae,al,2)

# ---------- scripts ----------
pairs_B=[
("<button class=\"quiz-back\" onclick=\"quizBk'+S+'()\">← Back</button>","<button class=\"quiz-back\" onclick=\"quizBk'+S+'()\">← Atpakaļ</button>"),
("'< 2 weeks (rush rate)':time==='flexible'?'4–8 weeks':'2–4 weeks'","'< 2 nedēļas (steidzami)':time==='flexible'?'4–8 nedēļas':'2–4 nedēļas'"),
('>per day</span>','>dienā</span>'),
("<span>Timeline: '+tl+'</span>","<span>Termiņš: '+tl+'</span>"),
('Fixed price agreed in writing','Fiksēta cena, saskaņota rakstiski'),
("What\\'s included","Kas iekļauts"),
("' — estimate '","' — tāme '"),
("tl='Depends on scope'","tl='Atkarīgs no apjoma'"),
]
for en,lv in pairs_B: B=R(B,en,lv)
qs=[
('What do you need?','Kas jums nepieciešams?'),('Landing page','Vienas lapas mājaslapa'),('One focused page','Viena mērķtiecīga lapa'),
('Business website','Uzņēmuma mājaslapa'),('Several pages, full structure','Vairākas lapas, pilna struktūra'),('Online store','Interneta veikals'),
('Products, cart, checkout','Preces, grozs, apmaksa'),('Custom tool or web app','Individuāls rīks vai lietotne'),('Calculator, dashboard, CRM, API','Kalkulators, panelis, CRM, API'),
('How many pages?','Cik lapu?'),('1 page','1 lapa'),('Everything on one screen flow','Viss vienā lapā'),('2–5 pages','2–5 lapas'),
('Home, services, about, contact','Sākums, pakalpojumi, par mums, kontakti'),('6–10 pages','6–10 lapas'),('Separate service or project pages','Atsevišķas pakalpojumu vai projektu lapas'),
('More than 10','Vairāk par 10'),('Large site or catalogue','Liela vietne vai katalogs'),('How many languages?','Cik valodās?'),
('One language','Viena valoda'),('English, Latvian or other','Latviešu, angļu vai cita'),('Two languages','Divas valodas'),('e.g. English + Latvian','piem., latviešu + angļu'),
('Three or more','Trīs vai vairāk'),('e.g. EN + LV + LT/EE/RU','piem., LV + EN + LT/EE/RU'),('Which features do you need?','Kādas funkcijas vajadzīgas?'),
('Contact form','Kontaktforma'),('Requests go to your email','Pieteikumi nonāk jūsu e-pastā'),('Online booking','Tiešsaistes rezervācija'),('Calendar, appointments','Kalendārs, pieraksti'),
('CRM integration','CRM integrācija'),('HubSpot, Pipedrive, etc.','HubSpot, Pipedrive u.c.'),('Booking + CRM','Rezervācija + CRM'),('Full lead flow','Pilna pieteikumu plūsma'),
('Are texts and images ready?','Vai teksti un attēli ir gatavi?'),('Yes, all ready','Jā, viss gatavs'),('I just need the site built','Vajag tikai izstrādāt mājaslapu'),
('Partially ready','Daļēji gatavs'),('Need help with some texts','Vajag palīdzību ar daļu tekstu'),('Starting from zero','Sākam no nulles'),('Need texts for every page','Vajag tekstus visām lapām'),
('ASAP (< 2 weeks)','Steidzami (< 2 nedēļas)'),('Rush project','Steidzams projekts'),('2–4 weeks','2–4 nedēļas'),('Standard timeline','Standarta termiņš'),
('No rush (1–2 months)','Bez steigas (1–2 mēneši)'),('Flexible','Elastīgi'),
('Custom tools are estimated in working days after a short discovery call. Most small tools take 4–10 days; about 30% of that time goes to testing and fixes.','Individuālus rīkus novērtējam darba dienās pēc īsas iepazīšanās sarunas. Lielākā daļa nelielu rīku aizņem 4–10 dienas, un ap 30% laika tiek veltīts testēšanai un labojumiem.'),
('Discovery call and written estimate','Iepazīšanās saruna un rakstiska tāme'),('Prototype before full build','Prototips pirms pilnas izstrādes'),('Testing on real data','Testēšana ar reāliem datiem'),('Handover and documentation','Nodošana un dokumentācija'),
('A focused page built for conversion: clear message, lead capture, fast launch.','Mērķtiecīga lapa pieteikumu iegūšanai: skaidrs vēstījums, pieteikumu forma, ātra palaišana.'),
('A multi-page business website with full structure, SEO foundations and analytics.','Vairāku lapu uzņēmuma mājaslapa ar pilnu struktūru, SEO pamatiem un analītiku.'),
('An online store with catalogue, cart, checkout and payments.','Interneta veikals ar katalogu, grozu, noformēšanu un maksājumiem.'),
('Responsive design','Pielāgots dizains visām ierīcēm'),('Lead capture form','Pieteikumu forma'),('Analytics setup','Analītikas iestatīšana'),('2 revision rounds','2 labojumu kārtas'),
('Structure and UI/UX design','Struktūra un UI/UX dizains'),('SEO foundations','SEO pamati'),('Product catalogue','Preču katalogs'),('Cart and checkout','Grozs un noformēšana'),
('Payment integration','Maksājumu integrācija'),('Order notifications','Pasūtījumu paziņojumi'),('Language versions with correct SEO setup','Valodu versijas ar pareizu SEO iestatījumu'),('Copywriting for the pages you need','Teksti nepieciešamajām lapām'),
# demo
('FASHION BRAND','MODES ZĪMOLS'),('Shop · About · Contact','Veikals · Par mums · Kontakti'),('New collection','Jaunā kolekcija'),('is live','jau pieejama'),
('Clothing brand from Estonia. Browse the collection and order online.','Apģērbu zīmols no Igaunijas. Apskatiet kolekciju un pasūtiet tiešsaistē.'),('Order now','Pasūtīt'),('new order received','saņemts jauns pasūtījums'),('E-commerce','E-komercija'),
('NGO PROJECT','NVO PROJEKTS'),('Modules · Partners','Moduļi · Partneri'),('digital infopack','digitālā infopaka'),
('A digital infopack that gives Erasmus+ participants everything in one place.','Digitālā infopaka, kurā Erasmus+ dalībnieki atrod visu vienuviet.'),('Open infopack','Atvērt infopaku'),('participant registered','dalībnieks reģistrēts'),('Erasmus+ infopack','Erasmus+ infopaka'),
('Flower shop','Ziedu veikals'),('Catalogue · Delivery','Katalogs · Piegāde'),('Fresh flowers','Svaigi ziedi'),('from Riga','no Rīgas'),('The flower shop catalogue with online ordering.','Ziedu veikala katalogs ar tiešsaistes pasūtījumiem.'),
('Order a bouquet','Pasūtīt pušķi'),('bouquet ordered','pušķis pasūtīts'),('Catalogue & orders','Katalogs un pasūtījumi'),
('DIGITAL MENU','DIGITĀLĀ ĒDIENKARTE'),('Mains · Drinks · Desserts','Ēdieni · Dzērieni · Deserti'),('Scan the QR,','Noskenējiet QR,'),('see the menu','skatiet ēdienkarti'),
('Soup of the day ........ €6\\nGrilled salmon ......... €16\\nOpens from a QR code, no app.','Dienas zupa ........... €6\\nGrilēts lasis ......... €16\\nAtveras ar QR kodu, bez lietotnes.'),
('Call a waiter','Izsaukt viesmīli'),('table request sent','galdiņa pieprasījums nosūtīts'),('Digital tool','Digitāls rīks'),
]
for en,lv in qs:
    q1="'"+en+"'"
    if q1 not in B: sys.exit('JS MISSING: '+en)
    B=B.replace(q1,"'"+lv+"'")
out=A+M+B
# keep EN demo label strings for the new-lead suffix "form.submit" (code, fine)
open('lv/index.html','w').write(out)
print('ok', len(out))
