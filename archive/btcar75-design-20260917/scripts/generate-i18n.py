#!/usr/bin/env python3
"""Génère locales.js et patche le site pour i18n single-URL."""

from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
I18N_DIR = ROOT / "assets" / "i18n"

_spec = importlib.util.spec_from_file_location("integrate", ROOT / "scripts" / "integrate-nuskow.py")
integrate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(integrate)

_spec2 = importlib.util.spec_from_file_location("perfs", ROOT / "scripts" / "patch-vehicle-perfs.py")
perfs_mod = importlib.util.module_from_spec(_spec2)
_spec2.loader.exec_module(perfs_mod)

PERFS = dict(perfs_mod.PERFS)
PERFS["mercedes-gt63s-eperformance"] = ("805 ch", "2,8 s", "315 km/h")

VEHICLE_I18N = {
    "mercedes-benz-g63-amg": {
        "de": {
            "category": "Ikonscher SUV",
            "tag": "Ikonscher SUV · Frankreich",
            "desc_short": "Die legendäre G-Class als AMG — Präsenz und Power.",
            "desc_long": "Der Mercedes-Benz G63 AMG ist eine zeitlose Ikone. 585 PS im mythischen Chassis — ein einzigartiges Erlebnis auf Straße und in der Stadt.",
        },
        "en": {
            "category": "Iconic SUV",
            "tag": "Iconic SUV · France",
            "desc_short": "The legendary G-Class AMG — presence and power.",
            "desc_long": "The Mercedes-Benz G63 AMG is a timeless icon. 585 hp in a legendary chassis for a unique on-road experience.",
        },
    },
    "mercedes-benz-gle63s-amg-coupe": {
        "de": {
            "category": "Sport-SUV-Coupé",
            "tag": "SUV-Coupé · Frankreich",
            "desc_short": "Coupé-Eleganz und AMG-Performance in einem Premium-SUV.",
            "desc_long": "Das GLE 63 S AMG Coupé vereint fließende Linien und V8-Biturbo. Komfort, Raum und Sportlichkeit für anspruchsvolle Fahrten.",
        },
        "en": {
            "category": "Sport SUV coupé",
            "tag": "SUV coupé · France",
            "desc_short": "Coupé elegance and AMG performance in a premium SUV.",
            "desc_long": "The GLE 63 S AMG Coupé blends fluid lines with a twin-turbo V8. Comfort, space and sportiness for premium travel.",
        },
    },
    "audi-rs3-2024": {
        "de": {
            "category": "Kompaktsportler",
            "tag": "Sportwagen · Frankreich",
            "desc_short": "Ultrasportliche Kompakte mit 400 PS für sofortige Emotionen.",
            "desc_long": "Der Audi RS3 2024 verbindet urbane Agilität mit Supercar-Performance. Ideal für Probefahrten oder sportliche Wochenenden.",
        },
        "en": {
            "category": "Compact sports car",
            "tag": "Sports car · France",
            "desc_short": "Ultra-sporty compact with 400 hp for instant thrills.",
            "desc_long": "The Audi RS3 2024 combines urban agility with supercar performance. Ideal for test drives or sporty weekends.",
        },
    },
    "bmw-m3-competition-510ch-2025": {
        "de": {
            "category": "Sportlimousine",
            "tag": "Sportlimousine · Frankreich",
            "desc_short": "Die Sportlimousinen-Referenz: 510 PS und präzises Fahrwerk.",
            "desc_long": "Die BMW M3 Competition 2025 bietet deutsche Sportlichkeit in Perfektion — Präzision, Power und Alltagstauglichkeit.",
        },
        "en": {
            "category": "Sport sedan",
            "tag": "Sport sedan · France",
            "desc_short": "The sport sedan benchmark: 510 hp and a sharp chassis.",
            "desc_long": "The BMW M3 Competition 2025 delivers the best of German sportiness — precision, power and everyday usability.",
        },
    },
    "audi-rsq8-apr-2023": {
        "de": {
            "category": "Sport-SUV",
            "tag": "Sport-SUV · Frankreich",
            "desc_short": "720 PS APR-SUV — extreme Präsenz und Performance.",
            "desc_long": "Der Audi RSQ8 APR 2023 vereint Luxus-SUV-Raum mit Supercar-Power. Perfekt für Gruppenfahrten ohne Kompromisse.",
        },
        "en": {
            "category": "Sport SUV",
            "tag": "Sport SUV · France",
            "desc_short": "720 hp APR SUV — extreme presence and performance.",
            "desc_long": "The Audi RSQ8 APR 2023 combines luxury SUV space with supercar power. Perfect for group travel without compromise.",
        },
    },
    "lamborghini-urus": {
        "de": {
            "category": "Super-Sport-SUV",
            "tag": "Super-Sport-SUV · Frankreich",
            "desc_short": "Der extremste SUV: 650 PS und unvergleichliche Präsenz.",
            "desc_long": "Der Lamborghini Urus definiert Luxus-SUVs neu mit Supercar-Performance. Ideal für Reisen zu mehreren ohne Kompromisse.",
        },
        "en": {
            "category": "Super sport SUV",
            "tag": "Super sport SUV · France",
            "desc_short": "The most extreme SUV: 650 hp and unmatched presence.",
            "desc_long": "The Lamborghini Urus redefines luxury SUVs with supercar performance. Ideal for group travel without compromise.",
        },
    },
    "lamborghini-urus-2": {
        "de": {
            "category": "Super-Sport-SUV",
            "tag": "Super-Sport-SUV · Frankreich",
            "desc_short": "Performante-Version: noch schärfer, 666 PS.",
            "desc_long": "Der Urus Performante treibt das Extreme weiter — optimiertes Chassis, mehr Power und maximale Präsenz.",
        },
        "en": {
            "category": "Super sport SUV",
            "tag": "Super sport SUV · France",
            "desc_short": "Performante edition: even sharper, 666 hp.",
            "desc_long": "The Urus Performante pushes extremes further — optimised chassis, more power and maximum presence.",
        },
    },
    "mercedes-gt63s-eperformance": {
        "de": {
            "category": "Performance-Hybrid",
            "tag": "Hybrid · Europa",
            "desc_short": "805 PS Hybrid — der Höhepunkt der AMG-Technologie.",
            "desc_long": "Der GT 63 S E-Performance mit 805 PS Hybridleistung — atemberaubende Beschleunigung und Spitzentechnologie.",
        },
        "en": {
            "category": "Performance hybrid",
            "tag": "Hybrid · Europe",
            "desc_short": "805 hp hybrid — the pinnacle of AMG technology.",
            "desc_long": "The GT 63 S E-Performance with 805 hybrid hp — breathtaking acceleration and cutting-edge tech.",
        },
    },
    "lamborghini-huracan-evo": {
        "de": {
            "category": "Supercar",
            "tag": "Supercar · Frankreich",
            "desc_short": "Atmosphärischer V10 und scharfes Design — pure Lamborghini-Emotion.",
            "desc_long": "Die Huracán Evo verkörpert Lamborghinis Sport-DNA. Aggressive Linien, V10 und sofortige Emotionen.",
        },
        "en": {
            "category": "Supercar",
            "tag": "Supercar · France",
            "desc_short": "Atmospheric V10 and sharp design — pure Lamborghini emotion.",
            "desc_long": "The Huracán Evo embodies Lamborghini's sporting DNA. Aggressive lines, V10 and instant thrills.",
        },
    },
}

