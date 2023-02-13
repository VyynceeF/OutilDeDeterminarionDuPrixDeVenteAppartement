import Outils, os, traitement

option = input("1 - Méthode analytique\n2 - Descente de gradient\n3 - Créer et initialiser votre fichier de données")

while (option != "10") :
    match option:
        case "1":
            print(Outils.analytique())
        case "2":
            print(Outils.gradientDescent())
        case "3":
            name = str(input("Entrer le nom du fichier à créer : ")) + ".txt"
            traitement.creation(name)
        case _:
            print("Option choisi incorrecte")

print("Au revoir")
