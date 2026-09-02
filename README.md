# NuskowCars — Site sur base btcar75

Site de location de véhicules de prestige [NuskowCars](https://www.nuskowcars-gmbh.com), construit sur le design **btcar75** avec le contenu issu de l'ancien site Webflow.

## Structure

| Emplacement | Contenu |
|---|---|
| **Racine** | Site actif FR : `index.html`, `flotte.html`, `a-propos.html`, `faq.html` |
| **`reservation.html`** | Formulaire de réservation multi-étapes (identique à l'ancien site) |
| **`vehicules/`** | 13 fiches véhicules (FR), dont Mercedes CLA45S AMG |
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

## Hébergement (GitHub Pages)

Ce site est **100 % statique** (HTML/CSS/JS) : **GitHub Pages suffit**, Render n'est pas nécessaire.

| Option | Verdict |
|---|---|
| **GitHub Pages** | Recommandé — gratuit, déploiement auto à chaque push sur `main` |
| **Render / Netlify / Vercel** | Possible aussi, mais pas obligatoire |
| **Serveur PHP/backend** | Non requis (formulaire réservation sans envoi email) |

### Activer Pages (obligatoire, une fois)

Le workflow ne peut **pas** activer Pages tout seul (limite de sécurité GitHub). Un admin du repo doit :

1. Ouvrir **Settings → Pages** : `https://github.com/mb-studioweb/nuskowcars/settings/pages`
2. **Build and deployment** → Source : **GitHub Actions**
3. Enregistrer, puis relancer le workflow **Deploy GitHub Pages** (onglet Actions)

**Dépôt privé :** sur le plan gratuit, GitHub Pages ne fonctionne que si le dépôt est **public**. Sinon, passer à GitHub Pro (compte perso) ou Team (organisation), ou utiliser Render/Netlify.

URL une fois en ligne : `https://mb-studioweb.github.io/nuskowcars/`

### Domaine personnalisé (optionnel)

Pour `www.nuskowcars-gmbh.com` : Pages → **Custom domain** → ajouter le domaine et configurer le DNS chez votre registrar (CNAME vers `mb-studioweb.github.io`).


```bash
python3 -m http.server 8080
```

Puis ouvrir http://localhost:8080

## Vidéos LFS (archive)

Les vidéos de l'ancien site restent dans `archive/nuskowcars-original-20250902/` via Git LFS. Le hero vidéo actif est `assets/hero.mp4` (copié depuis l'archive).

## Scripts

- `scripts/integrate-nuskow.py` — génération pages véhicules et contenu
- `scripts/build-reservation.py` — formulaire de réservation depuis l'archive Webflow
- `scripts/apply-i18n.py` — traductions DE/EN, CLA45, suppression Analytics

## Export design btcar75

ZIP source : [GitHub Release btcar75-export-20260902](https://github.com/mb-studioweb/nuskowcars/releases/tag/btcar75-export-20260902)