OFFER_LABELS_FR = {
    "24h semaine (250 km)": "24h semaine (250 km)",
    "24h semaine (illimité)": "24h semaine (illimité)",
    "24h week-end (250 km)": "24h week-end (250 km)",
    "24h week-end (illimité)": "24h week-end (illimité)",
    "24h week-end": "24h week-end",
    "48h week-end": "48h week-end",
    "48h week-end (illimité)": "48h week-end (illimité)",
    "72h": "72h",
    "7 jours": "7 jours",
    "24h semaine": "24h semaine",
}

OFFER_LABELS_DE = {
    "24h semaine (250 km)": "24h Wochentags (250 km)",
    "24h semaine (illimité)": "24h Wochentags (unbegrenzt)",
    "24h week-end (250 km)": "24h Wochenende (250 km)",
    "24h week-end (illimité)": "24h Wochenende (unbegrenzt)",
    "24h week-end": "24h Wochenende",
    "48h week-end": "48h Wochenende",
    "48h week-end (illimité)": "48h Wochenende (unbegrenzt)",
    "72h": "72h",
    "7 jours": "7 Tage",
    "24h semaine": "24h Wochentags",
}

OFFER_LABELS_EN = {
    "24h semaine (250 km)": "24h weekday (250 km)",
    "24h semaine (illimité)": "24h weekday (unlimited)",
    "24h week-end (250 km)": "24h weekend (250 km)",
    "24h week-end (illimité)": "24h weekend (unlimited)",
    "24h week-end": "24h weekend",
    "48h week-end": "48h weekend",
    "48h week-end (illimité)": "48h weekend (unlimited)",
    "72h": "72h",
    "7 jours": "7 days",
    "24h semaine": "24h weekday",
}

