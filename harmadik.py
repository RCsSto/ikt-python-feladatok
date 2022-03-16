from tkinter import * 
foablak = Tk()
can1 = Canvas(foablak, width = 460, height = 460, bg = "white")
foablak.title("Harom cella")
cimke1 = Label(foablak, text = "Első mező")
cimke1.pack(side = "left")
mezo1 = Entry(foablak)
mezo1.pack(side = "left") 

foablak.mainloop()