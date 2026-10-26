# Ressources du TP6 : packager l'application

Ce dossier reconstruit les fichiers du TP6 à partir du journal de bord. Il faut le recopier dans la racine du dépôt (`sentiment-app`) et vérifier les points de `docs/tp6-commandes.md`.

Contenu :

- `pyproject.toml` : métadonnées du paquet, version 0.6.0, commande `sentiment`.
- `sentiment_app/` : le paquet (`predict.py` pour le chargement et la prédiction, `cli.py` pour la commande).
- `api/model.py` : pont vers le paquet, sans `sys.path`.
- `extraits/predict_compatibilite.py` : fichier à copier dans `src/predict.py` au contrôle T36.
- `tests/test_tp6.py` : les deux tests « voulus » du kit et les contrôles de la commande.
- `.github/workflows/tp6-roue.yml` : étape CI « Roue installée hors du dépôt ».
- `.gitignore.ajout` : lignes à ajouter au `.gitignore`.
- `docs/tp6-commandes.md` : récapitulatif des contrôles T35 à T41.
