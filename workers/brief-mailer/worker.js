// Erewhile Digital — brief-mailer Worker. Sends the brief from /api/brief to Konstantin's inbox
// with Cloudflare Email Routing (send_email binding). Only reachable through the Pages service binding:
// turn off its workers.dev URL and Preview URLs in the Worker settings.
// Settings: binding SEND (Send Email), variables FROM (e.g. brief@erewhile.digital) and TO (verified address).
import { EmailMessage } from 'cloudflare:email';

const header = s => String(s || '').replace(/[\r\n]+/g, ' ').trim();
const b64 = s => {
  const bytes = new TextEncoder().encode(s); let bin = '';
  for (let i = 0; i < bytes.length; i += 0x8000) bin += String.fromCharCode(...bytes.subarray(i, i + 0x8000));
  return btoa(bin);
};

export default {
  async fetch(request, env) {
    if (request.method !== 'POST') return new Response('Not found', { status: 404 });
    const { subject, text, replyTo } = await request.json();
    const raw = [
      `From: Erewhile Digital Brief <${env.FROM}>`,
      `To: <${env.TO}>`,
      replyTo ? `Reply-To: <${header(replyTo)}>` : null,
      `Subject: =?UTF-8?B?${b64(header(subject))}?=`,
      `Message-ID: <${crypto.randomUUID()}@${env.FROM.split('@')[1]}>`,
      `Date: ${new Date().toUTCString()}`,
      'MIME-Version: 1.0',
      'Content-Type: text/plain; charset=UTF-8',
      'Content-Transfer-Encoding: base64',
      '',
      b64(String(text || '')).replace(/.{76}/g, '$&\r\n'),
    ].filter(l => l !== null).join('\r\n');
    try {
      await env.SEND.send(new EmailMessage(env.FROM, env.TO, raw));
      return new Response('ok');
    } catch (e) {
      return new Response('send failed: ' + e.message, { status: 500 });
    }
  },
};
