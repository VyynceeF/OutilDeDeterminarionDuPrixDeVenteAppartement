import math
import openfile

from statistics import median, mean
from math import isnan
from itertools import filterfalse

def analytique(donnees):
    """
    Determine le minimum d'une fonction de maniere analytique
    :param donnees: nom du fichier de données
    :return: le point minimum de la fonction
    """
    tab = openfile.formatageDonnees(donnees) #Récupération des données
    tabA = tab[0]  # Récupération tableau des a
    tabB = tab[1]  # Récupération tableau des b

    # Calcul de a, en applicant la formule "cov(x,y) / V(x)"
    a = (moyenneXY(tabA, tabB) - mean(tabA) * mean(tabB)) / (moyenneCarree(tabA) - (mean(tabA) ** 2))
    # Calcul de b, en applicant la formule "moy(y) - a * moy(x)"
    b = mean(tabB) - a * mean(tabA)

    return a, b


def moyenneCarree(tableau):
    """
    Calcul la moyenne des valeurs au carrée d'un tableau
    :param tableau: [x1,...,xn]
    :return: la moyenne des variables au carrées d'un tableau
    """
    somme = 0
    for val in tableau:
        somme += val ** 2
    return somme / len(tableau)


def moyenneXY(tableauA, tableauB):
    """
    Calcul la moyenne des x * y du tableau
    :param tableauA: tableau contenant toutes les donnees, tableau = [[x1,y1],...,[xn,yn]]
    :param tableauA: tableau contenant toutes les donnees, tableau = [[x1,y1],...,[xn,yn]]
    :return: la moyenne des xy
    """
    nouveauTableau = []
    for i in range (len(tableauA)):
        nouveauTableau.append(tableauA[i] * tableauB[i])
    return mean(nouveauTableau)

def mediane(tableau):
    """
    Calcul la médiane d'un tableau
    :param tableau: données à traités
    :return: la médiane du jeu de données
    """
    tableauPropre = list(filterfalse(isnan, tableau))  #Retire les valeurs NaN si présente
    sorted(tableauPropre)  #Tri des données dans l'ordre croissant
    return median(tableauPropre)

def gradient(a, b, sommeXi, sommeX2, sommeYi, sommeXY, lenTab):
    """
    Calcul le gradient d'une fonction de deux variables
    :param a: valeur de la premiere variable
    :param b: valeur de la seconde variable
    :param sommeXi: somme de tout les a du jeu de données
    :param sommeX2: somme de tout les a au carré du jeu de données
    :param sommeYi: somme de tout les b du jeu de données
    :param sommeXY: somme de tout les a+b du jeu de données
    :param lenTab: longueur de jeu de données
    :return: les dérivés partielles de a et b
    """
    deriveX = 2 * (a * sommeX2 + b * sommeXi - sommeXY)
    deriveY = 2 * (a * sommeXi + lenTab * b - sommeYi)

    return deriveX, deriveY


def gradientDescent(donnees):
    """
    Determine le minimum d'une fonction  en appliquant la descente de gradient
    :param donnees: nom du fichier de données
    :return: la pente et l'ordonnée à l'origine au point minimum
    """

    tableau = openfile.formatageDonnees(donnees) #Tuple de données
    ancienA = a = mediane(tableau[0]) #Optimisation du a en prenant la médiane des valeurs
    ancienB = b = mediane(tableau[1]) #Optimisation du b en prenant la médiane des valeurs

    lenTab = len(tableau[0])
    sommeXi = sum(tableau[0])
    sommeX2 = sum(a1 * a2 for a1, a2 in zip(tableau[0], tableau[0]))
    sommeYi = sum(tableau[1])
    sommeXY = sum(a * b for (a,b) in zip(tableau[0], tableau[1]))

    alpha = 0.01 #Taux d'apprentissage/ pas déplacement entre chaque itération
    derives = gradient(a, b, sommeXi, sommeX2, sommeYi, sommeXY, lenTab)
    normeGrad = math.sqrt(derives[0] ** 2 + derives[1] ** 2)

    while normeGrad > 1e-3:
        ancienA, a = a, a - alpha * derives[0]
        ancienB, b = b, b - alpha * derives[1]
        derives = gradient(a, b, sommeXi, sommeX2, sommeYi, sommeXY, lenTab)
        normeGrad = math.sqrt(derives[0] ** 2 + derives[1] ** 2)

        #Réduction du taux d'apprentissage au cours du programme
        if ancienA < a and ancienB < b :
            alpha /= 10

    return a, b