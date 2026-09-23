import random

nombre_mystere = random.randint(1,100)
print(f"Devinez un nombre compris entre 1 et 100. Vous avez 5 tentatives")
i = 0
while i <= 4:
    nombreMystere = int(input(f"Entrez le nombre : "))
    if nombreMystere == nombre_mystere:
        print(f"Bravooo vous avez gagne ! Nombre de tentative : {i+1} ")
        break
    elif nombreMystere < nombre_mystere:
        print("Le nombre est trop petit")
    else:
        print("Le nombre est trop grand")
    i = i + 1
    if i == 5:
        print(f"Nombre de tentatives épuisé ! Le nombre mystère était {nombre_mystere}")