#!/usr/bin/env python3
"""Traductions DE/EN complètes, CLA45, suppression Analytics, lien Réservation."""
from __future__ import annotations

import importlib.util
import re
import shutil
from pathlib import Path

ROOT = Path("/workspace")
ARCHIVE = ROOT / "archive/nuskowcars-original-20250902"

_spec = importlib.util.spec_from_file_location("integrate", ROOT / "scripts" / "integrate-nuskow.py")
integrate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(integrate)

CLA45 = {
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
    "i18n": {
        "de": {
            "title": "Mercedes-Benz CLA45S AMG",
            "desc_short": "Sportliche Limousine mit 520 PS — Performance und Eleganz.",
            "desc_long": "Der Mercedes-Benz CLA45S AMG vereint Coupé-Design und 520 PS AMG-Motor. Ideal für sportliche Probefahrten oder Kurzmieten.",
            "tag": "Sportlimousine · Deutschland",
        },
        "en": {
            "title": "Mercedes-Benz CLA45S AMG",
            "desc_short": "520 hp sport sedan — performance and elegance.",
            "desc_long": "The Mercedes-Benz CLA45S AMG combines coupe design with a 520 hp AMG engine. Ideal for sporty trials or short rentals.",
            "tag": "Sport sedan · Europe",
        },
    },
}

