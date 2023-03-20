import os
def creation(name):
    if not os.path.exists(name):
        newFile = open(name,"w")
        données = ""
        choix = ""

        while(choix != "NON"):

            choix = input("Voulez-vous saisir des données ? (OUI, NON) ")
            match choix:
                case "OUI":
                    données += initialisation()
                case "NON":
                    print("Votre fichier à été créer")
                case _:
                    print("Choix incorrect")

        newFile.write(données)
    else :
        print("Erreur! Le fichier existe déjà.")

def initialisation():
    texte = ""

    addSurface = typage(input("Entrer une surface : "))
    while(not isinstance(addSurface, (float))):
        print("Erreur! type de la valeur incorrecte.")
        addSurface = typage(input("Entrer une surface : "))

    addPrix = typage(input("Entrer le prix de cette surface : "))
    while (not isinstance(addPrix, (float))):
        print("Erreur! type de la valeur incorrecte.")
        addPrix = typage(input("Entrer le prix de cette surface : "))

    texte += str(addSurface) + "\t" + str(addPrix) + "\n"
    return texte

def typage(valeur):
    try:
        newValeur = float(valeur)
        return newValeur
    except:
        return valeur

name = str(input("Entrer un nom : "))
creation(name + ".txt")