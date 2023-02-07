#Ouverture d'un fichier et renvoie des valeurs dans un tableau
#Le paramètre name est le chemin du fichier
def openFile(name):
    tab = []
    file = open(name, "r") #Ouvre le fichier
    lines = file.readlines() #Récupère les lignes du fichiers
    for line in lines: #On boucle dans les lignes
        surface = float(line.split()[0]) #Recupere la surface
        prx = float(line.split()[1]) #Recupere le prix
        tab.append([surface, prx]) #Ajoute au tableau le sous-tableau [surface, prix]
    return tab


