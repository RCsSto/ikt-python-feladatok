from tkinter import * 
import math

foablak = Tk()


#def
def liter():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = int(mezo3.get())

    N = math.pi * b * b * c
    R = N / 100


    M = d / a
    mezo5.delete(0, END)
    mezo5.insert(0, str(s)+" bor")
    mezo6.delete(0, END)
    mezo6.insert(0, str()+" igen")

    mezo4.delete(0, END)
    mezo4.insert(0, str(PLNRW)+" liter")

#Kód

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

cimke3 = Label(foablak, text = ("A hordóba 100 liter folyadék fér"))
cimke3.grid(row = 6, column = 0)

elval3 = Label(foablak, text = " ")
elval3.grid(row = 7, column = 0)

mezo4 = Entry(foablak)
mezo4.grid(row = 8, column = 1)

gomb = Button(foablak, text="Kiszámítás", command=liter)
gomb.grid(row = 7, column = 1)

mezo5 = Entry(foablak)
mezo5.grid(row = 8, column = 3)

mezo6 = Entry(foablak)
mezo6.grid(row = 8, column = 5)

foablak.mainloop()