STRINGS = {
    "fr": {
        "nav.home": "Accueil",
        "nav.about": "À propos",
        "nav.about_sub": "L'agence",
        "nav.fleet": "Flotte",
        "nav.fleet_sub": "Nos véhicules",
        "nav.reservation": "Réservation",
        "nav.reservation_sub": "En ligne",
        "nav.faq": "FAQ",
        "nav.faq_sub": "Questions fréquentes",
        "nav.contact": "Contact",
        "nav.whatsapp": "WhatsApp",
        "common.rights": "Tous droits réservés.",
        "common.deposit": "Caution",
        "common.gallery": "Galerie",
        "common.pricing_title": "Tarifs de location",
        "common.pricing_note": "Tarifs indicatifs. Disponibilité et conditions confirmées sur WhatsApp selon vos dates.",
        "common.reserve_wa": "Réserver sur WhatsApp",
        "common.see_fleet": "Voir la flotte",
        "common.see_sheet": "Voir la fiche",
        "common.back_fleet": "← Retour à la flotte",
        "common.24h_week": "24h semaine",
        "fleet.hero_sub": "Location de prestige",
        "fleet.hero_title": "NOTRE FLOTTE",
        "faq.hero_sub": "Questions fréquentes",
        "faq.hero_title": "FAQ",
        "faq.cta": "Une autre question ? Écrivez-nous sur WhatsApp",
        "faq.q1": "Comment réserver un véhicule chez NuskowCars ?",
        "faq.a1": "Choisissez votre modèle dans notre flotte, puis contactez-nous sur WhatsApp avec vos dates et besoins. Nous vous confirmons la disponibilité, le tarif 24h et les modalités de location.",
        "faq.q2": "Quels documents sont demandés pour louer ?",
        "faq.a2": "Un permis de conduire valide depuis au moins 2,5 ans (5 ans pour certaines supercars) et une pièce d'identité sont requis. La caution peut être versée par virement, chèque, espèces ou garantie véhicule (valeur minimale 8 000 à 15 000 € selon modèle).",
        "faq.q3": "À quoi correspond la caution ?",
        "faq.a3": "La caution est un dépôt de garantie restitué après la location, sous réserve d'absence de dommages ou de frais supplémentaires. Son montant varie selon le véhicule choisi et vous est communiqué avant validation.",
        "faq.q4": "Proposez-vous des locations pour mariages ou événements ?",
        "faq.a4": "Oui. Nous accompagnons les mariages, soirées privées, tournages et événements professionnels en France et en région parisienne. Précisez votre usage lors de votre demande sur WhatsApp.",
        "faq.q5": "Où se fait la remise du véhicule ?",
        "faq.a5": "La prise en charge s'organise en France. Le lieu exact et les horaires sont définis avec vous lors de la confirmation, selon le véhicule et la durée de location.",
        "faq.q6": "Puis-je louer pour plusieurs jours ?",
        "faq.a6": "Bien sûr. Les tarifs affichés sont indiqués pour 24h ; pour une location prolongée, contactez-nous sur WhatsApp afin d'obtenir une proposition adaptée à votre durée.",
        "about.hero_text": "Agence de location haut de gamme en France",
        "about.hero_title": "À PROPOS",
        "about.hero_sub": "NuskowCars — L'excellence au volant",
        "about.heading": "NuskowCars, votre partenaire location de véhicules d'exception en France",
        "about.description": "NuskowCars est spécialisée dans la location de véhicules de prestige : sportives, SUV, supercars et modèles AMG. Notre mission : vous offrir des prix attractifs, du kilométrage illimité sur de nombreuses formules et un service de livraison flexible.",
        "about.excellence_1": "CONÇU POUR",
        "about.excellence_2": "L'EXCELLENCE",
        "about.service_desc": "Un service réactif en France, pour chaque demande de location",
        "vehicle.performances": "Performances",
        "vehicle.page_title_prefix": "Location",
        "home.hero_sub": "Location de prestige",
        "home.hero_title": "Louez votre véhicule de rêve",
        "home.hero_desc": "Chez NuskowCars — louez l'excellence, conduisez l'émotion.",
        "home.why_title": "Pourquoi choisir NuskowCars ?",
        "home.fleet_preview": "Aperçu de la flotte",
        "home.step1_title": "Choisir",
        "home.step1_desc": "Parcourez la flotte et choisissez votre modèle.",
        "home.step2_title": "WhatsApp",
        "home.step2_desc": "Envoyez vos dates et besoins en message.",
        "home.step3_title": "Valider",
        "home.step3_desc": "Tarif 24h et caution confirmés avec vous.",
        "home.step4_title": "Récupérer",
        "home.step4_desc": "Véhicule prêt en France, contrat signé.",
        "home.step5_title": "Retourner",
        "home.step5_desc": "Restitution du véhicule en fin de location.",
        "home.reviews_title": "Avis clients",
        "home.reviews_more": "Voir plus d'avis",
        "home.reviews_prev": "Avis précédents",
        "home.reviews_next": "Avis suivants",
        "page.fleet_title": "Flotte — Location véhicules prestige | NuskowCars",
        "page.faq_title": "FAQ — Location véhicules | NuskowCars",
        "page.about_title": "À propos — NuskowCars",
        "page.home_title": "NuskowCars — Location véhicules de prestige en France",
    },
    "de": {
        "nav.home": "Startseite",
        "nav.about": "Über uns",
        "nav.about_sub": "Die Agentur",
        "nav.fleet": "Flotte",
        "nav.fleet_sub": "Unsere Fahrzeuge",
        "nav.reservation": "Reservierung",
        "nav.reservation_sub": "Online",
        "nav.faq": "FAQ",
        "nav.faq_sub": "Häufige Fragen",
        "nav.contact": "Kontakt",
        "nav.whatsapp": "WhatsApp",
        "common.rights": "Alle Rechte vorbehalten.",
        "common.deposit": "Kaution",
        "common.gallery": "Galerie",
        "common.pricing_title": "Mietpreise",
        "common.pricing_note": "Indikative Preise. Verfügbarkeit und Bedingungen werden per WhatsApp bestätigt.",
        "common.reserve_wa": "Per WhatsApp buchen",
        "common.see_fleet": "Flotte ansehen",
        "common.see_sheet": "Details ansehen",
        "common.back_fleet": "← Zurück zur Flotte",
        "common.24h_week": "24h Wochentag",
        "fleet.hero_sub": "Premium-Vermietung",
        "fleet.hero_title": "UNSERE FLOTTE",
        "faq.hero_sub": "Häufige Fragen",
        "faq.hero_title": "FAQ",
        "faq.cta": "Weitere Frage? Schreiben Sie uns auf WhatsApp",
        "faq.q1": "Wie reserviere ich ein Fahrzeug bei NuskowCars?",
        "faq.a1": "Wählen Sie Ihr Modell in unserer Flotte und kontaktieren Sie uns per WhatsApp mit Ihren Daten. Wir bestätigen Verfügbarkeit, 24h-Tarif und Mietbedingungen.",
        "faq.q2": "Welche Unterlagen werden für die Miete benötigt?",
        "faq.a2": "Ein Führerschein seit mindestens 2,5 Jahren (5 Jahre für einige Supercars) und ein Ausweis sind erforderlich. Die Kaution per Überweisung, Scheck, Bargeld oder Fahrzeugbürgschaft (8.000–15.000 € je nach Modell).",
        "faq.q3": "Wofür ist die Kaution?",
        "faq.a3": "Die Kaution wird nach der Miete zurückerstattet, sofern keine Schäden oder Zusatzkosten anfallen. Die Höhe hängt vom Fahrzeug ab.",
        "faq.q4": "Bieten Sie Mieten für Hochzeiten oder Events an?",
        "faq.a4": "Ja. Wir begleiten Hochzeiten, private Feiern, Dreharbeiten und Business-Events. Nennen Sie den Anlass in Ihrer WhatsApp-Anfrage.",
        "faq.q5": "Wo erfolgt die Fahrzeugübergabe?",
        "faq.a5": "Die Übergabe erfolgt in Frankreich. Ort und Zeiten werden bei der Bestätigung festgelegt.",
        "faq.q6": "Kann ich für mehrere Tage mieten?",
        "faq.a6": "Natürlich. Die angezeigten Preise gelten für 24h; für längere Mieten kontaktieren Sie uns per WhatsApp.",
        "about.hero_text": "Premium-Vermietung in Frankreich",
        "about.hero_title": "ÜBER UNS",
        "about.hero_sub": "NuskowCars — Exzellenz am Steuer",
        "about.heading": "NuskowCars, Ihr Partner für außergewöhnliche Fahrzeugmieten in Frankreich",
        "about.description": "NuskowCars ist auf Premium-Fahrzeugvermietung spezialisiert: Sportwagen, SUVs, Supercars und AMG-Modelle mit attraktiven Preisen und flexiblem Lieferservice.",
        "about.excellence_1": "KONZIPIERT FÜR",
        "about.excellence_2": "EXZELLENZ",
        "about.service_desc": "Reaktiver Service in Frankreich für jede Mietanfrage",
        "vehicle.performances": "Leistung",
        "vehicle.page_title_prefix": "Miete",
        "home.hero_sub": "Premium-Vermietung",
        "home.hero_title": "Mieten Sie Ihr Traumauto",
        "home.hero_desc": "Bei NuskowCars — Exzellenz mieten, Emotionen fahren.",
        "home.why_title": "Warum NuskowCars wählen?",
        "home.fleet_preview": "Flottenübersicht",
        "home.step1_title": "Wählen",
        "home.step1_desc": "Durchstöbern Sie die Flotte und wählen Sie Ihr Modell.",
        "home.step2_title": "WhatsApp",
        "home.step2_desc": "Senden Sie Datum und Bedürfnisse in einer Nachricht.",
        "home.step3_title": "Bestätigen",
        "home.step3_desc": "24h-Tarif und Kaution werden mit Ihnen bestätigt.",
        "home.step4_title": "Abholen",
        "home.step4_desc": "Fahrzeug bereit in Frankreich, Vertrag unterschrieben.",
        "home.step5_title": "Zurückgeben",
        "home.step5_desc": "Rückgabe des Fahrzeugs am Ende der Miete.",
        "home.reviews_title": "Kundenbewertungen",
        "home.reviews_more": "Mehr Bewertungen",
        "home.reviews_prev": "Vorherige Bewertungen",
        "home.reviews_next": "Nächste Bewertungen",
        "page.fleet_title": "Flotte — Premium-Fahrzeugvermietung | NuskowCars",
        "page.faq_title": "FAQ — Fahrzeugvermietung | NuskowCars",
        "page.about_title": "Über uns — NuskowCars",
        "page.home_title": "NuskowCars — Premium-Fahrzeugvermietung in Frankreich",
    },
    "en": {
        "nav.home": "Home",
        "nav.about": "About",
        "nav.about_sub": "The agency",
        "nav.fleet": "Fleet",
        "nav.fleet_sub": "Our vehicles",
        "nav.reservation": "Reservation",
        "nav.reservation_sub": "Online",
        "nav.faq": "FAQ",
        "nav.faq_sub": "Frequently asked questions",
        "nav.contact": "Contact",
        "nav.whatsapp": "WhatsApp",
        "common.rights": "All rights reserved.",
        "common.deposit": "Deposit",
        "common.gallery": "Gallery",
        "common.pricing_title": "Rental rates",
        "common.pricing_note": "Indicative rates. Availability confirmed via WhatsApp.",
        "common.reserve_wa": "Book on WhatsApp",
        "common.see_fleet": "View fleet",
        "common.see_sheet": "View details",
        "common.back_fleet": "← Back to fleet",
        "common.24h_week": "24h weekday",
        "fleet.hero_sub": "Premium rental",
        "fleet.hero_title": "OUR FLEET",
        "faq.hero_sub": "Frequently asked questions",
        "faq.hero_title": "FAQ",
        "faq.cta": "Another question? Message us on WhatsApp",
        "faq.q1": "How do I book a vehicle with NuskowCars?",
        "faq.a1": "Choose your model from our fleet, then contact us on WhatsApp with your dates. We confirm availability, 24h rate and rental terms.",
        "faq.q2": "What documents are required to rent?",
        "faq.a2": "A valid licence for at least 2.5 years (5 years for some supercars) and ID are required. Deposit by transfer, cheque, cash or vehicle guarantee (€8,000–15,000 depending on model).",
        "faq.q3": "What is the deposit for?",
        "faq.a3": "The deposit is refunded after rental if there are no damages or extra charges. Amount varies by vehicle.",
        "faq.q4": "Do you offer rentals for weddings or events?",
        "faq.a4": "Yes. We support weddings, private parties, filming and corporate events. Specify your use case on WhatsApp.",
        "faq.q5": "Where is the vehicle handed over?",
        "faq.a5": "Handover takes place in France. Location and times are set at confirmation.",
        "faq.q6": "Can I rent for several days?",
        "faq.a6": "Of course. Displayed rates are for 24h; for longer rentals contact us on WhatsApp.",
        "about.hero_text": "Premium rental agency in France",
        "about.hero_title": "ABOUT US",
        "about.hero_sub": "NuskowCars — Excellence behind the wheel",
        "about.heading": "NuskowCars, your partner for exceptional vehicle rental in France",
        "about.description": "NuskowCars specializes in premium vehicle rental: sports cars, SUVs, supercars and AMG models with competitive pricing and flexible delivery.",
        "about.excellence_1": "DESIGNED FOR",
        "about.excellence_2": "EXCELLENCE",
        "about.service_desc": "Responsive service in France for every rental request",
        "vehicle.performances": "Performance",
        "vehicle.page_title_prefix": "Rental",
        "home.hero_sub": "Premium rental",
        "home.hero_title": "Rent your dream car",
        "home.hero_desc": "At NuskowCars — rent excellence, drive emotion.",
        "home.why_title": "Why choose NuskowCars?",
        "home.fleet_preview": "Fleet preview",
        "home.step1_title": "Choose",
        "home.step1_desc": "Browse the fleet and pick your model.",
        "home.step2_title": "WhatsApp",
        "home.step2_desc": "Send your dates and needs in one message.",
        "home.step3_title": "Confirm",
        "home.step3_desc": "24h rate and deposit confirmed with you.",
        "home.step4_title": "Pick up",
        "home.step4_desc": "Vehicle ready in France, contract signed.",
        "home.step5_title": "Return",
        "home.step5_desc": "Return the vehicle at the end of your rental.",
        "home.reviews_title": "Customer reviews",
        "home.reviews_more": "See more reviews",
        "home.reviews_prev": "Previous reviews",
        "home.reviews_next": "Next reviews",
        "page.fleet_title": "Fleet — Premium car rental | NuskowCars",
        "page.faq_title": "FAQ — Car rental | NuskowCars",
        "page.about_title": "About — NuskowCars",
        "page.home_title": "NuskowCars — Premium car rental in France",
    },
}

