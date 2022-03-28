from tkinter import *

def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a + b
    mezo3.delete(0, END)
    mezo3.insert(0, "Összeg: " +str(c))

def kivonas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a - b 
    mezo3.delete(0, END)
    mezo3.insert(0, "Összeg: " +str(c))

def szorzas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a * b 
    mezo3.delete(0, END)
    mezo3.insert(0, "Összeg: " +str(c))

def osztas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a / b 
    mezo3.delete(0, END)
    mezo3.insert(0, "Összeg: " +str(c))

def gyok():
    import math
    a = int(mezo1.get())
    c = math.sqrt(a)
    mezo3.delete(0, END)
    mezo3.insert(0, "Összeg: " +str(c))


foablak = Tk()

can1 = Canvas(foablak, width = 460, height = 460, bg = "white")
photo = PhotoImage(file = "H:\programózás\IKT python xddd\Flowing_Flag_of_the_People's_Republic_of_China_2.gif")
item = can1.create_image(80, 80, image = photo)
can1.pack(side = "top")

cimke = Label(foablak, text = "Üdvözlöm!", fg = "Blue")
cimke.pack()
gomb1 = Button(foablak, text = "OK")
gomb1.pack(side = "top")
gomb2 = Button(foablak, text = "Mégse")
gomb2.pack(side = "top")
gomb3 = Button(foablak, text = "Kilépés", command=foablak.destroy)
gomb3.pack(side = "top")
cimke3 = Label(foablak, text = " ")
cimke3.pack(side = "top")

gomb4 = Button(foablak, text = "Összeadás", command = osszeg)
gomb4.pack(side = "left")

gomb5 = Button(foablak, text = "Kivonás", command = kivonas)
gomb5.pack(side = "right")

gomb6 = Button(foablak, text = "Szorzás", command = szorzas)
gomb6.pack(side = "left")

gomb7 = Button(foablak, text = "Osztás", command = osztas)
gomb7.pack(side = "right")

gomb8 = Button(foablak, text = "Gyökvonás", command = gyok)
gomb8.pack(side = "left")

mezo1 = Entry(foablak)
mezo1.pack(side = "left")

cimke2 = Label(foablak, text = " ")
cimke2.pack(side = "left")

mezo2 = Entry(foablak)
mezo2.pack(side = "left")

gomb9 = Button(foablak, text = "=")
gomb9.pack(side = "left")

mezo3 = Entry(foablak)
mezo3.pack(side = "left")

foablak.mainloop()