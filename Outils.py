import openfile

def analytique() :
    tab = openfile.openFile("donnees.txt")

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