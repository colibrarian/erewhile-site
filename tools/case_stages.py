"""Client site headers rebuilt in HTML/CSS for the top of each case page.

Each stage reproduces the first screen of the client's live site: their header,
fonts, colours, background and hero copy (kept in the site's own language).
Markup and styles were ported from the client repositories (read-only).

Sizes are written for a 1200px wide stage as U(px), and for a 390px phone stage
as M(px). Both turn into container query units, so the stage scales like a real
page shrunk to fit, and switches to the client's mobile header under 620px.
Links inside the stage are plain spans: the whole stage is one link to the site.
"""
import re

KONDO = dict(
  ratio='16/9', mratio='4/5',
  html='''
<div class="k-hdr st-a">
  <img class="k-logo" src="/assets/cases/kondo/logo-header.png" alt="" width="260" height="240">
  <div class="k-nav"><span>About</span><span>Fabrics</span><span>Collections</span><span>Care</span><span>Contact</span></div>
  <div class="k-act"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M6 8h12l-1 12H7L6 8Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg><i class="st-burger"><b></b><b></b><b></b></i></div>
</div>
<div class="k-kanji" aria-hidden="true"><span>金</span><span>堂</span></div>
<div class="k-hero">
  <div class="k-eye st-a" style="--d:.1s">Golden Hall</div>
  <div class="k-h1 st-a" style="--d:.2s">KONDŌ</div>
  <div class="k-tag st-a" style="--d:.3s">Where the Dragon Dwells</div>
  <div class="k-sub st-a" style="--d:.4s">A philosophy of life — where every piece is created to support your journey toward inner and outer balance.</div>
  <div class="k-line st-a" style="--d:.5s"></div>
</div>''',
  css='''
.st-kondo{background:#fff;color:#111;font-family:'Inter',sans-serif}
.k-hdr{position:absolute;inset:0 0 auto;display:flex;align-items:center;justify-content:space-between;padding:U(20) U(44);z-index:3}
.k-logo{height:U(60);width:auto}
.k-nav{display:flex;gap:U(34);font-size:U(11.5);letter-spacing:.14em;text-transform:uppercase;color:#5c5c5c}
.k-act{display:flex;align-items:center;gap:U(18)}
.k-act svg{width:U(20);height:U(20)}
.k-kanji{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;flex-direction:column;align-items:center;font:700 U(560)/1 'Cinzel Decorative','Noto Serif JP','Songti SC','SimSun',serif;color:#111;opacity:.045;pointer-events:none;user-select:none}
.k-hero{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:U(90) U(48) U(30)}
.k-eye{font-size:U(12);letter-spacing:.34em;text-transform:uppercase;color:#8a8a8a;margin-bottom:U(24)}
.k-h1{font:900 U(100)/1 'Cinzel Decorative',serif}
.k-tag{font:400 U(21)/1.3 'EB Garamond',serif;letter-spacing:.03em;margin-top:U(16)}
.k-sub{font:italic 400 U(21)/1.6 'EB Garamond',serif;color:#5c5c5c;margin-top:U(24);max-width:U(540)}
.k-line{width:1px;height:U(44);margin-top:U(48);background:linear-gradient(#111,transparent);animation:k-pulse 2.4s ease-in-out infinite}
@keyframes k-pulse{0%,100%{opacity:.25}50%{opacity:1}}
@container (max-width:620px){
  .k-hdr{padding:M(16) M(20)}
  .k-logo{height:M(46)}
  .k-nav{display:none}
  .k-act{gap:M(18)}.k-act svg{width:M(20);height:M(20)}
  .st-kondo .st-burger{display:block;width:M(24);height:M(18);color:#111}
  .k-kanji{font-size:M(300)}
  .k-hero{padding:M(80) M(24) M(24)}
  .k-eye{font-size:M(11);margin-bottom:M(18)}
  .k-h1{font-size:M(54)}
  .k-tag{font-size:M(18)}
  .k-sub{font-size:M(18);max-width:none;margin-top:M(18)}
  .k-line{height:M(40);margin-top:M(36)}
}''')