# FR -> DE, EN replacements (longest first when applying)
REPLACEMENTS_DE = [
    ("Demande de réservation", "Buchungsanfrage"),
    ("Réservation", "Reservierung"),
    ("Réserver sur WhatsApp", "Per WhatsApp buchen"),
    ("Voir la fiche", "Details ansehen"),
    ("Voir la flotte", "Flotte ansehen"),
    ("Aperçu de la flotte", "Flottenübersicht"),
    ("NOTRE FLOTTE", "UNSERE FLOTTE"),
    ("Questions fréquentes", "Häufige Fragen"),
    ("À propos", "Über uns"),
    ("L'agence", "Die Agentur"),
    ("Nos véhicules", "Unsere Fahrzeuge"),
    ("Accueil", "Startseite"),
    ("Contact", "Kontakt"),
    ("Tous droits réservés.", "Alle Rechte vorbehalten."),
    ("Louez votre <b>véhicule de rêve</b>", "Mieten Sie Ihr <b>Traumauto</b>"),
    ("Location de véhicules de prestige — NuskowCars", "Premium-Fahrzeugvermietung — NuskowCars"),
    ("Chez NuskowCars — louez l'excellence, conduisez l'émotion.", "Bei NuskowCars — Exzellenz mieten, Emotionen fahren."),
    ("Pourquoi choisir NuskowCars ?", "Warum NuskowCars wählen?"),
    ("CONÇU POUR", "KONZIPIERT FÜR"),
    ("L'EXCELLENCE", "EXZELLENZ"),
    ("Prix attractifs, kilomètres illimités et livraison à domicile, aéroport ou gare", "Attraktive Preise, unbegrenzte Kilometer und Lieferung nach Hause, Flughafen oder Bahnhof"),
    ("Une flotte d'exception et un service discret pour vos déplacements sans limite.", "Eine außergewöhnliche Flotte und diskreter Service für Ihre Fahrten."),
    ("NuskowCars accompagne particuliers et professionnels avec des véhicules haut de gamme, soigneusement entretenus et prêts à prendre la route.", "NuskowCars begleitet Privat- und Geschäftskunden mit hochwertigen, sorgfältig gewarteten Fahrzeugen."),
    ("Mariages, événements, séjours ou déplacements professionnels : chaque location est pensée sur mesure, avec réactivité et exigence.", "Hochzeiten, Events, Aufenthalte oder Geschäftsreisen: jede Miete wird individuell und mit höchsten Ansprüchen betreut."),
    ("Louez l'excellence, conduisez l'émotion", "Mieten Sie Exzellenz, fahren Sie Emotion"),
    ("NuskowCars — l'excellence automobile au service de vos déplacements.", "NuskowCars — automobile Exzellenz für Ihre Fahrten."),
    ("À PROPOS", "ÜBER UNS"),
    ("Comment réserver un véhicule chez NuskowCars ?", "Wie reserviere ich ein Fahrzeug bei NuskowCars?"),
    ("Choisissez votre modèle dans notre flotte, puis contactez-nous sur WhatsApp avec vos dates et besoins. Nous vous confirmons la disponibilité, le tarif 24h et les modalités de location.", "Wählen Sie Ihr Modell in unserer Flotte und kontaktieren Sie uns per WhatsApp mit Ihren Daten. Wir bestätigen Verfügbarkeit, 24h-Tarif und Mietbedingungen."),
    ("Quels documents sont demandés pour louer ?", "Welche Unterlagen werden für die Miete benötigt?"),
    ("Un permis de conduire valide depuis au moins 2,5 ans (5 ans pour certaines supercars) et une pièce d'identité sont requis. La caution peut être versée par virement, chèque, espèces ou garantie véhicule (valeur minimale 8 000 à 15 000 € selon modèle).", "Ein Führerschein seit mindestens 2,5 Jahren (5 Jahre für einige Supercars) und ein Ausweis sind erforderlich. Die Kaution per Überweisung, Scheck, Bargeld oder Fahrzeugbürgschaft (8.000–15.000 € je nach Modell)."),
    ("À quoi correspond la caution ?", "Wofür ist die Kaution?"),
    ("La caution est un dépôt de garantie restitué après la location, sous réserve d'absence de dommages ou de frais supplémentaires. Son montant varie selon le véhicule choisi et vous est communiqué avant validation.", "Die Kaution wird nach der Miete zurückerstattet, sofern keine Schäden oder Zusatzkosten anfallen. Die Höhe hängt vom Fahrzeug ab."),
    ("Proposez-vous des locations pour mariages ou événements ?", "Bieten Sie Mieten für Hochzeiten oder Events an?"),
    ("Oui. Nous accompagnons mariages, soirées privées, tournages et événements professionnels. Précisez votre usage lors de votre demande sur WhatsApp.", "Ja. Wir begleiten Hochzeiten, private Feiern, Dreharbeiten und Business-Events. Nennen Sie den Anlass in Ihrer WhatsApp-Anfrage."),
    ("Où se fait la remise du véhicule ?", "Wo erfolgt die Fahrzeugübergabe?"),
    ("NuskowCars propose la livraison à domicile, à l'aéroport ou en gare. Le lieu et les horaires sont définis avec vous lors de la confirmation.", "NuskowCars bietet Lieferung nach Hause, zum Flughafen oder Bahnhof. Ort und Zeiten werden bei der Bestätigung festgelegt."),
    ("Puis-je louer pour plusieurs jours ?", "Kann ich für mehrere Tage mieten?"),
    ("Bien sûr. Les tarifs affichés sont indiqués pour 24h ; pour une location prolongée, contactez-nous sur WhatsApp afin d'obtenir une proposition adaptée à votre durée.", "Natürlich. Die angezeigten Preise gelten für 24h; für längere Mieten kontaktieren Sie uns per WhatsApp."),
    ("Une autre question ? Écrivez-nous sur WhatsApp", "Weitere Frage? Schreiben Sie uns auf WhatsApp"),
    ("Tarifs de location", "Mietpreise"),
    ("Caution", "Kaution"),
    ("Galerie", "Galerie"),
    ("← Retour à la flotte", "← Zurück zur Flotte"),
    ("24h semaine", "24h Wochentag"),
    ("Sur demande", "Auf Anfrage"),
    ("Sportive compacte", "Kompaktsportler"),
    ("Break sportif", "Sportkombi"),
    ("SUV sportif", "Sport-SUV"),
    ("Berline sportive", "Sportlimousine"),
    ("Supercar", "Supercar"),
    ("SUV super sport", "Super-Sport-SUV"),
    ("SUV iconique", "Ikonscher SUV"),
    ("SUV coupé", "SUV-Coupé"),
    ("SUV coupé sportif", "Sport-SUV-Coupé"),
    ("Grand tourisme", "Grand Tourisme"),
    ("Hybride performance", "Performance-Hybrid"),
    ("Hybride · France", "Hybrid · Europa"),
    ("Location de prestige", "Premium-Vermietung"),
    ("Choisir votre véhicule", "Fahrzeug wählen"),
    ("Nous écrire sur WhatsApp", "Uns auf WhatsApp schreiben"),
    ("Valider & caution", "Bestätigen & Kaution"),
    ("Récupérer le véhicule", "Fahrzeug abholen"),
    ("Réserver sur WhatsApp", "Per WhatsApp buchen"),
    ("Parcourez la flotte et repérez le modèle idéal pour votre occasion.", "Durchstöbern Sie die Flotte und finden Sie Ihr ideales Modell."),
    ("Indiquez vos dates, le véhicule souhaité et vos besoins en un message.", "Nennen Sie Datum, Wunschfahrzeug und Bedürfnisse in einer Nachricht."),
    ("Nous confirmons la disponibilité, le tarif 24h et le montant de la caution.", "Wir bestätigen Verfügbarkeit, 24h-Tarif und Kaution."),
    ("Récupérez le véhicule ou profitez de la livraison : domicile, aéroport ou gare.", "Holen Sie das Fahrzeug ab oder nutzen Sie die Lieferung."),
    ("Chez NuskowCars, nous proposons des prix attractifs, des kilomètres illimités sur de nombreuses formules et la livraison de votre véhicule à domicile, à l'aéroport ou en gare.", "Bei NuskowCars: attraktive Preise, unbegrenzte Kilometer auf vielen Tarifen und Lieferung nach Hause, Flughafen oder Bahnhof."),
    ("Profitez aussi de nos offres du moment : essais au volant, promotions (-25&nbsp;% du mardi au jeudi) et une flotte de sportives, SUV et supercars soigneusement entretenue.", "Profitieren Sie von Probefahrten, Aktionen (-25 % Di–Do) und einer gepflegten Flotte aus Sportwagen, SUVs und Supercars."),
    ("NuskowCars est spécialisée dans la location de véhicules de prestige : sportives, SUV, supercars et modèles AMG. Notre mission : vous offrir des prix attractifs, du kilométrage illimité sur de nombreuses formules et un service de livraison flexible.", "NuskowCars ist auf Premium-Fahrzeugvermietung spezialisiert: Sportwagen, SUVs, Supercars und AMG-Modelle mit attraktiven Preisen und flexiblem Lieferservice."),
    ("Flotte", "Flotte"),
    ("Flotte d'exception", "Außergewöhnliche Flotte"),
    ("Service sur mesure", "Maßgeschneiderter Service"),
    ("Engagement qualité", "Qualitätsversprechen"),
    ("Découvrir la flotte", "Flotte entdecken"),
    ("Nous contacter", "Kontaktieren Sie uns"),
    ("Tarifs indicatifs. Disponibilité et conditions confirmées sur WhatsApp selon vos dates.", "Indikative Preise. Verfügbarkeit per WhatsApp bestätigt."),
]

