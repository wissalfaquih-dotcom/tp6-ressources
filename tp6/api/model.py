"""Pont entre l'API et le paquet sentiment_app.

Aucune manipulation de sys.path : l'API importe le paquet comme n'importe quelle dépendance.
"""

from sentiment_app.predict import charger_modele, predire


def load_model():
    """Charge le modèle une fois, au démarrage de l'API."""
    return charger_modele()


def predict(classifier, text: str) -> dict:
    """Classe un texte avec le modèle déjà chargé."""
    return predire(text, modele=classifier)
