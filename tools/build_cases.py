"""Build portfolio case pages: python3 -I tools/build_cases.py

Writes portfolio/<slug>/index.html for every case in CASES, in this order
(the order also drives the "Next case" link). Shared styles live in
tools/case_style.css. Texts are English; client visuals are hot-linked
from the clients' own ImageKit folders or copied into assets/cases/<slug>/.
"""
import html, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from case_stages import STAGES, stage_css
import importlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://erewhile.digital'
STYLE = open(os.path.join(ROOT, 'tools', 'case_style.css'), encoding='utf-8').read()

CASES = [
  dict(
    slug='outland',
    store=True,
    name='Outland Miniatures',
    new=True,
    url='https://outlandminiatures.com',
    host='outlandminiatures.com',
    title='Outland Miniatures case study: WooCommerce store and 1 500 products moved from Etsy',
    desc='How we built a WordPress and WooCommerce store for Outland Miniatures, a Latvian maker of resin miniatures, and moved about 1 500 products from their Etsy shop with photos, variations and prices.',
    h1='A miniatures brand’s own store, with <span>1 500</span> products moved from Etsy',
    tags=['Online store', 'Latvia · worldwide', 'WooCommerce', 'Moved from Etsy'],
    lede='Outland Miniatures prints resin miniatures in Latvia: busts, terrain, heroes and monsters for D&D players, wargamers and display painters. The shop sold on Etsy and wanted its own store next to it, with the whole catalogue in one place.',
    cover='https://ik.imagekit.io/erewhile/erewhile/portfolio/om%20pic.jpg?tr=w-1600',
    cover_wh=(1200, 630),
    facts=[('Client', 'Outland Miniatures, Latvia'), ('Market', 'Worldwide shipping'), ('Platform', 'WordPress + WooCommerce'), ('Catalogue', 'About 1 500 products from Etsy')],
    task_h='Move a large catalogue without losing anything',
    task=['The catalogue had grown on Etsy over years: about 1 500 listings, each with several photos, sizes and options. Rebuilding it by hand in a new store would have taken months.', 'The new store had to keep every product with its photos and variations, sort them into clear categories and handle payment and shipping worldwide, while the Etsy shop kept working.'],
    built_h='A store with the full catalogue from day one',
    built=[('Catalogue moved from Etsy', 'About 1 500 products exported from Etsy, cleaned up and imported into WooCommerce with photos, variations and prices.'), ('Categories and filters', 'Pin-ups, terrain, busts, dragons, monsters and collections, with filters so buyers find a model fast.'), ('Payment and shipping', 'Checkout with online payment, tracked worldwide shipping and a free shipping threshold.'), ('Gifts and loyalty', 'Free mystery minis at set order amounts, a wishlist and a newsletter discount for the first order.')],
    vis_h='Grimdark fantasy on a dark stage',
    vis='Dark hero art and gold buttons set a grimdark mood, while light parchment sections keep the catalogue easy to browse. The two alternate down the page. Merriweather gives the headlines a fantasy-book feel, and Inter keeps prices, filters and checkout clear.',
    fonts=('Merriweather', 'Inter', 'Inter'),
    gf='family=Merriweather:wght@400;700&family=Inter:wght@400;500;600;700',
    display_w='700',
    display_ls='0',
    sample=('Your Journey Into Grimdark & Fantasy', 'Busts, terrain and heroes, crafted in resin and made to order.', 'Shop miniatures'),
    palette=[('#16130F', 'Dark ground'), ('#BB8630', 'Gold'), ('#64481E', 'Bronze lines'), ('#F5F0EA', 'Parchment'), ('#1E1A15', 'Text')],
    ink='#F5F0EA',
    logo_bg='#0E0C0A',
    logo='/assets/cases/outland/logo-white.png',
    logo_wh=(None, None),
    mark_color='#BB8630',
    dark_panel=True,
    gallery=['/assets/cases/outland/mini-1.jpg', '/assets/cases/outland/mini-2.jpg', '/assets/cases/outland/mini-3.jpg', '/assets/cases/outland/mini-4.jpg'],
    gallery_alt='Resin miniature from the Outland catalogue',
    gallery_ratio='1/1',
    handover=['Live WooCommerce store', 'About 1 500 products moved', 'Payment and shipping set up', 'Categories and filters', 'Wishlist and newsletter'],
    cta=('Selling on <span>Etsy</span> and want your own store?', 'Tell us how big your catalogue is and where you sell today. We will plan the move so nothing gets lost.'),
  ),
  dict(
    slug='oro', name='ORO Studio',
    url='https://orostudiotallinn.com', host='orostudiotallinn.com',
    title='ORO Studio case study: booking website for an event studio in Tallinn',
    desc='How we built an Estonian and Russian site for ORO Studio, a cosy event space in the centre of Tallinn: hourly rental, turnkey parties and a booking calendar linked to the studio’s Google Calendar.',
    h1='A studio site where guests <span>book</span> the date themselves',
    tags=['Event space', 'Tallinn', 'ET · RU', 'Booking calendar'],
    lede='ORO Studio is a small event space in the heart of Tallinn for up to 15 people. Experts rent it for workshops, consultations and women’s circles, and friends book it for birthdays and bachelorette parties, with or without a ready programme.',
    cover='/assets/cases/oro/cover.jpg', cover_wh=(1200, 630),
    facts=[('Client', 'ORO Studio, Tallinn'), ('Market', 'Tallinn, Estonia'), ('Languages', 'Estonian, Russian'), ('Booking', 'Calendar + email + invoice')],
    task_h='Fewer messages, more bookings',
    task=['Every rental started with the same chat: is the studio free that evening, how much is it for ten people, what is included. Answering it by hand took time and dates were easy to mix up.',
          'The site had to show the atmosphere, explain two very different offers (renting the space and a turnkey party) and let people pick a free time on their own.'],
    built_h='From first look to a booked evening',
    built=[('Booking calendar', 'Free hours come from the studio’s Google Calendar. A request blocks the time at once and arrives by email, with an invoice for the rent.'),
           ('Clear hourly prices', 'Three rates by group size, and the calendar shows the rent for the chosen hours before sending.'),
           ('Turnkey parties', 'Four hours in the studio with one of eight programmes, from making your own perfume to painting on canvas.'),
           ('Two languages, fast and private', 'Estonian and Russian versions, booking terms, FAQ and structured data. Fonts are hosted on the site, so it needs no cookie banner.')],
    vis_h='Ivory, olive and a golden flower of life',
    vis='Warm ivory and deep olive keep the studio calm, and gold comes from the real ORO logo. A soft light slowly travels along the gold lines of the logo on the first screen. An elegant serif for headlines, Montserrat for prices and the calendar.',
    fonts=('Cormorant Garamond', 'Montserrat', 'Montserrat'), gf='family=Cormorant+Garamond:ital,wght@0,500;1,500',
    display_w='500', display_ls='0',
    sample=('Ruum, kus on hea kokku saada', 'Hubane stuudio kohtumisteks ja töötubadeks.', 'Broneeri stuudio'),
    palette=[('#F7F3EC','Ivory background'), ('#4F5A3D','Deep olive'), ('#6F7A56','Olive'), ('#B08A45','Gold'), ('#3A3428','Text')],
    ink='#3A3428', logo_bg='#F7F3EC', logo='/assets/cases/oro/logo.webp', logo_wh=(360, 360),
    gallery=['/assets/cases/oro/perfume.jpg', '/assets/cases/oro/candles.jpg', '/assets/cases/oro/painting.jpg', '/assets/cases/oro/birthday-table.jpg'],
    gallery_alt='ORO Studio event', gallery_ratio='3/4',
    handover=['Live site in 2 languages', 'Booking calendar', 'Request emails and invoices', 'Booking terms and privacy', 'Sitemap, schema and llms.txt'],
    cta=('Renting out a <span>space</span>?', 'Tell us how people book you today. We will build a calendar that fills the free hours without the back-and-forth.'),
  ),
  dict(
    slug='zemits', store=True, name='Zemits',
    url='https://zemits-latvija.lv', host='zemits-latvija.lv',
    title='Zemits case study: three-language catalogue for a cosmetology equipment distributor',
    desc='How we built a Latvian, Russian and English site with a device catalogue, training and service pages for Zemits Skin Expert, the official Zemits representative in the Baltics.',
    h1='A three-language catalogue of <span>professional</span> beauty equipment',
    tags=['Beauty equipment', 'Latvia &amp; Baltics', 'LV · RU · EN', 'Device catalogue'],
    lede='Zemits Skin Expert is the official Zemits representative in the Baltic states. They sell professional face and body devices to salons, clinics and specialists, and back them with training, a 24-month warranty and local service.',
    cover='/assets/cases/zemits/cover.jpg', cover_wh=(1200, 630),
    facts=[('Client', 'Zemits Skin Expert'), ('Market', 'Latvia and the Baltics'), ('Languages', 'Latvian, Russian, English'), ('Catalogue', 'Devices with prices and details')],
    task_h='Help salons compare devices worth thousands of euros',
    task=['Salon owners and cosmetologists do not buy a laser or an RF platform on impulse. They compare technologies, prices and what support they get after the purchase.',
          'The site had to present the whole device range in three languages, show real treatment results and make it easy to ask a question or book training.'],
    built_h='From first look to a request',
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
    cta=('Is your product hard to <span>explain</span> in one sentence?', 'Tell us what you sell and who buys it. We will plan the pages that answer their questions before they call.'),
  ),
  dict(
    slug='kondo', store=True, name='Kondo',
    url='https://kondo.ee', host='kondo.ee',
    title='Kondo case study: website for a made-to-order clothing label',
    desc='How we built a one-page brand site with a pre-order bag for Kondo, an Estonian label making linen and ramie clothing to order.',
    h1='A brand site with <span>pre&#8209;orders</span> for linen outfits',
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
    cta=('Want to take orders <span>right on</span> your site?', 'Tell us how you take orders today. We will suggest the simplest site that fits, with a fixed price before work starts.'),
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
    task_h='Explain complex treatments clearly enough to book with confidence',
    task=['Treatments like RF microneedling or endospheres are hard to judge from a price list. Clients want to understand what the device does, whether it is safe, and who will do the procedure.',
          'The studio needed a site that feels as premium as the service and leads naturally to a booking.'],
    built_h='Technology, results and the team',
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
    slug='razalija', store=True, name='Razalija',
    url='https://razalija.lv', host='razalija.lv',
    title='Razalija case study: website for a flower shop in Riga',
    desc='How we built a Latvian and Russian site for Razalija, a florist in Mežaparks, Riga: bouquet gallery, delivery zones and ordering through WhatsApp.',
    h1='A flower shop site where ordering takes <span>minutes</span>',
    tags=['Florist', 'Riga', 'LV · RU', 'WhatsApp orders'],
    lede='Razalija is a florist in Mežaparks, Riga, with fresh bouquets, compositions for special occasions, custom orders and delivery across the city. Most customers order from a phone, often at the last minute.',
    cover='https://ik.imagekit.io/coworker/Razalija/raz%201.png?tr=w-1200,h-630,c-maintain_ratio', cover_wh=(1200, 630),
    facts=[('Client', 'Razalija flower shop'), ('Market', 'Riga, Latvia'), ('Languages', 'Latvian, Russian'), ('Ordering', 'Gallery + WhatsApp')],
    task_h='Make a last-minute bouquet easy to order from a phone',
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
    cta=('Want your prices to be <span>clear</span> at a glance?', 'Tell us about your offer. We will lay it out so people pick a plan instead of leaving.'),
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
    facts=[('Organisation', 'UNTU, youth NGO'), ('Audience', 'Young people 18–35, partners'), ('Format', 'Main site + project sections'), ('Sign-ups', 'Apply and partner forms')],
    task_h='One site for the organisation and all its projects',
    task=['An NGO speaks to several audiences at once: young people who want to join, partner organisations, and funders who need to see results.',
          'Each Erasmus+ project also needs its own space for programme, travel, participants and outputs that stays online after the project ends.'],
    built_h='The organisation first, then its projects',
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
    handed_h='What the organisation got at launch',
    gallery_alt='UNTU project moment', gallery_ratio='4/3',
    handover=['Live website', 'Project sections', 'Apply and partner forms', 'Privacy and terms', 'Sitemap'],
    cta=('Running an NGO or <span>Erasmus+</span> project?', 'Tell us about your project. We will plan pages for participants, partners and results that stay online after it ends.'),
  ),
  dict(
    slug='id-chef', name='ID Chef',
    url='https://idchef13.com', host='idchef13.com',
    title='ID Chef case study: personal brand website for a chef and restaurant consultant',
    desc='How we built a personal brand site in English, Latvian and Russian for Denis Ivankov, an executive chef and restaurant consultant with 30+ years of experience.',
    h1='A personal brand site for a chef who makes kitchens <span>profitable</span>',
    tags=['Personal brand', 'Riga', 'EN · LV · RU', 'Consulting'],
    lede='Denis Ivankov is an executive chef and restaurant consultant with more than 30 years in the industry. He launches restaurants from scratch and turns kitchen chaos into profitable systems.',
    cover='https://ik.imagekit.io/xwsgpirygo/id%20chef/logos/OG.png', cover_wh=(1200, 630),
    facts=[('Client', 'Denis Ivankov, ID Chef'), ('Market', 'Latvia and abroad'), ('Languages', 'English, Latvian, Russian'), ('Leads', 'Contact form + WhatsApp')],
    task_h='Show experience, not just a CV',
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
    task_h='Three offers, one simple page',
    task=['A restaurant, a takeaway and a water park attract different visitors with different questions: what is on the menu, when can I pick up, how do I book.',
          'The site had to answer all three without becoming confusing on a phone.'],
    built_h='A clear section for every reason to visit',
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

LANGS = ('en', 'lv', 'ru')


def pre(lang):
  return '' if lang == 'en' else '/' + lang


def header(lang='en', slug=None):
  """Site header for a case page. Language links point to the same case in the other languages."""
  t, p = UI[lang], pre(lang)
  alt = ''.join('<a href="%s/portfolio/%s/" hreflang="%s" lang="%s">%s</a>' % (pre(l), slug, l, l, l.upper())
                for l in LANGS if l != lang) if slug else ''
  malt = ''.join('<a href="%s/portfolio/%s/" hreflang="%s" lang="%s">%s</a>' % (pre(l), slug, l, l, UI[l]['lang_name'])
                 for l in LANGS if l != lang) if slug else ''
  return f'''<header>
  <div class="wrap hdr">
    <a class="brand" href="{p}/"><img src="https://ik.imagekit.io/erewhile/erewhile/logo%20erewhile.png?updatedAt=1777367873874" alt="Erewhile Digital">erewhile.digital</a>
    <nav><a href="{p}/">{t['nav_web']}</a><a href="{p}/portfolio/" class="active">{t['nav_port']}</a><a href="{p}/video/">{t['nav_video']}</a><a href="{p}/store-migration/">{t['nav_store']}</a><a href="{p}/#ew-contact">{t['nav_contact']}</a>{alt}</nav>
    <a class="btn btn-teal btn-sm" href="{p}/#ew-contact">{t['quote']}</a>
    <button class="burger" id="burgerBtn" aria-label="{t['menu']}" aria-expanded="false" aria-controls="mobileNav"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="mobile-nav" id="mobileNav" aria-label="Mobile navigation">
  <a href="{p}/">{t['nav_web']}</a>
  <a href="{p}/portfolio/" class="active">{t['nav_port']}</a>
  <a href="{p}/video/">{t['nav_video']}</a>
  <a href="{p}/store-migration/">{t['nav_store']}</a>
  <a href="{p}/#ew-contact">{t['nav_contact']}</a>
  {malt}
</div>'''


def alternates(slug):
  """hreflang links for a case that exists in all three languages."""
  return ''.join('  <link rel="alternate" hreflang="%s" href="%s%s/portfolio/%s/"/>\n' % (l, SITE, pre(l), slug) for l in LANGS) + \
         '  <link rel="alternate" hreflang="x-default" href="%s/portfolio/%s/"/>\n' % (SITE, slug)


UI = {
  'en': dict(lang_name='English', nav_web='Websites', nav_port='Portfolio', nav_video='Video', nav_store='Online stores', nav_contact='Contact',
             quote='Get a quote', menu='Open menu', new='New', open='Open', discuss='Discuss a similar site', task='The task', built='What we built',
             visual='Visual language', logo='Logo', roles=('Headings', 'Body text', 'Buttons and labels'), handed='Handed over',
             handed_h='What the client got at launch', all='← All projects', next='Next case:', start='Start a project',
             store='Online stores &amp; Etsy migration →', footer='© Erewhile Digital · Latvia', case_study='case study',
             stage_cap="The first screen of {host}, rebuilt from the site's own code: fonts, colours and layout.",
             stage_aria='First screen of {host}, rebuilt from the site code. Opens the live site', preview='website preview', logo_alt='logo'),
}
for _l in LANGS[1:]:
  UI[_l] = importlib.import_module('i18n.cases_' + _l).UI

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


def service_btn(c, lang='en'):
  """E-commerce cases link to the online store service page."""
  return '<a class="btn alt" href="%s/store-migration/">%s</a>' % (pre(lang), UI[lang]['store']) if c.get('store') else ''


def localize(c, lang):
  """The case with its texts in another language (tools/i18n/cases_<lang>.py); palette roles are given as a list."""
  if lang == 'en':
    return c
  tr = dict(importlib.import_module('i18n.cases_' + lang).CASES[c['slug']])
  roles = tr.pop('palette', None)
  out = dict(c, **tr)
  if roles:
    assert len(roles) == len(c['palette']), c['slug']
    out['palette'] = [(x, r) for (x, _), r in zip(c['palette'], roles)]
  return out


def page(c, nxt, lang='en'):
  e = html.escape
  t, p = UI[lang], pre(lang)
  c = localize(c, lang)
  d, b, u = c['fonts']
  gf = 'family=Montserrat:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500' + ('&' + c['gf'] if c['gf'] else '')
  dark = c.get('dark_panel')
  vars_ = ('--c-display:%s;--c-body:%s;--c-ui:%s;--c-display-w:%s;--c-display-ls:%s;--c-ink:%s;--c-logo-bg:%s;--c-mark:%s;--c-ui-color:%s'
           % (font_stack(d), font_stack(b), font_stack(u), c['display_w'], c['display_ls'], c['ink'], c['logo_bg'], c.get('mark_color', c['ink']),
              'rgba(255,255,255,.6)' if dark else '#8a8a8a'))
  panel_bg = c['logo_bg'] if dark else '#fff'
  ld = {"@context": "https://schema.org", "@type": "CreativeWork", "name": c['name'] + ' — ' + t['case_study'], "url": SITE + p + '/portfolio/%s/' % c['slug'],
        "about": c['desc'], "creator": {"@id": SITE + "/#org"}, "image": abs_url(c['cover']), "isBasedOn": c['url'], "inLanguage": lang}
  tags = ''.join('<span class="tag%s">%s</span>' % (' new' if i == 0 and c.get('new') else '', x)
                 for i, x in enumerate(([t['new']] if c.get('new') else []) + c['tags']))
  facts = ''.join('<div class="fact"><dt>%s</dt><dd>%s</dd></div>' % (k, v) for k, v in c['facts'])
  task = ''.join('<p>%s</p>' % p for p in c['task'])
  built = ''.join('<div class="item"><b>%s</b><span>%s</span></div>' % x for x in c['built'])
  if c.get('logo'):
    w, h = c.get('logo_wh', (None, None))
    wh = ' width="%d" height="%d"' % (w, h) if w else ''
    logo = '<img src="%s" alt="%s %s" loading="lazy"%s>' % (c['logo'], e(c['name']), t['logo_alt'], wh)
  else:
    logo = '<span class="bp-mark">%s</span>' % e(c['sample'][0])
  kanji = '<span class="kanji" aria-hidden="true">%s</span>' % c['kanji'] if c.get('kanji') else ''
  sw = ''.join('<div class="sw" style="background:%s;color:%s"><b>%s</b><span>%s</span></div>' % (x, '#fff' if luminance(x) < .45 else '#111', e(r), x)
               for x, r in c['palette'])
  fonts = []  # one card per font family, with every role it plays
  r1, r2, r3 = t['roles']
  for role, fam, cls, smp in ((r1, d, 'f-display', c['sample'][0]), (r2, b, 'f-body', c['sample'][1]), (r3, u, 'f-ui', c['sample'][2])):
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
    hero = (f'''<a class="stage st-{c['slug']} reveal" href="{c['url']}" target="_blank" rel="noopener" style="--ratio:{st['ratio']};--mratio:{st['mratio']}" aria-label="{t['stage_aria'].format(host=c['host'])}">
    <div class="st-in" aria-hidden="true">{st['html']}
    </div>
    <span class="st-open">{c['host']} ↗</span>
  </a>
  <p class="stage-cap reveal"><span>{t['stage_cap'].format(host=c['host'])}</span></p>''')
  else:
    hero = '<figure class="shot reveal"><img src="%s" alt="%s %s" loading="eager" width="%d" height="%d"></figure>' % (c['cover'], e(c['name']), t['preview'], cw, ch)
  return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <link rel="apple-touch-icon" sizes="180x180" href="https://res.cloudinary.com/da4ctmwz5/image/upload/v1770636900/apple-touch-icon_xewslz.png">
  <link rel="icon" type="image/png" sizes="32x32" href="https://res.cloudinary.com/da4ctmwz5/image/upload/v1770636904/favicon-32x32_zujayz.png">
  <link rel="icon" href="https://res.cloudinary.com/da4ctmwz5/image/upload/v1770636907/favicon_u65czo.ico">
  <title>{e(c['title'])} — Erewhile Digital</title>
  <meta name="description" content="{e(c['desc'])}"/>
  <link rel="canonical" href="{SITE}{p}/portfolio/{c['slug']}/"/>
{alternates(c['slug'])}  <meta property="og:title" content="{e(c['name'])} {t['case_study']} — Erewhile Digital"/>
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
  <script defer src="https://cloud.umami.is/script.js" data-website-id="05637fa8-68fc-4678-9073-128758979e4b"></script>
</head>
<body>
{header(lang, c['slug'])}

<main class="wrap case">
  <div class="crumbs"><a href="{p}/portfolio/">{t['nav_port']}</a> / {e(c['name'])}</div>

  <section class="intro">
    <div>
      <h1>{c['h1']}</h1>
      <div class="tags">{tags}</div>
    </div>
    <div>
      <p class="lede">{c['lede']}</p>
      <div class="actions"><a class="btn btn-teal" href="{c['url']}" target="_blank" rel="noopener">{t['open']} {c['host']} ↗</a><a class="btn btn-ghost" href="{p}/#ew-contact">{t['discuss']}</a></div>
    </div>
  </section>

  {hero}

  <dl class="facts reveal">{facts}</dl>

  <section class="block reveal">
    <div><div class="label">{t['task']}</div><h2>{c['task_h']}</h2></div>
    <div class="body">{task}</div>
  </section>

  <section class="block reveal">
    <div><div class="label">{t['built']}</div><h2>{c['built_h']}</h2></div>
    <div class="body"><div class="list">{built}</div></div>
  </section>

  <section class="block reveal">
    <div><div class="label">{t['visual']}</div><h2>{c['vis_h']}</h2></div>
    <div class="body wide">
      <p>{c['vis']}</p>
      <div class="sheet{' dark' if dark else ''}" style="--n:{len(fonts)}">
        <div class="sh-cell sh-logo"><div class="sh-cap"><span>{t['logo']}</span></div>{kanji}{logo}</div>
        {type_cards}
        <div class="sh-palette">{sw}</div>
      </div>
      {gallery}
    </div>
  </section>

  <section class="block reveal">
    <div><div class="label">{t['handed']}</div><h2>{c.get('handed_h', t['handed_h'])}</h2></div>
    <div class="body"><ul class="handover">{handover}</ul></div>
  </section>

  <div class="next"><a href="{p}/portfolio/">{t['all']}</a><span>{t['next']} <a href="{p}/portfolio/{nxt['slug']}/">{e(nxt['name'])} →</a></span></div>

  <section class="cta reveal">
    <h2>{c['cta'][0]}</h2>
    <p>{c['cta'][1]}</p>
    <a class="btn" href="{p}/#ew-contact">{t['start']}</a>{service_btn(c, lang)}
  </section>

  <footer><span>{t['footer']}</span><span><a href="mailto:web@erewhile.digital">web@erewhile.digital</a></span></footer>
</main>

{SCRIPT}
</body>
</html>
'''

# ── Knowledge base: the FTS library gets its own page layout ──────────────────
# NGO / Erasmus+ work: no commercial wording (no "client", "case", "order").
KB_STYLE = open(os.path.join(ROOT, 'tools', 'kb_style.css'), encoding='utf-8').read()
LIB = 'https://untu.ngo/projects/'
KB = dict(
  slug='fts-library', name='FTS Library',
  url=LIB + 'fts-library', host='untu.ngo',
  title='FTS Library: a knowledge base for youth workers',
  desc='How we designed the From Thinking to Speaking library: a knowledge base of presentations, guides and an interactive bias map for youth workers from six countries, made for an Erasmus+ training course by Biedrība UNTU.',
  cover='/assets/cases/fts-library/cover.jpg',
  topics=['Critical Thinking', 'Media Literacy', 'Public Speaking', 'Podcasting', 'Create &amp; Share', 'Youth Work'],
  # (topic, link, image, kind, title, text, wide)
  materials=[
    ('Critical Thinking', 'fts-bias-map', 'bias-map', 'Interactive map · 40 biases', 'Cognitive Bias Map', '40 cognitive biases around one brain, grouped like Buster Benson’s Cognitive Bias Codex and marked by how well the research holds up. Three views, filters by evidence and effect.', True),
    ('Critical Thinking', 'fts-biases-chapter-0/', 'biases-chapter-0', 'Presentation · 14 slides', 'Biases 0: What Is a Bias', 'An eyes-closed experiment, three quick quizzes, fast and slow thinking.', False),
    ('Critical Thinking', 'fts-biases-chapter-1/', 'biases-chapter-1', 'Presentation · 18 slides', 'Biases 1: Filter', 'Confirmation bias, anchoring, framing, availability and priming.', False),
    ('Critical Thinking', 'fts-biases-chapter-2/', 'biases-chapter-2', 'Presentation · 13 slides', 'Biases 2: Filling the Gaps', 'Thirty coin flips and why one vivid story beats the statistics.', False),
    ('Critical Thinking', 'fts-biases-chapter-3/', 'biases-chapter-3', 'Presentation · 19 slides', 'Biases 3: People', 'Attribution error, false consensus, double standards and more.', False),
    ('Critical Thinking', 'fts-biases-chapter-4/', 'biases-chapter-4', 'Presentation · 19 slides', 'Biases 4: Persuasion', 'A speech with eight hidden tricks and a hunt through real quotes.', False),
    ('Media Literacy', 'fts-media-literacy/', 'media-literacy', 'Presentation · 25 slides', 'True, False, Framed', 'Fake or real: lateral reading and SIFT, reverse image search, AI-generated content, and how one true event becomes many different stories.', True),
    ('Media Literacy', 'fts-fact-checking', 'fact-checking', 'Guide · one page', 'Don’t Get Fooled', 'A fact-checking toolkit with fact-checkers from all six countries.', False),
    ('Public Speaking', 'https://colibrarian.github.io/fts-public-speaking-slides/', 'public-speaking', 'Presentation · 19 slides', 'How We Speak', 'From one story to a one-minute talk, with a built-in timer.', False),
    ('Podcasting', 'fts-audacity/', 'audacity', 'Presentation · 10 slides', 'Podcast Audio in Audacity', 'A free production pipeline, from noise cleanup to export.', False),
    ('Podcasting', 'fts-podcast-conduct/', 'podcast-conduct', 'Memo · one page', 'On Air Together', 'How to talk to each other while recording a podcast.', False),
    ('Create &amp; Share', 'fts-team-video/', 'team-video', 'Presentation · 11 slides', 'One Bias, One Video', 'Crew roles, script, phone settings, editing and publishing.', False),
    ('Youth Work', 'fts-experience-first/', 'experience-first', 'Presentation · 8 slides', 'Experience First', 'How the learning worked, to take home to your own groups.', False),
  ],
)


def kb_page(c, nxt):
  e = html.escape
  slides = sum(int(m[3].split('·')[1].split()[0]) for m in c['materials'] if m[3].startswith('Presentation'))
  decks = sum(1 for m in c['materials'] if m[3].startswith('Presentation'))
  tabs = '<button type="button" aria-pressed="true" data-t="all">All</button>' + ''.join(
    '<button type="button" aria-pressed="false" data-t="%d">%s</button>' % (i, t) for i, t in enumerate(c['topics']))
  mats = ''.join(
    '<a class="mat%s" data-t="%d" href="%s" target="_blank" rel="noopener"><img src="/assets/cases/fts-library/%s.jpg" alt="Cover of %s" loading="lazy" width="800" height="450">'
    '<div class="mat-b"><span class="mat-k">%s</span><span class="mat-t">%s</span><span class="mat-d">%s</span><span class="mat-go">Open ↗</span></div></a>'
    % (' wide' if w else '', c['topics'].index(t), l if l.startswith('http') else LIB + l, img, e(title), k, title, d)
    for t, l, img, k, title, d, w in c['materials'])
  vars_ = ("--c-display:'Bricolage Grotesque',system-ui,sans-serif;--c-body:'Figtree',system-ui,sans-serif;--c-ui:'JetBrains Mono',ui-monospace,monospace;"
           "--c-display-w:800;--c-display-ls:-.02em;--c-ink:#16181d;--c-logo-bg:#f5f4ee;--c-mark:#16181d;--c-ui-color:#7a7c84")
  fonts = [('Headings', 'Bricolage Grotesque', 'f-display', 'Speaking is a skill.'),
           ('Body text', 'Figtree', 'f-body', 'What do I notice, and what do I miss?'),
           ('Labels and navigation', 'JetBrains Mono', 'f-ui', 'Chapter 1 · Filter')]
  type_cards = ''.join(
    '<div class="sh-cell sh-font"><div class="sh-cap"><span>%s</span><span>%s</span></div>'
    '<div class="sh-row"><span class="sh-aa %s">Aa</span><span class="%s sh-smp">%s</span></div></div>' % (r, f, cls, cls, smp)
    for r, f, cls, smp in fonts)
  palette = [('#0B0B0A', 'Ink'), ('#F5F4EE', 'Paper'), ('#F2ECDD', 'Cream'),
             ('#FF4520', 'Signal red'), ('#3F7FE0', 'Chapter blue'), ('#FFCF3F', 'Highlight')]
  sw = ''.join('<div class="sw" style="background:%s;color:%s"><b>%s</b><span>%s</span></div>' % (x, '#fff' if luminance(x) < .45 else '#111', r, x)
               for x, r in palette)
  ld = {"@context": "https://schema.org", "@type": "CreativeWork", "name": c['title'], "url": SITE + '/portfolio/%s/' % c['slug'],
        "about": c['desc'], "creator": {"@id": SITE + "/#org"}, "image": abs_url(c['cover']), "isBasedOn": c['url'],
        "inLanguage": "en", "educationalUse": "Youth work", "audience": {"@type": "Audience", "audienceType": "Youth workers"}}
  gf = ('family=Montserrat:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&family=Anton'
        '&family=Space+Grotesk:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Figtree:wght@400;600')
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
  <meta property="og:title" content="{e(c['title'])} — Erewhile Digital"/>
  <meta property="og:description" content="{e(c['desc'])}"/>
  <meta property="og:image" content="{abs_url(c['cover'])}"/>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?{gf}&display=swap" rel="stylesheet">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
  <style>
{STYLE}{KB_STYLE}
    .case{{{vars_}}}
  </style>
  <script defer src="https://cloud.umami.is/script.js" data-website-id="05637fa8-68fc-4678-9073-128758979e4b"></script>
</head>
<body>
{header('en')}

<main class="wrap case kb">
  <div class="crumbs"><a href="/portfolio">Portfolio</a> / {e(c['name'])}</div>

  <section class="intro">
    <div>
      <h1>A knowledge base for youth work, designed as one <span>library</span></h1>
      <div class="tags"><span class="tag new">Knowledge base</span><span class="tag">Erasmus+</span><span class="tag">Youth work</span><span class="tag">6 countries</span></div>
    </div>
    <div>
      <p class="lede">From Thinking to Speaking is an Erasmus+ training course on critical thinking, media literacy, public speaking and podcasting, organised by the Latvian youth organisation Biedrība UNTU. We designed its library: every presentation, guide and tool from the course, sorted by topic and open to any youth worker.</p>
      <div class="actions"><a class="btn btn-teal" href="{c['url']}" target="_blank" rel="noopener">Open the library ↗</a><a class="btn btn-ghost" href="/#ew-contact">Plan a knowledge base</a></div>
    </div>
  </section>

  <a class="kb-shot reveal" href="{c['url']}" target="_blank" rel="noopener" aria-label="The FTS library on untu.ngo. Opens the live library">
    <picture><source media="(max-width:640px)" srcset="/assets/cases/fts-library/library-screen-m.jpg"><img src="/assets/cases/fts-library/library-screen.jpg" alt="The FTS library page: six topics and a cover for every material" width="1800" height="1125" loading="eager"></picture>
    <span class="st-open">untu.ngo/projects/fts-library ↗</span>
  </a>

  <div class="kb-stats reveal">
    <div class="kb-stat"><b>{len(c['topics'])}</b><span>topics, from critical thinking to youth work methods</span></div>
    <div class="kb-stat"><b>{len(c['materials'])}</b><span>materials, each with its own cover</span></div>
    <div class="kb-stat"><b>{slides}</b><span>slides in {decks} decks that open in any browser</span></div>
    <div class="kb-stat"><b>40</b><span>cognitive biases on one interactive map</span></div>
  </div>
  <dl class="facts reveal">
    <div class="fact"><dt>Organised by</dt><dd>Biedrība UNTU, Latvia</dd></div>
    <div class="fact"><dt>Programme</dt><dd>Erasmus+ KA153-YOU</dd></div>
    <div class="fact"><dt>Used by youth workers from</dt><dd>Latvia, Estonia, Norway, France, Spain, Romania</dd></div>
    <div class="fact"><dt>Format</dt><dd>Library, slide decks, guides, interactive map</dd></div>
  </dl>

  <section class="lib reveal" aria-labelledby="lib-h">
    <div class="lib-top">
      <div>
        <div class="lib-eyebrow"><i></i>From Thinking to Speaking · Library</div>
        <h2 id="lib-h">Inside the library</h2>
      </div>
      <p class="lib-sub">The highlights, in the library’s own style. Pick a topic, open any material: they are live on untu.ngo.</p>
    </div>
    <div class="lib-tabs" role="group" aria-label="Filter by topic">{tabs}</div>
    <div class="lib-grid" id="libGrid">{mats}</div>
    <div class="lib-foot"><span>Erasmus+ KA153-YOU · Vircava, Latvia · 2026</span><a href="{c['url']}" target="_blank" rel="noopener">The whole library ↗</a></div>
  </section>

  <section class="block reveal">
    <div><div class="label">The task</div><h2>Make a week of training useful for months</h2></div>
    <div class="body">
      <p>A training course lasts a week. Youth workers need its materials much longer: to run the same activity with their own groups, to check a fact, to remember how a method worked.</p>
      <p>Participants and partner organisations from six countries needed one place where everything from the course can be found again, on a phone or a projector, without logins or downloads.</p>
    </div>
  </section>

  <section class="block reveal">
    <div><div class="label">What we built</div><h2>A library, not a folder of files</h2></div>
    <div class="body"><div class="list">
      <div class="item"><b>Library by topic</b><span>Six topics, and every material has a cover, a type and a length, so people find it by sight instead of by file name.</span></div>
      <div class="item"><b>Interactive bias map</b><span>40 cognitive biases around one brain, each marked by how well the research supports it. Click any bias to read an example and the sources.</span></div>
      <div class="item"><b>Slide decks in the browser</b><span>One idea per screen, a chapter colour that shows where you are, arrow-key navigation and an overview of all slides. Nothing to install.</span></div>
      <div class="item"><b>One-page guides and memos</b><span>A fact-checking toolkit and a podcast conversation memo, short enough to print and keep at hand.</span></div>
      <div class="item"><b>Visibility kit</b><span>A ready caption and partner tags with copy buttons, so every post from the course carries the required Erasmus+ text.</span></div>
      <div class="item"><b>Part of the project site</b><span>The library is page six of the project’s site on untu.ngo, next to the programme, travel and preparation pages.</span></div>
    </div></div>
  </section>

  <section class="block reveal">
    <div><div class="label">Visual language</div><h2>Loud on the shelf, calm inside</h2></div>
    <div class="body wide">
      <p>The library speaks in tall Anton capitals on dark ink, like the spines on a shelf. Inside, the materials switch to a calmer system for reading on a big screen: Bricolage Grotesque headings, Figtree text and JetBrains Mono labels on light paper. One idea per screen, and colour tells you which chapter you are in.</p>
      <div class="sheet" style="--n:3">
        <div class="sh-cell sh-logo"><div class="sh-cap"><span>Mark</span></div><span class="bp-mark" style="font-family:var(--k-anton);font-weight:400;letter-spacing:.02em;background:#3f7fe0;color:#fbfbf6;padding:10px 22px;border-radius:14px;transform:rotate(-3deg);font-size:clamp(40px,5vw,60px)">FTS</span></div>
        {type_cards}
        <div class="sh-palette">{sw}</div>
      </div>
    </div>
  </section>

  <section class="block reveal">
    <div><div class="label">Tested in the room</div><h2>Designed by someone who also taught with it</h2></div>
    <div class="body"><div class="note">
      <p>The library and the materials were designed by Konstantin, the designer behind Erewhile Digital. He was also one of the trainers on the course, so the slides were tested in front of the group by the person who designed them.</p>
    </div></div>
  </section>

  <section class="block reveal">
    <div><div class="label">Stays online</div><h2>Open after the course ends</h2></div>
    <div class="body"><ul class="handover"><li>Library with {len(c['topics'])} topics</li><li>Interactive bias map</li><li>{decks} slide decks</li><li>2 one-page guides</li><li>Visibility kit</li><li>Open to any youth worker</li></ul></div>
  </section>

  <div class="next"><a href="/portfolio">← All projects</a><span>Next project: <a href="/portfolio/{nxt['slug']}/">{e(nxt['name'])} →</a></span></div>

  <section class="cta reveal">
    <h2>Have knowledge worth <span>keeping</span>?</h2>
    <p>Tell us about your course, training or project. We will turn its materials into a library people can open again long after it ends.</p>
    <a class="btn" href="/#ew-contact">Start a project</a>
  </section>

  <footer><span>© Erewhile Digital · Latvia</span><span><a href="mailto:web@erewhile.digital">web@erewhile.digital</a></span></footer>
</main>

{SCRIPT}
<script>
(function(){{var g=document.getElementById('libGrid'),bs=document.querySelectorAll('.lib-tabs button');bs.forEach(function(b){{b.addEventListener('click',function(){{
bs.forEach(function(x){{x.setAttribute('aria-pressed',x===b)}});var t=b.dataset.t;g.querySelectorAll('.mat').forEach(function(m){{m.hidden=!(t==='all'||m.dataset.t===t)}})}})}})}})();
</script>
</body>
</html>
'''


if __name__ == '__main__':
  for lang in LANGS:
    for i, c in enumerate(CASES):
      out = os.path.join(ROOT, pre(lang).strip('/'), 'portfolio', c['slug'], 'index.html')
      os.makedirs(os.path.dirname(out), exist_ok=True)
      open(out, 'w', encoding='utf-8').write(page(c, CASES[(i + 1) % len(CASES)], lang))
      print('built', os.path.relpath(out, ROOT))
  # the FTS library is an English-language resource for international youth workers: English only
  out = os.path.join(ROOT, 'portfolio', KB['slug'], 'index.html')
  os.makedirs(os.path.dirname(out), exist_ok=True)
  open(out, 'w', encoding='utf-8').write(kb_page(KB, CASES[0]))
  print('built', os.path.relpath(out, ROOT))