ZEMITS = dict(
  ratio='16/10', mratio='9/13',
  html='''
<div class="z-bg"></div><div class="z-dots"></div>
<div class="z-nav st-a">
  <img class="z-logo" src="/assets/cases/zemits/logo-white.png" alt="" width="480" height="122">
  <div class="z-right">
    <div class="z-links"><span>Iekārtas</span><i></i><span>Par mums</span><i></i><span>Apmācības</span><i></i><span>Atsauksmes</span><i></i><span>Jautājumi</span><span class="z-cta">Sazināties</span></div>
    <div class="z-lang"><span class="on">LV</span><span>RU</span><span>EN</span></div>
    <i class="st-burger"><b></b><b></b><b></b></i>
  </div>
</div>
<div class="z-hero">
  <div class="z-content">
    <div class="z-title st-a" style="--d:.1s">Mūsdienīgas estētiskās kosmetoloģijas iekārtas<span>Redzami rezultāti.</span></div>
    <div class="z-sub st-a" style="--d:.2s">Zemits ir starptautiski atzīts estētiskās kosmetoloģijas un skaistumkopšanas iekārtu zīmols, kas piedāvā mūsdienīgus risinājumus sejas un ķermeņa procedūrām.</div>
    <div class="z-actions st-a" style="--d:.3s"><span class="z-btn">Visas iekārtas →</span><span class="z-btn z-out">Semināri</span></div>
  </div>
  <div class="z-side st-a" style="--d:.4s"><img src="/assets/cases/zemits/logo-white.png" alt="" width="480" height="122"></div>
</div>''',
  css='''
.st-zemits{color:#fff;font-family:'Outfit',sans-serif;font-weight:300}
.z-bg{position:absolute;inset:0;background:linear-gradient(135deg,#0d2040 0%,#1a4a8a 45%,#0a3060 100%)}
.z-dots{position:absolute;inset:0;opacity:.06;background-image:radial-gradient(circle at 1px 1px,rgba(255,255,255,.8) 1px,transparent 0);background-size:U(32) U(32)}
.z-nav{position:absolute;inset:0 0 auto;z-index:3;display:flex;align-items:center;justify-content:space-between;padding:U(16) U(60)}
.z-logo{height:U(30);width:auto}
.z-right{display:flex;align-items:center;gap:U(24)}
.z-links{display:flex;align-items:center;gap:U(13);font-size:U(13.5);letter-spacing:.04em;color:rgba(255,255,255,.85)}
.z-links i{width:1px;height:U(13);background:rgba(255,255,255,.28)}
.z-links .z-cta{margin-left:U(4)}
.z-cta{background:rgba(255,255,255,.15);border:1.5px solid rgba(255,255,255,.4);color:#fff;padding:U(8) U(20);border-radius:100px;font-weight:500}
.z-lang{display:flex;gap:U(4);background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:100px;padding:U(3)}
.z-lang span{padding:U(5) U(11);border-radius:100px;font-size:U(11);font-weight:600;letter-spacing:.08em;color:rgba(255,255,255,.7)}
.z-lang .on{background:#fff;color:#1a4a8a}
.z-hero{position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr;align-items:center;padding:U(60) U(60) 0;z-index:2}
.z-title{font:400 U(50)/1.12 'Playfair Display',serif;margin-bottom:U(16)}
.z-title span{display:block;font-style:italic;font-size:U(64);line-height:1.05;margin-top:U(6);color:#7ecbff}
.z-sub{font-size:U(15);line-height:1.8;color:rgba(255,255,255,.72);max-width:U(460);margin-bottom:U(34)}
.z-actions{display:flex;gap:U(14)}
.z-btn{background:#fff;color:#1a4a8a;padding:U(13) U(30);border-radius:100px;font-weight:600;font-size:U(14)}
.z-out{background:transparent;color:rgba(255,255,255,.85);border:1.5px solid rgba(255,255,255,.35);font-weight:400}
.z-side{display:flex;justify-content:center}
.z-side img{width:72%;height:auto;filter:drop-shadow(0 0 U(40) rgba(77,166,255,.28))}
@container (max-width:620px){
  .z-nav{padding:M(14) M(20)}
  .z-logo{height:M(26)}
  .z-links,.z-lang{display:none}
  .st-zemits .st-burger{display:block;width:M(24);height:M(18)}
  .z-hero{grid-template-columns:1fr;align-content:center;padding:M(70) M(20) M(20)}
  .z-title{font-size:M(32)}
  .z-title span{font-size:M(42)}
  .z-sub{font-size:M(14);max-width:none;margin-bottom:M(24)}
  .z-actions{gap:M(10);flex-wrap:wrap}
  .z-btn{padding:M(12) M(22);font-size:M(13.5)}
  .z-side{display:none}
}''')