REPLACEMENTS_EN = [
    ("Demande de réservation", "Reservation Request"),
    ("Réservation", "Reservation"),
    ("Réserver sur WhatsApp", "Book on WhatsApp"),
    ("Voir la fiche", "View details"),
    ("Voir la flotte", "View fleet"),
    ("Aperçu de la flotte", "Fleet preview"),
    ("NOTRE FLOTTE", "OUR FLEET"),
    ("Questions fréquentes", "Frequently asked questions"),
    ("À propos", "About"),
    ("L'agence", "The agency"),
    ("Nos véhicules", "Our vehicles"),
    ("Accueil", "Home"),
    ("Contact", "Contact"),
    ("Tous droits réservés.", "All rights reserved."),
    ("Louez votre <b>véhicule de rêve</b>", "Rent your <b>dream car</b>"),
    ("Location de véhicules de prestige — NuskowCars", "Premium car rental — NuskowCars"),
    ("Chez NuskowCars — louez l'excellence, conduisez l'émotion.", "At NuskowCars — rent excellence, drive emotion."),
    ("Pourquoi choisir NuskowCars ?", "Why choose NuskowCars?"),
    ("CONÇU POUR", "DESIGNED FOR"),
    ("L'EXCELLENCE", "EXCELLENCE"),
    ("Prix attractifs, kilomètres illimités et livraison à domicile, aéroport ou gare", "Competitive pricing, unlimited mileage and home, airport or station delivery"),
    ("Une flotte d'exception et un service discret pour vos déplacements sans limite.", "An exceptional fleet and discreet service for your journeys."),
    ("NuskowCars accompagne particuliers et professionnels avec des véhicules haut de gamme, soigneusement entretenus et prêts à prendre la route.", "NuskowCars serves private and business clients with premium, meticulously maintained vehicles."),
    ("Mariages, événements, séjours ou déplacements professionnels : chaque location est pensée sur mesure, avec réactivité et exigence.", "Weddings, events, stays or business travel: every rental is tailored with care and responsiveness."),
    ("Louez l'excellence, conduisez l'émotion", "Rent excellence, drive emotion"),
    ("NuskowCars — l'excellence automobile au service de vos déplacements.", "NuskowCars — automotive excellence for your journeys."),
    ("À PROPOS", "ABOUT US"),
    ("Comment réserver un véhicule chez NuskowCars ?", "How do I book a vehicle with NuskowCars?"),
    ("Choisissez votre modèle dans notre flotte, puis contactez-nous sur WhatsApp avec vos dates et besoins. Nous vous confirmons la disponibilité, le tarif 24h et les modalités de location.", "Choose your model from our fleet, then contact us on WhatsApp with your dates. We confirm availability, 24h rate and rental terms."),
    ("Quels documents sont demandés pour louer ?", "What documents are required to rent?"),
    ("Un permis de conduire valide depuis au moins 2,5 ans (5 ans pour certaines supercars) et une pièce d'identité sont requis. La caution peut être versée par virement, chèque, espèces ou garantie véhicule (valeur minimale 8 000 à 15 000 € selon modèle).", "A valid licence for at least 2.5 years (5 years for some supercars) and ID are required. Deposit by transfer, cheque, cash or vehicle guarantee (€8,000–15,000 depending on model)."),
    ("À quoi correspond la caution ?", "What is the deposit for?"),
    ("La caution est un dépôt de garantie restitué après la location, sous réserve d'absence de dommages ou de frais supplémentaires. Son montant varie selon le véhicule choisi et vous est communiqué avant validation.", "The deposit is refunded after rental if there are no damages or extra charges. Amount varies by vehicle."),
    ("Proposez-vous des locations pour mariages ou événements ?", "Do you offer rentals for weddings or events?"),
    ("Oui. Nous accompagnons mariages, soirées privées, tournages et événements professionnels. Précisez votre usage lors de votre demande sur WhatsApp.", "Yes. We support weddings, private parties, filming and corporate events. Specify your use case on WhatsApp."),
    ("Où se fait la remise du véhicule ?", "Where is the vehicle handed over?"),
    ("NuskowCars propose la livraison à domicile, à l'aéroport ou en gare. Le lieu et les horaires sont définis avec vous lors de la confirmation.", "NuskowCars offers home, airport or station delivery. Location and times are set at confirmation."),
    ("Puis-je louer pour plusieurs jours ?", "Can I rent for several days?"),
    ("Bien sûr. Les tarifs affichés sont indiqués pour 24h ; pour une location prolongée, contactez-nous sur WhatsApp afin d'obtenir une proposition adaptée à votre durée.", "Of course. Displayed rates are for 24h; for longer rentals contact us on WhatsApp."),
    ("Une autre question ? Écrivez-nous sur WhatsApp", "Another question? Message us on WhatsApp"),
    ("Tarifs de location", "Rental rates"),
    ("Caution", "Deposit"),
    ("Galerie", "Gallery"),
    ("← Retour à la flotte", "← Back to fleet"),
    ("24h semaine", "24h weekday"),
    ("Sur demande", "On request"),
    ("Sportive compacte", "Compact sports car"),
    ("Break sportif", "Sport estate"),
    ("SUV sportif", "Sport SUV"),
    ("Berline sportive", "Sport sedan"),
    ("Supercar", "Supercar"),
    ("SUV super sport", "Super sport SUV"),
    ("SUV iconique", "Iconic SUV"),
    ("SUV coupé", "SUV coupé"),
    ("SUV coupé sportif", "Sport SUV coupé"),
    ("Grand tourisme", "Grand tourer"),
    ("Hybride performance", "Performance hybrid"),
    ("Hybride · France", "Hybrid · Europe"),
    ("Location de prestige", "Premium rental"),
    ("Choisir votre véhicule", "Choose your vehicle"),
    ("Nous écrire sur WhatsApp", "Message us on WhatsApp"),
    ("Valider & caution", "Confirm & deposit"),
    ("Récupérer le véhicule", "Pick up the vehicle"),
    ("Réserver sur WhatsApp", "Book on WhatsApp"),
    ("Parcourez la flotte et repérez le modèle idéal pour votre occasion.", "Browse the fleet and find the ideal model for your occasion."),
    ("Indiquez vos dates, le véhicule souhaité et vos besoins en un message.", "Send your dates, desired vehicle and needs in one message."),
    ("Nous confirmons la disponibilité, le tarif 24h et le montant de la caution.", "We confirm availability, 24h rate and deposit amount."),
    ("Récupérez le véhicule ou profitez de la livraison : domicile, aéroport ou gare.", "Pick up the vehicle or enjoy delivery: home, airport or station."),
    ("Chez NuskowCars, nous proposons des prix attractifs, des kilomètres illimités sur de nombreuses formules et la livraison de votre véhicule à domicile, à l'aéroport ou en gare.", "At NuskowCars we offer competitive prices, unlimited mileage on many packages and delivery to your home, airport or station."),
    ("Profitez aussi de nos offres du moment : essais au volant, promotions (-25&nbsp;% du mardi au jeudi) et une flotte de sportives, SUV et supercars soigneusement entretenue.", "Enjoy trial drives, promotions (-25% Tue–Thu) and a well-maintained fleet of sports cars, SUVs and supercars."),
    ("NuskowCars est spécialisée dans la location de véhicules de prestige : sportives, SUV, supercars et modèles AMG. Notre mission : vous offrir des prix attractifs, du kilométrage illimité sur de nombreuses formules et un service de livraison flexible.", "NuskowCars specializes in premium vehicle rental: sports cars, SUVs, supercars and AMG models with competitive pricing and flexible delivery."),
    ("Tarifs indicatifs. Disponibilité et conditions confirmées sur WhatsApp selon vos dates.", "Indicative rates. Availability confirmed via WhatsApp."),
    ("Bonjour, je souhaite louer", "Hello, I would like to rent"),
    ("chez NuskowCars.", "at NuskowCars."),
]

