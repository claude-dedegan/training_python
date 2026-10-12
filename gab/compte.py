"""
Module comptes.py
------------------
Gere le chargement et la sauvegarde des comptes bancaires
à partir/vers un fichier JSON.
"""

import json
import os

# Chemin vers le fichier JSON (toujours relatif a ce fichier .py)
DOSSIER_COURANT = os.path.dirname(os.path.abspath(__file__))
CHEMIN_JSON = os.path.join(DOSSIER_COURANT,"data", "compte.json")


def charger_comptes():
    """Lit le fichier JSON et retourne le dictionnaire des comptes."""
    try:
        with open(CHEMIN_JSON, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        print("Erreur : fichier de compte introuvable.")
        return {}
    except json.JSONDecodeError:
        print("Erreur : le fichier de compte est corrompu.")
        return {}


def sauvegarder_comptes(compte):
    # écrit le dictionnaire des comptes dans le fichier JSON.
    with open(CHEMIN_JSON, "w", encoding="utf-8") as fichier:
        json.dump(compte, fichier, indent=4, ensure_ascii=False)



