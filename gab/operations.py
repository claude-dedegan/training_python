"""
Module operations.py
Contient les operations bancaires disponibles :
depot, retrait et consultation du solde.
"""

from datetime import datetime


def _enregistrer_transaction(compte, num_compte, type_operation, montant):
    #Ajoute une transaction (date, heure, type, montant) dans l'historique du compte.
    maintenant = datetime.now()
    transaction = {
        "date": maintenant.strftime("%Y-%m-%d"),
        "heure": maintenant.strftime("%H:%M:%S"),
        "type_operation": type_operation,
        "montant": montant
    }
    compte[num_compte].setdefault("transactions", [])
    compte[num_compte]["transactions"].append(transaction)


def depot(compte, num_compte):
    #Effectue un depot sur le compte donne.
    try:
        montant = int(input("Entrez le montant que vous voulez deposer : "))
        if montant >= 0:
            compte[num_compte]["solde"] += montant
            _enregistrer_transaction(compte, num_compte, "Depot", montant)
            print("Depot effectue avec succes !")
        else:
            print("Vous ne pouvez pas deposer un montant negatif.")
        return compte[num_compte]["solde"]
    except ValueError:
        print("Erreur ! Vous devez entrer les chiffres.")


def retrait(compte, num_compte):
    #Effectue un retrait sur le compte donne.
    try:
        montant = int(input("Entrez le montant que vous voulez retirer : "))
        if montant >= 0:
            if montant >= compte[num_compte]["solde"]:
                print("Solde insuffisant !")
            else:
                compte[num_compte]["solde"] -= montant
                _enregistrer_transaction(compte, num_compte, "Retrait", montant)
                print("Retrait effectue avec succes.")
        else:
            print("Vous ne pouvez pas retirer une somme negative.")
        return compte[num_compte]["solde"]
    except ValueError:
        print("Erreur ! Vous devez entrer les chiffres.")


def consultation(compte, num_compte):
    #Affiche le nom et le solde du compte.
    nom = compte[num_compte]["nom"]
    solde = compte[num_compte]["solde"]
    print(f"Nom : {nom}\nSolde : {solde}")