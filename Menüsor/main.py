# Import

from tkinter import * 

# Foablak 

foablak = Tk()
foablak.title("A téglatest adatai")
foablak.minsize(width = 300, height = 100)

# Fontosabb Def-ek

def nevjegy():
    ablak_egy = Toplevel(foablak)
    uzenet_egy = Message(ablak_egy, text = "Készítette: Riazáncev Csanád \n Baja \n 2022.04.20", width = 300)
    gomb_egy = Button(ablak_egy, text = "Kilépés", command = ablak_egy.destroy)

    uzenet_egy.pack()
    gomb_egy.pack()

    ablak_egy.mainloop()


# Def

def felszin():
    def szamit():
        a = eval(mezo_egy.get())
        b = eval(mezo_ketto.get())
        c = eval(mezo_harom.get())

        felszin = 2 * (a * b + a * c + b * c)

        if felszin < 0 and type(felszin) == str:
            mezo_negy.delete(0, END)
            mezo_negy.insert(0, str("A szám kisebb mint 0, vagy egy betű került bele!"))
        else:
            mezo_negy.delete(0, END)
            mezo_negy.insert(0, str(felszin))


def terfogat():
    def szamit():
        a = eval(mezo_egy.get())
        b = eval(mezo_ketto.get())
        c = eval(mezo_harom.get())

        terfogat = a * b * c

        if terfogat < 0 and type(felszin) == str:
            mezo_negy.delete(0, END)
            mezo_negy.insert(0, str("A szám kisebb mint 0, vagy egy betű került bele!"))
        else:
            mezo_negy.delete(0, END)
            mezo_negy.insert(0, str(terfogat))

# Menu

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)

menu_egy = Menubutton(menusor, text = "Fájl", underline = 0)
menu_egy.pack(side = LEFT)

file = Menu(menu_egy)
file.add_command(label = "Névjegy", command = nevjegy, underline = 0)
file.add_command(label = "Kilépés", command = foablak.destroy, underline = 0)
menu_egy.config(menu = file)

menu_ketto = Menubutton(menusor, text = "Téglatest", underline = 0)
menu_ketto.pack(side = LEFT)

teglatest = Menu(menu_ketto)
teglatest.add_command(label = "Felszín", command = felszin, underline = 0)
teglatest.add_command(label = "Térfogat", command = terfogat, underline = 0)
menu_ketto.config(menu = teglatest)

# Mellékablakok

ablak_ketto = Toplevel(foablak)
ablak_ketto.title("A téglatest felszíne")
ablak_ketto.minsize(width = 300, height = 300)

ablak_ketto = Toplevel(foablak)
ablak_ketto.title("A téglatest térfogata")
ablak_ketto.minsize(width = 300, height = 300)

# Widgetek

    # Felszín
    
szoveg_egy = Label(ablak_ketto, text = "a")
szoveg_ketto = Label(ablak_ketto, text = "b")
szoveg_harom = Label(ablak_ketto, text = "c")
szoveg_negy = Label(ablak_ketto, text = "Eredmény: ")

gomb_egy = Button(ablak_ketto, text = "Kiszámítás", command = felszin)

mezo_egy = Entry(ablak_ketto)
mezo_ketto = Entry(ablak_ketto)
mezo_harom = Entry(ablak_ketto)
mezo_negy = Entry(ablak_ketto)


    # Térfogat

szoveg_egy = Label(ablak_ketto, text = "a")
szoveg_ketto = Label(ablak_ketto, text = "b")
szoveg_harom = Label(ablak_ketto, text = "c")
szoveg_negy = Label(ablak_ketto, text = "Eredmény: ")

gomb_egy = Button(ablak_ketto, text = "Kiszámítás", command = terfogat)

mezo_egy = Entry(ablak_ketto)
mezo_ketto = Entry(ablak_ketto)
mezo_harom = Entry(ablak_ketto)
mezo_negy = Entry(ablak_ketto)

# Poziciónálás

    #Felszín

szoveg_egy.grid(row = 1)
szoveg_ketto.grid(row = 2)
szoveg_harom.grid(row = 3)
szoveg_negy.grid(row = 4)

gomb_egy.grid(row = 4, column = 2, sticky = W)

mezo_egy.grid(row = 1, column = 2, sticky = W)
mezo_ketto.grid(row = 2, column = 2, sticky = W)
mezo_harom.grid(row = 3, column = 2, sticky = W)
mezo_negy.grid(row = 5, column = 2, sticky = W)

ablak_ketto.mainloop()

    #Térfogat

szoveg_egy.grid(row = 1)
szoveg_ketto.grid(row = 2)
szoveg_harom.grid(row = 3)
szoveg_negy.grid(row = 4)

gomb_egy.grid(row = 4, column = 2, sticky = W)

mezo_egy.grid(row = 1, column = 2, sticky = W)
mezo_ketto.grid(row = 2, column = 2, sticky = W)
mezo_harom.grid(row = 3, column = 2, sticky = W)
mezo_negy.grid(row = 5, column = 2, sticky = W)

ablak_ketto.mainloop()

# Mainloop

foablak.mainloop()