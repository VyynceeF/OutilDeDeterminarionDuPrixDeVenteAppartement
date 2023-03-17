import Outils
from tkinter import *
from tkinter import filedialog

def fileOpen():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))
    label.configure(text="Fichier actuel: " + filename)


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