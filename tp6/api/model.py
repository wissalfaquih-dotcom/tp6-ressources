"l'API importe le paquet proprement"

from sentiment_app.predict import charger_modele, predire


def load_model():
    """Charge le modèle une fois, au démarrage de l'API."""
    return charger_modele()


def predict(classifier, text: str) -> dict:
    """Classe un texte avec le modèle déjà chargé."""
    return predire(text, modele=classifier)
