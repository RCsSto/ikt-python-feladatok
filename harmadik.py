from tkinter import * 
foablak = Tk()
can1 = Canvas(foablak, width = 460, height = 460, bg = "white")
foablak.title("Harom cella")


cimke1 = Label(foablak, text = "Első mező")
cimke1.pack(anchor = "w")
mezo1 = Entry(foablak)
mezo1.pack(anchor = "sw") 

cimke5 = Label(foablak, text = " ")
cimke5.pack(anchor = "w")

cimke2 = Label(foablak, text = "Második mező")
cimke2.pack(anchor = "w")
mezo2 = Entry(foablak)
mezo2.pack(anchor = "sw") 

cimke4 = Label(foablak, text = " ")
cimke4.pack(anchor = "w")

cimke3 = Label(foablak, text = "Harmadik mező")
cimke3.pack(anchor = "w") 
mezo3 = Entry(foablak)
mezo3.pack(anchor = "sw") 

foablak.mainloop()