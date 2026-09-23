mot_de_passe = "1234"
motDePasse = input(f"Entrez votre mot de passe : ")

while motDePasse != mot_de_passe:
    motDePasse = input(f"Mot de passe incorrect ! Entrez à nouveau votre mot de passe : ")
print("Bienvenu !")