"""Build portfolio case pages: python3 -I tools/build_cases.py

Writes portfolio/<slug>/index.html for every case in CASES, in this order
(the order also drives the "Next case" link). Shared styles live in
tools/case_style.css. Texts are English; client visuals are hot-linked
from the clients' own ImageKit folders or copied into assets/cases/<slug>/.
"""
import html, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from case_stages import STAGES, stage_css

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://erewhile.digital'
STYLE = open(os.path.join(ROOT, 'tools', 'case_style.css'), encoding='utf-8').read()

CASES = [
  dict(
    slug='zemits', name='Zemits', new=True,
    url='https://zemits-latvija.lv', host='zemits-latvija.lv',
    title='Zemits case study: three-language catalogue for a cosmetology equipment distributor',
    desc='How we built a Latvian, Russian and English site with a device catalogue, training and service pages for Zemits Skin Expert, the official Zemits representative in the Baltics.',
    h1='A three-language catalogue that sells <span>professional</span> beauty equipment',
    tags=['Beauty equipment', 'Latvia &amp; Baltics', 'LV · RU · EN', 'Device catalogue'],
    lede='Zemits Skin Expert is the official Zemits representative in the Baltic states. They sell professional face and body devices to salons, clinics and specialists, and back them with training, a 24-month warranty and local service.',
    cover='/assets/cases/zemits/cover.jpg', cover_wh=(1200, 630),
    facts=[('Client', 'Zemits Skin Expert'), ('Market', 'Latvia and the Baltics'), ('Languages', 'Latvian, Russian, English'), ('Catalogue', 'Devices with prices and details')],
    task_h='Help salons compare devices worth thousands of euros',
    task=['Salon owners and cosmetologists do not buy a laser or an RF platform on impulse. They compare technologies, prices and what support they get after the purchase.',
          'The site had to present the whole device range in three languages, show real treatment results and make it easy to ask a question or book training.'],
    built_h='From first look to a request in one flow',
    built=[('Device catalogue', 'Each device has a card and a detail popup with price, features and photos, on the home page and a full catalogue page.'),
           ('Training and seminars', 'Masterclasses and seminars are part of the offer, so buyers see they will not be left alone with the device.'),
           ('Results and reviews', 'Before-and-after photos and client reviews build trust for a technical, high-ticket product.'),
           ('Search-ready in three languages', 'Language versions with hreflang, structured data for every device with its price, a sitemap and link previews for each page.')],
    vis_h='Clinical blue with an editorial touch',
    vis='A deep blue palette signals medical precision, and an elegant serif for headlines keeps it from feeling like a hospital. A clean sans handles prices, specs and buttons.',
    fonts=('Playfair Display', 'Outfit', 'Outfit'), gf='family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Outfit:wght@300;400;500;600',
    display_w='500', display_ls='0',
    sample=('Visible results.', 'Advanced aesthetic cosmetology equipment', 'Zemits Skin Expert'),
    palette=[('#1A4A8A','Brand blue'), ('#2D6BBF','Links, hovers'), ('#4DA6FF','Light accent'), ('#1A2340','Text'), ('#F7F8FA','Background')],
    ink='#ffffff', logo_bg='#1A4A8A', logo='/assets/cases/zemits/logo-white.png', logo_wh=(None, None), mark_color='#fff', dark_panel=True,
    gallery=['https://ik.imagekit.io/xwsgpirygo/Zemits/aparati/1.png?tr=w-500', 'https://ik.imagekit.io/xwsgpirygo/Zemits/aparati/2.png?tr=w-500',
             'https://ik.imagekit.io/xwsgpirygo/Zemits/aparati/3.png?tr=w-500', 'https://ik.imagekit.io/xwsgpirygo/Zemits/aparati/4.png?tr=w-500'],
    gallery_alt='Zemits device from the catalogue', gallery_ratio='1/1',
    handover=['Live site in 3 languages', 'Device catalogue', 'Build script for easy edits', 'Link previews for every page', 'Sitemap, schema and llms.txt'],
    cta=('Selling something that needs <span>explaining</span>?', 'Tell us what you sell and who buys it. We will plan the pages that answer their questions before they call.'),
  ),
  dict(
    slug='kondo', name='Kondo',
    url='https://kondo.ee', host='kondo.ee',
    title='Kondo case study: website for a made-to-order clothing label',
    desc='How we built a one-page brand site with a pre-order bag for Kondo, an Estonian label making linen and ramie clothing to order.',
    h1='A brand site that takes <span>pre&#8209;orders</span> for a clothing label',
    tags=['Fashion', 'Estonia', 'Fixed deadline', 'One-page site', 'Pre-order bag'],
    lede='Kondo makes linen and ramie clothing for yoga and everyday wear, sewn to order. They needed a site that tells the story of the fabrics and lets people put together an order without a full online store.',
    cover='/assets/cases/kondo/cover.jpg', cover_wh=(1200, 630),
    facts=[('Client', 'Kondo, clothing label'), ('Deadline', 'Live before the launch event'), ('Format', 'One-page site with sections'), ('Ordering', 'Pre-order bag + enquiry form')],
    task_h='Launch before the collection presentation',
    task=['Kondo had a presentation event for its new clothing line already scheduled, and the site had to be live by then. The deadline was fixed, so the scope had to be tight and the launch reliable.',
          'Every Kondo piece is made after the order, with a 50% deposit and 1–2 weeks of production. A standard e-commerce platform with stock, shipping rules and instant payment did not fit that model.',
          'The brand also needed space to explain why ramie and linen are worth it, and how to care for them, so buyers understand the price before they order.'],
    built_h='One page that leads from story to order',
    built=[('Brand story and fabrics', 'About, Fabrics and Care sections explain the materials and how to look after them.'),
           ('Two collections', 'Yoga Drop and City Drop, each with prices, so buyers see the range at a glance.'),
           ('Pre-order bag', 'Visitors add pieces to a bag and see an estimated total. Items priced on request are confirmed separately.'),
           ('Enquiry form', 'Name, phone, email and a comment. Works with or without selected pieces, so custom requests come in too.')],
    vis_h='Quiet luxury with a dragon in the hall',
    vis='The name means "Golden Hall", so the site follows a temple-like calm: white space, black ink, a faint 金堂 watermark and a dragon mark. A decorative display face for the name, a classic serif for the story, and a clean sans for prices and buttons.',
    fonts=('Cinzel Decorative', 'EB Garamond', 'Inter'), gf='family=Cinzel+Decorative:wght@900&family=EB+Garamond:ital@0;1&family=Inter:wght@400;600',
    display_w='900', display_ls='.03em', kanji='金堂',
    sample=('KONDŌ', 'Where the Dragon Dwells', 'Golden Hall'),
    palette=[('#FFFFFF','Background'), ('#111111','Ink'), ('#5C5C5C','Body text'), ('#E2E2E2','Lines')],
    ink='#111111', logo_bg='#ffffff', logo='/assets/cases/kondo/dragon.png', logo_wh=(480, 441),
    gallery=['https://ik.imagekit.io/colibrarian/Kondo/products/kimono/1.jpg?tr=w-500,q-75,f-auto', 'https://ik.imagekit.io/colibrarian/Kondo/products/skirt/1.jpg?tr=w-500,q-75,f-auto',
             'https://ik.imagekit.io/colibrarian/Kondo/products/top/1.jpg?tr=w-500,q-75,f-auto', 'https://ik.imagekit.io/colibrarian/Kondo/products/aladdin/1.jpg?tr=w-500,q-75,f-auto'],
    gallery_alt='Kondo garment', gallery_ratio='3/4',
    handover=['Live website', 'Pre-order flow', 'Mobile layout', 'Privacy policy', 'Instagram link'],
    cta=('Need a site that <span>sells</span> your way?', 'Tell us how you take orders today. We will suggest the simplest site that fits, with a fixed price before work starts.'),
  ),
  dict(
    slug='solvata-beauty', name='Solvata Beauty',
    url='https://solvatabeauty.lv', host='solvatabeauty.lv',
    title='Solvata Beauty case study: website for a hardware cosmetology studio',
    desc='How we built a premium website for Solvata Beauty, a hardware cosmetology studio in Latvia: technologies, results, team and booking.',
    h1='A premium studio site that explains the <span>technology</span>',
    tags=['Beauty', 'Latvia', 'Multi-page', 'Booking'],
    lede='Solvata Beauty is a hardware cosmetology studio that works only with original, clinically tested premium devices. The site had to show that care and expertise before a client books.',
    cover='https://ik.imagekit.io/erewhile/Solvata/logo%20and%20og/OG%20image%20solvata.png', cover_wh=(1200, 630),
    facts=[('Client', 'Solvata Beauty studio'), ('Market', 'Latvia'), ('Format', 'Home page + treatment pages'), ('Booking', 'Online booking + WhatsApp')],
    task_h='Turn complex treatments into a confident booking',
    task=['Treatments like RF microneedling or endospheres are hard to judge from a price list. Clients want to understand what the device does, whether it is safe, and who will do the procedure.',
          'The studio needed a site that feels as premium as the service and leads naturally to a booking.'],
    built_h='Technology, proof and people on one path',
    built=[('Technology section', 'Every device gets a photo and a plain explanation of what it does and how it feels.'),
           ('Dedicated treatment pages', 'Separate pages for services and RF microneedling give room for detail and search.'),
           ('Before and after, reviews', 'Real results and client words answer the "does it work" question.'),
           ('Team and booking', 'The people behind the studio, a map and a booking call to action in every section.')],
    vis_h='Deep plum and an elegant serif',
    vis='A deep plum accent and a refined serif give the studio a calm, high-end feel, while a light geometric sans keeps treatment details easy to read.',
    fonts=('Cormorant Garamond', 'Cormorant Garamond', 'Jost'), gf='family=Cormorant+Garamond:ital,wght@0,500;1,500&family=Jost:wght@400;500',
    display_w='500', display_ls='0',
    sample=('Solvata Beauty', 'Dabiskais skaistums un jaunība', 'Pierakstīties'),
    palette=[('#410022','Deep plum'), ('#6B0038','Accent'), ('#FAF8F7','Background'), ('#1A1015','Text'), ('#7A6670','Muted text')],
    ink='#1A1015', logo_bg='#FAF8F7', logo='https://ik.imagekit.io/erewhile/Solvata/logo%20solvata%20beauty.png?tr=w-480', logo_wh=(None, None),
    gallery=['https://ik.imagekit.io/erewhile/Solvata/main%20photo.png?tr=w-500', 'https://ik.imagekit.io/erewhile/Solvata/Endymed%20Intensive%20Microneedling.png?tr=w-500',
             'https://ik.imagekit.io/erewhile/Solvata/endospheres.png?tr=w-500', 'https://ik.imagekit.io/erewhile/Solvata/pollogen%20geneo.JPG?tr=w-500'],
    gallery_alt='Solvata Beauty studio and devices', gallery_ratio='3/4',
    handover=['Live website', 'Treatment pages', 'Booking flow', 'Map and contacts', 'Privacy policy'],
    cta=('Want clients to <span>trust</span> you before the first visit?', 'Tell us about your studio and treatments. We will plan a site that explains them clearly and leads to booking.'),
  ),
  dict(
    slug='razalija', name='Razalija',
    url='https://razalija.lv', host='razalija.lv',
    title='Razalija case study: website for a flower shop in Riga',
    desc='How we built a Latvian and Russian site for Razalija, a florist in Mežaparks, Riga: bouquet gallery, delivery zones and ordering through WhatsApp.',
    h1='A flower shop site where ordering takes <span>minutes</span>',
    tags=['Florist', 'Riga', 'LV · RU', 'WhatsApp orders'],
    lede='Razalija is a florist in Mežaparks, Riga, with fresh bouquets, compositions for special occasions, custom orders and delivery across the city. Most customers order from a phone, often at the last minute.',
    cover='https://ik.imagekit.io/coworker/Razalija/raz%201.png?tr=w-1200,h-630,c-maintain_ratio', cover_wh=(1200, 630),
    facts=[('Client', 'Razalija flower shop'), ('Market', 'Riga, Latvia'), ('Languages', 'Latvian, Russian'), ('Ordering', 'Gallery + WhatsApp')],
    task_h='Make a last-minute bouquet order easy from a phone',
    task=['Flowers are often bought in a hurry: for a birthday tonight or a meeting tomorrow. A long checkout loses those customers.',
          'The shop needed a site where people see ready bouquets, understand delivery, and send an order in a few taps, in Latvian or Russian.'],
    built_h='See it, pick it, send it',
    built=[('Bouquet gallery', 'Ready bouquets with photos, so customers choose by eye, not by description.'),
           ('Order through WhatsApp', 'The chosen bouquet goes into a WhatsApp message, where the shop confirms details and the address.'),
           ('Delivery zones', 'Free delivery areas and prices across Riga are clear before ordering.'),
           ('Local search basics', 'FAQ, map, opening hours, structured data and Latvian and Russian versions for local search.')],
    vis_h='Bright, fresh and a little playful',
    vis='Soft violet and pink accents on white match the mood of the bouquets. A characterful serif for headings and a neutral sans for prices and practical details.',
    fonts=('Fraunces', 'Inter', 'Inter'), gf='family=Fraunces:ital,wght@0,600;1,600&family=Inter:wght@400;600;700;800',
    display_w='600', display_ls='-.01em',
    sample=('Razalija', 'Ziedi, kas izskatās kā svētki', 'Pasūtīt pušķi'),
    palette=[('#7C3AED','Violet'), ('#EC4899','Pink'), ('#38BDF8','Sky'), ('#FFFFFF','Cards'), ('#FBFBFE','Background')],
    ink='#1b1530', logo_bg='#FBFBFE', logo=None, mark_color='#7C3AED',
    gallery=['https://ik.imagekit.io/coworker/Razalija/raz%202.png?tr=w-500', 'https://ik.imagekit.io/coworker/Razalija/raz%203.png?tr=w-500',
             'https://ik.imagekit.io/coworker/Razalija/raz%204.png?tr=w-500', 'https://ik.imagekit.io/coworker/Razalija/raz%205.png?tr=w-500'],
    gallery_alt='Razalija bouquet', gallery_ratio='3/4',
    handover=['Live site in 2 languages', 'Bouquet gallery', 'WhatsApp ordering', 'Delivery info', 'Sitemap, schema and llms.txt'],
    cta=('Want orders to come in <span>faster</span>?', 'Tell us how customers order from you today. We will make that path shorter.'),
  ),
  dict(
    slug='jelgava-coworking', name='Jelgava Coworking',
    url='https://www.jelgavacoworking.lv', host='jelgavacoworking.lv',
    title='Jelgava Coworking case study: website for a coworking space',
    desc='How we built a Latvian, Russian and English site for Jelgava Coworking Space: atmosphere, clear packages with prices, FAQ and an application form.',
    h1='A coworking site that answers <span>“how much”</span> right away',
    tags=['Coworking', 'Jelgava', 'LV · RU · EN', 'Lead form'],
    lede='Jelgava Coworking Space is a quiet, 24/7 workspace for freelancers, IT specialists, creators, students and entrepreneurs from Jelgava and nearby towns.',
    cover='https://ik.imagekit.io/coworker/Jelgava%20Coworking%20Space/og-image.png', cover_wh=(1200, 630),
    facts=[('Client', 'Jelgava Coworking Space'), ('Market', 'Jelgava region, Latvia'), ('Languages', 'Latvian, Russian, English'), ('Leads', 'Application form + WhatsApp')],
    task_h='Show the space and the prices before people visit',
    task=['People choosing a coworking want two answers fast: what the place feels like and how much it costs.',
          'The site had to show the atmosphere, explain who the space is for, lay out the packages clearly and collect applications in three languages.'],
    built_h='Atmosphere first, then a clear choice',
    built=[('Atmosphere gallery', 'Large photos of the space and the meeting room set the mood in the first seconds.'),
           ('Packages with prices', 'Focus, Flow, Studio and Business plans, a day pass and meeting room rates side by side.'),
           ('Who it is for', 'Freelancers, IT, photographers, students and entrepreneurs each see themselves in the offer.'),
           ('Application form and FAQ', 'Every package leads to one form, and common questions are answered on the page.')],
    vis_h='Calm white with one strong red',
    vis='White space and black text keep the site as quiet as the space itself. One deep red from the logo marks actions and prices. A single modern grotesque runs through everything.',
    fonts=('Space Grotesk', 'Space Grotesk', 'Space Grotesk'), gf='family=Space+Grotesk:wght@400;500;600;700',
    display_w='700', display_ls='-.02em',
    sample=('Jelgava Coworking', 'A calm place to focus', 'Apskatīt paketes'),
    palette=[('#880002','Logo red'), ('#111111','Text'), ('#666666','Muted text'), ('#E9E9E9','Lines'), ('#FFFFFF','Background')],
    ink='#111111', logo_bg='#ffffff', logo='https://ik.imagekit.io/coworker/Jelgava%20Coworking%20Space/Jelgava_Coworking_Space_Red.png?tr=f-auto,w-440', logo_wh=(None, None),
    gallery=['https://ik.imagekit.io/coworker/Jelgava%20Coworking%20Space/cowork%201.png?tr=f-auto,w-600', 'https://ik.imagekit.io/coworker/Jelgava%20Coworking%20Space/Cowork%202.png?tr=f-auto,w-600',
             'https://ik.imagekit.io/coworker/Jelgava%20Coworking%20Space/Cowork%203.png?tr=f-auto,w-600', 'https://ik.imagekit.io/coworker/Jelgava%20Coworking%20Space/conference%20room.png?tr=f-auto,w-600'],
    gallery_alt='Jelgava Coworking Space interior', gallery_ratio='4/3',
    handover=['Live site in 3 languages', 'Packages and prices', 'Application form', 'Privacy policy in 3 languages', 'Sitemap, schema and llms.txt'],
    cta=('Need your prices to <span>sell</span>, not scare?', 'Tell us about your offer. We will lay it out so people pick a plan instead of leaving.'),
  ),
  dict(
    slug='untu', name='UNTU',
    url='https://untu.ngo', host='untu.ngo',
    title='UNTU case study: website for a youth NGO and its Erasmus+ projects',
    desc='How we built the UNTU website: an NGO home page with events and calls to apply, plus dedicated project sections for Erasmus+ programmes like From Thinking to Speaking.',
    h1='A youth NGO site with a home for every <span>project</span>',
    tags=['NGO', 'Erasmus+', 'Project pages', 'Applications'],
    lede='UNTU is a non-profit youth organisation for people aged 18–35, running international projects, trainings, volunteering and cultural exchange.',
    cover='https://ik.imagekit.io/xshkpkf2i/Untu/Logo%20and%20Og/UNTU%20OG%20image.png', cover_wh=(1200, 630),
    facts=[('Client', 'UNTU, youth NGO'), ('Audience', 'Young people 18–35, partners'), ('Format', 'Main site + project sections'), ('Leads', 'Apply and partner forms')],
    task_h='One site for the organisation and all its projects',
    task=['An NGO speaks to several audiences at once: young people who want to join, partner organisations, and funders who need to see results.',
          'Each Erasmus+ project also needs its own space for programme, travel, participants and outputs that stays online after the project ends.'],
    built_h='Organisation on top, projects underneath',
    built=[('Events and calls', 'Upcoming programmes and an "apply" path right from the first screen.'),
           ('Vision and about', 'What UNTU stands for, in clear language for young people and partners.'),
           ('Project sections', 'FTS and DWCM have their own pages: programme, travel info, participants, library, media and learning modules.'),
           ('Apply and partner forms', 'One form for participants and one for organisations that want to collaborate.')],
    vis_h='Night blue with a bright yellow spark',
    vis='A dark background with a bright yellow accent gives the NGO energy without looking corporate. Bold Montserrat headings and a dragon character make it recognisable.',
    fonts=('Montserrat', 'Montserrat', 'Montserrat'), gf='',
    display_w='900', display_ls='-.03em',
    sample=('Grow, connect, create.', 'A non-profit youth organization for real-world growth.', 'Get involved'),
    palette=[('#0B0D12','Night background'), ('#FFD233','Yellow accent'), ('#FFFFFF','Text')],
    ink='#ffffff', logo_bg='#0B0D12', logo='https://ik.imagekit.io/xshkpkf2i/Untu/logo%20untu.png?tr=w-480', logo_wh=(None, None), dark_panel=True,
    gallery=['https://ik.imagekit.io/xshkpkf2i/Untu/DSC_6724.jpg?tr=w-500', 'https://ik.imagekit.io/xshkpkf2i/Untu/IMG_7184.JPG?tr=w-500',
             'https://ik.imagekit.io/xshkpkf2i/Untu/asset%20photo%20session.png?tr=w-500', 'https://ik.imagekit.io/xshkpkf2i/Untu/ctml.png?tr=w-500'],
    gallery_alt='UNTU project moment', gallery_ratio='4/3',
    handover=['Live website', 'Project sections', 'Apply and partner forms', 'Privacy and terms', 'Sitemap'],
    cta=('Running an NGO or <span>Erasmus+</span> project?', 'Tell us about your project. We will plan pages for participants, partners and results that stay online after it ends.'),
  ),
  dict(
    slug='id-chef', name='ID Chef',
    url='https://idchef13.com', host='idchef13.com',
    title='ID Chef case study: personal brand website for a chef and restaurant consultant',
    desc='How we built a personal brand site in English, Latvian and Russian for Denis Ivankov, an executive chef and restaurant consultant with 30+ years of experience.',
    h1='A personal brand site for a chef who <span>fixes</span> kitchens',
    tags=['Personal brand', 'Riga', 'EN · LV · RU', 'Consulting'],
    lede='Denis Ivankov is an executive chef and restaurant consultant with more than 30 years in the industry. He launches restaurants from scratch and turns kitchen chaos into profitable systems.',
    cover='https://ik.imagekit.io/xwsgpirygo/id%20chef/logos/OG.png', cover_wh=(1200, 630),
    facts=[('Client', 'Denis Ivankov, ID Chef'), ('Market', 'Latvia and abroad'), ('Languages', 'English, Latvian, Russian'), ('Leads', 'Contact form + WhatsApp')],
    task_h='Sell experience, not just a CV',
    task=['Restaurant owners hire a consultant when something is going wrong. They need to trust the person quickly and understand what he will actually do.',
          'The site had to tell a 30-year career story in a few screens and turn it into clear services and a way to get in touch.'],
    built_h='Story, services, approach, contact',
    built=[('Career story', 'A short path from line cook to consultant, with the formats and projects behind it.'),
           ('Services', 'Restaurant launches, kitchen systems and consulting explained in plain terms.'),
           ('Approach', 'How he works with a team and an owner, so expectations are clear before the first call.'),
           ('Contact in three languages', 'A language switch and a contact form plus WhatsApp for quick questions.')],
    vis_h='Dark kitchen with a gold edge',
    vis='A near-black base with warm gold accents feels like a serious kitchen after service. A wide display face gives the name weight, and a neutral sans keeps the story readable.',
    fonts=('Unbounded', 'Noto Sans', 'Noto Sans'), gf='family=Unbounded:wght@700&family=Noto+Sans:wght@400;600',
    display_w='700', display_ls='-.01em',
    sample=('ID CHEF', 'From chaos to a profitable kitchen', 'Contact'),
    palette=[('#08080A','Background'), ('#1C1C20','Surfaces'), ('#E8E4DC','Text'), ('#C8A96E','Gold accent'), ('#B8341A','Ember red')],
    ink='#E8E4DC', logo_bg='#08080A', logo=None, mark_color='#C8A96E', dark_panel=True,
    gallery=['https://ik.imagekit.io/xwsgpirygo/id%20chef/IMG_1156.JPG?tr=w-500', 'https://ik.imagekit.io/xwsgpirygo/id%20chef/klubs%201.jpeg?tr=w-500',
             'https://ik.imagekit.io/xwsgpirygo/id%20chef/IMG_1163.JPG?tr=w-500', 'https://ik.imagekit.io/xwsgpirygo/id%20chef/IMG_1160.JPG?tr=w-500'],
    gallery_alt='Chef Denis Ivankov at work', gallery_ratio='3/4',
    handover=['Live site in 3 languages', 'Contact form', 'WhatsApp link', 'Privacy and cookie notes', 'Link preview image'],
    cta=('Building a <span>personal</span> brand?', 'Tell us what you do and who hires you. We will turn your experience into a site that brings the right requests.'),
  ),
  dict(
    slug='grill-in', name='Grill In',
    url='http://grill-in.lv', host='grill-in.lv',
    title='Grill In case study: website for a grill bar and water park',
    desc='How we built a one-page site for Grill In in Jēkabpils: grill bar menu, takeaway orders, water park bookings and directions.',
    h1='One page for a grill bar, takeaway and a <span>water park</span>',
    tags=['Restaurant', 'Jēkabpils', 'One-page site', 'Takeaway + bookings'],
    lede='Grill In is a grill bar by the lake in Mežaparks, Jēkabpils, with a wide menu, takeaway and an inflatable water park on the lake.',
    cover='https://ik.imagekit.io/erewhile/erewhile/portfolio/4.jpg', cover_wh=(1600, 900),
    facts=[('Client', 'Grill In'), ('Market', 'Jēkabpils, Latvia'), ('Format', 'One-page site'), ('Actions', 'Takeaway, booking, directions')],
    task_h='Three businesses, one simple page',
    task=['A restaurant, a takeaway and a water park attract different visitors with different questions: what is on the menu, when can I pick up, how do I book.',
          'The site had to answer all three without becoming confusing on a phone.'],
    built_h='Clear sections for each reason to visit',
    built=[('Grill bar', 'Menu highlights and the lakeside atmosphere.'),
           ('Takeaway', 'Open the menu, choose dishes and set a pickup time.'),
           ('Water park', 'What the park offers and a booking call to action.'),
           ('Location', 'Map, free parking and directions to Mežaparks.')],
    vis_h='Coal, ember and gold',
    vis='Dark coal backgrounds with ember orange and gold accents bring the feel of an open grill. A tall condensed display face for headings, a friendly sans for menus.',
    fonts=('Bebas Neue', 'DM Sans', 'DM Sans'), gf='family=Bebas+Neue&family=DM+Sans:wght@400;600',
    display_w='400', display_ls='.04em',
    sample=('GRILL IN', 'Grill bar by the lake', 'Take away'),
    palette=[('#0E0D0B','Coal background'), ('#2A2720','Surfaces'), ('#C8410A','Ember orange'), ('#F5A623','Gold'), ('#F5F4F0','Light text')],
    ink='#F0EEE8', logo_bg='#0E0D0B', logo=None, mark_color='#F5A623', dark_panel=True,
    gallery=[], gallery_alt='', gallery_ratio='4/3',
    handover=['Live website', 'Menu section', 'Takeaway flow', 'Water park booking', 'Map and directions'],
    cta=('Running a <span>venue</span> with more than one offer?', 'Tell us what people come for. We will give each reason a clear path on one site.'),
  ),
]

