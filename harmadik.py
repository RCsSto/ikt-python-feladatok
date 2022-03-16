from tkinter import * 
foablak = Tk()
can1 = Canvas(foablak, width = 460, height = 460, bg = "white")
foablak.title("Harom cella")
cimke1 = Label(foablak, text = "Első mező")
cimke1.pack(side = "left")
mezo1 = Entry(foablak)
mezo1.pack(side = "left") 

cimke2 = Label(foablak, text = " ")
cimke2.pack(side = "left")

cimke3 = Label(foablak, text = "Második mező")
mezo2 = Entry(foablak)
mezo2.pack(side = "left") 

cimke4 = Label(foablak, text = " ")
cimke2.pack(side = "left")

cimke5 = Label(foablak, text = "Harmadik mező")
mezo3 = Entry(foablak)
mezo3.pack(side = "left") 

foablak.mainloop()