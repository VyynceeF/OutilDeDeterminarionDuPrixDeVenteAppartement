import openfile, math

#Calcul du point critique qui correspond à un minimum
#Le point critique est le point où s'annule le gradient
def analytique() :

    tabX = [] #Déclaration tableau des x
    tabY = [] #Déclaration tableau des y
    tab = openfile.openFile("donnees.txt") #Récupération des valeurs du fichier

    #On insere les x et les y dans tabX et tabY
    for val in tab:
        tabX.append(val[0])
        tabY.append(val[1])

    #Calcul de a
    a = (moyenneXY(tab) - moyenneX(tabX) * moyenneX(tabY)) / (moyenneCarree(tabX) - (moyenneX(tabX)**2))
    #Calcul de b
    b = moyenneX(tabY) - a * moyenneX(tabX)

    return (a,b)

#Calcul la moyenne des valeurs aux carrée du tableau tab
def moyenneCarree(tab):
    somme = 0
    for val in tab:
        somme += val ** 2
    return somme / len(tab)

#Calcul la moyenne des valeurs du tableau
def moyenneX(tableau):
    somme = 0
    for val in tableau:
        somme += val
    return somme / len(tableau)

#Calcul la moyenne des x*y du tableau (tableau = [[x1,y1],[x2,y2]])
def moyenneXY(tableau):
    nouveauTableau = []
    for val in tableau:
        nouveauTableau.append(val[0]*val[1])
    return moyenneX(nouveauTableau)

def gradient(a, b) :
    tab = openfile.openFile("donnees.txt")  # Récupération des valeurs du fichier

    sommeXi = 0
    sommeX2 = 0
    sommeYi = 0
    sommeXY = 0
    for i in tab:
        sommeXi += i[0]
        sommeX2 += i[0] ** 2
        sommeYi += i[1]
        sommeXY += i[0]*i[1]

    deriveX = 2 * (a * sommeX2 + b * sommeXi - sommeXY)
    deriveY = 2 * (a * sommeXi + len(tab) * b - sommeYi)

    return (deriveX, deriveY)

def gradientDescent():
    a = 1
    b = 1
    alpha = 0.00001
    derives = gradient(a, b)
    normeGrad = math.sqrt(derives[0]**2+derives[1]**2)
    while(abs(normeGrad) > 0.001):
        derives = gradient(a,b)
        normeGrad = math.sqrt(derives[0]**2+derives[1]**2)
        a = a - alpha * derives[0]
        b = b - alpha * derives[1]
    return (a,b)

print(analytique())
print(gradientDescent())
