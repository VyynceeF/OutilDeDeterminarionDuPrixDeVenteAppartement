import openfile
def analytique() :

    tabX = []
    tabY = []
    tab = openfile.openfile("donnees.txt")

    for val in tab:
        tabX.append(val[0])
        tabY.append(val[1])

    minimun = (moyenneXY(tab) - moyenneX(tabX) * moyenneX(tabY)) / moyenneCarre(tabX) - moyenneX(tabX)**2

    return minimun

def moyenneCarree(tab):
    somme = 0
    for val in tab:
        somme += val**2
    return somme/ len(tab)

analytique()
