#Import
from tkinter import * 

foablak = Tk()

#Def
def ablak():
    ablak_egy = Toplevel(foablak)
    uzenet_egy = Message(ablak_egy, text = "Készítette: Gipsz Jakab\n Piripócs\n 2009.06.04", width = 300)
    gomb_egy = Button(foablak, text = "Kilépés", command = ablak_egy.destroy)
    uzenet_egy.pack()
    gomb_egy.pack()

#Widgets
szoveg_egy = Label(foablak, text = "Kattints ide!")
gomb_ketto = Button(foablak, text = "Névjegy", command = ablak)
szoveg_egy.pack()
gomb_ketto.pack()

foablak.mainloop()
