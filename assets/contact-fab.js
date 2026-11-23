/* Floating contact button: Konstantin's avatar in the corner; tap opens a small card with WhatsApp, Telegram and email.
   Appears after a short scroll, hides while the request form (#ew-contact) is on screen. Language from <html lang>.
   PHOTO: set to an image URL (square portrait) to replace the initial. */
(function(){
  var PHOTO = '';
  var WA = 'https://wa.me/37120579106', TG = 'https://t.me/Colibrarian', MAIL = 'web@erewhile.digital';
  var T = {
    en: {name:'Konstantin', role:'Project manager · Erewhile', text:'Hi, I’m Konstantin, project manager at Erewhile. It’s usually quickest to talk things through in a chat, so message me directly and I’ll be glad to help.', open:'Message Konstantin', close:'Close', mail:'or email'},
    lv: {name:'Konstantīns', role:'Projektu vadītājs · Erewhile', text:'Sveiki, mani sauc Konstantīns, esmu Erewhile projektu vadītājs. Visu parasti ir vienkāršāk apspriest čatā, tāpēc rakstiet man tieši, labprāt palīdzēšu.', open:'Rakstīt Konstantīnam', close:'Aizvērt', mail:'vai e-pasts'},
    ru: {name:'Константин', role:'Менеджер проектов · Erewhile', text:'Привет, меня зовут Константин, я менеджер проектов в Erewhile. Обычно проще всего обсудить всё в чате, так что пишите мне напрямую, с радостью помогу.', open:'Написать Константину', close:'Закрыть', mail:'или почта'}
  };
  var lang = (document.documentElement.lang || 'en').slice(0, 2), t = T[lang] || T.en;
  function track(n){ try{ if(window.umami) umami.track(n) }catch(e){} }
  var css = '.cfab{position:fixed;right:max(18px,env(safe-area-inset-right,0px));bottom:calc(18px + env(safe-area-inset-bottom,0px));z-index:900;font-family:Montserrat,system-ui,sans-serif;transition:opacity .3s,transform .3s}'
   +'.cfab.off{opacity:0;transform:translateY(16px);pointer-events:none}'
   +'.cfab-btn{position:relative;width:60px;height:60px;border-radius:50%;border:3px solid #fff;padding:0;cursor:pointer;background:#0D3E3E;color:#fff;font-weight:800;font-size:22px;box-shadow:0 12px 30px rgba(13,62,62,.28);display:grid;place-items:center;overflow:visible;transition:transform .2s}'
   +'.cfab-btn:hover{transform:translateY(-2px)}'
   +'.cfab-btn:focus-visible,.cfab a:focus-visible,.cfab-x:focus-visible{outline:2px solid #0D3E3E;outline-offset:3px}'
   +'.cfab-ava{width:100%;height:100%;border-radius:50%;object-fit:cover;display:grid;place-items:center}'
   +'.cfab-dot{position:absolute;right:-2px;bottom:-2px;width:20px;height:20px;border-radius:50%;background:#25D366;border:3px solid #fff;display:grid;place-items:center}'
   +'.cfab-dot svg{width:10px;height:10px;fill:#fff}'
   +'.cfab-card{position:absolute;right:0;bottom:74px;width:min(320px,calc(100vw - 36px));background:#fff;color:#111;border:1px solid #e4e4e0;border-radius:20px;padding:18px;box-shadow:0 24px 60px rgba(13,62,62,.18);opacity:0;transform:translateY(8px) scale(.98);transform-origin:bottom right;pointer-events:none;transition:opacity .22s,transform .22s}'
   +'.cfab.open .cfab-card{opacity:1;transform:none;pointer-events:auto}'
   +'.cfab-head{display:flex;gap:12px;align-items:center;padding-right:26px}'
   +'.cfab-head .cfab-ava{display:grid;place-items:center;width:46px;height:46px;flex:0 0 46px;background:#0D3E3E;color:#fff;font-weight:800;font-size:18px}'
   +'.cfab-head b{display:block;font-size:15px;font-weight:800;letter-spacing:-.02em}'
   +'.cfab-head span{display:block;font-size:11.5px;color:#6b6b6b}'
   +'.cfab-x{position:absolute;top:12px;right:12px;width:28px;height:28px;border:0;border-radius:50%;background:#f3f3f0;color:#555;font-size:16px;line-height:1;cursor:pointer}'
   +'.cfab-card p{font-size:13px;line-height:1.55;color:#3a3a3a;margin:12px 0 14px}'
   +'.cfab-links{display:grid;grid-template-columns:1fr 1fr;gap:8px}'
   +'.cfab-links a{display:flex;align-items:center;justify-content:center;gap:7px;padding:11px 10px;border-radius:12px;font-size:13px;font-weight:700;text-decoration:none;color:#fff}'
   +'.cfab-links svg{width:16px;height:16px;fill:currentColor}'
   +'.cfab-wa{background:#0D3E3E}.cfab-tg{background:#0D3E3E}'
   +'.cfab-links a:hover{background:#072828}'
   +'.cfab-mail{display:block;margin-top:10px;text-align:center;font-size:12px;color:#6b6b6b}'
   +'.cfab-mail a{color:#0D3E3E;font-weight:600}'
   +'@media(prefers-reduced-motion:reduce){.cfab,.cfab-card,.cfab-btn{transition:none}}'
   +'@media print{.cfab{display:none}}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  var ini = t.name.charAt(0);
  function ava(cls){ return PHOTO ? '<img class="cfab-ava'+(cls||'')+'" src="'+PHOTO+'" alt="">' : '<span class="cfab-ava'+(cls||'')+'">'+ini+'</span>'; }
  var waI = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.6 14.2c-.2.7-1.4 1.3-1.9 1.3-.5.1-1.1.1-1.8-.1a16 16 0 0 1-1.6-.6 12.6 12.6 0 0 1-4.9-4.3c-.4-.5-1-1.5-1-2.8s.7-2 1-2.3c.2-.3.5-.4.7-.4h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.7 1.2 1.6 1.9 1.1.9 2 1.2 2.3 1.4.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l2 .9c.3.1.5.2.5.3.1.2.1.7-.1 1.4z"/></svg>';
  var tgI = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21.9 4.3 18.6 20c-.2 1.1-.9 1.4-1.8.9l-5-3.7-2.4 2.3c-.3.3-.5.5-1 .5l.4-5.1 9.2-8.3c.4-.4-.1-.6-.6-.2L6 13.6 1.1 12c-1.1-.3-1.1-1.1.2-1.6L20.5 3c.9-.3 1.7.2 1.4 1.3z"/></svg>';
  var box = document.createElement('div');
  box.className = 'cfab off';
  box.innerHTML =
    '<div class="cfab-card" id="cfabCard" role="dialog" aria-label="'+t.open+'">'
   +'<button class="cfab-x" type="button" aria-label="'+t.close+'">×</button>'
   +'<div class="cfab-head">'+ava()+'<div><b>'+t.name+'</b><span>'+t.role+'</span></div></div>'
   +'<p>'+t.text+'</p>'
   +'<div class="cfab-links"><a class="cfab-wa" href="'+WA+'" target="_blank" rel="noopener">'+waI+'WhatsApp</a><a class="cfab-tg" href="'+TG+'" target="_blank" rel="noopener">'+tgI+'Telegram</a></div>'
   +'<span class="cfab-mail">'+t.mail+' <a href="mailto:'+MAIL+'">'+MAIL+'</a></span>'
   +'</div>'
   +'<button class="cfab-btn" type="button" aria-expanded="false" aria-controls="cfabCard" aria-label="'+t.open+'">'+ava()+'<span class="cfab-dot">'+waI+'</span></button>';
  document.body.appendChild(box);
  var btn = box.querySelector('.cfab-btn');
  function set(o){ box.classList.toggle('open', o); btn.setAttribute('aria-expanded', o); }
  btn.addEventListener('click', function(){ var o = !box.classList.contains('open'); set(o); if(o) track('Contact button open'); });
  box.querySelector('.cfab-x').addEventListener('click', function(){ set(false); btn.focus(); });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') set(false); });
  document.addEventListener('click', function(e){ if(!box.contains(e.target)) set(false); });
  box.querySelector('.cfab-tg').addEventListener('click', function(){ track('Telegram click'); });
  /* visibility: after a short scroll, and not while the request form is on screen */
  var form = document.getElementById('ew-contact'), formOn = false;
  function upd(){ var show = window.scrollY > 320 && !formOn; box.classList.toggle('off', !show); if(!show) set(false); }
  if(form && 'IntersectionObserver' in window) new IntersectionObserver(function(es){ formOn = es[0].isIntersecting; upd(); }, {threshold: .15}).observe(form);
  addEventListener('scroll', upd, {passive: true}); upd();
})();