WA_INTRO = {
    "fr": "Bonjour, je souhaite louer",
    "de": "Hallo, ich möchte mieten",
    "en": "Hello, I would like to rent",
}

LANG_SWITCHER = """<div class="header__lang" aria-label="Langue">
  <button type="button" class="header__lang-btn" data-lang="fr" aria-label="Français">🇫🇷</button>
  <button type="button" class="header__lang-btn" data-lang="de" aria-label="Deutsch">🇩🇪</button>
  <button type="button" class="header__lang-btn" data-lang="en" aria-label="English">🇬🇧</button>
</div>"""

LANG_CSS = """
.header__lang{display:flex;align-items:center;gap:.35rem;margin-right:.75rem}
.header__lang-btn,.header__lang a{font-size:1.1rem;line-height:1;opacity:.55;transition:opacity .2s,transform .2s;text-decoration:none;background:none;border:0;cursor:pointer;padding:0}
.header__lang-btn:hover,.header__lang-btn.is-active,.header__lang a:hover,.header__lang a.is-active{opacity:1;transform:scale(1.1)}
@media(max-width:48em){.header__lang{margin-right:.25rem}.header__lang-btn,.header__lang a{font-size:1rem}}
"""

BOOT_SCRIPT = """<script>
(function(){try{var p=new URLSearchParams(location.search),l=p.get('lang')||localStorage.getItem('nuskow-lang');if(l&&/^(de|en|fr)$/.test(l))document.documentElement.lang=l==='de'?'de-DE':l==='en'?'en':'fr-FR';}catch(e){}})();
</script>"""

