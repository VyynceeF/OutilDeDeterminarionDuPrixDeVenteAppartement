import math
import openfile

def analytique() :
    """
    Determine le minimum d'une fonction de maniere analytique
    en applicant la formule "cov(x,y) / V(x)"
    :return: la pente et l'ordonnée à l'origin
    """

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

def moyenneCarree(tableau):
    """
    Calcul la moyenne des valeurs au carrée d'un tableau
    :param tableau: [x1,...,xn]
    :return: la moyenne des variables d'un tableau
    """
    somme = 0
    for val in tableau:
        somme += val ** 2
    return somme / len(tableau)

def moyenneX(tableau):
    """
    Calcul la moyenne des valeurs d'un tableau
    :param tableau: tableau contenant les données en x, tableau [x1,...,xn]
    :return: la moyenne d'un tableau contenant qu'une variable
    """
    somme = 0
    for val in tableau:
        somme += val
    return somme / len(tableau)

def moyenneXY(tableau):
    """
    Calcul la moyenne des x * y du tableau
    :param tableau: tableau contenant toutes les donnees, tableau = [[x1,y1],...,[xn,yn]]
    :return: la moyenne des xy
    """
    nouveauTableau = []
    for val in tableau:
        nouveauTableau.append(val[0]*val[1])
    return moyenneX(nouveauTableau)

def gradient(a, b) :
    """
    Calcul le gradient de a et b
    :param a: pente de la droite
    :param b: ordonnée à l'origine
    :return:  les derives partielles de a et b
    """
    tab = openfile.openFile("donnees.txt")  #Récupération des valeurs du fichier

    sommeXi = 0
    sommeX2 = 0
    sommeYi = 0
    sommeXY = 0

    for i in tab:
        sommeXi += i[0]
        sommeX2 += i[0]**2
        sommeYi += i[1]
        sommeXY += i[0] * i[1]

    deriveX = 2 * (a * sommeX2 + b * sommeXi - sommeXY)
    deriveY = 2 * (a * sommeXi + len(tab) * b - sommeYi)

    return (deriveX, deriveY)

def gradientDescent():
    """
    Determine le minimum d'une fonction  en appliquant la descente de gradient
    :return: la pente et l'ordonnée à l'origin au point minimum
    """
    a = 1
    b = 1
    alpha = 0.00001
    derives = gradient(a, b)
    normeGrad = math.sqrt(derives[0]**2+derives[1]**2)
    while(abs(normeGrad)>1e-6) :
        derives = gradient(a,b)
        normeGrad = math.sqrt(derives[0]**2+derives[1]**2)
        a = a - alpha * derives[0]
        b = b - alpha * derives[1]
    return (a,b)
