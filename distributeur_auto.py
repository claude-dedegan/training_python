total_ventes = 0

while True:
    print("\n--- DISTRIBUTEUR AUTOMATIQUE ---")
    print("1. Eau - 250 F")
    print("2. Jus - 500 F")
    print("3. Café - 400 F")
    print("4. Quitter")

    choix = input("Votre choix (1-4) : ")

    if choix == "1":
        prix_boisson = 250
        nom_boisson = "Eau"
    elif choix == "2":
        prix_boisson = 500
        nom_boisson = "Jus"
    elif choix == "3":
        prix_boisson = 400
        nom_boisson = "Café"
    elif choix == "4":
        print(f"\nFin du service. Total des ventes : {total_ventes} F")
        break
    else:
        print("Choix invalide, réessayez.")
        continue

    montant = int(input(f"Vous avez choisi {nom_boisson} ({prix_boisson} F). Insérez l'argent : "))

    while montant < prix_boisson:
        manque = prix_boisson - montant
        print(f"Montant insuffisant. Il manque encore {manque} F.")
        complement = int(input("Ajoutez de l'argent : "))
        montant = montant + complement

    monnaie = montant - prix_boisson
    print(f"Monnaie à rendre : {monnaie} F")
    print(f"{nom_boisson} servie! Bonne dégustation.")

    total_ventes = total_ventes + prix_boisson