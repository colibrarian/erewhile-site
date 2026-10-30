"""Build a translated homepage from index.html.

Usage (from the repo root):
  python3 tools/build_page.py lv      -> lv/index.html
  python3 tools/build_page.py ru      -> ru/index.html
  python3 tools/build_page.py lv --md -> translations/lv.md (for a language review)

Texts live in tools/i18n/<lang>.py. Each English phrase must exist in index.html,
otherwise the script stops and names it, so the pages cannot silently drift apart.
Legal texts in the modals stay in English.
"""
import importlib, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def replace(part, en, tr, min_count=1):
    if part.count(en) < min_count:
        sys.exit('MISSING in index.html: ' + en[:80])
    return part.replace(en, tr)


def build(t):
    src = open('index.html').read()
    i = src.index('<!-- MODALS -->'); j = src.index('<script>', i)
    head, modals, scripts = src[:i], src[i:j], src[j:]
    for en, tr in t.PAIRS_HTML:
        head = replace(head, en, tr)
    for qe, qt, ae, at in t.FAQ:  # question and answer appear twice: JSON-LD and the page
        head = replace(head, qe, qt, 2)
        head = replace(head, ae, at, 2)
    for en, tr in t.PAIRS_JS:
        scripts = replace(scripts, en, tr)
    for en, tr in t.JS_STRINGS:
        scripts = replace(scripts, "'" + en + "'", "'" + tr + "'")
    os.makedirs(t.LANG, exist_ok=True)
    out = head + modals + scripts
    open(os.path.join(t.LANG, 'index.html'), 'w').write(out)
    print('built', t.LANG + '/index.html', len(out), 'bytes')


def plain(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'^(content|placeholder|aria-label)="|"$', '', s)
    return s.replace('\\n', ' / ').replace('|', '\\|').strip(" >(<'\",")


def export_md(t):
    rows = []
    for en, tr in t.PAIRS_HTML + t.PAIRS_JS + t.JS_STRINGS:
        e, r = plain(en), plain(tr)
        if e and r and e != r and re.search(r'[A-Za-z]{3}', e) and not e.startswith('http') and '": "' not in e and r not in ('English', 'EN'):
            rows.append((e, r))
    for qe, qt, ae, at in t.FAQ:
        rows += [(qe, qt), (ae, at)]
    seen, uniq = set(), []
    for e, r in rows:
        if e not in seen:
            seen.add(e); uniq.append((e, r))
    name = {'lv': 'Latvian', 'ru': 'Russian'}.get(t.LANG, t.LANG)
    lines = [
        f'# Erewhile Digital — {name} website texts for review', '',
        f'Website of a web design studio in Latvia (websites, landing pages, video, integrations).',
        f'Audience: small businesses, NGOs and Erasmus+ projects in the Baltics.', '',
        '## Instructions for the reviewer', '',
        f'1. Check every {name} text in the table for grammar, spelling, natural phrasing and consistent terminology.',
        '2. Keep the meaning of the English source. Keep prices, numbers, brand names and symbols (€, →, ·) as they are.',
        '3. Keep the tone short, clear and professional, the way a local studio would write.',
        '4. Return the full table with the same IDs. Put the corrected text in the last column, or leave it empty when no change is needed.',
        '5. After the table, list any terms you changed everywhere (for example, one word for "landing page").', '',
        f'| ID | English source | {name} (current) | {name} (corrected) |',
        '|---|---|---|---|',
    ]
    for n, (e, r) in enumerate(uniq, 1):
        lines.append(f'| {t.LANG.upper()}-{n:03d} | {e} | {r} | |')
    os.makedirs('translations', exist_ok=True)
    path = f'translations/{t.LANG}.md'
    open(path, 'w').write('\n'.join(lines) + '\n')
    print('exported', path, len(uniq), 'rows')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    t = importlib.import_module('i18n.' + sys.argv[1])
    export_md(t) if '--md' in sys.argv else build(t)
