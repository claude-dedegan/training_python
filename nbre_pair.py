n = int(input("Combien de nombres souhaitez-vous saisir ? : "))

nombre_pair = 0
nombre_impair = 0
for i in range(n):
    nombre_i = int(input(f"Entrez le nombre {i+1}: "))
    if nombre_i % 2 == 0:
        nombre_pair = nombre_pair + 1
    else:
        nombre_impair = nombre_impair + 1
print(f"On a {nombre_pair} nombres pairs et {nombre_impair} nombres impairs !")