import Outils, os, traitement
import Outils
from tkinter import *
from tkinter import filedialog

option = input("1 - Méthode analytique\n2 - Descente de gradient\n3 - Créer et initialiser votre fichier de données")
def fileOpen():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))
    label.configure(text="Fichier actuel: " + filename)

while (option != "10") :
    match option:
        case "1":
            print(Outils.analytique())
        case "2":
            print(Outils.gradientDescent())
        case "3":
            name = str(input("Entrer le nom du fichier à créer : ")) + ".txt"
            traitement.creation(name)
        case _:
            print("Option choisi incorrecte")

window = Tk()
window.title("Outil d'aide à la determination")
window.geometry('500x500')
window.resizable(width = 0, height = 0)
window["bg"] = "#e1e6ec"

label = Label(window, text="Fichier actuel : ")
label.pack()

saisie = Entry(window, width=10)
saisie.pack()

bouton = Button( window , text = "Choisir un fichier", command=fileOpen)
bouton.pack()

window.mainloop()