HEADER = '''<header>
  <div class="wrap hdr">
    <a class="brand" href="/"><img src="https://ik.imagekit.io/erewhile/erewhile/logo%20erewhile.png?updatedAt=1777367873874" alt="Erewhile Digital">erewhile.digital</a>
    <nav><a href="/">Websites</a><a href="/portfolio" class="active">Portfolio</a><a href="/video">Video</a><a href="/#ew-contact">Contact</a></nav>
    <a class="btn btn-teal btn-sm" href="/#ew-contact">Get a quote</a>
    <button class="burger" id="burgerBtn" aria-label="Open menu" aria-expanded="false" aria-controls="mobileNav"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="mobile-nav" id="mobileNav" aria-label="Mobile navigation">
  <a href="/">Websites</a>
  <a href="/portfolio" class="active">Portfolio</a>
  <a href="/video">Video</a>
  <a href="/#ew-contact">Contact</a>
</div>'''

SCRIPT = '''<script>
(function(){var els=document.querySelectorAll('.reveal');if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('on')});return}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}})},{threshold:.12});
els.forEach(function(e){io.observe(e)})})();
(function(){var b=document.getElementById('burgerBtn'),n=document.getElementById('mobileNav');b.addEventListener('click',function(){var o=b.classList.toggle('open');n.classList.toggle('open',o);b.setAttribute('aria-expanded',o);document.body.style.overflow=o?'hidden':''})})();
(function(){if(matchMedia('(prefers-reduced-motion:reduce)').matches)return;document.querySelectorAll('[data-slides]').forEach(function(box){var s=box.children,i=0;if(s.length<2)return;
setInterval(function(){s[i].classList.remove('on');i=(i+1)%s.length;s[i].classList.add('on')},4200)})})();
</script>'''


