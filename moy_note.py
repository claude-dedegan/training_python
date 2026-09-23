n = int(input("Combien de notes souhaitez-vous saisir ? : "))

somme = 0
for i in range(n):
    note_i = int(input(f"Entrez la note {i+1}: "))
    somme = somme + note_i
moy = somme / n
print(f"La moyenne est {moy}")
if moy >= 10:
    print("Admis !")
else:
    print("Non admis !")