I18N_SCRIPTS_ROOT = """
<script src="assets/i18n/locales.js"></script>
<script src="assets/i18n/i18n.js"></script>
<script src="assets/i18n/pages.js"></script>
"""

I18N_SCRIPTS_VEH = """
<script src="../assets/i18n/locales.js"></script>
<script src="../assets/i18n/i18n.js"></script>
<script src="../assets/i18n/pages.js"></script>
"""


def build_vehicles():
    items = []
    for v in integrate.VEHICLES:
        slug = v["slug"]
        items.append(
            {
                "slug": slug,
                "title": v["title"],
                "brand": v["brand"],
                "category": v["category"],
                "tag": v["tag"],
                "power": v["power"],
                "hero_title": v["hero_title"],
                "desc_short": v["desc_short"],
                "desc_long": v["desc_long"],
                "deposit": v["deposit"],
                "price_24h": v["price_24h"],
                "pricing": v["pricing"],
                "perfs": list(PERFS.get(slug, ("", "", ""))),
                "i18n": VEHICLE_I18N.get(slug, {}),
            }
        )
    return items


def write_locales():
    payload = {
        "strings": STRINGS,
        "vehicles": build_vehicles(),
        "offerLabels": {
            "fr": OFFER_LABELS_FR,
            "de": OFFER_LABELS_DE,
            "en": OFFER_LABELS_EN,
        },
        "perfLabels": {
            "fr": list(perfs_mod.LABELS["fr"]),
            "de": list(perfs_mod.LABELS["de"]),
            "en": list(perfs_mod.LABELS["en"]),
        },
        "fleetPerfLabels": {
            "fr": list(perfs_mod.FLEET_LABELS["fr"]),
            "de": list(perfs_mod.FLEET_LABELS["de"]),
            "en": list(perfs_mod.FLEET_LABELS["en"]),
        },
        "waIntro": WA_INTRO,
    }
    js = "window.NUSKOW_LOCALES = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n"
    (I18N_DIR / "locales.js").write_text(js, encoding="utf-8")


