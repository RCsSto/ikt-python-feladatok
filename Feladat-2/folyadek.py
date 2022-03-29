from tkinter import * 
import math

foablak = Tk()

def liter():
    szam = int(mezo1.get())
    print(szam)

def callback():
    global buttonClicked
    buttonClicked = not buttonClicked 

buttonClicked = False
hordo = 100

szoveg = Label(foablak, text = "Van egy henger alakú hordónk, melybe nem tudjuk, hogy belefér-e a rendelkezésre álló bor.")
szoveg.grid(row = 0, column = 0)

cimke = Label(foablak, text = "Bor mennyiség: ")
cimke.grid(row = 1, column = 0)

mezo1 = Entry(foablak)
mezo1.grid(row = 1, column = 1)

elval = Label(foablak, text = " ")
elval.grid(row = 1, column = 2)

elval1 = Label(foablak, text = " ")
elval1.grid(row = 2, column = 0)

cimke1 = Label(foablak, text = "Hordó magassága: ")
cimke1.grid(row = 3, column = 0)

mezo2 = Entry(foablak)
mezo2.grid(row = 3, column = 1)

elval2 = Label(foablak, text = " ")
elval2.grid(row = 4, column = 0)

cimke2 = Label(foablak, text = "Mi a hordó sugara?")
cimke2.grid(row = 5, column = 0)

mezo3 = Entry(foablak)
mezo3.grid(row = 5, column = 1)

elval3 = Label(foablak, text = " ")
elval3.grid(row = 4, column = 0)

cimke3 = Label(foablak, text = ("A hordóba", hordo, " liter folyadék fér"))
cimke3.grid(row = 6, column = 0)

foablak.mainloop()