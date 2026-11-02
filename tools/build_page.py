"""Build the Latvian and Russian versions of the site from the English pages.

Usage (from the repo root):
  python3 tools/build_page.py lv              -> every page in Latvian (lv/index.html, lv/portfolio/ ...)
  python3 tools/build_page.py ru portfolio    -> one page
  python3 tools/build_page.py lv --md         -> translations/lv.md (homepage texts, for a language review)
  python3 tools/build_page.py lv --md inner   -> translations/lv-inner.md (portfolio, video, thanks)

Texts live in tools/i18n/<lang>.py (homepage) and tools/i18n/<lang>_<page>.py (inner pages).
Each English phrase must exist in the source page, otherwise the script stops and names it,
so the pages cannot silently drift apart. Pairs in OPTIONAL may be missing (texts that only
some versions of a page have). Legal texts in the modals stay in English.

After the texts are replaced, internal links are pointed at the same language
(/portfolio -> /lv/portfolio/, / -> /lv/ ...), and the language switcher gets the English link.
"""
import importlib, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SITE = 'https://erewhile.digital'
# page name -> (English source file, English URL path, i18n module suffix)
PAGES = {
    'home':      ('index.html',           '/',           ''),
    'portfolio': ('portfolio/index.html', '/portfolio/', '_portfolio'),
    'video':     ('video/index.html',     '/video/',     '_video'),
    'thanks':    ('thanks/index.html',    '/thanks/',    '_thanks'),
}
LOCAL_PATHS = {'/': '/', '/portfolio': '/portfolio/', '/portfolio/': '/portfolio/',
               '/video': '/video/', '/video/': '/video/'}
SWITCH = {'en': ('EN', 'English'), 'lv': ('LV', 'Latviski'), 'ru': ('RU', 'Русский')}
MODAL_MARKERS = ('<!-- MODALS -->', '<!-- ── MODALS ── -->')


def replace(part, en, tr, min_count=1, src='page'):
    if part.count(en) < min_count:
        sys.exit(f'MISSING in {src}: ' + en[:80])
    return part.replace(en, tr)


def split_modals(src):
    """(page before the legal modals, the modals, the scripts). Modals stay in English."""
    for m in MODAL_MARKERS:
        if m in src:
            i = src.index(m); j = src.index('<script', i)
            return src[:i], src[i:j], src[j:]
    j = src.find('<script>')
    return (src, '', '') if j < 0 else (src[:j], '', src[j:])


def localize_links(html, lang):
    """Point internal page links at the same language. Links that carry hreflang
    (the language switcher) and links to assets or case pages are left alone."""
    def fix(m):
        path, frag = m.group(1), m.group(2) or ''
        if path not in LOCAL_PATHS:
            return m.group(0)
        return f'href="/{lang}{LOCAL_PATHS[path]}{frag}"'
    html = re.sub(r'href="(/[a-z]*/?)(#[^"]*)?"(?!\s+hreflang)', fix, html)
    html = re.sub(r"url:'(/portfolio|/video)'", lambda m: f"url:'/{lang}{LOCAL_PATHS[m.group(1)]}'", html)
    html = html.replace(f'value="{SITE}/thanks/"', f'value="{SITE}/{lang}/thanks/"')
    return html


def switcher(html, lang, en_url):
    """In the language switcher, the link to this page's own language becomes the English link."""
    code, name = SWITCH[lang]; ecode, ename = SWITCH['en']
    html = re.sub(rf'<a href="[^"]*" hreflang="{lang}" lang="{lang}">{code}</a>',
                  f'<a href="{en_url}" hreflang="en" lang="en">{ecode}</a>', html)
    html = re.sub(rf'<a href="[^"]*" hreflang="{lang}" lang="{lang}">{name}</a>',
                  f'<a href="{en_url}" hreflang="en" lang="en">{ename}</a>', html)
    return html


def write(path, out):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    open(path, 'w').write(out)
    print('built', path, len(out), 'bytes')


def build_home(t):
    src = open('index.html').read()
    head, modals, scripts = split_modals(src)
    for en, tr in t.PAIRS_HTML:
        head = replace(head, en, tr, src='index.html')
    for qe, qt, ae, at in t.FAQ:  # question and answer appear twice: JSON-LD and the page
        head = replace(head, qe, qt, 2, 'index.html')
        head = replace(head, ae, at, 2, 'index.html')
    for en, tr in t.PAIRS_JS:
        scripts = replace(scripts, en, tr, src='index.html')
    for en, tr in t.JS_STRINGS:
        scripts = replace(scripts, "'" + en + "'", "'" + tr + "'", src='index.html')
    out = localize_links(head + modals + scripts, t.LANG)
    write(os.path.join(t.LANG, 'index.html'), out)


