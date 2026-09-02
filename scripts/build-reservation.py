#!/usr/bin/env python3
"""Génère reservation.html (FR/DE/EN) à partir de l'archive Webflow, style btcar75."""
from __future__ import annotations

import importlib.util
import re
import shutil
from html import unescape
from pathlib import Path

ROOT = Path("/workspace")
ARCHIVE = ROOT / "archive/nuskowcars-original-20250902"
RES_ASSETS = ROOT / "assets" / "reservation"

# Load integrate-nuskow helpers
_spec = importlib.util.spec_from_file_location("integrate", ROOT / "scripts" / "integrate-nuskow.py")
integrate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(integrate)

SITE = integrate.SITE
header_html = integrate.header_html
footer_html = integrate.footer_html
LANG_CSS = integrate.LANG_CSS

ARCHIVE_SOURCES = {
    "fr": ARCHIVE / "reservation.html",
    "de": ARCHIVE / "german" / "reservation.html",
    "en": ARCHIVE / "en" / "reservation.html",
}

OUTPUTS = {
    "fr": ROOT / "reservation.html",
    "de": ROOT / "german" / "reservation.html",
    "en": ROOT / "en" / "reservation.html",
}

PAGE_KEYS = {"fr": "reservation.html", "de": "german/reservation.html", "en": "en/reservation.html"}
PREFIX = {"fr": "", "de": "../", "en": "../"}

BT_OVERRIDE = """
body{opacity:1!important}
.reservation-page{background:#0a0a0a;color:#fff;min-height:100vh;padding:clamp(6rem,10vw,8rem) 1.25rem 4rem}
.reservation-page .section-reservation{max-width:72rem;margin:0 auto}
.reservation-page h1{font-family:Inter Tight,sans-serif;font-weight:300;font-size:clamp(2rem,1rem + 4vw,3.5rem);text-align:center;margin:0 0 2.5rem;letter-spacing:-.02em}
.reservation-page .form_block{background:#111;border-radius:20px;padding:clamp(1.5rem,4vw,2.5rem);border:1px solid rgba(255,255,255,.08)}
.reservation-page .niveau-etapes_wrapper{display:flex;flex-wrap:wrap;gap:.5rem 1rem;justify-content:center;margin-bottom:2rem}
.reservation-page .niveau-etape{opacity:.45;font-family:Geist Mono,monospace;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase}
.reservation-page .niveau-etape.is-now{opacity:1;color:#cbc3e5}
.reservation-page .questions_title{font-family:Inter Tight,sans-serif;font-size:clamp(1.25rem,.9rem + 1.5vw,1.75rem);margin-bottom:1rem}
.reservation-page .choix-car_grid,.reservation-page .choix-offre_grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:1rem}
.reservation-page .choix-offre_card{background:#1a1a1a;border:1px solid rgba(255,255,255,.1);border-radius:14px;overflow:hidden;transition:border-color .2s,transform .2s}
.reservation-page .choix-offre_card:has(input:checked){border-color:#cbc3e5;transform:translateY(-2px)}
.reservation-page .form-radio_field{display:block;cursor:pointer;padding:1rem}
.reservation-page .form_radio-btn{position:absolute;opacity:0}
.reservation-page .form_radio-picto img{width:3rem;height:3rem;object-fit:contain;margin-bottom:.75rem}
.reservation-page .offer-duration,.reservation-page .country{font-family:Inter Tight,sans-serif;font-size:.95rem;line-height:1.3}
.reservation-page .offer-price,.reservation-page .text-size-small{font-size:.8rem;opacity:.65;margin-top:.25rem}
.reservation-page .info-title,.reservation-page .field-label{display:block;font-family:Geist Mono,monospace;font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;opacity:.7;margin-bottom:.35rem}
.reservation-page .input,.reservation-page .text-field-2,.reservation-page .w-input{width:100%;background:#0a0a0a;border:1px solid rgba(255,255,255,.15);border-radius:10px;padding:.85rem 1rem;color:#fff;font-family:Inter Tight,sans-serif;font-size:1rem}
.reservation-page .grid-date{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.reservation-page .button.is-suivant,.reservation-page input[type=submit]{display:inline-flex;align-items:center;justify-content:center;background:#fff;color:#111;border:none;border-radius:999px;padding:.9rem 2rem;font-family:Inter Tight,sans-serif;font-weight:500;cursor:pointer;text-decoration:none}
.reservation-page .back-link-block{color:#fff;opacity:.7;display:inline-flex;align-items:center;margin-right:1rem}
.reservation-page .button-next_wrapper{display:flex;align-items:center;justify-content:flex-end;margin-top:1.5rem}
.reservation-page .form_step{display:none}
.reservation-page .form_step.is-active{display:block}
.reservation-page .w-form-done,.reservation-page .w-form-fail{padding:2rem;text-align:center;border-radius:14px;margin-top:1rem}
.reservation-page .w-form-done{background:rgba(100,200,100,.15);display:none}
.reservation-page .w-form-fail{background:rgba(200,80,80,.15);display:none}
.reservation-page .captcha-wrapper{display:none}
@media(max-width:48em){.reservation-page .grid-date{grid-template-columns:1fr}}
"""


