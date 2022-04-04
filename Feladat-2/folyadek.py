from tkinter import * 
import math

foablak = Tk()


#def
def liter():
    m = int(mezo2.get()) 
    r = int(mezo3.get())
    mennyiseg = int(mezo7.get())

    terfogat = math.pi * (m * m) * r

    mezo5.delete(0, END)
    mezo5.insert(0, str(mennyiseg)+" liter borunk van")
    mezo6.delete(0, END)
    
    if mennyiseg <= 100:
        mezo6.insert(0, str()+" Belefér-e? Igen")
    else:
        mezo6.insert(0, str()+" Belefér-e? Nem")

    mezo4.delete(0, END)
    mezo4.insert(0, str(terfogat)  +" a hordó térfogata.")

#Kód

szoveg = Label(foablak, text = "Van egy henger alakú hordónk, melybe nem tudjuk, hogy belefér-e a rendelkezésre álló bor.")
szoveg.grid(row = 0, column = 0)

elval = Label(foablak, text = " ")
elval.grid(row = 1, column = 1)

elval1 = Label(foablak, text = " ")
elval1.grid(row = 2, column = 0)

cimke1 = Label(foablak, text = "Hordó magassága: ")
cimke1.grid(row = 3, column = 0)

mezo2 = Entry(foablak)
mezo2.grid(row = 3, column = 1)

elval2 = Label(foablak, text = " ")
elval2.grid(row = 4, column = 0)

cimke2 = Label(foablak, text = "Hordó sugara: ")
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

cimke4 = Label(foablak, text = "A hordóba ennyi folyadék fér: ")
cimke4.grid(row = 2, column = 0)

mezo7 = Entry(foablak)
mezo7.grid(row = 2, column = 1)

foablak.mainloop()