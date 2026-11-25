// Erewhile Digital — /api/brief (Cloudflare Pages Function).
// POST {action:'check', code}            -> 200 if the code is valid, 403 if not.
// POST {action:'submit', code, ...brief} -> checks the code again, then emails the brief.
// Settings in the Pages project (Settings -> Variables and Secrets / Bindings):
//   BRIEF_CODES  secret, comma-separated 6-digit access codes, e.g. "482193,730215" (one per client)
//   MAILER       service binding to the "brief-mailer" Worker (workers/brief-mailer), which sends the email.
const json = (body, status = 200) => new Response(JSON.stringify(body), {
  status, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex' } });

function validCode(env, code) {
  const codes = String(env.BRIEF_CODES || '').split(',').map(c => c.trim()).filter(c => /^\d{6}$/.test(c));
  return /^\d{6}$/.test(String(code)) && codes.includes(String(code));
}
const clean = (s, max) => String(s || '').replace(/[\r\n]+/g, ' ').trim().slice(0, max);

export async function onRequestPost({ request, env }) {
  let b;
  try { b = await request.json(); } catch { return json({ ok: false, error: 'bad request' }, 400); }
  if (!validCode(env, b.code)) {
    await new Promise(r => setTimeout(r, 800)); // slows down code guessing
    return json({ ok: false, error: 'bad code' }, 403);
  }
  if (b.action === 'check') return json({ ok: true });
  if (b.action !== 'submit') return json({ ok: false, error: 'bad action' }, 400);

  const name = clean(b.name, 120), brand = clean(b.brand, 120), email = clean(b.email, 200);
  const text = String(b.text || '').slice(0, 40000);
  if (!name || !text) return json({ ok: false, error: 'empty' }, 400);
  if (!env.MAILER) return json({ ok: false, error: 'mailer not configured' }, 500);

  const subject = `Бриф (${clean(b.typeTitle, 60) || 'сайт'}): ${brand || name}`;
  const body = [
    `Новый бриф с erewhile.digital/brief/`, '',
    `Имя: ${name}`, `Бренд: ${brand || '—'}`, `Email: ${email || '—'}`,
    `Код: ${clean(b.code, 60)}`, `Язык формы: ${clean(b.lang, 5)}`, `Отправлен: ${new Date().toISOString()}`, '',
    text,
  ].join('\n');

  const r = await env.MAILER.fetch('https://mailer/send', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ subject, text: body, replyTo: /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) ? email : '' }),
  });
  return r.ok ? json({ ok: true }) : json({ ok: false, error: 'send failed' }, 502);
}

export const onRequest = () => json({ ok: false, error: 'method not allowed' }, 405);
