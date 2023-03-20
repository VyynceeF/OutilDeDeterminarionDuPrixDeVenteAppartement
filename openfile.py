"""
Ensemble de méthodes permettant l'usage de fichier de
données pour l'utilisation dans la calcul analytique
et dans la desce
"""

def openFile(name):
    """
    Ouverture d'un fichier
    :param name: nom du fichier à ouvrir
    :return: un tableau de tableau [[x1,y1],...,[xn,yn]]
    """
    tab = []
    file = open(name, "r") #Ouvre le fichier
    lines = file.readlines() #Récupère les lignes du fichiers
    for line in lines: #On boucle dans les lignes
        surface = float(line.split()[0]) #Recupere la surface
        prx = float(line.split()[1]) #Recupere le prix
        tab.append([surface, prx]) #Ajoute au tableau le sous-tableau [surface, prix]
    return tab

def formatageDonnees(donnees):
    """
    Formate les données récupérées dans un fichier sous forme de tuple
    :param donnees: nom du fichier
    :return: les données sous forme d'un tuple = ([a1,...,an], [b1,...,bn])
    """
    tabX = []  # Déclaration tableau des x
    tabY = []  # Déclaration tableau des y
    tab = openFile(donnees)  # Récupération des valeurs du fichier

    # On insere les x et les y dans tabX et tabY
    for val in tab:
        tabX.append(val[0])
        tabY.append(val[1])

    return(tabX, tabY)
