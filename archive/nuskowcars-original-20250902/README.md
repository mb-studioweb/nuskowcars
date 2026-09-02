# NuskowCars - Archive du site Webflow

Sauvegarde statique du site [nuskowcars-gmbh.com](https://www.nuskowcars-gmbh.com) récupérée le 2 septembre 2026.

## Contenu

- **50 pages HTML** : accueil, véhicules, réservation, mentions légales (FR / DE / EN)
- **~250 assets locaux** : images, CSS, JavaScript, polices
- **5 vidéos lourdes** : conservées via le CDN Webflow d'origine (limite API)

## Lancer en local

```bash
python3 -m http.server 8080
```

Puis ouvrir http://localhost:8080


## Vidéos (Git LFS)

Les 5 vidéos de fond sont stockées via Git LFS. Après clone :

```bash
git lfs install
git lfs pull
```
