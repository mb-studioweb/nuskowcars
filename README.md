# NuskowCars — Site statique (ancien Webflow)

Site de location de véhicules de prestige [NuskowCars](https://www.nuskowcars-gmbh.com), export statique de l’ancien site Webflow.

Le design **btcar75** développé ensuite est conservé en archive : [`archive/btcar75-design-20260917/`](archive/btcar75-design-20260917/).

## Pages

| Page | Fichier |
|---|---|
| Accueil | `index.html` |
| Nos véhicules | `nos-vehicules.html` |
| Réservation | `reservation.html` |
| Mentions légales | `mentions-legales.html` |
| Fiches véhicules | `vehicules/` |
| Allemand | `german.html` + `german/` |
| Anglais | `en.html` + `en/` |

## Lancer en local

```bash
python3 -m http.server 8080
```

Puis ouvrir http://localhost:8080

## Hébergement (GitHub Pages)

Site **100 % statique** (HTML/CSS/JS) — GitHub Pages suffit.

1. **Settings → Pages** → Source : **GitHub Actions**
2. Relancer le workflow **Deploy GitHub Pages**

URL : `https://mb-studioweb.github.io/nuskowcars/`

## Vidéos (Git LFS)

Les vidéos sont stockées via Git LFS. Après clone :

```bash
git lfs install
git lfs pull
```

## Archives

| Dossier | Contenu |
|---|---|
| [`archive/nuskowcars-original-20250902/`](archive/nuskowcars-original-20250902/) | Copie de référence de cet export Webflow |
| [`archive/btcar75-design-20260917/`](archive/btcar75-design-20260917/) | Design btcar75 complet (accueil, flotte, carrosserie, FAQ, etc.) |