VEHICLE_I18N = {
    "mercedes-benz-cla45s-amg": CLA45["i18n"],
}


def copy_cla45_images():
    rels = [
        "cdn.prod.website-files.com/666bb9e682a568931397e7f9/667d76ae08ad8b729408e07e_1.jpg",
        "cdn.prod.website-files.com/666bb9e682a568931397e7f9/667d76b0616b791515617d50_2.jpg",
        "cdn.prod.website-files.com/666bb9e682a568931397e7f9/667d76b108f927ea95e64c28_3.jpg",
        "cdn.prod.website-files.com/666bb9e682a568931397e7f9/667d76b3c2791074f4b4f83a_4.jpg",
    ]
    dest = ROOT / "assets/vehicules/mercedes-benz-cla45s-amg"
    dest.mkdir(parents=True, exist_ok=True)
    for i, rel in enumerate(rels, 1):
        src = ARCHIVE / "assets" / rel
        if src.exists():
            shutil.copy2(src, dest / f"{i}.jpg")


def remove_analytics(text: str) -> str:
    text = re.sub(r"\s*<script async src=\"https://www.googletagmanager.com/gtag[^\"]*\"[^>]*></script>\s*", "\n", text)
    text = re.sub(r"\s*<script>\s*window\.dataLayer[\s\S]*?gtag\('config'[^)]*\);\s*</script>\s*", "\n", text)
    text = re.sub(r"\s*<script type=\"text/javascript\">\s*\(function\(c,l,a,r,i,t,y\)[\s\S]*?clarity[\s\S]*?</script>\s*", "\n", text)
    return text