UNTU = dict(
  ratio='16/10', mratio='9/14',
  html='''
<div class="u-bg"></div>
<div class="u-hdr st-a">
  <div class="u-brand">
    <img src="https://ik.imagekit.io/xshkpkf2i/Untu/logo%20untu.png?tr=w-96" alt="" width="42" height="42">
    <div><div class="u-title">UNTU</div><div class="u-slogan"><span>Young people</span><i>.</i><em>Youth workers</em><i>.</i><b>Educators</b></div></div>
  </div>
  <div class="u-links"><span>Events</span><span>About</span><span>Vision</span><span>Projects</span><span class="u-btn u-pri">Get involved</span></div>
  <i class="st-burger"><b></b><b></b><b></b></i>
</div>
<div class="u-hero">
  <div class="u-left">
    <div class="u-kicker st-a" style="--d:.1s">Youth empowerment • Cultural exchange • Peacebuilding</div>
    <div class="u-h1 st-a" style="--d:.2s">Grow, connect, and create positive change.</div>
    <div class="u-lead st-a" style="--d:.3s">UNTU is a non-profit organization empowering young people aged 18–35 through international projects, trainings, volunteering, and cultural exchange.</div>
    <div class="u-actions st-a" style="--d:.4s"><span class="u-btn u-pri">Apply to participate</span><span class="u-btn">Explore projects</span></div>
    <div class="u-cards st-a" style="--d:.5s">
      <div class="u-card"><div class="u-ct">Who we work for</div><p>Young people who want to become active, open-minded, and skilled through learning-by-doing and travel.</p></div>
      <div class="u-card"><div class="u-ct">What we build</div><p>A network of empowered individuals creating shared solutions for wellbeing, sustainability, and peace.</p></div>
    </div>
  </div>
  <div class="u-visual st-a" style="--d:.3s">
    <img src="https://ik.imagekit.io/xshkpkf2i/Untu/untu%20dragon.png?tr=w-900" alt="" loading="lazy">
    <div class="u-badge"><i></i><span>International training courses, youth exchanges, volunteering, local initiatives, and digital campaigns.</span></div>
  </div>
</div>''',
  css='''
.st-untu{color:#fff;font-family:'Montserrat',sans-serif;background:#0b0d12}
.u-bg{position:absolute;inset:0;background:radial-gradient(70% 70% at 15% 15%,rgba(255,210,51,.09),transparent 60%),radial-gradient(60% 60% at 85% 25%,rgba(255,255,255,.06),transparent 55%),linear-gradient(180deg,#0e1016,#0a0c12)}
.u-hdr{position:absolute;inset:0 0 auto;z-index:3;display:flex;align-items:center;justify-content:space-between;padding:U(14) U(40);border-bottom:1px solid rgba(255,255,255,.07);background:rgba(10,12,18,.42)}
.u-brand{display:flex;align-items:center;gap:U(12)}
.u-brand img{width:U(42);height:U(42);object-fit:contain}
.u-title{font-weight:900;letter-spacing:.02em;font-size:U(14);line-height:1.1}
.u-slogan{display:flex;gap:U(6);font-size:U(11.5);margin-top:U(2);color:rgba(255,255,255,.62);text-transform:uppercase;letter-spacing:.1em}
.u-slogan i{font-style:normal;opacity:.7}
.u-slogan b{font-weight:700}
.u-links{display:flex;align-items:center;gap:U(8);font-size:U(13);color:rgba(255,255,255,.8)}
.u-links>span:not(.u-btn){padding:U(8) U(10)}
.u-btn{display:inline-flex;align-items:center;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.06);color:#fff;font-weight:900;font-size:U(13);padding:U(10) U(14);border-radius:999px;box-shadow:0 U(14) U(40) rgba(0,0,0,.35);white-space:nowrap}
.u-pri{background:linear-gradient(180deg,rgba(255,210,51,.98),rgba(245,196,0,.96));color:#111;border-color:rgba(255,210,51,.42)}
.u-hero{position:absolute;inset:U(71) U(40) U(40);display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:U(34);padding-top:U(44);z-index:2}
.u-kicker{font-weight:900;font-size:U(11.5);letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.66)}
.u-h1{font-weight:900;letter-spacing:-.02em;line-height:1.02;font-size:U(54);margin:U(10) 0 U(14)}
.u-lead{color:rgba(255,255,255,.75);font-size:U(14.5);line-height:1.7;max-width:U(560)}
.u-actions{display:flex;gap:U(12);margin-top:U(20)}
.u-cards{display:grid;grid-template-columns:1fr 1fr;gap:U(16);margin-top:U(22)}
.u-card{border-radius:U(28);border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.05);padding:U(20) U(22)}
.u-ct{font-weight:900;font-size:U(12.5);letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.85);margin-bottom:U(8)}
.u-card p{margin:0;color:rgba(255,255,255,.78);font-size:U(13);line-height:1.6}
.u-visual{position:relative;border-radius:U(34);border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.04);overflow:hidden;box-shadow:0 U(18) U(60) rgba(0,0,0,.55)}
.u-visual img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.92}
.u-visual::after{content:'';position:absolute;inset:0;background:radial-gradient(80% 60% at 20% 20%,rgba(255,210,51,.14),transparent 55%),linear-gradient(180deg,rgba(10,12,18,.4),rgba(10,12,18,.86))}
.u-badge{position:absolute;left:U(18);right:U(18);bottom:U(18);z-index:2;display:flex;gap:U(12);align-items:center;border-radius:U(22);border:1px solid rgba(255,255,255,.14);background:rgba(10,12,18,.45);backdrop-filter:blur(12px);padding:U(14)}
.u-badge i{width:U(10);height:U(10);border-radius:99px;background:#FFD233;box-shadow:0 0 0 U(6) rgba(255,210,51,.12);flex:0 0 auto}
.u-badge span{color:rgba(255,255,255,.8);font-size:U(12.5);line-height:1.4}
@container (max-width:620px){
  .u-hdr{padding:M(12) M(20)}
  .u-brand img{width:M(38);height:M(38)}
  .u-title{font-size:M(14)}
  .u-slogan,.u-links{display:none}
  .st-untu .st-burger{display:block;width:M(24);height:M(18)}
  .u-hero{inset:M(63) M(20) M(20);grid-template-columns:1fr;grid-template-rows:auto 1fr;gap:M(18);padding-top:M(26)}
  .u-kicker{font-size:M(10.5)}
  .u-h1{font-size:M(38)}
  .u-lead{font-size:M(14);max-width:none}
  .u-actions{gap:M(10);margin-top:M(18)}
  .u-btn{font-size:M(13);padding:M(10) M(14)}
  .u-cards{display:none}
  .u-visual{border-radius:M(28)}
  .u-badge{left:M(12);right:M(12);bottom:M(12);padding:M(12);gap:M(10);border-radius:M(18)}
  .u-badge i{width:M(10);height:M(10)}
  .u-badge span{font-size:M(12)}
}''')

