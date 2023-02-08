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


