"""
Module main.py
----------------
Point d'entrée du programme : boucle principale de GAB.
"""

from gab.compte import charger_comptes, sauvegarder_comptes
from auth import authentification
from operations import depot, retrait, consultation


def menu():
    print("\n------MENU GAB--------")
    print("1. Faire un Depot")
    print("2. Faire un Retrait")
    print("3. Consulter le solde")
    print("0. Quitter")


def main():
    compte = charger_comptes()

    while True:
        num = authentification(compte)
        if num is None:
            continue

        while True:
            menu()
            try:
                choix = int(input("Quelle operation voulez-vous faire ? : "))
            except ValueError:
                print("Choix invalide")
                continue

            if choix == 1:
                print("Bienvenu au portail de Depot !")
                depot(compte, num)
                sauvegarder_comptes(compte)
            elif choix == 2:
                print("Bienvenu au portail de Retrait !")
                retrait(compte, num)
                sauvegarder_comptes(compte)
            elif choix == 3:
                consultation(compte, num)
            elif choix == 0:
                print("Merci pour l'utilisation de notre GAB. Au revoir !")
                break
            else:
                print("Choix invalide")


if __name__ == "__main__":
    main()