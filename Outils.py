import openfile

def analytique() :

    tabX = []
    tabY = []
    tab = openfile.openfile("donnees.txt")

    for val in tab:
        tabX.append(val[0])
        tabY.append(val[1])

    minimun = (moyenneXY(tab) - moyenneX(tabX) * moyenneX(tabY)) / moyenneCarre(tabX) - moyenneX(tabX) ** 2

    return minimun


def moyenneCarree(tab):
    somme = 0
    for val in tab:
        somme += val ** 2
    return somme / len(tab)

def moyenneX(tableau) :
    somme = 0
    for val in tableau :
        somme += val
    return somme / len(tableau)


def moyenneXY(tableau) :
    nouveauTableau = []
    for val in tableau :
        nouveauTableau.append(val[0]*val[1])
    return moyenneX(nouveauTableau)

analytique()

print(moyenneXY(openfile.openFile("donnees.txt")))