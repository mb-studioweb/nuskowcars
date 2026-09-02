#!/usr/bin/env python3
"""Intègre le contenu NuskowCars dans le template btcar75."""
from __future__ import annotations

import json
import re
import shutil
from html import escape, unescape
from pathlib import Path
from urllib.parse import quote

ROOT = Path("/workspace")
ARCHIVE = ROOT / "archive/nuskowcars-original-20250902"
ASSETS = ROOT / "assets"
CDN = ARCHIVE / "assets/cdn.prod.website-files.com"

SITE = {
    "name": "NuskowCars",
    "url": "https://www.nuskowcars-gmbh.com",
    "phone": "06 37 00 20 45",
    "phone_tel": "+33637002045",
    "wa": "33637002045",
    "instagram": "https://www.instagram.com/nuskowcars/",
    "snapchat": "https://snapchat.com/t/FrTH4qct",
    "location": "France",
}

VEHICLES = [
    {
        "slug": "audi-rs3-2024",
        "title": "Audi RS3 2024",
        "brand": "Audi",
        "category": "Sportive compacte",
        "power": "400 ch",
        "price_24h": "dès 299 €",
        "deposit": "6 000 €",
        "hero_title": "AUDI RS3",
        "tag": "Sportive · France",
        "desc_short": "Compacte ultra-sportive, 400 ch pour des sensations immédiates.",
        "desc_long": "L'Audi RS3 2024 allie agilité urbaine et performances de supercar compacte. Idéale pour un essai au volant ou un week-end sportif, avec kilométrage flexible selon formule.",
        "pricing": [
            ("24h semaine (250 km)", "299 €"),
            ("24h semaine (illimité)", "399 €"),
            ("48h week-end", "900 €"),
            ("72h", "1 100 €"),
            ("7 jours", "1 770 €"),
        ],
        "on_demand": False,
    },
    {
        "slug": "audi-rs6-performance",
        "title": "Audi RS6 Performance",
        "brand": "Audi",
        "category": "Break sportif",
        "power": "635 ch",
        "price_24h": "dès 999 €",
        "deposit": "10 000 €",
        "hero_title": "AUDI RS6",
        "tag": "Break sportif · France",
        "desc_short": "Le break le plus radical : 635 ch et polyvalence absolue.",
        "desc_long": "L'Audi RS6 Performance incarne le break sportif ultime. Puissance, espace et confort pour voyager vite et loin, en toute discrétion.",
        "pricing": [
            ("24h semaine (illimité)", "999 €"),
            ("24h week-end", "1 100 €"),
            ("48h week-end", "1 900 €"),
        ],
        "on_demand": True,
    },
    {
        "slug": "audi-rsq8-apr-2023",
        "title": "Audi RSQ8 APR 2023",
        "brand": "Audi",
        "category": "SUV sportif",
        "power": "720 ch",
        "price_24h": "dès 499 €",
        "deposit": "10 000 €",
        "hero_title": "AUDI RSQ8",
        "tag": "SUV sportif · France",
        "desc_short": "SUV de 720 ch préparé APR — présence et performances extrêmes.",
        "desc_long": "L'Audi RSQ8 APR 2023 combine l'espace d'un SUV de luxe avec la puissance d'une supercar. Parfait pour les déplacements en groupe sans compromis sur les performances.",
        "pricing": [
            ("24h semaine (250 km)", "499 €"),
            ("24h semaine (illimité)", "699 €"),
            ("24h week-end (250 km)", "1 000 €"),
            ("24h week-end (illimité)", "1 300 €"),
            ("48h week-end", "1 900 €"),
            ("72h", "2 300 €"),
            ("7 jours", "3 800 €"),
        ],
        "on_demand": False,
    },
    {
        "slug": "bmw-m3-competition-510ch-2025",
        "title": "BMW M3 Compétition 2025",
        "brand": "BMW",
        "category": "Berline sportive",
        "power": "510 ch",
        "price_24h": "dès 399 €",
        "deposit": "8 000 €",
        "hero_title": "BMW M3",
        "tag": "Berline sportive · France",
        "desc_short": "La référence berline sportive : 510 ch et châssis affûté.",
        "desc_long": "La BMW M3 Compétition 2025 offre le meilleur de la sportivité allemande : précision, puissance et quotidien possible. Location idéale pour événements ou plaisir de conduite.",
        "pricing": [
            ("24h semaine (250 km)", "399 €"),
            ("24h semaine (illimité)", "499 €"),
            ("48h week-end", "1 200 €"),
            ("72h", "1 400 €"),
            ("7 jours", "2 200 €"),
        ],
        "on_demand": False,
    },
    {
        "slug": "ferrari-488",
        "title": "Ferrari 488",
        "brand": "Ferrari",
        "category": "Supercar",
        "power": "670 ch",
        "price_24h": "dès 1 850 €",
        "deposit": "10 000 €",
        "hero_title": "FERRARI 488",
        "tag": "Supercar · France",
        "desc_short": "L'icône italienne : V8 biturbo et émotions pures.",
        "desc_long": "La Ferrari 488 représente l'excellence de Maranello. Une supercar mythique pour les moments d'exception, disponible sur demande.",
        "pricing": [
            ("24h semaine (illimité)", "1 850 €"),
            ("24h week-end", "2 000 €"),
        ],
        "on_demand": True,
    },
    {
        "slug": "lamborghini-huracan-evo",
        "title": "Lamborghini Huracán Evo",
        "brand": "Lamborghini",
        "category": "Supercar",
        "power": "640 ch",
        "price_24h": "dès 1 750 €",
        "deposit": "10 000 €",
        "hero_title": "HURACÁN EVO",
        "tag": "Supercar · France",
        "desc_short": "V10 atmosphérique et design acéré — l'émotion Lamborghini.",
        "desc_long": "La Huracán Evo incarne l'ADN sportif de Lamborghini. Lignes agressives, V10 et sensations immédiates pour vivre la route autrement.",
        "pricing": [
            ("24h semaine", "1 750 €"),
            ("24h week-end", "1 900 €"),
            ("48h week-end", "3 500 €"),
        ],
        "on_demand": False,
    },
    {
        "slug": "lamborghini-urus",
        "title": "Lamborghini Urus",
        "brand": "Lamborghini",
        "category": "SUV super sport",
        "power": "650 ch",
        "price_24h": "dès 1 800 €",
        "deposit": "10 000 €",
        "hero_title": "URUS",
        "tag": "SUV super sport · France",
        "desc_short": "Le SUV le plus extrême : 650 ch et présence inégalée.",
        "desc_long": "Le Lamborghini Urus redéfinit le SUV de luxe avec des performances de supercar. Idéal pour voyager à plusieurs sans renoncer à l'exceptionnel.",
        "pricing": [
            ("24h semaine", "1 800 €"),
            ("24h week-end", "2 000 €"),
            ("48h week-end", "3 500 €"),
        ],
        "on_demand": False,
    },
    {
        "slug": "lamborghini-urus-2",
        "title": "Lamborghini Urus Performante",
        "brand": "Lamborghini",
        "category": "SUV super sport",
        "power": "666 ch",
        "price_24h": "dès 2 000 €",
        "deposit": "10 000 €",
        "hero_title": "URUS PERFORMANTE",
        "tag": "SUV super sport · France",
        "desc_short": "Version Performante : encore plus affûtée, 666 ch.",
        "desc_long": "L'Urus Performante pousse l'extrême encore plus loin. Châssis optimisé, puissance accrue et présence maximale pour les événements d'exception.",
        "pricing": [
            ("24h semaine (illimité)", "2 000 €"),
            ("24h week-end (illimité)", "2 500 €"),
            ("48h week-end (illimité)", "4 000 €"),
        ],
        "on_demand": False,
    },
    {
        "slug": "mercedes-benz-g63-amg",
        "title": "Mercedes-Benz G63 AMG",
        "brand": "Mercedes-Benz",
        "category": "SUV iconique",
        "power": "585 ch",
        "price_24h": "dès 699 €",
        "deposit": "10 000 €",
        "hero_title": "G63 AMG",
        "tag": "SUV iconique · France",
        "desc_short": "Le G-Class légendaire version AMG — présence et puissance.",
        "desc_long": "Le Mercedes-Benz G63 AMG est une icône indémodable. 585 ch dans un châssis mythique, pour une expérience unique sur route ou en ville.",
        "pricing": [
            ("24h semaine (250 km)", "699 €"),
            ("24h semaine (illimité)", "999 €"),
            ("24h week-end", "1 300 €"),
            ("48h week-end", "2 200 €"),
            ("72h", "2 800 €"),
            ("7 jours", "4 500 €"),
        ],
        "on_demand": False,
    },
    {
        "slug": "mercedes-benz-gle63s-amg-coupe",
        "title": "Mercedes GLE 63 S AMG Coupé",
        "brand": "Mercedes-Benz",
        "category": "SUV coupé sportif",
        "power": "585 ch",
        "price_24h": "dès 499 €",
        "deposit": "10 000 €",
        "hero_title": "GLE 63 S",
        "tag": "SUV coupé · France",
        "desc_short": "Élégance coupé et performances AMG dans un SUV premium.",
        "desc_long": "Le GLE 63 S AMG Coupé allie lignes fluides et moteur V8 biturbo. Confort, espace et sportivité pour vos déplacements haut de gamme.",
        "pricing": [
            ("24h semaine (250 km)", "499 €"),
            ("24h semaine (illimité)", "699 €"),
            ("24h week-end (250 km)", "1 000 €"),
            ("48h week-end", "1 900 €"),
            ("7 jours", "3 800 €"),
        ],
        "on_demand": False,
    },
    {
        "slug": "mercedes-gt63-amg",
        "title": "Mercedes GT63 AMG",
        "brand": "Mercedes-Benz",
        "category": "Grand tourisme",
        "power": "585 ch",
        "price_24h": "dès 1 400 €",
        "deposit": "10 000 €",
        "hero_title": "GT63 AMG",
        "tag": "Grand tourisme · France",
        "desc_short": "Coupé 4 places ultra-performant signé AMG.",
        "desc_long": "Le Mercedes GT63 AMG combine grand tourisme et performances de supercar. Disponible sur demande pour vos événements et séjours d'exception.",
        "pricing": [
            ("24h semaine", "1 400 €"),
            ("24h week-end", "1 500 €"),
            ("48h week-end", "2 700 €"),
        ],
        "on_demand": True,
    },
    {
        "slug": "mercedes-gt63s-eperformance",
        "title": "Mercedes GT 63 S E-Performance",
        "brand": "Mercedes-Benz",
        "category": "Hybride performance",
        "power": "805 ch",
        "price_24h": "dès 699 €",
        "deposit": "10 000 €",
        "hero_title": "GT 63 S E-PERF",
        "tag": "Hybride · France",
        "desc_short": "805 ch hybrides — le summum de la technologie AMG.",
        "desc_long": "Le GT 63 S E-Performance repousse les limites avec 805 ch hybrides. Accélérations fulgurantes et technologie de pointe pour une expérience inoubliable.",
        "pricing": [
            ("24h semaine", "699 €"),
            ("24h week-end", "1 300 €"),
            ("48h week-end", "2 200 €"),
        ],
        "on_demand": False,
    },
    {
        "slug": "mercedes-benz-cla45s-amg",
        "title": "Mercedes-Benz CLA45S AMG",
        "brand": "Mercedes-Benz",
        "category": "Berline sportive",
        "power": "520 ch",
        "price_24h": "dès 299 €",
        "deposit": "6 000 €",
        "hero_title": "CLA45S AMG",
        "tag": "Berline sportive · France",
        "desc_short": "Compacte sportive 520 ch — performances et élégance au quotidien.",
        "desc_long": "La Mercedes-Benz CLA45S AMG combine design coupé et moteur AMG de 520 ch. Idéale pour un essai sportif ou une location courte, avec formules flexibles.",
        "pricing": [
            ("24h semaine (250 km)", "299 €"),
            ("24h semaine (illimité)", "399 €"),
            ("48h week-end", "1 500 €"),
            ("72h", "1 900 €"),
        ],
        "on_demand": False,
    },
]

