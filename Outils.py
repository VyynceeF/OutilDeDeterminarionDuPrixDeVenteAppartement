import math
import openfile

from statistics import median
from math import isnan
from itertools import filterfalse


def formatageDonnees(donnees):

    tabX = []  # Déclaration tableau des x
    tabY = []  # Déclaration tableau des y
    tab = openfile.openFile(donnees)  # Récupération des valeurs du fichier

    # On insere les x et les y dans tabX et tabY
    for val in tab:
        tabX.append(val[0])
        tabY.append(val[1])

    return(tabX, tabY)

def analytique(donnees):
    """
    Determine le minimum d'une fonction de maniere analytique
    en applicant la formule "cov(x,y) / V(x)"
    :return: la pente et l'ordonnée à l'origin
    """
    tab = formatageDonnees(donnees)
    tabA = tab[0]  # Déclaration tableau des x
    tabB = tab[1]  # Déclaration tableau des y
    
    # Calcul de a
    a = (moyenneXY(tabA, tabB) - moyenneX(tabA) * moyenneX(tabB)) / (moyenneCarree(tabA) - (moyenneX(tabA) ** 2))
    # Calcul de b
    b = moyenneX(tabB) - a * moyenneX(tabA)

    return (a, b)


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


def moyenneXY(tableauA, tableauB):
    """
    Calcul la moyenne des x * y du tableau
    :param tableau: tableau contenant toutes les donnees, tableau = [[x1,y1],...,[xn,yn]]
    :return: la moyenne des xy
    """
    nouveauTableau = []
    for i in range (len(tableauA)):
        nouveauTableau.append(tableauA[i] * tableauB[i])
    return moyenneX(nouveauTableau)

def mediane(tableau):

    tableauPropre = list(filterfalse(isnan, tableau))  # Strip NaN values
    sorted(tableauPropre)  # Sorting now works as expected
    return median(tableauPropre)

def gradient(a, b, donnees):
    """
    Calcul le gradient de a et b
    :param a: pente de la droite
    :param b: ordonnée à l'origine
    :return:  les derives partielles de a et b
    """
    tab = openfile.openFile(donnees)  # Récupération des valeurs du fichier

    sommeXi = 0
    sommeX2 = 0
    sommeYi = 0
    sommeXY = 0

    for i in tab:
        sommeXi += i[0]
        sommeX2 += i[0] ** 2
        sommeYi += i[1]
        sommeXY += i[0] * i[1]

    deriveX = 2 * (a * sommeX2 + b * sommeXi - sommeXY)
    deriveY = 2 * (a * sommeXi + len(tab) * b - sommeYi)

    return (deriveX, deriveY)


def gradientDescent(donnees):
    """
    Determine le minimum d'une fonction  en appliquant la descente de gradient
    :return: la pente et l'ordonnée à l'origine au point minimum
    """

    tableau = formatageDonnees(donnees)
    ancienA = a = mediane(tableau[0])
    ancienB = b = mediane(tableau[1])
    ite = 0
    alpha = 0.01
    derives = gradient(a, b, donnees)

    normeGrad = math.sqrt(derives[0] ** 2 + derives[1] ** 2)

    while normeGrad > 1e-3:
        ite += 1
        ancienA, a = a, a - alpha * derives[0]
        ancienB, b = b, b - alpha * derives[1]
        derives = gradient(a, b, donnees)
        normeGrad = math.sqrt(derives[0] ** 2 + derives[1] ** 2)

        if ancienA < a and ancienB < b :
            alpha /= 10
        print(a,b)

    return a, b, ite

donnees = "donnees.txt"
print(analytique(donnees))
print(gradientDescent(donnees))