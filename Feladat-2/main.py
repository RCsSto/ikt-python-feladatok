#Import
from tkinter import * 

foablak = Tk()
foablak.title("Adatok")
foablak.minsize(width = 300, height = 100)

#Def
def ablak():
    ablak_egy = Toplevel(foablak)
    ablak_egy.title("Eredmények")
    ablak_egy.minsize(width = 300, height = 100)

    #Widgets a második ablakon
    szoveg_egy = Label(ablak_egy, text = "Felszín: ")
    szoveg_ketto =  Label(ablak_egy, text = "Térfogat: ")
    mezo_egy = Entry(ablak_egy)
    mezo_ketto = Entry(ablak_egy)

    #Place a második ablakon
    szoveg_egy.grid(row = 1)
    szoveg_ketto.grid(row = 2)
    mezo_egy.grid(row = 1, column = 2, sticky = W)
    mezo_ketto.grid(row = 2, column = 2, sticky = W)

    #Math
    a = int(mezo_egy.get())
    b = int(mezo_ketto.get())
    c = int(mezo_harom.get())

    felszin = 2 * (a * b + b * c + a * c)
    terfogat = a * b * c

    mezo_egy.delete(0, END)
    mezo_egy.insert(0, str(felszin))
    mezo_ketto.delete(0, END)
    mezo_ketto.insert(0, str(terfogat))

    ablak_egy.mainloop()

#Widgets a főablakon
szoveg_negy = Label(foablak, text = "a: ")
szoveg_ot = Label(foablak, text = "b: ")
szoveg_hat = Label(foablak, text = "c: ")

gomb_egy = Button(foablak, text = "Számítás", command = ablak)

mezo_negy = Entry(foablak)
mezo_ot = Entry(foablak)
mezo_hat = Entry(foablak)

#Place a főablakon
szoveg_negy.grid(row = 1)
szoveg_ot.grid(row = 2)
szoveg_hat.grid(row = 3)

gomb_egy.grid(row = 4, column = 2, sticky = W)

mezo_negy.grid(row = 1, column = 2, sticky = W)
mezo_ot.grid(row = 2, column = 2, sticky = W)
mezo_hat.grid(row = 3, column = 2, sticky = W)

foablak.mainloop()