LANG_CSS = """
.header__lang{display:flex;align-items:center;gap:.35rem;margin-right:.75rem}
.header__lang a{font-size:1.1rem;line-height:1;opacity:.55;transition:opacity .2s,transform .2s;text-decoration:none}
.header__lang a:hover,.header__lang a.is-active{opacity:1;transform:scale(1.1)}
@media(max-width:48em){.header__lang{margin-right:.25rem}.header__lang a{font-size:1rem}}
"""

TRANSLATIONS = {
    "fr": {
        "home": "Accueil", "about": "À propos", "about_sub": "L'agence", "fleet": "Flotte",
        "fleet_sub": "Nos véhicules", "faq": "FAQ", "faq_sub": "Questions fréquentes",
        "contact": "Contact", "whatsapp": "WhatsApp", "back_fleet": "← Retour à la flotte",
        "gallery": "Galerie", "pricing_title": "Tarifs de location", "deposit": "Caution",
        "pricing_note": "Tarifs indicatifs. Disponibilité et conditions confirmées sur WhatsApp selon vos dates.",
        "reserve_wa": "Réserver sur WhatsApp", "see_fleet": "Voir la flotte", "see_sheet": "Voir la fiche",
        "24h_week": "24h semaine", "rights": "Tous droits réservés.",
        "hero_sub": "Location de prestige", "hero_h1_sub": "Louez votre", "hero_h1_main": "véhicule de rêve",
        "hero_desc": "Chez NuskowCars — louez l'excellence, conduisez l'émotion.",
        "fleet_preview": "Aperçu de la flotte", "fleet_page_title": "NOTRE FLOTTE",
        "on_demand": "Sur demande",
        "reservation": "Réservation",
        "reservation_sub": "En ligne",
    },
    "de": {
        "home": "Startseite", "about": "Über uns", "about_sub": "Die Agentur", "fleet": "Flotte",
        "fleet_sub": "Unsere Fahrzeuge", "faq": "FAQ", "faq_sub": "Häufige Fragen",
        "contact": "Kontakt", "whatsapp": "WhatsApp", "back_fleet": "← Zurück zur Flotte",
        "gallery": "Galerie", "pricing_title": "Mietpreise", "deposit": "Kaution",
        "pricing_note": "Indikative Preise. Verfügbarkeit und Bedingungen werden per WhatsApp bestätigt.",
        "reserve_wa": "Per WhatsApp buchen", "see_fleet": "Flotte ansehen", "see_sheet": "Details ansehen",
        "24h_week": "24h Wochentag", "rights": "Alle Rechte vorbehalten.",
        "hero_sub": "Premium-Vermietung", "hero_h1_sub": "Mieten Sie Ihr", "hero_h1_main": "Traumauto",
        "hero_desc": "Bei NuskowCars — Exzellenz mieten, Emotionen fahren.",
        "fleet_preview": "Flottenübersicht", "fleet_page_title": "UNSERE FLOTTE",
        "on_demand": "Auf Anfrage",
        "reservation": "Reservierung",
        "reservation_sub": "Online",
    },
    "en": {
        "home": "Home", "about": "About", "about_sub": "The agency", "fleet": "Fleet",
        "fleet_sub": "Our vehicles", "faq": "FAQ", "faq_sub": "Frequently asked questions",
        "contact": "Contact", "whatsapp": "WhatsApp", "back_fleet": "← Back to fleet",
        "gallery": "Gallery", "pricing_title": "Rental rates", "deposit": "Deposit",
        "pricing_note": "Indicative rates. Availability and terms confirmed via WhatsApp.",
        "reserve_wa": "Book on WhatsApp", "see_fleet": "View fleet", "see_sheet": "View details",
        "24h_week": "24h weekday", "rights": "All rights reserved.",
        "hero_sub": "Premium rental", "hero_h1_sub": "Rent your", "hero_h1_main": "dream car",
        "hero_desc": "At NuskowCars — rent excellence, drive emotion.",
        "fleet_preview": "Fleet preview", "fleet_page_title": "OUR FLEET",
        "on_demand": "On request",
        "reservation": "Reservation",
        "reservation_sub": "Online",
    },
}


