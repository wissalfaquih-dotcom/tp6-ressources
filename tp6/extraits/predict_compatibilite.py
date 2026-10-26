"""Fichier de compatibilité : ancien emplacement de predict.py (TP2 à TP5).

Copié dans src/predict.py au contrôle T36, il permet de continuer à lancer
`python src/predict.py "texte"` après le déplacement du module dans le paquet.
"""

import sys

from sentiment_app.predict import ModeleIntrouvable, charger_modele, predire


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print("usage : python src/predict.py \"texte de l'avis\"", file=sys.stderr)
        return 2
    try:
        modele = charger_modele()
    except ModeleIntrouvable as erreur:
        print(f"Erreur : {erreur}", file=sys.stderr)
        return 1
    resultat = predire(argv[0], modele)
    print(f"{resultat['label'].lower()} (confiance {round(resultat['score'] * 100)}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
