# Import

from tkinter import * 

# Foablak 

foablak = Tk()
foablak.title("A téglatest adatai")
foablak.minsize(width = 300, height = 100)

# Menu

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)

menu_egy = Menubutton(menusor, text = "File", underline = 0)
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

# Def
def nevjegy():
    ablak_egy = Toplevel(foablak)




# Mainloop

foablak.mainloop