# Brief page setup (erewhile.digital/brief/)

The page is closed by an access code. The code is checked on the server (Pages Function
`functions/api/brief.js`), and the answers are emailed through Cloudflare Email Routing
by a small Worker (`workers/brief-mailer/worker.js`). No third-party form services.

## 1. Email Routing (once)
Cloudflare dashboard → erewhile.digital → **Email** → **Email Routing**:
- Enable it (if not yet) and let Cloudflare add the DNS records.
- **Destination addresses** → add konstantin.raugevich@gmail.com (the inbox for briefs) and confirm it from the email Cloudflare sends.

## 2. The mailer Worker
**Workers & Pages** → **Create** → **Worker** → name it `brief-mailer` → Deploy → **Edit code**,
paste `workers/brief-mailer/worker.js`, Deploy. Then in the Worker **Settings**:
- **Bindings** → Add → **Send Email** → variable name `SEND`, destination address = the inbox from step 1.
- **Variables and Secrets** → `FROM` = `brief@erewhile.digital`, `TO` = the inbox from step 1.
- **Domains & Routes** → turn off **workers.dev** and **Preview URLs** (the Worker should only be reachable from the site).

## 3. The Pages project (erewhile-site)
**Workers & Pages** → erewhile-site → **Settings**:
- **Variables and Secrets** → add a **Secret** `BRIEF_CODES` with 6-digit codes, for example `482193` (several separated by commas, one per client; avoid easy ones like 123456).
- **Bindings** → Add → **Service binding** → variable name `MAILER`, service `brief-mailer`.
- Redeploy (Deployments → latest → Retry deployment) so the settings take effect.

## Using it
Send the client the link and their code: `https://erewhile.digital/brief/?lang=lv` (or `ru`, `en`).
To close access, remove the code from `BRIEF_CODES` and redeploy.
New site types (landing page, ecosystem) are added in `brief/brief-data.js`.