def copy_reservation_assets():
    """Copie CSS/JS Webflow et assets CDN référencés dans les 3 pages réservation."""
    RES_ASSETS.mkdir(parents=True, exist_ok=True)
    cdn_src = ARCHIVE / "assets" / "cdn.prod.website-files.com" / "666a07b245930cb23ff3b913"
    cdn_dst = RES_ASSETS / "cdn"
    for sub in ("css", "js"):
        src_dir = cdn_src / sub
        if src_dir.exists():
            dst_dir = cdn_dst / sub
            dst_dir.mkdir(parents=True, exist_ok=True)
            for f in src_dir.glob("*.css" if sub == "css" else "*.js"):
                shutil.copy2(f, dst_dir / f.name)
    # jquery archive
    jq_src = ARCHIVE / "assets" / "d3e54v103j8qbb.cloudfront.net" / "js"
    if jq_src.exists():
        jq_dst = RES_ASSETS / "jquery"
        jq_dst.mkdir(exist_ok=True)
        for f in jq_src.glob("*.js"):
            shutil.copy2(f, jq_dst / f.name)

    # Copy all png/jpg/svg referenced in reservation pages
    refs = set()
    for src in ARCHIVE_SOURCES.values():
        html = src.read_text(encoding="utf-8", errors="replace")
        for m in re.findall(r'(?:src|srcset)="([^"]+)"', html):
            for part in m.split(","):
                path = part.strip().split(" ")[0]
                if path.startswith("../"):
                    path = path[3:]
                if path.startswith("assets/cdn"):
                    refs.add(path)
    for rel in refs:
        src = ARCHIVE / rel
        dst = ROOT / rel.replace("assets/cdn.prod.website-files.com/", "assets/reservation/cdn/", 1)
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    # Rattrapage si des fichiers ont été copiés sous l'ancien chemin
    legacy = RES_ASSETS / "cdn.prod.website-files.com"
    if legacy.exists():
        for src in legacy.rglob("*"):
            if src.is_file():
                rel = src.relative_to(legacy)
                dst = RES_ASSETS / "cdn" / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                if not dst.exists():
                    shutil.copy2(src, dst)


def rewrite_asset_paths(html: str, prefix: str) -> str:
    html = html.replace("../assets/cdn.prod.website-files.com/", f"{prefix}assets/reservation/cdn/")
    html = html.replace("assets/cdn.prod.website-files.com/", f"{prefix}assets/reservation/cdn/")
    html = html.replace('href="reservation.html#', f'href="{prefix}reservation.html#')
    html = html.replace("href='reservation.html#", f"href='{prefix}reservation.html#")
    return html


def extract_form_body(html: str) -> str:
    """Extrait h1 + formulaire multi-étapes."""
    # H1 title
    h1 = re.search(r'<h1[^>]*class="[^"]*heading[^"]*"[^>]*>([^<]+)</h1>', html)
    title = unescape(h1.group(1)) if h1 else "Demande de réservation"
    form_start = html.find('<div class="form_block w-form">')
    if form_start < 0:
        form_start = html.find('<form ')
    form_end = html.find("</form>", form_start)
    if form_end < 0:
        raise ValueError("Form not found")
    form_end += len("</form>")
    # success/fail blocks after form
    tail = html[form_end : form_end + 3000]
    done = re.search(r'<div class="w-form-done"[^>]*>.*?</div>\s*</div>', tail, re.S)
    fail = re.search(r'<div class="w-form-fail"[^>]*>.*?</div>\s*</div>', tail, re.S)
    extra = ""
    if done:
        extra += done.group(0)
    if fail:
        extra += fail.group(0)
    return f'<h1 class="heading reservation-title">{title}</h1>\n{html[form_start:form_end]}\n{extra}'


def reservation_page(lang: str) -> str:
    prefix = PREFIX[lang]
    src_html = ARCHIVE_SOURCES[lang].read_text(encoding="utf-8", errors="replace")
    body = extract_form_body(src_html)
    body = rewrite_asset_paths(body, prefix)
    body = re.sub(
        r'(<div[^>]*if-step="Vehicule choice"[^>]*class="form_step)(")',
        r"\1 is-active\2",
        body,
        count=1,
    )
    page = PAGE_KEYS[lang]
    titles = {"fr": "Réservation", "de": "Reservierung", "en": "Reservation"}
    t = integrate.TRANSLATIONS[lang]
    return f"""<!DOCTYPE html>
<html lang="{'fr' if lang=='fr' else ('de' if lang=='de' else 'en')}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{titles[lang]} — {SITE['name']}</title>
  <meta name="description" content="{titles[lang]} {SITE['name']} — formulaire en ligne." />
  <link rel="canonical" href="{SITE['url']}/{page}" />
  <link rel="icon" href="{prefix}assets/favicon.png" type="image/png" />
  <link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png" />
  <link rel="stylesheet" href="{prefix}wp-content/themes/digital-present/front/build/assets/main-BGeNNPuO.css" />
  <link rel="stylesheet" href="{prefix}assets/reservation/cdn/css/nuskowcars-a76063.webflow.shared.4401e8879.css" />
  <style id="nuskow-reservation">{LANG_CSS}{BT_OVERRIDE}</style>
  <script src="{prefix}assets/reservation/jquery/jquery-3.5.1.min.dc5e7f18c8_bcee2273.js"></script>
</head>
<body>
{header_html(lang, page, prefix)}
<main class="reservation-page">
  <section class="section-reservation remove-canvas">
    {body}
  </section>
</main>
{footer_html(lang, prefix)}
<script src="{prefix}assets/reservation/cdn/js/webflow.schunk.36b8fb49256177c8.js"></script>
<script src="{prefix}assets/reservation/cdn/js/webflow.schunk.b4d22231aff0ace7.js"></script>
<script src="{prefix}assets/reservation/cdn/js/webflow.8681f271.6361df568e788d72.js"></script>
<script src="{prefix}assets/reservation/reservation-steps.js"></script>
</body>
</html>"""


def main():
    print("Copying reservation assets...")
    copy_reservation_assets()
    for lang, out in OUTPUTS.items():
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(reservation_page(lang), encoding="utf-8")
        print("Wrote", out)


if __name__ == "__main__":
    main()