def apply_replacements(text: str, pairs: list[tuple[str, str]]) -> str:
    for fr, tr in sorted(pairs, key=lambda x: -len(x[0])):
        text = text.replace(fr, tr)
    return text


def translate_file(path: Path, lang: str):
    if not path.exists():
        return
    pairs = REPLACEMENTS_DE if lang == "de" else REPLACEMENTS_EN
    text = path.read_text(encoding="utf-8")
    text = remove_analytics(text)
    text = apply_replacements(text, pairs)
    if lang == "de":
        text = text.replace('lang="fr"', 'lang="de"', 1)
    elif lang == "en":
        text = text.replace('lang="fr"', 'lang="en"', 1)
    path.write_text(text, encoding="utf-8")


def add_reservation_nav(html: str, prefix: str = "") -> str:
  res = f'{prefix}reservation.html'
  if 'reservation.html' in html and 'header__a a" href="' + res in html:
    return html
  block = f'''          <li class="header__li">
            <a class="header__a a" href="{res}">
              <span class="a-main anim-a">Réservation</span>
              <span class="a-sub anim-sub-a">En ligne</span>
            </a>
          </li>'''
  return html.replace(
    '<li class="header__li">\n            <a class="header__a a" href="' + prefix + 'faq.html"',
    block + '\n          <li class="header__li">\n            <a class="header__a a" href="' + prefix + 'faq.html"',
    1,
  )


