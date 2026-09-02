# NuskowCars — Site sur base btcar75

Site de location de véhicules de prestige [NuskowCars](https://www.nuskowcars-gmbh.com), construit sur le design **btcar75** avec le contenu issu de l'ancien site Webflow.

## Structure

| Emplacement | Contenu |
|---|---|
| **Racine** | Site actif FR : `index.html`, `flotte.html`, `a-propos.html`, `faq.html` |
| **`reservation.html`** | Formulaire de réservation multi-étapes (identique à l'ancien site) |
| **`german.html`** + **`german/`** | Version allemande (accueil + pages + véhicules) |
| **`en.html`** + **`en/`** | Version anglaise |
| **`assets/`** | Logo, favicon, hero, images véhicules (`assets/vehicules/{slug}/`) |
| **`archive/nuskowcars-original-20250902/`** | Ancien site Webflow (référence permanente) |

## Langues

- **FR** : racine (`index.html`, `flotte.html`, …)
- **DE** : `german.html` (accueil) + `german/flotte.html`, `german/vehicules/…`
- **EN** : `en.html` + `en/flotte.html`, `en/vehicules/…`

Sélecteur de langue (🇫🇷 🇩🇪 🇬🇧) dans le header de chaque page.

## Contact

- Téléphone / WhatsApp : **06 37 00 20 45**
- Instagram : [@nuskowcars](https://www.instagram.com/nuskowcars/)
- Snapchat : [nuskowcars](https://snapchat.com/t/FrTH4qct)

## Lancer en local

```bash
python3 -m http.server 8080
```

Puis ouvrir http://localhost:8080

## Vidéos LFS (archive)

Les vidéos de l'ancien site restent dans `archive/nuskowcars-original-20250902/` via Git LFS. Le hero vidéo actif est `assets/hero.mp4` (copié depuis l'archive).

## Script d'intégration

`scripts/integrate-nuskow.py` — régénère pages véhicules et peut repatcher le contenu depuis l'archive.

## Export design btcar75

ZIP source : [GitHub Release btcar75-export-20260902](https://github.com/mb-studioweb/nuskowcars/releases/tag/btcar75-export-20260902)