def build_inner(lang, page):
    src_file, url, suffix = PAGES[page]
    t = importlib.import_module(f'i18n.{lang}{suffix}')
    src = open(src_file).read()
    head, modals, scripts = split_modals(src)
    local_url = f'/{lang}{url}'
    head = head.replace('<html lang="en">', f'<html lang="{lang}">', 1)
    head = re.sub(r'(<link rel="canonical" href=")[^"]*(")', rf'\g<1>{SITE}{local_url}\g<2>', head, count=1)
    for en, tr in t.PAIRS:
        head = replace(head, en, tr, src=src_file)
    for en, tr in getattr(t, 'OPTIONAL', []):
        head = head.replace(en, tr)
    for en, tr in getattr(t, 'PAIRS_JS', []):
        scripts = replace(scripts, en, tr, src=src_file)
    out = switcher(localize_links(head + modals + scripts, lang), lang, url)
    write(os.path.join(lang, src_file), out)


def build(lang, pages):
    for page in pages:
        if page == 'home':
            build_home(importlib.import_module('i18n.' + lang))
        else:
            build_inner(lang, page)


def plain(s):
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'^(content|placeholder|aria-label|value)="|"$', '', s)
    return s.replace('\\n', ' / ').replace('|', '\\|').strip(" >(<'\",")


HEADER = [
    '# Erewhile Digital — {name} website texts for review', '',
    'Website of a web design studio in Latvia (websites, landing pages, video, integrations).',
    'Audience: small businesses, NGOs and Erasmus+ projects in the Baltics.', '{scope}',
    '## Instructions for the reviewer', '',
    '1. Check every {name} text in the table for grammar, spelling, natural phrasing and consistent terminology.',
    '2. Keep the meaning of the English source. Keep prices, numbers, brand names and symbols (€, →, ·) as they are.',
    '3. Keep the tone short, clear and professional, the way a local studio would write.',
    '4. Return the full table with the same IDs. Put the corrected text in the last column, or leave it empty when no change is needed.',
    '5. After the table, list any terms you changed everywhere (for example, one word for "landing page").', '',
]


def rows_of(pairs):
    rows = []
    for en, tr in pairs:
        e, r = plain(en), plain(tr)
        if e and r and e != r and re.search(r'[A-Za-z]{3}', e) and not e.startswith('http') and '": "' not in e and r not in ('English', 'EN'):
            rows.append((e, r))
    return rows


def export_md(lang, inner=False):
    name = {'lv': 'Latvian', 'ru': 'Russian'}.get(lang, lang)
    sections = []
    if inner:
        scope = ('\nThese are the inner pages: Portfolio, Video and the "thank you" page after the contact form. '
                 'The homepage was reviewed separately; its terms (mājaslapa, mērķlapa, pieteikums ...) are already agreed.\n')
        for page in ('portfolio', 'video', 'thanks'):
            t = importlib.import_module(f'i18n.{lang}{PAGES[page][2]}')
            sections.append((page, rows_of(t.PAIRS + getattr(t, 'OPTIONAL', []) + getattr(t, 'PAIRS_JS', []))))
        prefix, path = lang.upper() + '-IN', f'translations/{lang}-inner.md'
    else:
        scope = ''
        t = importlib.import_module('i18n.' + lang)
        rows = rows_of(t.PAIRS_HTML + t.PAIRS_JS + t.JS_STRINGS)
        for qe, qt, ae, at in t.FAQ:
            rows += [(qe, qt), (ae, at)]
        sections.append((None, rows))
        prefix, path = lang.upper(), f'translations/{lang}.md'
    lines = [l.format(name=name, scope=scope) for l in HEADER]
    seen, n = set(), 0
    for page, rows in sections:
        if page:
            lines += [f'## {page.capitalize()} page', '']
        lines += [f'| ID | English source | {name} (current) | {name} (corrected) |', '|---|---|---|---|']
        for e, r in rows:
            if e in seen:
                continue
            seen.add(e); n += 1
            lines.append(f'| {prefix}-{n:03d} | {e} | {r} | |')
        lines.append('')
    os.makedirs('translations', exist_ok=True)
    open(path, 'w').write('\n'.join(lines))
    print('exported', path, n, 'rows')


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        sys.exit(__doc__)
    lang, rest = args[0], args[1:]
    if '--md' in sys.argv:
        export_md(lang, inner='inner' in rest)
    else:
        build(lang, rest or list(PAGES))
