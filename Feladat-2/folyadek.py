from tkinter import * 
foablak = Tk()

def liter():
    szam = int(mezo1.get())
    print(szam)
Button1 = foablak.Button(text = 'enter', command = liter).pack()

kertszamok = int(input("Hany liter borunk van?"))

hordo = 100

cimke = Label(foablak, text = "Hány liter borunk van?")
cimke.pack(anchor = "center")

mezo1 = Entry(foablak)
mezo1.pack(anchor = "center")

cimke1 = Label(foablak, text = ("A hordóba", hordo, " liter folyadék fér"))
cimke1.pack(anchor = "center")


cimke2 = Label(foablak, text = " ")
cimke2.pack(anchor = "center")

if hordo > cimke: 
    cimke3 = Label(foablak, text = "Belefér a bor!")
    cimke3.pack(anchor = "center")
else:
    cimke4 = Label(foablak, text = "Nem fér bele a bor!")
    cimke4.pack(anchor = "center")

foablak.mainloop()