RAZALIJA = dict(
  ratio='16/10', mratio='9/14',
  html='''
<div class="r-bloom"></div>
<div class="r-nav st-a">
  <div class="r-brand"><b>Razalija</b><span>Kokneses prospekts 18, Rīga</span></div>
  <div class="r-links">
    <span class="r-chip r-phone"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>+371 26 068 971</span>
    <span class="r-chip r-hide">Pakalpojumi</span><span class="r-chip r-hide">Pušķi</span><span class="r-chip r-hide">Kontakti</span>
    <span class="r-cta r-hide">Pasūtīt pušķi</span>
    <span class="r-lang"><i class="on">LV</i><i>RU</i></span>
  </div>
</div>
<div class="r-hero st-a" style="--d:.15s">
  <div class="r-slides" data-slides>
    <i class="on" style="background-image:url(https://ik.imagekit.io/coworker/Razalija/raz%201.png?tr=w-1400)"></i>
    <i style="background-image:url(https://ik.imagekit.io/coworker/Razalija/raz%202.png?tr=w-1400)"></i>
    <i style="background-image:url(https://ik.imagekit.io/coworker/Razalija/raz%203.png?tr=w-1400)"></i>
    <i style="background-image:url(https://ik.imagekit.io/coworker/Razalija/raz%204.png?tr=w-1400)"></i>
  </div>
  <div class="r-content">
    <span class="r-kicker"><i></i>Ziedi, kas izskatās kā svētki</span>
    <div class="r-h1">Razalija — svaigi, skaisti ziedi no Mežaparka</div>
    <div class="r-sub">Izvēlies gatavu pušķi galerijā un aizpildi pieteikumu minūtes laikā. Mēs precizēsim detaļas un visu sakārtosim tā, lai izskatās perfekti.</div>
    <div class="r-actions"><span class="r-btn r-pri">Izvēlēties pušķi</span><span class="r-btn">Atstāt pieteikumu</span></div>
  </div>
</div>''',
  css='''
.st-razalija{background:#fbfbfe;color:rgba(43,30,63,.92);font-family:'Inter',sans-serif}
.r-bloom{position:absolute;inset:0;background:radial-gradient(38% 32% at 14% 8%,rgba(124,58,237,.16),transparent 72%),radial-gradient(34% 30% at 88% 16%,rgba(236,72,153,.15),transparent 72%),radial-gradient(42% 36% at 80% 82%,rgba(56,189,248,.14),transparent 72%),radial-gradient(38% 34% at 8% 86%,rgba(236,72,153,.11),transparent 72%)}
.r-nav{position:absolute;inset:0 0 auto;z-index:3;display:flex;align-items:center;justify-content:space-between;padding:U(14) U(58);background:rgba(255,255,255,.72);border-bottom:1px solid rgba(43,30,63,.08)}
.r-brand{display:flex;flex-direction:column;gap:U(2);line-height:1.05}
.r-brand b{font:600 U(20)/1.05 'Fraunces',serif;letter-spacing:-.02em}
.r-brand span{font-size:U(12.5);color:rgba(63,46,92,.72)}
.r-links{display:flex;align-items:center;gap:U(14)}
.r-chip{padding:U(9) U(12);border-radius:999px;background:rgba(43,30,63,.045);border:1px solid rgba(43,30,63,.1);color:rgba(43,30,63,.82);font-size:U(14)}
.r-phone{display:flex;align-items:center;gap:U(6);font-weight:700;color:rgba(43,30,63,.92)}
.r-phone svg{width:U(16);height:U(16)}
.r-cta{padding:U(10) U(14);border-radius:999px;border:1px solid rgba(43,30,63,.08);background:linear-gradient(135deg,rgba(124,58,237,.26),rgba(236,72,153,.2),rgba(56,189,248,.18));box-shadow:0 U(14) U(30) rgba(18,12,28,.12);font-weight:800;font-size:U(14)}
.r-lang{display:inline-flex;border:1px solid rgba(43,30,63,.1);border-radius:999px;background:rgba(255,255,255,.5);padding:U(3);gap:U(2)}
.r-lang i{font-style:normal;font-size:U(12.5);font-weight:700;letter-spacing:.03em;color:rgba(63,46,92,.7);padding:U(6) U(10);border-radius:999px}
.r-lang .on{color:#fff;background:linear-gradient(135deg,#7c3aed,#ec4899)}
.r-hero{position:absolute;left:U(58);right:U(58);top:U(115);bottom:U(44);border-radius:U(26);overflow:hidden;border:1px solid rgba(255,255,255,.16);box-shadow:0 U(16) U(50) rgba(18,12,28,.12);display:flex;align-items:flex-end;padding:U(26) U(24) U(24);z-index:2}
.r-slides{position:absolute;inset:0;background:linear-gradient(135deg,#efe4ff 0%,#fbe6f2 55%,#e6f3ff 100%)}
.r-slides i{position:absolute;inset:0;background-size:cover;background-position:center;transform:scale(1.03);opacity:0;transition:opacity 1.1s ease}
.r-slides i.on{opacity:1}
.r-slides::after{content:'';position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(0,0,0,.05) 0%,rgba(0,0,0,.28) 55%,rgba(0,0,0,.52) 100%),radial-gradient(100% 100% at 50% 45%,rgba(0,0,0,0) 35%,rgba(0,0,0,.4) 100%)}
.r-content{position:relative;z-index:2;max-width:U(760);display:flex;flex-direction:column;align-items:flex-start;gap:U(14)}
.r-kicker{display:inline-flex;align-items:center;gap:U(8);font-size:U(13);color:rgba(255,255,255,.86);padding:U(8) U(12);border-radius:999px;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.1)}
.r-kicker i{width:U(8);height:U(8);border-radius:99px;background:radial-gradient(circle at 30% 30%,rgba(255,255,255,.95),rgba(255,255,255,0) 60%),linear-gradient(135deg,#7c3aed,#ec4899,#38bdf8)}
.r-h1{font:600 U(54)/1.04 'Fraunces',serif;letter-spacing:-.02em;color:rgba(255,255,255,.96);text-shadow:0 U(10) U(30) rgba(0,0,0,.3)}
.r-sub{font-size:U(16);line-height:1.6;color:rgba(255,255,255,.82);max-width:U(540)}
.r-actions{display:flex;gap:U(10);margin-top:U(6)}
.r-btn{padding:U(12) U(14);border-radius:U(14);border:1px solid rgba(43,30,63,.12);background:rgba(255,255,255,.55);color:rgba(43,30,63,.88);font-weight:700;font-size:U(16)}
.r-pri{color:#fff;border-color:rgba(255,255,255,.16);background:linear-gradient(135deg,rgba(124,58,237,.92),rgba(236,72,153,.88),rgba(56,189,248,.82))}
@container (max-width:620px){
  .r-nav{padding:M(12) M(18)}
  .r-brand b{font-size:M(18)}.r-brand span{font-size:M(10.5)}
  .r-hide{display:none}
  .r-links{gap:M(8)}
  .r-chip{font-size:M(12);padding:M(8) M(10);white-space:nowrap}
  .r-brand span{white-space:nowrap}
  .r-phone svg{width:M(14);height:M(14)}
  .r-lang{padding:M(3)}.r-lang i{font-size:M(12);padding:M(6) M(9)}
  .r-hero{left:M(18);right:M(18);top:M(84);bottom:M(18);border-radius:M(22);padding:M(20) M(18)}
  .r-content{gap:M(12)}
  .r-kicker{font-size:M(12);padding:M(7) M(11);gap:M(7)}
  .r-kicker i{width:M(8);height:M(8)}
  .r-h1{font-size:M(34)}
  .r-sub{font-size:M(14.5);max-width:none}
  .r-actions{flex-wrap:wrap;gap:M(8)}
  .r-btn{font-size:M(14.5);padding:M(11) M(13);border-radius:M(13)}
}''')