def replace_lang_switcher(html: str) -> str:
    return re.sub(
        r'<div class="header__lang"[^>]*>.*?</div>',
        LANG_SWITCHER,
        html,
        count=1,
        flags=re.S,
    )


def inject_head(html: str, depth: str = "") -> str:
    prefix = "../" if depth == "vehicules" else ""
    if BOOT_SCRIPT not in html:
        html = html.replace("<head>", "<head>\n" + BOOT_SCRIPT, 1)
    if "assets/i18n/i18n.js" not in html:
        scripts = I18N_SCRIPTS_VEH if depth == "vehicules" else I18N_SCRIPTS_ROOT
        html = html.replace("</body>", scripts + "\n</body>", 1)
    if ".header__lang-btn" not in html:
        html = html.replace(
            ".header__lang a{font-size:1.1rem",
            LANG_CSS.strip() + "\n.header__lang a{font-size:1.1rem",
            1,
        )
    return html


def add_i18n_attr(html: str, old: str, key: str, *, html_mode: bool = False) -> str:
    attr = "data-i18n-html" if html_mode else "data-i18n"
    if attr + '="' + key + '"' in html:
        return html
    if old not in html:
        return html
    return html.replace(old, f'<span {attr}="{key}">{old}</span>', 1)


def patch_nav_footer(html: str) -> str:
    replacements = [
        ('<span class="a-main anim-a">Accueil</span>', '<span class="a-main anim-a" data-i18n="nav.home">Accueil</span>'),
        ('<span class="a-main anim-a">À propos</span>', '<span class="a-main anim-a" data-i18n="nav.about">À propos</span>'),
        ("<span class=\"a-sub anim-sub-a\">L'agence</span>", '<span class="a-sub anim-sub-a" data-i18n="nav.about_sub">L\'agence</span>'),
        ('<span class="a-main anim-a">Flotte</span>', '<span class="a-main anim-a" data-i18n="nav.fleet">Flotte</span>'),
        ('<span class="a-sub anim-sub-a">Nos véhicules</span>', '<span class="a-sub anim-sub-a" data-i18n="nav.fleet_sub">Nos véhicules</span>'),
        ('<span class="a-main anim-a">Réservation</span>', '<span class="a-main anim-a" data-i18n="nav.reservation">Réservation</span>'),
        ('<span class="a-sub anim-sub-a">En ligne</span>', '<span class="a-sub anim-sub-a" data-i18n="nav.reservation_sub">En ligne</span>'),
        ('<span class="a-main anim-a">FAQ</span>', '<span class="a-main anim-a" data-i18n="nav.faq">FAQ</span>'),
        ('<span class="a-sub anim-sub-a">Questions fréquentes</span>', '<span class="a-sub anim-sub-a" data-i18n="nav.faq_sub">Questions fréquentes</span>'),
        ('class="header-link a" target="_blank" rel="noopener">Contact</a>', 'class="header-link a" target="_blank" rel="noopener" data-i18n="nav.contact">Contact</a>'),
        ('<div class="txt"><p>Contact</p><p class="link" role="link">WhatsApp</p></div>', '<div class="txt"><p data-i18n="nav.contact">Contact</p><p class="link" role="link" data-i18n="nav.whatsapp">WhatsApp</p></div>'),
        ("© NuskowCars — Tous droits réservés.", '© NuskowCars — <span data-i18n="common.rights">Tous droits réservés.</span>'),
    ]
    for old, new in replacements:
        if new not in html:
            html = html.replace(old, new, 1)
    return html


