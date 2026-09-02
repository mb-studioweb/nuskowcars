# NuskowCars — Site en refonte

Ce dépôt héberge la refonte du site [NuskowCars](https://www.nuskowcars-gmbh.com).

## Structure actuelle

| Emplacement | Rôle |
|---|---|
| **Racine** | Site actif **btcar75** (design cible, export du 2 sept. 2026) |
| **`archive/nuskowcars-original-20250902/`** | Ancien site Webflow NuskowCars complet (référence contenu) |

## Site actif (btcar75)

Pages HTML : `index.html`, `flotte.html`, `a-propos.html`, `faq.html`, fiches véhicules, etc.

Assets : `assets/`, `wp-content/`, `wp-includes/`

## Prochaine étape — intégration contenu Nuskow

Le contenu de l'ancien site (textes, véhicules, images, logo, pages FR/DE/EN, vidéos LFS) sera migré depuis `archive/nuskowcars-original-20250902/` vers la base btcar75. **Aucune fusion n'a encore été effectuée.**

## Lancer en local

```bash
python3 -m http.server 8080
```

Puis ouvrir http://localhost:8080

## Vidéos LFS (archive Nuskow)

Les 5 vidéos de l'ancien site sont dans l'archive, trackées via Git LFS. Après clone :

```bash
git lfs install
git lfs pull
```

## Export btcar75 (release)

Le ZIP source est disponible en [GitHub Release](https://github.com/mb-studioweb/nuskowcars/releases/tag/btcar75-export-20260902) : `btcar75-export-20260902.zip`
