import os
import Outils
from tkinter import *
from tkinter import filedialog

option = ""
global filename
def fileOpen():
    global filename
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File")
    name = ""
    i = len(filename)-1
    while filename[i] != "\\":
        name = filename[i] + name
        i -= 1

    label.configure(text="Fichier actuel :\n" + name)

def creer():
    os.system("py " + os.getcwd() + "\\traitement.py")

def calculAnalytique():
    global filename
    if filename != "":
        resultat = Outils.analytique(filename)
        labelResultatAnalytique.configure(text= "a = " + str(round(resultat[0], 2)) + " b = " + str(round(resultat[1],2)))

def descenteGrdt():
    global filename
    if filename != "":
        resultat = Outils.gradientDescent(filename)
        labelResultatGrdt.configure(text= "a = " + str(round(resultat[0],2)) + " b = " + str(round(resultat[1],2)))

window = Tk()
window.title("Outil d'aide à la determination")
window.geometry('450x350')
window.resizable(width = 900, height = 900)
window["bg"] = "#e1e6ec"

frameTop = Frame(window)
frameTop.pack(side=TOP, pady=10, padx=10)

frameBottom = Frame(window)
frameBottom.pack(side=TOP, pady=10, padx=10)

#Frame Haut Droite
frameDroite = Frame(frameTop)
frameDroite.pack(side = LEFT, pady=10, padx=10)

label = Label(frameDroite, text="Selectionner un fichier")
label.pack(padx= 10, pady = 10)

bouton = Button( frameDroite, text = "Choisir un fichier", command=fileOpen)
bouton.pack(padx= 10, pady = 10)

#Frame bas droite
frameBasDroite = Frame(frameBottom)
frameBasDroite.pack(side = LEFT, padx= 10, pady = 10)

labelAnalytique = Label(frameBasDroite, text="Calcul Analytique")
labelAnalytique.pack(padx= 10, pady = 10)

buttonAnalytique = Button(frameBasDroite, text="Calculer", command = calculAnalytique)
buttonAnalytique.pack(padx= 10, pady = 10)

labelResultatAnalytique = Label(frameBasDroite)
labelResultatAnalytique.pack(padx= 10, pady = 10)

#Frame Haut Gauche
frameGauche = Frame(frameTop)
frameGauche.pack(side = RIGHT, padx= 10, pady = 10)

labelCreer = Label(frameGauche, text="Créer un fichier de données")
labelCreer.pack(padx= 10, pady = 10)

btn = Button(frameGauche, text="Creer", command=creer)
btn.pack()

#Frame Bas Gauche
frameBasGauche = Frame(frameBottom)
frameBasGauche.pack(side = RIGHT, padx= 10, pady = 10)

labelGrd = Label(frameBasGauche, text="Descente de gradient")
labelGrd.pack(padx= 10, pady = 10)

buttonGrdt = Button(frameBasGauche, text="Calculer", command = descenteGrdt)
buttonGrdt.pack(padx= 10, pady = 10)

labelResultatGrdt = Label(frameBasGauche)
labelResultatGrdt.pack(padx= 10, pady = 10)

window.mainloop()