def patch_fleet(html: str) -> str:
    html = add_i18n_attr(html, "Location de prestige", "fleet.hero_sub")
    html = add_i18n_attr(html, "NOTRE FLOTTE", "fleet.hero_title")
    html = re.sub(
        r'(<section class="fleet-list[^"]*"[^>]*>).*?(</section>)',
        r'\1\n\n</section>',
        html,
        count=1,
        flags=re.S,
    )
    html = html.replace(
        '<section class="fleet-list remove-canvas" aria-label="Véhicules disponibles">',
        '<section class="fleet-list remove-canvas" aria-label="Véhicules disponibles" data-fleet-list>',
        1,
    )
    return html


def patch_faq(html: str) -> str:
    html = add_i18n_attr(html, "Questions fréquentes", "faq.hero_sub")
    for i in range(1, 7):
        html = add_i18n_attr(html, STRINGS["fr"][f"faq.q{i}"], f"faq.q{i}")
        html = add_i18n_attr(html, STRINGS["fr"][f"faq.a{i}"], f"faq.a{i}")
    html = add_i18n_attr(html, STRINGS["fr"]["faq.cta"], "faq.cta")
    return html


def patch_about(html: str) -> str:
    mapping = [
        ("Agence de location haut de gamme en France", "about.hero_text"),
        ("À PROPOS", "about.hero_title"),
        ("NuskowCars — L'excellence au volant", "about.hero_sub"),
        (STRINGS["fr"]["about.heading"], "about.heading"),
        (STRINGS["fr"]["about.description"], "about.description"),
        ("CONÇU POUR", "about.excellence_1"),
        ("L'EXCELLENCE", "about.excellence_2"),
        ("Un service réactif en France, pour chaque demande de location", "about.service_desc"),
    ]
    for text, key in mapping:
        html = add_i18n_attr(html, text, key)
    return html


