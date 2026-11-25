/* Erewhile Digital — brief questions.
   One entry per site type in BRIEFS. To add a type (landing page, digital ecosystem...),
   add another key with the same shape; the type picker appears by itself once there are two.
   Every text is [English, Latvian, Russian]. Option answers reach the email in Russian.
   Question types: text, email, tel, textarea, radio (one answer), check (several answers).
   other: true adds a free "Other" field to radio/check questions. req: true makes it required. */
window.BRIEFS = {
  store: {
    title: ['Online store brief', 'Interneta veikala brīfs', 'Бриф на интернет-магазин'],
    sections: [
      { t: ['About you and the business', 'Par jums un uzņēmumu', 'О вас и бизнесе'], q: [
        { id: 'name', type: 'text', req: true, l: ['Your name', 'Jūsu vārds', 'Ваше имя'] },
        { id: 'brand', type: 'text', l: ['Brand or company name (if you have one)', 'Zīmola vai uzņēmuma nosaukums (ja ir)', 'Название бренда или компании (если есть)'] },
        { id: 'email', type: 'email', req: true, l: ['Email', 'E-pasts', 'Email'] },
        { id: 'phone', type: 'tel', l: ['Phone or WhatsApp', 'Tālrunis vai WhatsApp', 'Телефон или WhatsApp'] },
        { id: 'links', type: 'textarea', l: ['Current website or social media links', 'Esošā mājaslapa vai sociālo tīklu saites', 'Текущий сайт или ссылки на соцсети'] },
        { id: 'what', type: 'textarea', req: true, l: ['What do you sell?', 'Ko jūs pārdodat?', 'Что вы продаёте?'] },
        { id: 'who', type: 'textarea', l: ['Who are your customers?', 'Kas ir jūsu pircēji?', 'Кто ваши покупатели?'],
          h: ['Age, interests, where they live, how they find you now.', 'Vecums, intereses, kur dzīvo, kā jūs atrod tagad.', 'Возраст, интересы, где живут, как сейчас вас находят.'] },
        { id: 'refs', type: 'textarea', l: ['2–3 competitors or online stores you like', '2–3 konkurenti vai interneta veikali, kas jums patīk', '2–3 конкурента или интернет-магазина, которые вам нравятся'],
          h: ['Links, and what exactly you like about them.', 'Saites un tas, kas tieši jums patīk.', 'Ссылки и что именно в них нравится.'] },
      ]},
      { t: ['Products', 'Preces', 'Товары'], q: [
        { id: 'count', type: 'radio', req: true, l: ['How many products do you have now?', 'Cik preču jums ir tagad?', 'Сколько товаров у вас сейчас?'],
          o: [['Up to 20', 'Līdz 20', 'До 20'], ['20–100', '20–100', '20–100'], ['100–500', '100–500', '100–500'], ['More than 500', 'Vairāk nekā 500', 'Больше 500']] },
        { id: 'growth', type: 'text', l: ['How many do you expect in a year?', 'Cik preču plānojat pēc gada?', 'Сколько планируете через год?'] },
        { id: 'variants', type: 'check', other: true, l: ['Do products come in variants?', 'Vai precēm ir varianti?', 'Есть ли у товаров варианты?'],
          o: [['Size', 'Izmērs', 'Размер'], ['Colour', 'Krāsa', 'Цвет'], ['Material', 'Materiāls', 'Материал'], ['No variants', 'Nav variantu', 'Вариантов нет']] },
        { id: 'photos', type: 'radio', l: ['Product photos', 'Preču fotogrāfijas', 'Фото товаров'],
          o: [['Ready', 'Gatavas', 'Готовы'], ['Some are ready', 'Daļa ir gatava', 'Часть готова'], ['Need help with photos', 'Vajag palīdzību ar foto', 'Нужна помощь с фото']] },
        { id: 'texts', type: 'radio', l: ['Product descriptions', 'Preču apraksti', 'Описания товаров'],
          o: [['Ready', 'Gatavi', 'Готовы'], ['Some are ready', 'Daļa ir gatava', 'Часть готова'], ['Need help with texts', 'Vajag palīdzību ar tekstiem', 'Нужна помощь с текстами']] },
        { id: 'source', type: 'check', other: true, l: ['Where are your products listed now?', 'Kur jūsu preces ir tagad?', 'Где сейчас ваши товары?'],
          o: [['Nowhere yet', 'Vēl nekur', 'Пока нигде'], ['Excel or Google Sheets', 'Excel vai Google Sheets', 'Excel или Google Таблицы'], ['Etsy', 'Etsy', 'Etsy'], ['Shopify', 'Shopify', 'Shopify'], ['Wix', 'Wix', 'Wix'], ['Instagram or Facebook', 'Instagram vai Facebook', 'Instagram или Facebook']] },
      ]},
      { t: ['Languages and markets', 'Valodas un tirgi', 'Языки и рынки'], q: [
        { id: 'langs', type: 'check', req: true, other: true, l: ['Website languages', 'Mājaslapas valodas', 'Языки сайта'],
          o: [['Latvian', 'Latviešu', 'Латышский'], ['English', 'Angļu', 'Английский'], ['Russian', 'Krievu', 'Русский'], ['Lithuanian', 'Lietuviešu', 'Литовский'], ['Estonian', 'Igauņu', 'Эстонский']] },
        { id: 'markets', type: 'check', l: ['Where will you sell?', 'Kur pārdosiet?', 'Куда будете продавать?'],
          o: [['Latvia', 'Latvija', 'Латвия'], ['Baltic states', 'Baltijas valstis', 'Страны Балтии'], ['European Union', 'Eiropas Savienība', 'Евросоюз'], ['Worldwide', 'Visa pasaule', 'Весь мир']] },
        { id: 'currency', type: 'text', l: ['Currency (EUR or other)', 'Valūta (EUR vai cita)', 'Валюта (EUR или другая)'] },
      ]},
      { t: ['Payment and delivery', 'Apmaksa un piegāde', 'Оплата и доставка'], q: [
        { id: 'pay', type: 'check', other: true, l: ['How should customers pay?', 'Kā pircēji maksās?', 'Как покупатели будут платить?'],
          o: [['Bank card online', 'Ar karti tiešsaistē', 'Картой онлайн'], ['Bank link (Swedbank, SEB, Citadele...)', 'Bankas saite (Swedbank, SEB, Citadele...)', 'Через банк (Swedbank, SEB, Citadele...)'], ['Apple Pay / Google Pay', 'Apple Pay / Google Pay', 'Apple Pay / Google Pay'], ['PayPal', 'PayPal', 'PayPal'], ['Bank transfer by invoice', 'Pārskaitījums pēc rēķina', 'Перевод по счёту'], ['Cash on pickup', 'Skaidrā naudā, saņemot preci', 'Наличными при получении']] },
        { id: 'ship', type: 'check', other: true, l: ['Delivery options', 'Piegādes veidi', 'Способы доставки'],
          o: [['Omniva parcel lockers', 'Omniva pakomāti', 'Пакоматы Omniva'], ['DPD', 'DPD', 'DPD'], ['Latvijas Pasts', 'Latvijas Pasts', 'Latvijas Pasts'], ['Courier', 'Kurjers', 'Курьер'], ['Pickup', 'Saņemšana uz vietas', 'Самовывоз'], ['International shipping', 'Starptautiskā piegāde', 'Международная доставка']] },
        { id: 'vat', type: 'radio', l: ['Are you a VAT (PVN) payer?', 'Vai esat PVN maksātājs?', 'Вы плательщик НДС (PVN)?'],
          o: [['Yes', 'Jā', 'Да'], ['No', 'Nē', 'Нет'], ['Not sure', 'Nezinu', 'Не знаю']] },
        { id: 'invoice', type: 'radio', l: ['Do business customers need invoices from the store?', 'Vai uzņēmumiem vajag rēķinus no veikala?', 'Нужны ли счета для компаний-покупателей?'],
          o: [['Yes', 'Jā', 'Да'], ['No', 'Nē', 'Нет']] },
        { id: 'returns', type: 'radio', l: ['Returns and delivery terms', 'Atgriešanas un piegādes noteikumi', 'Условия возврата и доставки'],
          o: [['I have them written', 'Man tie ir uzrakstīti', 'Уже написаны'], ['Need help writing them', 'Vajag palīdzību tos uzrakstīt', 'Нужна помощь с текстом']] },
      ]},
      { t: ['Managing the store', 'Veikala pārvaldība', 'Управление магазином'], q: [
        { id: 'admin', type: 'radio', req: true, l: ['Who will update products, prices and texts?', 'Kas atjauninās preces, cenas un tekstus?', 'Кто будет обновлять товары, цены и тексты?'],
          o: [['We will, in an admin panel', 'Mēs paši, administrēšanas panelī', 'Мы сами, через админку'], ['We will send changes to Erewhile Digital', 'Izmaiņas sūtīsim Erewhile Digital', 'Будем присылать правки Erewhile Digital'], ['Not sure yet', 'Vēl nezinu', 'Пока не знаю']] },
        { id: 'often', type: 'radio', l: ['How often will things change?', 'Cik bieži būs izmaiņas?', 'Как часто будут изменения?'],
          o: [['Every week', 'Katru nedēļu', 'Каждую неделю'], ['Every month', 'Katru mēnesi', 'Каждый месяц'], ['Rarely', 'Reti', 'Редко']] },
        { id: 'team', type: 'text', l: ['How many people will work with the store?', 'Cik cilvēku strādās ar veikalu?', 'Сколько человек будут работать с магазином?'] },
      ]},
      { t: ['Design', 'Dizains', 'Дизайн'], q: [
        { id: 'logo', type: 'radio', l: ['Logo', 'Logotips', 'Логотип'],
          o: [['Have one', 'Ir', 'Есть'], ['Have one, but it needs an update', 'Ir, bet vajag atjaunot', 'Есть, но нужно обновить'], ['Need a new one', 'Vajag jaunu', 'Нужен новый']] },
        { id: 'style', type: 'radio', l: ['Brand colours and fonts', 'Zīmola krāsas un fonti', 'Фирменные цвета и шрифты'],
          o: [['Have them', 'Ir', 'Есть'], ['Partly', 'Daļēji', 'Частично'], ['No', 'Nav', 'Нет']] },
        { id: 'mood', type: 'check', other: true, l: ['What should the store feel like?', 'Kādu sajūtu veikalam jārada?', 'Какое настроение у магазина?'],
          o: [['Minimal', 'Minimālistisks', 'Минималистичный'], ['Warm and cosy', 'Silts un mājīgs', 'Тёплый, уютный'], ['Premium', 'Premium', 'Премиальный'], ['Bright and bold', 'Spilgts un drosmīgs', 'Яркий, смелый'], ['Playful', 'Rotaļīgs', 'Игривый'], ['Classic', 'Klasisks', 'Классический']] },
        { id: 'dislike', type: 'textarea', l: ['Anything you definitely don’t want to see?', 'Kaut kas, ko noteikti nevēlaties redzēt?', 'Что точно не хотите видеть?'],
          h: ['Colours, styles, websites you don’t like.', 'Krāsas, stili, mājaslapas, kas nepatīk.', 'Цвета, стили, сайты, которые не нравятся.'] },
      ]},
      { t: ['Features', 'Funkcijas', 'Функции'], q: [
        { id: 'features', type: 'check', other: true, l: ['What should the store have?', 'Kas veikalā ir vajadzīgs?', 'Что должно быть в магазине?'],
          o: [['Filters and search', 'Filtri un meklēšana', 'Фильтры и поиск'], ['Customer accounts', 'Pircēju konti', 'Личный кабинет покупателя'], ['Discount codes', 'Atlaižu kodi', 'Промокоды'], ['Gift cards', 'Dāvanu kartes', 'Подарочные карты'], ['Product reviews', 'Preču atsauksmes', 'Отзывы о товарах'], ['Wishlist', 'Vēlmju saraksts', 'Избранное'], ['Newsletter', 'Jaunumu vēstule', 'Рассылка'], ['Instagram / Facebook shop', 'Instagram / Facebook veikals', 'Магазин в Instagram / Facebook'], ['Blog', 'Blogs', 'Блог'], ['Wholesale prices', 'Vairumtirdzniecības cenas', 'Оптовые цены'], ['Pre-orders', 'Priekšpasūtījumi', 'Предзаказ']] },
        { id: 'integr', type: 'textarea', l: ['Services the store should connect to', 'Servisi, ar kuriem veikals jāsavieno', 'Сервисы, с которыми нужно связать магазин'],
          h: ['Accounting, warehouse, CRM, email marketing...', 'Grāmatvedība, noliktava, CRM, e-pasta mārketings...', 'Бухгалтерия, склад, CRM, email-рассылки...'] },
      ]},
      { t: ['Domain and legal', 'Domēns un juridiskā daļa', 'Домен и юридическое'], q: [
        { id: 'domain', type: 'radio', l: ['Domain', 'Domēns', 'Домен'],
          o: [['I have one', 'Man ir', 'Есть'], ['Need to buy one', 'Vajag iegādāties', 'Нужно купить']] },
        { id: 'domainName', type: 'text', l: ['Domain name, if you have one', 'Domēna nosaukums, ja ir', 'Адрес домена, если есть'] },
        { id: 'legal', type: 'radio', l: ['Privacy policy, cookies and terms of sale', 'Privātuma politika, sīkdatnes un pārdošanas noteikumi', 'Политика конфиденциальности, cookies и условия продажи'],
          o: [['I have them', 'Man ir', 'Есть'], ['Need help', 'Vajag palīdzību', 'Нужна помощь']] },
      ]},
      { t: ['Timing and budget', 'Termiņi un budžets', 'Сроки и бюджет'], q: [
        { id: 'date', type: 'text', l: ['When would you like to launch?', 'Kad vēlaties palaist veikalu?', 'Когда хотите запустить магазин?'] },
        { id: 'budget', type: 'radio', l: ['Approximate budget', 'Aptuvenais budžets', 'Примерный бюджет'],
          o: [['Up to €2 000', 'Līdz 2 000 €', 'До 2 000 €'], ['€2 000–3 500', '2 000–3 500 €', '2 000–3 500 €'], ['€3 500–6 000', '3 500–6 000 €', '3 500–6 000 €'], ['More than €6 000', 'Vairāk nekā 6 000 €', 'Больше 6 000 €'], ['Not sure, I’d like a proposal', 'Nezinu, gaidu piedāvājumu', 'Не знаю, жду предложение']] },
        { id: 'notes', type: 'textarea', l: ['Anything else we should know?', 'Vēl kaut kas, kas mums jāzina?', 'Что ещё нам стоит знать?'] },
      ]},
    ],
  },
};