def luminance(hexc):
  r, g, b = (int(hexc.lstrip('#')[i:i + 2], 16) / 255 for i in (0, 2, 4))
  return .2126 * r + .7152 * g + .0722 * b


def font_stack(name):
  serif = any(w in name for w in ('Garamond', 'Playfair', 'Fraunces', 'Cinzel', 'Serif'))
  return "'%s',%s" % (name, 'Georgia,serif' if serif else 'system-ui,sans-serif')


def abs_url(u):
  return u if u.startswith('http') else SITE + u


def page(c, nxt):
  e = html.escape
  d, b, u = c['fonts']
  gf = 'family=Montserrat:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500' + ('&' + c['gf'] if c['gf'] else '')
  dark = c.get('dark_panel')
  vars_ = ('--c-display:%s;--c-body:%s;--c-ui:%s;--c-display-w:%s;--c-display-ls:%s;--c-ink:%s;--c-logo-bg:%s;--c-mark:%s;--c-ui-color:%s'
           % (font_stack(d), font_stack(b), font_stack(u), c['display_w'], c['display_ls'], c['ink'], c['logo_bg'], c.get('mark_color', c['ink']),
              'rgba(255,255,255,.6)' if dark else '#8a8a8a'))
  panel_bg = c['logo_bg'] if dark else '#fff'
  ld = {"@context": "https://schema.org", "@type": "CreativeWork", "name": c['name'] + ' — case study', "url": SITE + '/portfolio/%s/' % c['slug'],
        "about": c['desc'], "creator": {"@id": SITE + "/#org"}, "image": abs_url(c['cover']), "isBasedOn": c['url']}
  tags = ''.join('<span class="tag%s">%s</span>' % (' new' if i == 0 and c.get('new') else '', t)
                 for i, t in enumerate((['New'] if c.get('new') else []) + c['tags']))
  facts = ''.join('<div class="fact"><dt>%s</dt><dd>%s</dd></div>' % (k, v) for k, v in c['facts'])
  task = ''.join('<p>%s</p>' % p for p in c['task'])
  built = ''.join('<div class="item"><b>%s</b><span>%s</span></div>' % x for x in c['built'])
  if c.get('logo'):
    w, h = c.get('logo_wh', (None, None))
    wh = ' width="%d" height="%d"' % (w, h) if w else ''
    logo = '<img src="%s" alt="%s logo" loading="lazy"%s>' % (c['logo'], e(c['name']), wh)
  else:
    logo = '<span class="bp-mark">%s</span>' % e(c['sample'][0])
  kanji = '<span class="kanji" aria-hidden="true">%s</span>' % c['kanji'] if c.get('kanji') else ''
  sw = ''.join('<div class="sw" style="background:%s;color:%s"><b>%s</b><span>%s</span></div>' % (x, '#fff' if luminance(x) < .45 else '#111', e(r), x)
               for x, r in c['palette'])
  fonts = []  # one card per font family, with every role it plays
  for role, fam, cls, smp in (('Headings', d, 'f-display', c['sample'][0]), ('Body text', b, 'f-body', c['sample'][1]), ('Buttons and labels', u, 'f-ui', c['sample'][2])):
    for f in fonts:
      if f[1] == fam:
        f[0].append(role.lower()); break
    else:
      fonts.append(([role], fam, cls, smp))
  type_cards = ''.join(
    '<div class="sh-cell sh-font"><div class="sh-cap"><span>%s</span><span>%s</span></div>'
    '<div class="sh-row"><span class="sh-aa %s">Aa</span><span class="%s sh-smp">%s</span></div></div>'
    % (e(' · '.join(r)), e(fam), cls, cls, e(smp)) for r, fam, cls, smp in fonts)
  gallery = ''
  if c['gallery']:
    gallery = '<div class="gallery">%s</div>' % ''.join(
      '<img src="%s" alt="%s" loading="lazy" style="aspect-ratio:%s">' % (g, e(c['gallery_alt']), c['gallery_ratio']) for g in c['gallery'])
  handover = ''.join('<li>%s</li>' % h for h in c['handover'])
  cw, ch = c['cover_wh']
  st = STAGES.get(c['slug'])
  if st:
    hero = (f'''<a class="stage st-{c['slug']} reveal" href="{c['url']}" target="_blank" rel="noopener" style="--ratio:{st['ratio']};--mratio:{st['mratio']}" aria-label="First screen of {c['host']}, rebuilt from the site code. Opens the live site">
    <div class="st-in" aria-hidden="true">{st['html']}
    </div>
    <span class="st-open">{c['host']} ↗</span>
  </a>
  <p class="stage-cap reveal"><span>The first screen of {c['host']}, rebuilt from the site's own code: fonts, colours and layout.</span></p>''')
  else:
    hero = '<figure class="shot reveal"><img src="%s" alt="%s website preview" loading="eager" width="%d" height="%d"></figure>' % (c['cover'], e(c['name']), cw, ch)
  return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <link rel="apple-touch-icon" sizes="180x180" href="https://res.cloudinary.com/da4ctmwz5/image/upload/v1770636900/apple-touch-icon_xewslz.png">
  <link rel="icon" type="image/png" sizes="32x32" href="https://res.cloudinary.com/da4ctmwz5/image/upload/v1770636904/favicon-32x32_zujayz.png">
  <link rel="icon" href="https://res.cloudinary.com/da4ctmwz5/image/upload/v1770636907/favicon_u65czo.ico">
  <title>{e(c['title'])} — Erewhile Digital</title>
  <meta name="description" content="{e(c['desc'])}"/>
  <link rel="canonical" href="{SITE}/portfolio/{c['slug']}/"/>
  <meta property="og:title" content="{e(c['name'])} case study — Erewhile Digital"/>
  <meta property="og:description" content="{e(c['desc'])}"/>
  <meta property="og:image" content="{abs_url(c['cover'])}"/>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?{gf}&display=swap" rel="stylesheet">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
  <style>
{STYLE}{stage_css(c['slug'])}
    .case{{{vars_}}}
  </style>
