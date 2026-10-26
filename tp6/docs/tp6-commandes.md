# TP6 : commandes de référence

## Contrôles dans l'ordre

| Étape | Commande | Attendu |
| --- | --- | --- |
| T35 | `python -m pytest -q` (après le kit) | 2 échecs voulus : `test_le_modele_se_place_ou_l_on_veut`, `test_l_api_ne_bricole_plus_le_chemin_de_python` |
| T36 | `git mv src/predict.py sentiment_app/predict.py`, puis copier `extraits/predict_compatibilite.py` vers `src/predict.py` | `python src/predict.py "Livraison rapide, produit conforme, très satisfait"` affiche `positive (confiance 78%)` |
| T37 | `python -m pytest -q`, `ruff check .`, `mypy api` | Aucun échec ; `Select-String` ne trouve pas `sys.path` |
| T38 | `pip install -e .`, puis `sentiment --version`, `sentiment predict "..."` | `sentiment-app 0.6.0` ; `POSITIVE 0.777` ; `INDETERMINE 0.5162` pour `xqzvb wlkptr grombu` |
| T39 | `python -m build --wheel` | `dist/sentiment_app-0.6.0-py3-none-any.whl` avec `api`, `sentiment_app`, `ui` |
| T40 | Dans un venv hors du dépôt, installer la roue puis `sentiment predict` | Sans variable : `modèle introuvable`, code 1 ; avec `SENTIMENT_MODELE` : `POSITIVE 0.777` |
| T41 | `git tag -a v0.6.0 -m "TP6 : paquet installable"`, `git push origin v0.6.0` | CI verte, étiquette visible sur GitHub |

## Points à vérifier

- `SEUIL_ABSTENTION` dans `sentiment_app/predict.py` doit correspondre à la valeur retenue au TP4. Vérifiez-la avec `python src/courbe_seuil.py`.
- `api/model.py` remplace la version du TP3 ; les routes de `api/main.py` doivent appeler `load_model()` et `predict(classifier, text)`.
- Les scores exacts (0.777, 0.7465, 0.5162) supposent le modèle de démonstration entraîné avec la graine 42.
