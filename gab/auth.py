

"""
Module auth.py
Gere l'authentification d'un utilisateur (numero de compte + code pin).
"""


def authentification(comptes):
    """
    Demande le numero de compte et le code pin.
    Retourne le numero de compte si l'authentification reussit,
    sinon retourne None.
    """
    num_compte = input("Saisissez votre numero de compte : ")
    if num_compte not in comptes:
        print("Compte introuvable")
        return None

    code = input("Entrez votre mot de passe : ")
    while code != comptes[num_compte]["code_pin"]:
        code = input("mot de passe incorrect! Entrez-le a nouveau : ")

    nom = comptes[num_compte]["nom"]
    print(f"Bienvenue Mr/Mme {nom} !")

    return num_compte