def patch_vehicle(html: str, path: Path) -> str:
    slug = path.stem
    if 'data-vehicle-slug="' not in html:
        html = html.replace("<body>", f'<body data-vehicle-slug="{slug}">', 1)
    return html


def patch_index(html: str) -> str:
    mapping = [
        ("Location de prestige", "home.hero_sub"),
        ("Chez NuskowCars — louez l'excellence, conduisez l'émotion.", "home.hero_desc"),
        ("Pourquoi choisir NuskowCars ?", "home.why_title"),
        ("Aperçu de la flotte", "home.fleet_preview"),
        ("Parcourez la flotte et choisissez votre modèle.", "home.step1_desc"),
        ("Envoyez vos dates et besoins en message.", "home.step2_desc"),
        ("Tarif 24h et caution confirmés avec vous.", "home.step3_desc"),
        ("Véhicule prêt en France, contrat signé.", "home.step4_desc"),
        ("Restitution du véhicule en fin de location.", "home.step5_desc"),
        ('aria-label="Avis précédents"', 'data-i18n-aria="home.reviews_prev" aria-label="Avis précédents"'),
        ('aria-label="Avis suivants"', 'data-i18n-aria="home.reviews_next" aria-label="Avis suivants"'),
    ]
    for text, key in mapping:
        if key.startswith("data-i18n"):
            html = html.replace(text, key, 1)
        else:
            html = add_i18n_attr(html, text, key)
    return html


def patch_file(path: Path):
    html = path.read_text(encoding="utf-8")
    depth = "vehicules" if "vehicules" in path.parts else ""
    html = inject_head(html, depth)
    html = replace_lang_switcher(html)
    html = patch_nav_footer(html)
    name = path.name
    if name == "flotte.html":
        html = patch_fleet(html)
        if 'data-i18n-page-title' not in html:
            html = html.replace("<body>", '<body data-i18n-page-title="page.fleet_title">', 1)
    elif name == "faq.html":
        html = patch_faq(html)
        html = html.replace("<body>", '<body data-i18n-page-title="page.faq_title">', 1)
    elif name == "a-propos.html":
        html = patch_about(html)
        html = html.replace("<body>", '<body data-i18n-page-title="page.about_title">', 1)
    elif name == "index.html":
        html = patch_index(html)
        html = html.replace("<body>", '<body data-i18n-page-title="page.home_title">', 1)
    elif name.endswith(".html") and "vehicules" in path.parts:
        html = patch_vehicle(html, path)
    path.write_text(html, encoding="utf-8")
    print("patched", path.relative_to(ROOT))


def write_redirect(rel_from: str, target: str, lang: str):
    path = ROOT / rel_from
    path.parent.mkdir(parents=True, exist_ok=True)
    depth = rel_from.count("/")
    prefix = "../" * depth
    target_url = prefix + target + f"?lang={lang}"
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8" />
  <meta http-equiv="refresh" content="0;url={target_url}" />
  <script>location.replace("{target_url}");</script>
  <title>Redirect</title>
</head>
<body><p><a href="{target_url}">Continue</a></p></body>
</html>
"""
    path.write_text(html, encoding="utf-8")


def write_redirects():
    write_redirect("german.html", "index.html", "de")
    write_redirect("en.html", "index.html", "en")
    for page in ("flotte.html", "a-propos.html", "faq.html", "reservation.html"):
        write_redirect(f"german/{page}", page, "de")
        write_redirect(f"en/{page}", page, "en")
    for slug in [v["slug"] for v in integrate.VEHICLES]:
        write_redirect(f"german/vehicules/{slug}.html", f"vehicules/{slug}.html", "de")
        write_redirect(f"en/vehicules/{slug}.html", f"vehicules/{slug}.html", "en")


def main():
    I18N_DIR.mkdir(parents=True, exist_ok=True)
    write_locales()
    pages = [
        ROOT / "index.html",
        ROOT / "flotte.html",
        ROOT / "faq.html",
        ROOT / "a-propos.html",
        ROOT / "reservation.html",
    ]
    pages += sorted((ROOT / "vehicules").glob("*.html"))
    for path in pages:
        patch_file(path)
    write_redirects()
    print("done")


if __name__ == "__main__":
    main()
