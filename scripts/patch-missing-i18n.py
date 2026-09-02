#!/usr/bin/env python3
"""Ajoute les traductions manquantes accueil + à propos."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location("gen", ROOT / "scripts" / "generate-i18n.py")
gen = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gen)

EXTRA = {
    "fr": {
        "about.pillar1_num": "01 — Flotte",
        "about.pillar1_title": "Véhicules d'exception",
        "about.pillar1_desc": "Une sélection rigoureuse : G63 AMG, GLE 63 S, RS3, M3, RSQ8, Urus, Huracán Evo et GT 63 S E-Performance. Kilométrage illimité, livraison et réservation WhatsApp — chaque véhicule entretenu avec soin.",
        "about.pillar2_num": "02 — Service",
        "about.pillar2_title": "Accompagnement sur mesure",
        "about.pillar2_desc": "Réservation simple par WhatsApp, réponse rapide, véhicule préparé selon vos dates et un suivi personnalisé jusqu'à la remise des clés.",
        "about.pillar3_num": "03",
        "about.pillar3_title": "Capitale & région",
        "about.pillar3_desc": "Prise en charge en France et en région parisienne. Nous adaptons lieu et horaires à votre usage : ville, événement, escapade.",
        "about.engagement_title": "Notre engagement",
        "about.engagement_p1": "Chez NuskowCars, la location haut de gamme ne se résume pas à livrer un véhicule : nous créons une expérience fluide, confidentielle et à la hauteur de vos attentes.",
        "about.engagement_p2": "Transparence sur les tarifs, conditions claires et équipe joignable pour répondre à toutes vos questions avant, pendant et après la location.",
        "about.engagement_li1": "Flotte renouvelée et soigneusement entretenue",
        "about.engagement_li2": "Tarifs semaine et week-end selon le véhicule",
        "about.engagement_li3": "Réservation et échanges via WhatsApp",
        "about.engagement_li4": "Discrétion et réactivité à chaque étape",
        "about.engagement_li5": "Accompagnement pour mariages, événements et professionnels",
        "about.cta_title": "Prêt à vivre l'expérience NuskowCars ?",
        "about.cta_desc": "Découvrez notre flotte ou contactez-nous pour organiser votre prochaine location en France.",
        "about.cta_wa": "Nous contacter sur WhatsApp",
        "home.hero_title_html": "Louez votre <b>véhicule de rêve</b>",
        "home.hero_country": " en France ",
        "home.hero_agency": "Agence de location de prestige",
        "home.hero_md": "Une flotte d'exception et un service discret pour vos déplacements sans limite.",
        "home.hero_sm_html": "NuskowCars accompagne particuliers et professionnels avec des véhicules haut de gamme, soigneusement entretenus et prêts à prendre la route.<br /><br />Mariages, événements, séjours ou déplacements professionnels : chaque location est pensée sur mesure, avec réactivité et exigence.",
        "home.stacked_tagline": "NuskowCars — l'excellence automobile au service de vos déplacements.",
        "home.stacked_1": "NUSKOW",
        "home.stacked_2": "CARS",
        "home.stacked_3": "PARTOUT",
        "home.stacked_4": "EN FRANCE",
        "home.excellence_1": "CONÇU POUR",
        "home.excellence_2": "L'EXCELLENCE",
        "home.service_desc": "Un service réactif en France, pour chaque demande de location",
        "home.content_heading": "Des locations haut de gamme pour chaque occasion en France",
        "home.content_desc_html": "Chez NuskowCars, nous proposons des prix attractifs, des kilomètres illimités sur de nombreuses formules et la livraison de votre véhicule à domicile, à l'aéroport ou en gare.<br><br>Profitez aussi de nos offres du moment : essais au volant, promotions (-25&nbsp;% du mardi au jeudi) et une flotte de sportives, SUV et supercars soigneusement entretenue.",
        "home.fleet_nav_prev": "Véhicule précédent",
        "home.fleet_nav_next": "Véhicule suivant",
        "home.fleet_hint": "Glisser ou utiliser les flèches pour parcourir la flotte",
        "home.morph_step1_title": "Choisir votre véhicule",
        "home.morph_step1_desc": "Parcourez la flotte et repérez le modèle idéal pour votre occasion.",
        "home.morph_step2_title": "Nous écrire sur WhatsApp",
        "home.morph_step2_desc": "Indiquez vos dates, le véhicule souhaité et vos besoins en un message.",
        "home.morph_step3_title": "Valider & caution",
        "home.morph_step3_desc": "Nous confirmons la disponibilité, le tarif 24h et le montant de la caution.",
        "home.morph_step4_title": "Récupérer le véhicule",
        "home.morph_step4_desc": "Prise en charge en France : véhicule préparé, contrat signé, vous prenez la route.",
        "home.morph_step5_title": "Retourner le véhicule",
        "home.morph_step5_desc": "Restituez le véhicule en fin de location. Nous vérifions l'état et restituons la caution.",
        "home.reviews_heading": "Les avis de nos clients",
        "home.reviews_stars": "5 étoiles sur 5",
        "home.review1": "Nous avons loué 3 véhicules de sport pour 48h le week-end dernier, la prestation a été de qualité : personnels à l'écoute, professionnels et sympathiques. Je recommande les yeux fermés ! 👍",
        "home.review2": "Service au top ! Professionnel, pleins de conseils ; autant pour l'achat de véhicule (Audi A1). Ou pour la location de voiture de haut de gamme. Je recommande les yeux fermés.",
        "home.review3": "Jai vendu mon véhicule en passant par eux très rapidement ! Un équipe professionnelle, rapide et efficace ! Je vous les recommande vivement !",
        "home.review4": "J'ai acheter une polo dans ce garage, j'en suis très satisfaite personnel à l'écoute et agréable. Pas eu besoins de faire trop de procédure il se sont occupé de la carte grise etc. 🙃",
        "home.review5": "J'ai été agréablement accueilli à l'agence NUSKOWCARS pour loué un véhicule pour le mariage de mon frere , Ayant loué un véhicule de prestige chez eux j'ai été plus que ravis",
        "home.review6": "Garage au top je conseille a tout le monde, très grand professionnel à tout les niveaux…(vous serez pas déçu)",
        "home.faq_all": "Voir toutes les questions",
        "home.contact_title": "Contactez-nous",
        "home.contact_circle": "CONTACTEZ-NOUS CONTACTEZ-NOUS CONTACTEZ-NOUS CONTACTEZ-NOUS CONTACTEZ-NOUS CONTACTEZ-NOUS",
        "home.faq_a2_home": "Une pièce d'identité valide et un permis de conduire en cours de validité sont requis. Selon le véhicule, des justificatifs complémentaires peuvent vous être demandés lors de la confirmation.",
    },
    "de": {
        "about.pillar1_num": "01 — Flotte",
        "about.pillar1_title": "Außergewöhnliche Fahrzeuge",
        "about.pillar1_desc": "Eine sorgfältige Auswahl: G63 AMG, GLE 63 S, RS3, M3, RSQ8, Urus, Huracán Evo und GT 63 S E-Performance. Unbegrenzte Kilometer, Lieferung und WhatsApp-Buchung — jedes Fahrzeug perfekt gewartet.",
        "about.pillar2_num": "02 — Service",
        "about.pillar2_title": "Maßgeschneiderte Betreuung",
        "about.pillar2_desc": "Einfache Buchung per WhatsApp, schnelle Antwort, Fahrzeug nach Ihren Daten vorbereitet und persönliche Begleitung bis zur Schlüsselübergabe.",
        "about.pillar3_num": "03",
        "about.pillar3_title": "Hauptstadt & Region",
        "about.pillar3_desc": "Übergabe in Frankreich und in der Region Paris. Wir passen Ort und Zeiten an Ihren Anlass an: Stadt, Event oder Ausflug.",
        "about.engagement_title": "Unser Versprechen",
        "about.engagement_p1": "Bei NuskowCars bedeutet Premium-Miete mehr als ein Fahrzeug zu liefern: Wir schaffen ein reibungsloses, diskretes Erlebnis auf höchstem Niveau.",
        "about.engagement_p2": "Transparente Preise, klare Bedingungen und ein erreichbares Team für alle Fragen vor, während und nach der Miete.",
        "about.engagement_li1": "Erneuerte und sorgfältig gewartete Flotte",
        "about.engagement_li2": "Wochen- und Wochenendtarife je nach Fahrzeug",
        "about.engagement_li3": "Buchung und Kommunikation per WhatsApp",
        "about.engagement_li4": "Diskretion und Reaktivität in jedem Schritt",
        "about.engagement_li5": "Begleitung für Hochzeiten, Events und Business",
        "about.cta_title": "Bereit für das NuskowCars-Erlebnis?",
        "about.cta_desc": "Entdecken Sie unsere Flotte oder kontaktieren Sie uns für Ihre nächste Miete in Frankreich.",
        "about.cta_wa": "Kontakt per WhatsApp",
        "home.hero_title_html": "Mieten Sie Ihr <b>Traumauto</b>",
        "home.hero_country": " in Frankreich ",
        "home.hero_agency": "Premium-Vermietung",
        "home.hero_md": "Eine außergewöhnliche Flotte und diskreter Service für Ihre Fahrten ohne Grenzen.",
        "home.hero_sm_html": "NuskowCars begleitet Privat- und Geschäftskunden mit hochwertigen, sorgfältig gewarteten Fahrzeugen.<br /><br />Hochzeiten, Events, Aufenthalte oder Geschäftsreisen: jede Miete wird individuell und mit höchsten Ansprüchen betreut.",
        "home.stacked_tagline": "NuskowCars — automobile Exzellenz für Ihre Fahrten.",
        "home.stacked_1": "NUSKOW",
        "home.stacked_2": "CARS",
        "home.stacked_3": "ÜBERALL",
        "home.stacked_4": "IN FRANKREICH",
        "home.excellence_1": "KONZIPIERT FÜR",
        "home.excellence_2": "EXZELLENZ",
        "home.service_desc": "Reaktiver Service in Frankreich für jede Mietanfrage",
        "home.content_heading": "Premium-Mieten für jeden Anlass in Frankreich",
        "home.content_desc_html": "Bei NuskowCars: attraktive Preise, unbegrenzte Kilometer auf vielen Tarifen und Lieferung nach Hause, Flughafen oder Bahnhof.<br><br>Profitieren Sie von Probefahrten, Aktionen (-25&nbsp;% Di–Do) und einer gepflegten Flotte aus Sportwagen, SUVs und Supercars.",
        "home.fleet_nav_prev": "Vorheriges Fahrzeug",
        "home.fleet_nav_next": "Nächstes Fahrzeug",
        "home.fleet_hint": "Wischen oder Pfeile nutzen, um die Flotte zu durchstöbern",
        "home.morph_step1_title": "Fahrzeug wählen",
        "home.morph_step1_desc": "Durchstöbern Sie die Flotte und finden Sie Ihr ideales Modell.",
        "home.morph_step2_title": "Uns auf WhatsApp schreiben",
        "home.morph_step2_desc": "Nennen Sie Datum, Wunschfahrzeug und Bedürfnisse in einer Nachricht.",
        "home.morph_step3_title": "Bestätigen & Kaution",
        "home.morph_step3_desc": "Wir bestätigen Verfügbarkeit, 24h-Tarif und Kaution.",
        "home.morph_step4_title": "Fahrzeug abholen",
        "home.morph_step4_desc": "Übergabe in Frankreich: Fahrzeug bereit, Vertrag unterschrieben, los geht's.",
        "home.morph_step5_title": "Fahrzeug zurückgeben",
        "home.morph_step5_desc": "Rückgabe am Mietende. Wir prüfen den Zustand und erstatten die Kaution.",
        "home.reviews_heading": "Kundenbewertungen",
        "home.reviews_stars": "5 von 5 Sternen",
        "home.review1": "Wir haben letztes Wochenende 3 Sportwagen für 48h gemietet — top Service: aufmerksames, professionelles und sympathisches Team. Sehr empfehlenswert! 👍",
        "home.review2": "Top Service! Professionell und voller guter Ratschläge — sowohl beim Kauf (Audi A1) als auch bei Premium-Mieten. Sehr empfehlenswert.",
        "home.review3": "Ich habe mein Fahrzeug sehr schnell über sie verkauft! Professionelles, schnelles und effizientes Team — wärmstens empfohlen!",
        "home.review4": "Ich habe einen Polo in dieser Garage gekauft und bin sehr zufrieden — freundliches Team, sie haben sich um alles gekümmert. 🙃",
        "home.review5": "Ich wurde bei NUSKOWCARS herzlich empfangen, um ein Fahrzeug für die Hochzeit meines Bruders zu mieten — mehr als zufrieden!",
        "home.review6": "Garage top, ich empfehle jedem — sehr professionell auf allen Ebenen…(Sie werden nicht enttäuscht)",
        "home.faq_all": "Alle Fragen ansehen",
        "home.contact_title": "Kontaktieren Sie uns",
        "home.contact_circle": "KONTAKT KONTAKT KONTAKT KONTAKT KONTAKT KONTAKT",
        "home.faq_a2_home": "Ein gültiger Ausweis und Führerschein sind erforderlich. Je nach Fahrzeug können bei der Bestätigung weitere Nachweise verlangt werden.",
    },
    "en": {
        "about.pillar1_num": "01 — Fleet",
        "about.pillar1_title": "Exceptional vehicles",
        "about.pillar1_desc": "A rigorous selection: G63 AMG, GLE 63 S, RS3, M3, RSQ8, Urus, Huracán Evo and GT 63 S E-Performance. Unlimited mileage, delivery and WhatsApp booking — every vehicle meticulously maintained.",
        "about.pillar2_num": "02 — Service",
        "about.pillar2_title": "Tailored support",
        "about.pillar2_desc": "Simple WhatsApp booking, fast response, vehicle prepared for your dates and personal follow-up until key handover.",
        "about.pillar3_num": "03",
        "about.pillar3_title": "Capital & region",
        "about.pillar3_desc": "Handover in France and the Paris region. We adapt location and times to your use: city, event or getaway.",
        "about.engagement_title": "Our commitment",
        "about.engagement_p1": "At NuskowCars, premium rental is more than delivering a vehicle: we create a smooth, discreet experience that meets your expectations.",
        "about.engagement_p2": "Transparent pricing, clear terms and a reachable team for all your questions before, during and after rental.",
        "about.engagement_li1": "Renewed and meticulously maintained fleet",
        "about.engagement_li2": "Weekday and weekend rates per vehicle",
        "about.engagement_li3": "Booking and communication via WhatsApp",
        "about.engagement_li4": "Discretion and responsiveness at every step",
        "about.engagement_li5": "Support for weddings, events and business",
        "about.cta_title": "Ready for the NuskowCars experience?",
        "about.cta_desc": "Discover our fleet or contact us to arrange your next rental in France.",
        "about.cta_wa": "Contact us on WhatsApp",
        "home.hero_title_html": "Rent your <b>dream car</b>",
        "home.hero_country": " in France ",
        "home.hero_agency": "Premium rental agency",
        "home.hero_md": "An exceptional fleet and discreet service for unlimited journeys.",
        "home.hero_sm_html": "NuskowCars serves private and business clients with premium, meticulously maintained vehicles.<br /><br />Weddings, events, stays or business travel: every rental is tailored with care and responsiveness.",
        "home.stacked_tagline": "NuskowCars — automotive excellence for your journeys.",
        "home.stacked_1": "NUSKOW",
        "home.stacked_2": "CARS",
        "home.stacked_3": "EVERYWHERE",
        "home.stacked_4": "IN FRANCE",
        "home.excellence_1": "DESIGNED FOR",
        "home.excellence_2": "EXCELLENCE",
        "home.service_desc": "Responsive service in France for every rental request",
        "home.content_heading": "Premium rentals for every occasion in France",
        "home.content_desc_html": "At NuskowCars we offer competitive prices, unlimited mileage on many packages and delivery to your home, airport or station.<br><br>Enjoy trial drives, promotions (-25% Tue–Thu) and a well-maintained fleet of sports cars, SUVs and supercars.",
        "home.fleet_nav_prev": "Previous vehicle",
        "home.fleet_nav_next": "Next vehicle",
        "home.fleet_hint": "Swipe or use arrows to browse the fleet",
        "home.morph_step1_title": "Choose your vehicle",
        "home.morph_step1_desc": "Browse the fleet and find the ideal model for your occasion.",
        "home.morph_step2_title": "Message us on WhatsApp",
        "home.morph_step2_desc": "Send your dates, desired vehicle and needs in one message.",
        "home.morph_step3_title": "Confirm & deposit",
        "home.morph_step3_desc": "We confirm availability, 24h rate and deposit amount.",
        "home.morph_step4_title": "Pick up the vehicle",
        "home.morph_step4_desc": "Handover in France: vehicle ready, contract signed, you're on the road.",
        "home.morph_step5_title": "Return the vehicle",
        "home.morph_step5_desc": "Return at the end of rental. We check condition and refund the deposit.",
        "home.reviews_heading": "Customer reviews",
        "home.reviews_stars": "5 out of 5 stars",
        "home.review1": "We rented 3 sports cars for 48h last weekend — quality service: attentive, professional and friendly staff. Highly recommended! 👍",
        "home.review2": "Top service! Professional with great advice for both buying (Audi A1) and premium rentals. Highly recommended.",
        "home.review3": "I sold my car through them very quickly! Professional, fast and efficient team — warmly recommended!",
        "home.review4": "I bought a Polo from this garage and I'm very happy — friendly staff, they handled everything. 🙃",
        "home.review5": "I was warmly welcomed at NUSKOWCARS to rent for my brother's wedding — more than delighted with the prestige car!",
        "home.review6": "Great garage, I recommend to everyone — very professional at every level…(you won't be disappointed)",
        "home.faq_all": "See all questions",
        "home.contact_title": "Contact us",
        "home.contact_circle": "CONTACT US CONTACT US CONTACT US CONTACT US CONTACT US CONTACT US",
        "home.faq_a2_home": "A valid ID and driving licence are required. Depending on the vehicle, additional documents may be requested at confirmation.",
    },
}

for lang in EXTRA:
    gen.STRINGS[lang].update(EXTRA[lang])

gen.write_locales()
print("locales.js updated")

# --- Patch a-propos.html ---
about = (ROOT / "a-propos.html").read_text(encoding="utf-8")
about = about.replace(
    '<span class="about-pillars__num">01 — Flotte</span>',
    '<span class="about-pillars__num" data-i18n="about.pillar1_num">01 — Flotte</span>',
)
about = about.replace(
    "<h3>Véhicules d'exception</h3>",
    '<h3 data-i18n="about.pillar1_title">Véhicules d\'exception</h3>',
    1,
)
about = about.replace(
    "<p>Une sélection rigoureuse : G63 AMG, GLE 63 S, RS3, M3, RSQ8, Urus, Huracán Evo et GT 63 S E-Performance. Kilométrage illimité, livraison et réservation WhatsApp — chaque véhicule entretenu avec soin.</p>",
    '<p data-i18n="about.pillar1_desc">Une sélection rigoureuse : G63 AMG, GLE 63 S, RS3, M3, RSQ8, Urus, Huracán Evo et GT 63 S E-Performance. Kilométrage illimité, livraison et réservation WhatsApp — chaque véhicule entretenu avec soin.</p>',
)
about = about.replace(
    '<span class="about-pillars__num">02 — Service</span>',
    '<span class="about-pillars__num" data-i18n="about.pillar2_num">02 — Service</span>',
)
about = about.replace(
    "<h3>Accompagnement sur mesure</h3>",
    '<h3 data-i18n="about.pillar2_title">Accompagnement sur mesure</h3>',
)
about = about.replace(
    "<p>Réservation simple par WhatsApp, réponse rapide, véhicule préparé selon vos dates et un suivi personnalisé jusqu'à la remise des clés.</p>",
    '<p data-i18n="about.pillar2_desc">Réservation simple par WhatsApp, réponse rapide, véhicule préparé selon vos dates et un suivi personnalisé jusqu\'à la remise des clés.</p>',
)
about = about.replace(
    '<span class="about-pillars__num">03</span>',
    '<span class="about-pillars__num" data-i18n="about.pillar3_num">03</span>',
)
about = about.replace(
    "<h3>Capitale &amp; région</h3>",
    '<h3 data-i18n="about.pillar3_title">Capitale &amp; région</h3>',
)
about = about.replace(
    "<p>Prise en charge en France et en région parisienne. Nous adaptons lieu et horaires à votre usage : ville, événement, escapade.</p>",
    '<p data-i18n="about.pillar3_desc">Prise en charge en France et en région parisienne. Nous adaptons lieu et horaires à votre usage : ville, événement, escapade.</p>',
)
about = about.replace("<h2>Notre engagement</h2>", '<h2 data-i18n="about.engagement_title">Notre engagement</h2>')
about = about.replace(
    "Chez NuskowCars, la location haut de gamme ne se résume pas à livrer un véhicule : nous créons une expérience fluide, confidentielle et à la hauteur de vos attentes.",
    '<span data-i18n="about.engagement_p1">Chez NuskowCars, la location haut de gamme ne se résume pas à livrer un véhicule : nous créons une expérience fluide, confidentielle et à la hauteur de vos attentes.</span>',
    1,
)
about = about.replace(
    "Transparence sur les tarifs, conditions claires et équipe joignable pour répondre à toutes vos questions avant, pendant et après la location.",
    '<span data-i18n="about.engagement_p2">Transparence sur les tarifs, conditions claires et équipe joignable pour répondre à toutes vos questions avant, pendant et après la location.</span>',
    1,
)
for i, fr in enumerate(
    [
        "Flotte renouvelée et soigneusement entretenue",
        "Tarifs semaine et week-end selon le véhicule",
        "Réservation et échanges via WhatsApp",
        "Discrétion et réactivité à chaque étape",
        "Accompagnement pour mariages, événements et professionnels",
    ],
    1,
):
    about = about.replace(f"<li>{fr}</li>", f'<li data-i18n="about.engagement_li{i}">{fr}</li>', 1)
about = about.replace(
    "<h2>Prêt à vivre l'expérience NuskowCars ?</h2>",
    '<h2 data-i18n="about.cta_title">Prêt à vivre l\'expérience NuskowCars ?</h2>',
)
about = about.replace(
    "<p>Découvrez notre flotte ou contactez-nous pour organiser votre prochaine location en France.</p>",
    '<p data-i18n="about.cta_desc">Découvrez notre flotte ou contactez-nous pour organiser votre prochaine location en France.</p>',
)
about = about.replace(
    'class="a about-cta__btn about-cta__btn--dark">Voir la flotte</a>',
    'class="a about-cta__btn about-cta__btn--dark" data-i18n="common.see_fleet">Voir la flotte</a>',
)
about = about.replace(
    'rel="noopener">Nous contacter sur WhatsApp</a>',
    'rel="noopener" data-i18n="about.cta_wa">Nous contacter sur WhatsApp</a>',
    1,
)
(ROOT / "a-propos.html").write_text(about, encoding="utf-8")
print("a-propos.html patched")

# --- Patch index.html ---
idx = (ROOT / "index.html").read_text(encoding="utf-8")
idx = idx.replace(
    """                        <span class="sub-text anim-fade-in">
                        Louez votre <b>véhicule de rêve</b>                        </span>
                        <span class="main-text heading"> en France </span>""",
    """                        <span class="sub-text anim-fade-in" data-i18n-html="home.hero_title_html">
                        Louez votre <b>véhicule de rêve</b>                        </span>
                        <span class="main-text heading" data-i18n="home.hero_country"> en France </span>""",
)
idx = idx.replace(
    "Agence de location de prestige                    </p>",
    '<span data-i18n="home.hero_agency">Agence de location de prestige</span>                    </p>',
)
idx = idx.replace(
    "Une flotte d'exception et un service discret pour vos déplacements sans limite.                        </h3>",
    '<span data-i18n="home.hero_md">Une flotte d\'exception et un service discret pour vos déplacements sans limite.</span>                        </h3>',
)
old_sm = """NuskowCars accompagne particuliers et professionnels avec des véhicules haut de gamme, soigneusement entretenus et prêts à prendre la route.<br />
<br />
Mariages, événements, séjours ou déplacements professionnels : chaque location est pensée sur mesure, avec réactivité et exigence.                        </h2>"""
new_sm = """<span data-i18n-html="home.hero_sm_html">NuskowCars accompagne particuliers et professionnels avec des véhicules haut de gamme, soigneusement entretenus et prêts à prendre la route.<br />
<br />
Mariages, événements, séjours ou déplacements professionnels : chaque location est pensée sur mesure, avec réactivité et exigence.</span>                        </h2>"""
idx = idx.replace(old_sm, new_sm)
idx = idx.replace('<p class="related">Aperçu de la flotte</p>', '<p class="related"><span data-i18n="home.fleet_preview">Aperçu de la flotte</span></p>', 1)
idx = idx.replace('aria-label="Véhicule précédent"', 'data-i18n-aria="home.fleet_nav_prev" aria-label="Véhicule précédent"')
idx = idx.replace('aria-label="Véhicule suivant"', 'data-i18n-aria="home.fleet_nav_next" aria-label="Véhicule suivant"')
idx = idx.replace(
    '<p class="fleet-swiper__hint">Glisser ou utiliser les flèches pour parcourir la flotte</p>',
    '<p class="fleet-swiper__hint" data-i18n="home.fleet_hint">Glisser ou utiliser les flèches pour parcourir la flotte</p>',
)
idx = idx.replace(
    "NuskowCars — l'excellence automobile au service de vos déplacements.                    </p>",
    '<span data-i18n="home.stacked_tagline">NuskowCars — l\'excellence automobile au service de vos déplacements.</span>                    </p>',
)
for i, line in enumerate(["NUSKOW", "CARS", "PARTOUT", "EN FRANCE"], 1):
    idx = idx.replace(
        f'<span class="heading-no-revert hero-line">{line}</span>',
        f'<span class="heading-no-revert hero-line" data-i18n="home.stacked_{i}">{line}</span>',
        1,
    )
idx = idx.replace(
    '<h2 class="heading"><span>CONÇU POUR</span>L\'EXCELLENCE</h2>',
    '<h2 class="heading"><span data-i18n="home.excellence_1">CONÇU POUR</span><span data-i18n="home.excellence_2">L\'EXCELLENCE</span></h2>',
)
idx = idx.replace(
    "Un service réactif en France, pour chaque demande de location                            </p>",
    '<span data-i18n="home.service_desc">Un service réactif en France, pour chaque demande de location</span>                            </p>',
)
idx = idx.replace(
    "Des locations haut de gamme pour chaque occasion en France",
    '<span data-i18n="home.content_heading">Des locations haut de gamme pour chaque occasion en France</span>',
)
old_content = """Chez NuskowCars, nous proposons des prix attractifs, des kilomètres illimités sur de nombreuses formules et la livraison de votre véhicule à domicile, à l'aéroport ou en gare.
                    <br><br>Profitez aussi de nos offres du moment : essais au volant, promotions (-25&nbsp;% du mardi au jeudi) et une flotte de sportives, SUV et supercars soigneusement entretenue."""
idx = idx.replace(
    old_content,
    '<span data-i18n-html="home.content_desc_html">' + old_content + "</span>",
)

morph = [
    ("Choisir votre véhicule", "home.morph_step1_title", "Parcourez la flotte et repérez le modèle idéal pour votre occasion.", "home.morph_step1_desc"),
    ("Nous écrire sur WhatsApp", "home.morph_step2_title", "Indiquez vos dates, le véhicule souhaité et vos besoins en un message.", "home.morph_step2_desc"),
    ("Valider &amp; caution", "home.morph_step3_title", "Nous confirmons la disponibilité, le tarif 24h et le montant de la caution.", "home.morph_step3_desc"),
    ("Récupérer le véhicule", "home.morph_step4_title", "Prise en charge en France : véhicule préparé, contrat signé, vous prenez la route.", "home.morph_step4_desc"),
    ("Retourner le véhicule", "home.morph_step5_title", "Restituez le véhicule en fin de location. Nous vérifions l'état et restituons la caution.", "home.morph_step5_desc"),
]
for title, tkey, desc, dkey in morph:
    idx = idx.replace(f">{title}</a>", f' data-i18n="{tkey}">{title}</a>', 1)
    idx = idx.replace(f"<p>{desc}</p>", f'<p data-i18n="{dkey}">{desc}</p>', 1)

idx = idx.replace("<h2>Les avis de nos clients</h2>", '<h2 data-i18n="home.reviews_heading">Les avis de nos clients</h2>')
for i in range(1, 7):
    fr = EXTRA["fr"][f"home.review{i}"]
    idx = idx.replace(
        f'<p class="review-card__text" itemprop="reviewBody">{fr}</p>',
        f'<p class="review-card__text" itemprop="reviewBody" data-i18n="home.review{i}">{fr}</p>',
        1,
    )
idx = idx.replace('aria-label="5 étoiles sur 5"', 'data-i18n-aria="home.reviews_stars" aria-label="5 étoiles sur 5"')
idx = idx.replace(
    'rel="noopener noreferrer">Voir plus</a>',
    'rel="noopener noreferrer" data-i18n="home.reviews_more">Voir plus</a>',
)
idx = idx.replace('href="faq.html" class="a">Voir toutes les questions</a>', 'href="faq.html" class="a" data-i18n="home.faq_all">Voir toutes les questions</a>')

# Homepage FAQ
for i in range(1, 7):
    q = gen.STRINGS["fr"][f"faq.q{i}"]
    a = gen.STRINGS["fr"][f"faq.a{i}"] if i != 2 else EXTRA["fr"]["home.faq_a2_home"]
    akey = f"faq.a{i}" if i != 2 else "home.faq_a2_home"
    idx = idx.replace(
        f"""                                {q}
                                <img src=""",
        f"""                                <span data-i18n="faq.q{i}">{q}</span>
                                <img src=""",
        1,
    )
    idx = idx.replace(
        f'<p itemprop="text">{a}</p>',
        f'<p itemprop="text" data-i18n="{akey}">{a}</p>',
        1,
    )

idx = idx.replace("<p>Contactez-nous</p>", '<p data-i18n="home.contact_title">Contactez-nous</p>', 1)
idx = idx.replace(
    ">CONTACTEZ-NOUS CONTACTEZ-NOUS CONTACTEZ-NOUS CONTACTEZ-NOUS CONTACTEZ-NOUS CONTACTEZ-NOUS</textPath>",
    ' data-i18n="home.contact_circle">CONTACTEZ-NOUS CONTACTEZ-NOUS CONTACTEZ-NOUS CONTACTEZ-NOUS CONTACTEZ-NOUS CONTACTEZ-NOUS</textPath>',
)

(ROOT / "index.html").write_text(idx, encoding="utf-8")
print("index.html patched")