def strip_tags(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", unescape(s))).strip()


def prefix_paths(html: str, prefix: str) -> str:
    if not prefix:
        return html
    for p in ("assets/", "wp-content/", "wp-includes/"):
        html = html.replace(f'"{p}', f'"{prefix}{p}')
        html = html.replace(f"('{p}", f"('{prefix}{p}")
    # internal page links
    for page in ("index.html", "flotte.html", "a-propos.html", "faq.html", "german.html", "en.html"):
        html = html.replace(f'href="{page}"', f'href="{prefix}{page}"')
    html = html.replace('href="vehicules/', f'href="{prefix}vehicules/')
    return html


def wa_link(text: str, lang: str = "fr") -> str:
    msg = quote(text)
    return f"https://wa.me/{SITE['wa']}?text={msg}"


def lang_links(current: str, page: str, prefix: str = "") -> str:
    pages = {
        "fr": {"index": "index.html", "flotte": "flotte.html", "about": "a-propos.html", "faq": "faq.html", "reservation": "reservation.html"},
        "de": {"index": "german.html", "flotte": "german/flotte.html", "about": "german/a-propos.html", "faq": "german/faq.html", "reservation": "german/reservation.html"},
        "en": {"index": "en.html", "flotte": "en/flotte.html", "about": "en/a-propos.html", "faq": "en/faq.html", "reservation": "en/reservation.html"},
    }
    vehicle_suffix = ""
    if page.startswith("vehicules/"):
        vehicle_suffix = page.split("/", 1)[1]
        page_key = "vehicules"
    else:
        page_key = {"index.html": "index", "flotte.html": "flotte", "a-propos.html": "about", "faq.html": "faq", "reservation.html": "reservation",
                    "german.html": "index", "en.html": "index"}.get(page, "index")

    def href(lang_code: str) -> str:
        if vehicle_suffix:
            if lang_code == "fr":
                return f"{prefix}vehicules/{vehicle_suffix}"
            return f"{prefix}{'german' if lang_code == 'de' else 'en'}/vehicules/{vehicle_suffix}"
        base = pages[lang_code][page_key]
        if prefix and lang_code == "fr":
            return prefix + base.replace("index.html", "index.html")
        if prefix and lang_code != "fr":
            return prefix + base
        return base

    flags = [("fr", "🇫🇷"), ("de", "🇩🇪"), ("en", "🇬🇧")]
    items = []
    for code, flag in flags:
        cls = " is-active" if code == current else ""
        items.append(f'<a href="{href(code)}" class="header__lang-link{cls}" hreflang="{code}" aria-label="{code.upper()}">{flag}</a>')
    return f'<div class="header__lang" aria-label="Langue">{"".join(items)}</div>'


def header_html(lang: str, page: str, prefix: str = "") -> str:
    t = TRANSLATIONS[lang]
    home = f"{prefix}index.html" if lang == "fr" else (f"{prefix}german.html" if lang == "de" else f"{prefix}en.html")
    sub = SITE["name"]
    return f"""    <header class="header">
      <div class="header__inner">
        <a href="{home}" class="a">
          <img src="{prefix}assets/logo.png" alt="{SITE['name']}" class="header__logo" />
        </a>
        <a href="{home}" class="header__title a">{SITE['name']}</a>
        <nav class="header__nav">
          {lang_links(lang, page, prefix)}
          <a href="https://wa.me/{SITE['wa']}" class="header-link a" target="_blank" rel="noopener">{t['contact']}</a>
          <button type="menu" class="toggle-btn">
            <div class="hamburger-icon"><span></span></div>
          </button>
        </nav>
      </div>
      <nav class="header__dropdown">
        <ul>
          <li class="header__li">
            <a class="header__a a" href="{home}">
              <span class="a-main anim-a">{t['home']}</span>
              <span class="a-sub anim-sub-a">{sub}</span>
            </a>
          </li>
          <li class="header__li">
            <a class="header__a a" href="{prefix}{'a-propos.html' if lang=='fr' else ('german/a-propos.html' if lang=='de' else 'en/a-propos.html')}">
              <span class="a-main anim-a">{t['about']}</span>
              <span class="a-sub anim-sub-a">{t['about_sub']}</span>
            </a>
          </li>
          <li class="header__li">
            <a class="header__a a" href="{prefix}{'flotte.html' if lang=='fr' else ('german/flotte.html' if lang=='de' else 'en/flotte.html')}">
              <span class="a-main anim-a">{t['fleet']}</span>
              <span class="a-sub anim-sub-a">{t['fleet_sub']}</span>
            </a>
          </li>
          <li class="header__li">
            <a class="header__a a" href="{prefix}{'reservation.html' if lang=='fr' else ('german/reservation.html' if lang=='de' else 'en/reservation.html')}">
              <span class="a-main anim-a">{t['reservation']}</span>
              <span class="a-sub anim-sub-a">{t['reservation_sub']}</span>
            </a>
          </li>
          <li class="header__li">
            <a class="header__a a" href="{prefix}{'faq.html' if lang=='fr' else ('german/faq.html' if lang=='de' else 'en/faq.html')}">
              <span class="a-main anim-a">{t['faq']}</span>
              <span class="a-sub anim-sub-a">{t['faq_sub']}</span>
            </a>
          </li>
        </ul>
        <div class="header__contact">
          <a href="https://wa.me/{SITE['wa']}" class="a contact-block" target="_blank" rel="noopener">
            <div class="txt"><p>{t['contact']}</p><p class="link" role="link">{t['whatsapp']}</p></div>
            <img src="{prefix}wp-content/themes/digital-present/front/build/assets/mail-_8aEdFii.png" alt="" />
          </a>
        </div>
      </nav>
    </header>"""


def footer_html(lang: str, prefix: str = "") -> str:
    t = TRANSLATIONS[lang]
    return f"""<footer class="footer footer-light">
\t<div class="footer__inner">
\t\t<div class="address-block">
\t\t\t<p>{SITE['name']}</p>
\t\t\t<address>© {SITE['name']} — {t['rights']}<br />{SITE['location']} · {SITE['phone']}</address>
\t\t</div>
\t\t<div class="social-links">
\t\t\t<a href="{SITE['instagram']}" target="_blank" rel="noopener">Ig</a>
\t\t\t<a href="{SITE['snapchat']}" target="_blank" rel="noopener">Snap</a>
\t\t\t<a href="https://wa.me/{SITE['wa']}" target="_blank" rel="noopener">Wa</a>
\t\t</div>
\t\t<div class="address-block">
\t\t\t<p>Powered by</p>
\t\t\t<a href="https://mb-studioweb.com" target="_blank" rel="noopener"><address>MB-StudioWeb</address></a>
\t\t</div>
\t</div>
</footer>"""


def vehicle_page(v: dict, lang: str = "fr", prefix: str = "") -> str:
    t = TRANSLATIONS[lang]
    slug = v["slug"]
    page_path = f"vehicules/{slug}.html"
    url = f"{SITE['url']}/{page_path}" if lang == "fr" else f"{SITE['url']}/{'german/' if lang=='de' else 'en/'}{page_path}"
    img = f"{prefix}assets/vehicules/{slug}/1.jpg"
    gallery_items = ""
    vdir = ASSETS / "vehicules" / slug
    imgs = sorted(vdir.glob("*.jpg")) if vdir.exists() else []
    if len(imgs) <= 1:
        gallery_items = f'<figure role="listitem"><img src="{prefix}assets/vehicules/{slug}/1.jpg" alt="{escape(v["title"])}" loading="lazy" /></figure>'
        grid_class = "vehicle-gallery__grid--single"
    else:
        for i, p in enumerate(imgs[:6], 1):
            gallery_items += f'<figure role="listitem"><img src="{prefix}assets/vehicules/{slug}/{p.name}" alt="{escape(v["title"])} — photo {i}" loading="lazy" /></figure>\n'
        grid_class = ""
    pricing_rows = "".join(
        f'<li><span>{escape(row[0])}</span><span>{escape(row[1])}</span></li>' for row in v["pricing"]
    )
    pricing_rows += f'<li class="is-caution"><span>{t["deposit"]}</span><span>{v["deposit"]}</span></li>'
    wa_text = f"Bonjour, je souhaite louer {v['title']} chez NuskowCars."
    if lang == "de":
        wa_text = f"Hallo, ich möchte den {v['title']} bei NuskowCars mieten."
    elif lang == "en":
        wa_text = f"Hello, I would like to rent the {v['title']} at NuskowCars."
    fleet_link = f"{prefix}{'flotte.html' if lang=='fr' else ('german/flotte.html' if lang=='de' else 'en/flotte.html')}"
    return f"""<!DOCTYPE html>
<html lang="{'fr' if lang=='fr' else ('de' if lang=='de' else 'en')}">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Location {escape(v['title'])} — {SITE['name']}</title>
    <meta name="description" content="Louez {escape(v['title'])} ({v['power']}) avec {SITE['name']}. Caution {v['deposit']}. Réservation WhatsApp." />
    <link rel="canonical" href="{url}" />
    <link rel="alternate" hreflang="fr-FR" href="{SITE['url']}/vehicules/{slug}.html" />
    <link rel="alternate" hreflang="de-DE" href="{SITE['url']}/german/vehicules/{slug}.html" />
    <link rel="alternate" hreflang="en" href="{SITE['url']}/en/vehicules/{slug}.html" />
    <meta property="og:site_name" content="{SITE['name']}" />
    <meta property="og:title" content="Location {escape(v['title'])} — {SITE['name']}" />
    <meta property="og:image" content="{SITE['url']}/assets/vehicules/{slug}/1.jpg" />
    <link rel="icon" href="{prefix}assets/favicon.png" type="image/png" />
    <link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png" />
    <link rel='stylesheet' href='{prefix}wp-content/themes/digital-present/front/build/assets/main-BGeNNPuO.css' type='text/css' media='all' />
    <style id="nuskow-vehicle">
.header__inner .header__logo{{display:block!important;height:clamp(2rem,4vw,2.75rem);width:auto;max-width:9rem;object-fit:contain}}
{LANG_CSS}
.hero__video-bg{{overflow:hidden;pointer-events:none;position:absolute;top:0;left:0;right:0;bottom:0;width:100%;height:105%;z-index:0}}
.hero__video-bg .hero__video,.hero__video-bg img{{width:100%;height:100%;object-fit:cover;display:block}}
.hero__video-bg::after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.4) 0%,rgba(0,0,0,.65) 100%)}}
.vehicle-hero{{position:relative;min-height:100vh;overflow:hidden}}
.vehicle-hero .hero__inner{{position:relative;z-index:1}}
.vehicle-back{{display:inline-flex;align-items:center;gap:.5rem;font-family:Geist Mono,monospace;font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;opacity:.75;margin-bottom:1.5rem}}
.vehicle-intro,.vehicle-pricing{{padding:clamp(4rem,8vw,7rem) 4rem;background:#fff;color:#000}}
.vehicle-intro__inner,.vehicle-pricing__inner{{max-width:56rem;margin:0 auto}}
.vehicle-intro__tag{{font-family:Geist Mono,monospace;font-size:.75rem;letter-spacing:.2em;text-transform:uppercase;opacity:.65;margin:0 0 1rem}}
.vehicle-intro__title{{font-family:Inter Tight,sans-serif;font-size:clamp(2rem,1rem + 4vw,3.25rem);font-weight:300;line-height:1.15;margin:0 0 1.5rem}}
.vehicle-intro__text{{font-family:Inter Tight,sans-serif;font-size:clamp(1rem,.85rem + .5vw,1.2rem);line-height:1.6;opacity:.88;margin:0}}
.vehicle-gallery{{padding:clamp(3rem,6vw,5rem) 4rem;background:#fff;color:#000}}
.vehicle-gallery h2{{font-family:Inter Tight,sans-serif;font-size:clamp(1.5rem,1rem + 2vw,2rem);font-weight:400;margin:0 0 2.5rem;text-align:center}}
.vehicle-gallery__grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.25rem;max-width:72rem;margin:0 auto}}
.vehicle-gallery__grid--single{{grid-template-columns:1fr;max-width:56rem}}
.vehicle-gallery__grid figure{{margin:0;border-radius:16px;overflow:hidden;aspect-ratio:16/10;background:#e8e8e8}}
.vehicle-gallery__grid img{{width:100%;height:100%;object-fit:cover;display:block}}
.vehicle-pricing h2{{font-family:Inter Tight,sans-serif;font-size:clamp(1.5rem,1rem + 2vw,2rem);font-weight:400;margin:0 0 2rem;text-align:center}}
.vehicle-pricing__list{{list-style:none;margin:0;padding:0;border-top:1px solid rgba(0,0,0,.12)}}
.vehicle-pricing__list li{{display:flex;justify-content:space-between;gap:2rem;padding:1.25rem 0;border-bottom:1px solid rgba(0,0,0,.12);font-family:Inter Tight,sans-serif}}
.vehicle-pricing__note{{text-align:center;margin-top:1.5rem;font-size:.875rem;opacity:.6}}
.vehicle-cta{{padding:clamp(3rem,6vw,5rem) 4rem 6rem;background:#000;color:#fff;text-align:center}}
.vehicle-cta__actions{{display:flex;flex-wrap:wrap;justify-content:center;gap:1rem}}
.vehicle-btn{{display:inline-flex;align-items:center;justify-content:center;min-width:11rem;height:3.25rem;padding:0 1.75rem;border-radius:999px;font-family:Inter Tight,sans-serif}}
.vehicle-btn--outline{{border:1px solid rgba(255,255,255,.35);color:#fff}}
.vehicle-btn--wa{{background:#fff;color:#111}}
</style>
    <script src="{prefix}wp-includes/js/jquery/jquery.min.js"></script>
  </head>
  <body>
{header_html(lang, page_path, prefix)}
<main>
  <div id="smooth-wrapper"><div id="smooth-content">
      <section class="hero main-hero vehicle-hero">
        <div class="hero__inner">
          <a href="{fleet_link}" class="a vehicle-back">{t['back_fleet']}</a>
          <p class="anim-fade-in small-description">{escape(v['tag'])}</p>
          <h1 class="main-text heading">{escape(v['hero_title'])}</h1>
        </div>
        <div class="hero__video-bg" aria-hidden="true">
          <img src="{img}" alt="{escape(v['title'])}" />
        </div>
      </section>
      <div class="color-change-break" data-header-color="black"></div>
      <section class="vehicle-intro remove-canvas">
        <div class="vehicle-intro__inner">
          <p class="vehicle-intro__tag">{SITE['name']} · {escape(v['brand'])} · {v['power']}</p>
          <h2 class="vehicle-intro__title">{escape(v['title'])}</h2>
          <p class="vehicle-intro__text">{escape(v['desc_long'])}</p>
        </div>
      </section>
      <section class="vehicle-gallery remove-canvas" aria-labelledby="vehicle-gallery-title">
        <h2 id="vehicle-gallery-title">{t['gallery']}</h2>
        <div class="vehicle-gallery__grid {grid_class}" role="list">{gallery_items}</div>
      </section>
      <section class="vehicle-pricing remove-canvas">
        <div class="vehicle-pricing__inner">
          <h2>{t['pricing_title']}</h2>
          <ul class="vehicle-pricing__list">{pricing_rows}</ul>
          <p class="vehicle-pricing__note">{t['pricing_note']}</p>
        </div>
      </section>
      <section class="vehicle-cta remove-canvas">
        <h2>{escape(v['title'])}</h2>
        <div class="vehicle-cta__actions">
          <a href="{fleet_link}" class="a vehicle-btn vehicle-btn--outline">{t['see_fleet']}</a>
          <a href="{wa_link(wa_text, lang)}" class="a vehicle-btn vehicle-btn--wa" target="_blank" rel="noopener">{t['reserve_wa']}</a>
        </div>
      </section>
{footer_html(lang, prefix)}
  </div></div>
</main>
<script src="{prefix}wp-content/themes/digital-present/front/build/assets/main-B2AruZ9N.js"></script>
</body>
</html>"""


def fleet_card(v: dict, t: dict, prefix: str = "", compact: bool = False) -> str:
    slug = v["slug"]
    desc = "" if compact else f'<p class="desc">{escape(v["desc_short"])}</p>'
    demand = f' · {t["on_demand"]}' if v.get("on_demand") else ""
    return f"""<article class="fleet-card">
  <div class="fleet-card__img"><img src="{prefix}assets/vehicules/{slug}/1.jpg" alt="{escape(v['title'])}" /></div>
  <div class="fleet-card__content">
    <p class="location">{escape(v['category'])}{demand}</p>
    <h3 class="title">{escape(v['title'])}</h3>
    {desc}
    <div class="fleet-pricing">
      <div class="fleet-pricing__item"><span class="fleet-pricing__label">{t['24h_week']}</span><span class="fleet-pricing__value">{v['price_24h']}</span></div>
      <div class="fleet-pricing__item"><span class="fleet-pricing__label">{t['deposit']}</span><span class="fleet-pricing__value">{v['deposit']}</span></div>
    </div>
    <a href="{prefix}vehicules/{slug}.html" class="a btn">{t['see_sheet']}</a>
  </div>
</article>"""


def fleet_list_item(v: dict, t: dict, prefix: str = "") -> str:
    slug = v["slug"]
    demand = f" · {t['on_demand']}" if v.get("on_demand") else ""
    wa = wa_link(f"Bonjour, je souhaite louer {v['title']} chez NuskowCars.")
    return f"""<article class="fleet-list__item">
  <div class="fleet-list__media"><img src="{prefix}assets/vehicules/{slug}/1.jpg" alt="{escape(v['title'])}" /></div>
  <div class="fleet-list__body">
    <p class="fleet-list__tag">{escape(v['category'])}{demand}</p>
    <h2 class="fleet-list__title">{escape(v['title'])}</h2>
    <p class="fleet-list__desc">{escape(v['desc_short'])} · {v['power']}</p>
    <div class="fleet-pricing">
      <div class="fleet-pricing__item"><span class="fleet-pricing__label">{t['24h_week']}</span><span class="fleet-pricing__value">{v['price_24h']}</span></div>
      <div class="fleet-pricing__item"><span class="fleet-pricing__label">{t['deposit']}</span><span class="fleet-pricing__value">{v['deposit']}</span></div>
    </div>
    <div class="fleet-list__actions">
      <a href="{prefix}vehicules/{slug}.html" class="a fleet-list__btn fleet-list__btn--outline">{t['see_sheet']}</a>
      <a href="{wa}" class="a fleet-list__btn fleet-list__btn--wa" target="_blank" rel="noopener">{t['reserve_wa']}</a>
    </div>
  </div>
</article>"""


def copy_branding_assets():
    logo_src = CDN / "666a07b245930cb23ff3b913/666a4156648b83c7d4054d94_Logo nuskow off-p-800.jpg"
    fav_src = CDN / "666a07b245930cb23ff3b913/6672e4cd45fb958c490406ca_mini 2.jpg"
    apple_src = CDN / "666a07b245930cb23ff3b913/6672e4689aebf2e4a633a119_minii.jpg"
    shutil.copy2(logo_src, ASSETS / "logo.png")
    shutil.copy2(fav_src, ASSETS / "favicon.png")
    shutil.copy2(apple_src, ASSETS / "apple-touch-icon.png")
    # hero video from archive LFS
    hero_vid = ARCHIVE / "assets/cdn.prod.website-files.com/666a07b245930cb23ff3b913/668801726c7ee14880ab8e85_vidéo background(1)(1)-transcode.mp4"
    if hero_vid.exists():
        shutil.copy2(hero_vid, ASSETS / "hero.mp4")
    # hero image from g63
    g63_img = list((CDN / "666bb9e682a568931397e7f9").glob("*_1.jpg"))
    if g63_img:
        shutil.copy2(g63_img[0], ASSETS / "1.jpg")
        shutil.copy2(g63_img[0], ASSETS / "hero-flotte.jpg")
        shutil.copy2(g63_img[0], ASSETS / "og-share.jpg")


def extract_vehicle_images(slug: str) -> list[str]:
    html = (ARCHIVE / "vehicules" / f"{slug}.html").read_text(encoding="utf-8", errors="replace")
    imgs = re.findall(r'src="(\.\./assets/[^"]+\.jpg)"', html)
    paths = []
    for i in imgs:
        if "-p-" in i or "poster" in i:
            continue
        rel = i.replace("../assets/", "")
        paths.append(rel)
    return list(dict.fromkeys(paths))[:6]


def copy_vehicle_assets():
    for v in VEHICLES:
        slug = v["slug"]
        dest = ASSETS / "vehicules" / slug
        dest.mkdir(parents=True, exist_ok=True)
        srcs = extract_vehicle_images(slug)
        for idx, rel in enumerate(srcs, 1):
            src = ARCHIVE / "assets" / rel
            if src.exists():
                shutil.copy2(src, dest / f"{idx}.jpg")


def replace_branding_in_file(path: Path):
    text = path.read_text(encoding="utf-8")
    reps = [
        ("BT CAR 75", SITE["name"]),
        ("btcar75.onrender.com", "www.nuskowcars-gmbh.com"),
        ("https://btcar75.onrender.com", SITE["url"]),
        ("33665535367", SITE["wa"]),
        ("https://www.instagram.com/btcar75/", SITE["instagram"]),
        ("https://www.snapchat.com/add/bt_car75", SITE["snapchat"]),
        ("https://www.facebook.com/share/1LsrMvBLzo/?mibextid=wwXIfr", SITE["instagram"]),
        ("Paris, France · FRA", f"{SITE['location']} · {SITE['phone']}"),
        ("à Paris", ""),
        (" — Paris", ""),
        (" · Paris", ""),
    ]
    for a, b in reps:
        text = text.replace(a, b)
    path.write_text(text, encoding="utf-8")


def build_sitemap():
    urls = [
        "/", "/flotte.html", "/a-propos.html", "/faq.html", "/reservation.html",
        "/german.html", "/german/flotte.html", "/german/a-propos.html", "/german/faq.html", "/german/reservation.html",
        "/en.html", "/en/flotte.html", "/en/a-propos.html", "/en/faq.html", "/en/reservation.html",
    ]
    for v in VEHICLES:
        urls.append(f"/vehicules/{v['slug']}.html")
        urls.append(f"/german/vehicules/{v['slug']}.html")
        urls.append(f"/en/vehicules/{v['slug']}.html")
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        lines.append(f"  <url><loc>{SITE['url']}{u if u != '/' else '/'}</loc><changefreq>weekly</changefreq></url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n", encoding="utf-8")


def branding_replacements(text: str) -> str:
    reps = [
        ("BT CAR 75", SITE["name"]),
        ("btcar75.onrender.com", "www.nuskowcars-gmbh.com"),
        ("https://btcar75.onrender.com", SITE["url"]),
        ("33665535367", SITE["wa"]),
        ("https://www.instagram.com/btcar75/", SITE["instagram"]),
        ("https://www.snapchat.com/add/bt_car75", SITE["snapchat"]),
        ("https://www.facebook.com/share/1LsrMvBLzo/?mibextid=wwXIfr", SITE["instagram"]),
        ("Paris, France · FRA", f"{SITE['location']} · {SITE['phone']}"),
        ("à Paris", "en France"),
        (" — Paris", ""),
        (" · Paris", ""),
        ("sur Paris", "partout en France"),
        ("en capitale", "sans limite"),
        ("Agence de location de prestige — Paris", "Location de véhicules de prestige — NuskowCars"),
        ("Location <b>haut de gamme</b>", "Louez votre <b>véhicule de rêve</b>"),
        (" à Paris ", ""),
        ("Un service réactif à Paris, pour chaque demande de location", "Prix attractifs, kilomètres illimités et livraison à domicile, aéroport ou gare"),
        ("Des locations haut de gamme pour chaque occasion à Paris", "Pourquoi choisir NuskowCars ?"),
        ("Prise en charge à Paris : véhicule préparé, contrat signé, vous prenez la route.", "Récupérez le véhicule ou profitez de la livraison : domicile, aéroport ou gare."),
        ("Le prestige sur Paris", "Louez l'excellence, conduisez l'émotion"),
        ("Le prestige", "NuskowCars"),
        ("SUR PARIS", ""),
        ("l'excellence automobile au service de vos déplacements parisiens.", "l'excellence automobile au service de vos déplacements."),
    ]
    for a, b in reps:
        text = text.replace(a, b)
    return text


def inject_lang_css(text: str) -> str:
    if LANG_CSS.strip() in text:
        return text
    return text.replace(
        ".header__inner .header__logo{display:block!important;",
        LANG_CSS + "\n.header__inner .header__logo{display:block!important;",
        1,
    )


def replace_header_footer(text: str, lang: str, page: str, prefix: str = "") -> str:
    text = re.sub(r"<header class=\"header\">.*?</header>", header_html(lang, page, prefix), text, count=1, flags=re.S)
    text = re.sub(r"<footer class=\"footer footer-light\">.*?</footer>", footer_html(lang, prefix), text, count=1, flags=re.S)
    return text


def featured_fleet_html(lang: str = "fr", prefix: str = "", compact: bool = False) -> str:
    t = TRANSLATIONS[lang]
    featured = [v for v in VEHICLES if not v.get("on_demand")][:6]
    return "\n".join(fleet_card(v, t, prefix, compact) for v in featured)


def mobile_fleet_html(lang: str = "fr", prefix: str = "") -> str:
    t = TRANSLATIONS[lang]
    featured = [v for v in VEHICLES if not v.get("on_demand")][:6]
    blocks = []
    for v in featured:
        blocks.append(f"""                        <div class="slider-projects__slide">
                            <div class="project-card">
                            <div class="project-card__img">
                                <img src="{prefix}assets/vehicules/{v['slug']}/1.jpg" alt="{escape(v['title'])}" />
                            </div>
                            <div class="project-card__content">
                                <p class="location">{escape(v['category'])}</p>
                                <h3 class="title">{escape(v['title'])}</h3>
                                <div class="fleet-pricing">
                                    <div class="fleet-pricing__item"><span class="fleet-pricing__label">{t['24h_week']}</span><span class="fleet-pricing__value">{v['price_24h']}</span></div>
                                    <div class="fleet-pricing__item"><span class="fleet-pricing__label">{t['deposit']}</span><span class="fleet-pricing__value">{v['deposit']}</span></div>
                                </div>
                                <a href="{prefix}vehicules/{v['slug']}.html" class="a btn">{t['see_sheet']}</a>
                            </div>
                            </div>
                        </div>""")
    return "\n".join(blocks)


def patch_index(path: Path, lang: str = "fr", prefix: str = ""):
    page = "index.html" if lang == "fr" else ("german.html" if lang == "de" else "en.html")
    text = path.read_text(encoding="utf-8")
    text = branding_replacements(text)
    text = inject_lang_css(text)
    text = replace_header_footer(text, lang, page, prefix)
    t = TRANSLATIONS[lang]

    if lang != "fr":
        text = text.replace("Louez votre <b>véhicule de rêve</b>", f"{t['hero_h1_sub']} <b>{t['hero_h1_main']}</b>")
        text = text.replace("Location de véhicules de prestige — NuskowCars", t["hero_desc"])
        text = text.replace("Aperçu de la flotte", t["fleet_preview"])
        text = text.replace("Voir la flotte", t["see_fleet"])

    text = re.sub(
        r'<div class="fleet-swiper__track">.*?</div>\s*<div class="fleet-swiper__dots"',
        f'<div class="fleet-swiper__track">\n{featured_fleet_html(lang, prefix)}\n                            </div>\n                        <div class="fleet-swiper__dots"',
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r'<section class="slider-projects fleet-preview" id="flotte-mobile">.*?<div class="slider-projects__controls">',
        f'<section class="slider-projects fleet-preview" id="flotte-mobile">\n                    <p class="related">{t["fleet_preview"]}</p>\n                    <div class="slider-projects__viewport">\n                        <div class="slider-projects__container">\n{mobile_fleet_html(lang, prefix)}\n                                                    </div>\n                        <div class="slider-projects__buttons">\n                        <button class="slider-projects__button slider-projects__button--prev" type="button" disabled=""><svg class="slider-projects__button__svg" viewBox="0 0 532 532"><path fill="currentColor" d="M355.66 11.354c13.793-13.805 36.208-13.805 50.001 0 13.785 13.804 13.785 36.238 0 50.034L201.22 266l204.442 204.61c13.785 13.805 13.785 36.239 0 50.044-13.793 13.796-36.208 13.796-50.002 0a5994246.277 5994246.277 0 0 0-229.332-229.454 35.065 35.065 0 0 1-10.326-25.126c0-9.2 3.393-18.26 10.326-25.2C172.192 194.973 332.731 34.31 355.66 11.354Z"></path></svg></button><button class="slider-projects__button slider-projects__button--next" type="button" disabled=""><svg class="slider-projects__button__svg" viewBox="0 0 532 532"><path fill="currentColor" d="M176.34 520.646c-13.793 13.805-36.208 13.805-50.001 0-13.785-13.804-13.785-36.238 0-50.034L330.78 266 126.34 61.391c-13.785-13.805-13.785-36.239 0-50.044 13.793-13.796 36.208-13.796 50.002 0 22.928 22.947 206.395 206.507 229.332 229.454a35.065 35.065 0 0 1 10.326 25.126c0 9.2-3.393 18.26-10.326 25.2-45.865 45.901-206.404 206.564-229.332 229.52Z"></path></svg></button></div></div>\n                    <div class="slider-projects__controls">',
        text,
        count=1,
        flags=re.S,
    )

    # Pop-up gallery images
    gallery_imgs = [f"assets/vehicules/{v['slug']}/1.jpg" for v in VEHICLES[:6]]
    for i, img in enumerate(gallery_imgs):
        text = re.sub(rf'<div class="media"><img src="assets/[^"]+" alt="[^"]*" /></div>', f'<div class="media"><img src="{prefix}{img}" alt="{SITE["name"]}" /></div>', text, count=1)
    for img in gallery_imgs:
        text = re.sub(rf'<img src="assets/[^"]+" alt="[^"]*" />', f'<img src="{prefix}{img}" alt="{SITE["name"]}" />', text, count=1)

    # Content section Nuskow
    if lang == "fr":
        text = re.sub(
            r'<p class="content-section__description">.*?</p>',
            """<p class="content-section__description">
                    Chez NuskowCars, nous proposons des prix attractifs, des kilomètres illimités sur de nombreuses formules et la livraison de votre véhicule à domicile, à l'aéroport ou en gare.
                    <br><br>Profitez aussi de nos offres du moment : essais au volant, promotions (-25&nbsp;% du mardi au jeudi) et une flotte de sportives, SUV et supercars soigneusement entretenue.
                </p>""",
            text,
            count=1,
            flags=re.S,
        )
        text = text.replace(
            "BT CAR 75 propose une flotte d'exception pour vos mariages, événements privés, déplacements professionnels et escapades en capitale. Chaque véhicule est sélectionné pour son confort, sa présence et la qualité de conduite qu'il offre.",
            "",
        )

    # Morph slider background images
    morph_imgs = [f"{prefix}assets/vehicules/{v['slug']}/1.jpg" for v in VEHICLES[:4]]
    for old_pat in ["g800-brabus/1.jpg", "audi-rs6/1.jpg", "Lamborghini-Huracan-Tecnica/1.jpg", "sl63s/1.jpg"]:
        if morph_imgs:
            text = text.replace(old_pat, morph_imgs.pop(0).replace(f"{prefix}assets/", "assets/") if not prefix else morph_imgs[-1], 1)

    text = text.replace('alt="G800 Brabus"', f'alt="{SITE["name"]}"')
    text = text.replace('alt="Audi RS6"', f'alt="{SITE["name"]}"')
    text = text.replace('alt="Lamborghini Huracán Tecnica"', f'alt="{SITE["name"]}"')

    if lang == "de":
        text = text.replace("<html lang=\"fr\">", '<html lang="de">')
        text = text.replace("NuskowCars — Location de véhicules haut de gamme", "NuskowCars — Premium-Fahrzeugvermietung")
    elif lang == "en":
        text = text.replace("<html lang=\"fr\">", '<html lang="en">')
        text = text.replace("NuskowCars — Location de véhicules haut de gamme", "NuskowCars — Premium car rental")

    path.write_text(text, encoding="utf-8")


def patch_flotte(path: Path, lang: str = "fr", prefix: str = ""):
    page = "flotte.html" if lang == "fr" else f"{'german' if lang=='de' else 'en'}/flotte.html"
    text = path.read_text(encoding="utf-8")
    text = branding_replacements(text)
    text = inject_lang_css(text)
    text = replace_header_footer(text, lang, page, prefix)
    t = TRANSLATIONS[lang]
    text = text.replace("NOTRE FLOTTE", t["fleet_page_title"])
    text = text.replace("Location de prestige — Paris", t["hero_sub"])
    items = "\n".join(fleet_list_item(v, t, prefix) for v in VEHICLES)
    text = re.sub(
        r'<section class="fleet-list remove-canvas" aria-label="[^"]*">.*?</section>',
        f'<section class="fleet-list remove-canvas" aria-label="Véhicules disponibles">\n\n{items}\n\n      </section>',
        text,
        count=1,
        flags=re.S,
    )
    text = text.replace("assets/hero-fotte.jpg", f"{prefix}assets/hero-fotte.jpg")
    if lang == "de":
        text = text.replace("<html lang=\"fr\">", '<html lang="de">')
    elif lang == "en":
        text = text.replace("<html lang=\"fr\">", '<html lang="en">')
    path.write_text(text, encoding="utf-8")


def patch_about(path: Path, lang: str = "fr", prefix: str = ""):
    page = "a-propos.html" if lang == "fr" else f"{'german' if lang=='de' else 'en'}/a-propos.html"
    text = path.read_text(encoding="utf-8")
    text = branding_replacements(text)
    text = inject_lang_css(text)
    text = replace_header_footer(text, lang, page, prefix)
    if lang == "fr":
        text = re.sub(
            r'<p class="content-section__description">.*?</p>',
            """<p class="content-section__description">
                    NuskowCars est spécialisée dans la location de véhicules de prestige : sportives, SUV, supercars et modèles AMG. Notre mission : vous offrir des prix attractifs, du kilométrage illimité sur de nombreuses formules et un service de livraison flexible.
                </p>""",
            text,
            count=1,
            flags=re.S,
        )
        text = text.replace("assets/g800-brabus/video.mp4", f"{prefix}assets/hero.mp4")
        text = text.replace('type="video/mp4"', 'type="video/mp4"')
    if lang == "de":
        text = text.replace("<html lang=\"fr\">", '<html lang="de">')
        text = text.replace("À PROPOS", "ÜBER UNS")
    elif lang == "en":
        text = text.replace("<html lang=\"fr\">", '<html lang="en">')
        text = text.replace("À PROPOS", "ABOUT US")
    path.write_text(text, encoding="utf-8")


def patch_faq(path: Path, lang: str = "fr", prefix: str = ""):
    page = "faq.html" if lang == "fr" else f"{'german' if lang=='de' else 'en'}/faq.html"
    text = path.read_text(encoding="utf-8")
    text = branding_replacements(text)
    text = inject_lang_css(text)
    text = replace_header_footer(text, lang, page, prefix)
    text = text.replace("assets/Lamborghini-Huracan-Tecnica/video.mp4", f"{prefix}assets/hero.mp4")
    text = text.replace("Comment réserver un véhicule chez NuskowCars ?", "Comment réserver un véhicule chez NuskowCars ?")
    text = text.replace(
        "Une pièce d'identité valide et un permis de conduire en cours de validité sont requis. Selon le véhicule, des justificatifs complémentaires peuvent vous être demandés lors de la confirmation.",
        "Un permis de conduire valide depuis au moins 2,5 ans (5 ans pour certaines supercars) et une pièce d'identité sont requis. La caution peut être versée par virement, chèque, espèces ou garantie véhicule (valeur minimale 8 000 à 15 000 € selon modèle).",
    )
    text = text.replace(
        "La prise en charge s'organise à Paris. Le lieu exact et les horaires sont définis avec vous lors de la confirmation, selon le véhicule et la durée de location.",
        "NuskowCars propose la livraison à domicile, à l'aéroport ou en gare. Le lieu et les horaires sont définis avec vous lors de la confirmation.",
    )
    text = text.replace(
        "Oui. Nous accompagnons les mariages, soirées privées, tournages et événements professionnels à Paris et en région parisienne. Précisez votre usage lors de votre demande sur WhatsApp.",
        "Oui. Nous accompagnons mariages, soirées privées, tournages et événements professionnels. Précisez votre usage lors de votre demande sur WhatsApp.",
    )
    if lang == "de":
        text = text.replace("<html lang=\"fr\">", '<html lang="de">')
    elif lang == "en":
        text = text.replace("<html lang=\"fr\">", '<html lang="en">')
    path.write_text(text, encoding="utf-8")


def create_lang_copies():
    shutil.copy2(ROOT / "index.html", ROOT / "german.html")
    shutil.copy2(ROOT / "index.html", ROOT / "en.html")
    (ROOT / "german").mkdir(exist_ok=True)
    (ROOT / "en").mkdir(exist_ok=True)
    for name in ("flotte.html", "a-propos.html", "faq.html"):
        shutil.copy2(ROOT / name, ROOT / "german" / name)
        shutil.copy2(ROOT / name, ROOT / "en" / name)


def main():
    print("Copying assets...")
    copy_branding_assets()
    copy_vehicle_assets()
    if (ASSETS / "hero-flotte.jpg").exists():
        shutil.copy2(ASSETS / "hero-flotte.jpg", ASSETS / "hero-fotte.jpg")

    for old in ["g800-brabus.html", "audi-rs6.html", "lamborghini-huracan-tecnica.html", "mercedes-sl63s-amg.html"]:
        p = ROOT / old
        if p.exists():
            p.unlink()
    for old_dir in ["g800-brabus", "audi-rs6", "Lamborghini-Huracan-Tecnica", "sl63s"]:
        d = ASSETS / old_dir
        if d.exists():
            shutil.rmtree(d)

    veh_dir = ROOT / "vehicules"
    veh_dir.mkdir(exist_ok=True)
    for v in VEHICLES:
        (veh_dir / f"{v['slug']}.html").write_text(vehicle_page(v, "fr", "../"), encoding="utf-8")
    for lang in ("de", "en"):
        lang_veh = ROOT / ("german" if lang == "de" else "en") / "vehicules"
        lang_veh.mkdir(parents=True, exist_ok=True)
        for v in VEHICLES:
            (lang_veh / f"{v['slug']}.html").write_text(vehicle_page(v, lang, "../../"), encoding="utf-8")

    print("Patching FR main pages...")
    patch_index(ROOT / "index.html", "fr")
    patch_flotte(ROOT / "flotte.html", "fr")
    patch_about(ROOT / "a-propos.html", "fr")
    patch_faq(ROOT / "faq.html", "fr")

    print("Creating DE/EN copies...")
    create_lang_copies()
    patch_index(ROOT / "german.html", "de")
    patch_index(ROOT / "en.html", "en", "")
    patch_flotte(ROOT / "german" / "flotte.html", "de", "../")
    patch_flotte(ROOT / "en" / "flotte.html", "en", "../")
    patch_about(ROOT / "german" / "a-propos.html", "de", "../")
    patch_about(ROOT / "en" / "a-propos.html", "en", "../")
    patch_faq(ROOT / "german" / "faq.html", "de", "../")
    patch_faq(ROOT / "en" / "faq.html", "en", "../")

    build_sitemap()
    print("Integration complete.")


if __name__ == "__main__":
    main()