def patch_header_reservation_all():
    for path in ROOT.rglob("*.html"):
        if "archive" in str(path) or "reservation" in str(path) and path.name == "reservation.html":
            pass
        if "archive" in str(path):
            continue
        rel = path.relative_to(ROOT)
        depth = len(rel.parts) - 1
        prefix = "../" * depth if depth else ""
        text = path.read_text(encoding="utf-8")
        text = remove_analytics(text)
        new = add_reservation_nav(text, prefix)
        if new != text:
            path.write_text(new, encoding="utf-8")


def regenerate_with_cla45():
    if not any(v["slug"] == CLA45["slug"] for v in integrate.VEHICLES):
        integrate.VEHICLES.append(CLA45)
    copy_cla45_images()
    # regenerate vehicle pages
    for v in integrate.VEHICLES:
        (ROOT / "vehicules" / f"{v['slug']}.html").write_text(
            integrate.vehicle_page(v, "fr", "../"), encoding="utf-8"
        )
    for lang in ("de", "en"):
        sub = "german" if lang == "de" else "en"
        for v in integrate.VEHICLES:
            vp = v.copy()
            if v["slug"] in VEHICLE_I18N:
                tr = VEHICLE_I18N[v["slug"]][lang]
                vp.update(tr)
            (ROOT / sub / "vehicules" / f"{v['slug']}.html").write_text(
                integrate.vehicle_page(vp, lang, "../../"), encoding="utf-8"
            )
    # patch flotte pages - rerun integrate patch_flotte
    integrate.patch_flotte(ROOT / "flotte.html", "fr")
    integrate.patch_flotte(ROOT / "german" / "flotte.html", "de", "../")
    integrate.patch_flotte(ROOT / "en" / "flotte.html", "en", "../")
    integrate.build_sitemap()


def main():
    print("Adding CLA45 and regenerating fleet...")
    regenerate_with_cla45()
    print("Adding reservation nav + removing analytics on FR...")
    for p in [ROOT / "index.html", ROOT / "flotte.html", ROOT / "a-propos.html", ROOT / "faq.html", ROOT / "reservation.html"]:
        if p.exists():
            t = remove_analytics(p.read_text(encoding="utf-8"))
            t = add_reservation_nav(t, "")
            p.write_text(t, encoding="utf-8")
    print("Translating DE...")
    for p in [ROOT / "german.html", ROOT / "german/flotte.html", ROOT / "german/a-propos.html", ROOT / "german/faq.html"]:
        translate_file(p, "de")
    for p in (ROOT / "german/vehicules").glob("*.html"):
        translate_file(p, "de")
    translate_file(ROOT / "german/reservation.html", "de")
    print("Translating EN...")
    for p in [ROOT / "en.html", ROOT / "en/flotte.html", ROOT / "en/a-propos.html", ROOT / "en/faq.html"]:
        translate_file(p, "en")
    for p in (ROOT / "en/vehicules").glob("*.html"):
        translate_file(p, "en")
    translate_file(ROOT / "en/reservation.html", "en")
  # reservation nav on all pages
    patch_header_reservation_all()
    # translate reservation nav labels on DE/EN pages
    for path, pairs in [(ROOT/"german.html", REPLACEMENTS_DE), (ROOT/"en.html", REPLACEMENTS_EN)]:
        if path.exists():
            t = apply_replacements(path.read_text(encoding="utf-8"), [("Réservation", "Reservierung" if "german" in str(path) else "Reservation"), ("En ligne", "Online")])
            path.write_text(t, encoding="utf-8")
    for sub, res_label, online in [("german", "Reservierung", "Online"), ("en", "Reservation", "Online")]:
        for name in ["flotte.html", "a-propos.html", "faq.html", "reservation.html"]:
            p = ROOT / sub / name
            if p.exists():
                t = p.read_text(encoding="utf-8").replace("Réservation", res_label).replace("En ligne", online)
                p.write_text(t, encoding="utf-8")
    print("Done.")


if __name__ == "__main__":
    main()
