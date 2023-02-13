import Outils

option = input("1 - Méthode analytique\n2 - Descente de gradient\n")

while (option != 10) :
    match option:
        case "1":
            print(Outils.analytique())

        case "2":
            print(Outils.gradientDescent())

        case _:
            print("Option choisi incorrecte")

print("Au revoir")