JELGAVA = dict(
  ratio='16/9', mratio='9/14',
  html='''
<div class="j-hdr st-a">
  <div class="j-brand"><img src="https://ik.imagekit.io/coworker/Jelgava%20Coworking%20Space/Jelgava_Coworking_Space_Red.png?tr=f-auto,w-440" alt="" width="220" height="40"><span>Kazarmes iela 16B, Jelgava</span></div>
  <div class="j-nav"><span>Atmosfēra</span><span>Kam paredzēts</span><span>Paketes</span><span>BUJ</span><span>Kontakti</span></div>
  <div class="j-act"><span class="j-lang"><i class="on">LV</i><i>RU</i><i>EN</i></span><span class="j-btn j-pri">Sazinies ar mums</span><i class="st-burger"><b></b><b></b><b></b></i></div>
</div>
<div class="j-hero">
  <div class="j-left">
    <div class="j-kick st-a" style="--d:.1s">Coworking Jelgavā</div>
    <div class="j-h1 st-a" style="--d:.2s">Coworking jeb kopstrādes telpa Jelgavā mierīgam un produktīvam darbam</div>
    <div class="j-lead st-a" style="--d:.3s">Jelgava Coworking Space — klusa coworking telpa Jelgavā freelanceriem, studentiem un uzņēmējiem. Ērta darba vide, stabils internets, kafija un vieta fokusam.</div>
    <div class="j-cta st-a" style="--d:.4s"><span class="j-btn j-pri">Atstāt pieteikumu</span><span class="j-btn">Apskatīt paketes</span></div>
  </div>
  <div class="j-photo st-a" style="--d:.3s"><img src="https://ik.imagekit.io/coworker/Jelgava%20Coworking%20Space/cowork%201.png?tr=f-auto,w-1000" alt="" loading="lazy"></div>
</div>''',
  css='''
.st-jelgava-coworking{background:#fff;color:#111;font-family:'Space Grotesk',sans-serif;letter-spacing:.1px}
.j-hdr{position:absolute;inset:0 0 auto;z-index:3;display:flex;align-items:center;justify-content:space-between;gap:U(16);padding:U(14) U(40);background:rgba(255,255,255,.72);border-bottom:1px solid rgba(0,0,0,.05)}
.j-brand{display:flex;flex-direction:column;gap:U(6)}
.j-brand img{height:U(40);width:auto}
.j-brand span{font-size:U(12);color:#666;line-height:1.25}
.j-nav{display:flex;gap:U(18);font-size:U(14);color:#666;white-space:nowrap}
.j-act{display:flex;align-items:center;gap:U(10)}
.j-lang{display:flex;gap:U(6);padding:U(4);border:1px solid #e9e9e9;border-radius:999px}
.j-lang i{font-style:normal;font-size:U(12);padding:U(7) U(10);border-radius:999px;color:#666}
.j-lang .on{background:#f4f4f4;color:#111;font-weight:500}
.j-btn{display:inline-flex;align-items:center;padding:U(10) U(14);border-radius:999px;border:1px solid #e9e9e9;background:#fff;font-size:U(14);white-space:nowrap}
.j-pri{background:#880002;color:#fff;border-color:transparent}
.j-hero{position:absolute;inset:U(85) U(40) 0;display:grid;grid-template-columns:1.1fr .9fr;gap:U(26);align-items:center;padding-bottom:U(30);z-index:2}
.j-kick{font-size:U(12);color:#666;text-transform:uppercase;letter-spacing:1.8px;margin-bottom:U(10)}
.j-h1{font-size:U(46);line-height:1.08;font-weight:600;letter-spacing:-.5px;margin-bottom:U(14)}
.j-lead{font-size:U(18);line-height:1.55;color:#666;margin-bottom:U(22)}
.j-cta{display:flex;gap:U(10)}
.j-photo{aspect-ratio:4/3;border-radius:U(18);background:#f6f6f6;border:1px solid #e9e9e9;overflow:hidden;box-shadow:0 U(10) U(30) rgba(0,0,0,.06)}
.j-photo img{width:100%;height:100%;object-fit:cover}
@container (max-width:620px){
  .j-hdr{padding:M(12) M(18)}
  .j-brand img{height:M(30)}.j-brand span{font-size:M(11)}
  .j-nav,.j-lang,.j-act .j-btn{display:none}
  .st-jelgava-coworking .st-burger{display:block;width:M(24);height:M(18)}
  .j-hero{inset:M(78) M(18) M(18);grid-template-columns:1fr;grid-template-rows:auto 1fr;gap:M(18);align-items:start;padding:M(12) 0 0}
  .j-kick{font-size:M(11);margin-bottom:M(8)}
  .j-h1{font-size:M(30)}
  .j-lead{font-size:M(15);margin-bottom:M(16)}
  .j-cta{gap:M(8);flex-wrap:wrap}
  .j-btn{font-size:M(14);padding:M(10) M(14)}
  .j-photo{aspect-ratio:auto;height:100%;border-radius:M(16)}
}''')

STAGES = {'kondo': KONDO, 'zemits': ZEMITS, 'untu': UNTU, 'razalija': RAZALIJA, 'jelgava-coworking': JELGAVA}


def _units(css):
  css = re.sub(r'U\(([\d.]+)\)', lambda m: '%.3gcqw' % (float(m.group(1)) / 12), css)
  return re.sub(r'M\(([\d.]+)\)', lambda m: '%.3gcqw' % (float(m.group(1)) / 3.9), css)


def stage_css(slug):
  return _units(STAGES[slug]['css']) if slug in STAGES else ''