</head>
<body>
{HEADER}

<main class="wrap case">
  <div class="crumbs"><a href="/portfolio">Portfolio</a> / {e(c['name'])}</div>

  <section class="intro">
    <div>
      <h1>{c['h1']}</h1>
      <div class="tags">{tags}</div>
    </div>
    <div>
      <p class="lede">{c['lede']}</p>
      <div class="actions"><a class="btn btn-teal" href="{c['url']}" target="_blank" rel="noopener">Open {c['host']} ↗</a><a class="btn btn-ghost" href="/#ew-contact">Discuss a similar site</a></div>
    </div>
  </section>

  {hero}

  <dl class="facts reveal">{facts}</dl>

  <section class="block reveal">
    <div><div class="label">The task</div><h2>{c['task_h']}</h2></div>
    <div class="body">{task}</div>
  </section>

  <section class="block reveal">
    <div><div class="label">What we built</div><h2>{c['built_h']}</h2></div>
    <div class="body"><div class="list">{built}</div></div>
  </section>

  <section class="block reveal">
    <div><div class="label">Visual language</div><h2>{c['vis_h']}</h2></div>
    <div class="body wide">
      <p>{c['vis']}</p>
      <div class="sheet{' dark' if dark else ''}" style="--n:{len(fonts)}">
        <div class="sh-cell sh-logo"><div class="sh-cap"><span>Logo</span></div>{kanji}{logo}</div>
        {type_cards}
        <div class="sh-palette">{sw}</div>
      </div>
      {gallery}
    </div>
  </section>

  <section class="block reveal">
    <div><div class="label">Handed over</div><h2>What the client got at launch</h2></div>
    <div class="body"><ul class="handover">{handover}</ul></div>
  </section>

  <div class="next"><a href="/portfolio">← All projects</a><span>Next case: <a href="/portfolio/{nxt['slug']}/">{e(nxt['name'])} →</a></span></div>

  <section class="cta reveal">
    <h2>{c['cta'][0]}</h2>
    <p>{c['cta'][1]}</p>
    <a class="btn" href="/#ew-contact">Start a project</a>
  </section>

  <footer><span>© Erewhile Digital · Latvia</span><span><a href="mailto:web@erewhile.digital">web@erewhile.digital</a></span></footer>
</main>

{SCRIPT}
</body>
</html>
'''


if __name__ == '__main__':
  for i, c in enumerate(CASES):
    out = os.path.join(ROOT, 'portfolio', c['slug'], 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(page(c, CASES[(i + 1) % len(CASES)]))
    print('built', os.path.relpath(out, ROOT))
