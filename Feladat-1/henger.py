from tkinter import * 
import math

ablak = Tk()
ablak.title("Henger")
ablak.geometry("300x300")

vas = 7.384
fa = 0.43

def szamitas():
    R = int(mezo1.get()) #sugár
    M = int(mezo2.get()) #magasság
    V = math.pi * R**2 * M #Térfogat
    H =  vas * V
    S = fa * V
    mezo3.delete(0, END)
    mezo3.insert(0, "cm3 " + str(V))
    mezo4.delete(0, END)
    mezo4.insert(0, "g " + str(H))
    mezo5.delete(0, END)
    mezo5.insert(0, "g " + str(S))


cimke1 = Label(ablak, text = "Sugár (cm):")
cimke1.grid(row = 1, column = 1)
mezo1 = Entry(ablak)
mezo1.grid(row = 1, column = 2) 

cimke2 = Label(ablak, text = "Magasság (cm):")
cimke2.grid(row = 2, column = 1)
mezo2 = Entry(ablak)
mezo2.grid(row = 2, column = 2) 

gomb1 = Button(ablak, text = "Kiszámít", command = szamitas)
gomb1.grid(row = 3, column = 2)

cimke3 = Label(ablak, text = "Térfogat:")
cimke3.grid(row = 4, column = 1)
mezo3 = Entry(ablak)
mezo3.grid(row = 4, column = 2) 

cimke4 = Label(ablak, text = "Vashenger:")
cimke4.grid(row = 5, column = 1)
mezo4 = Entry(ablak)
mezo4.grid(row = 5, column = 2) 


cimke5 = Label(ablak, text = "Fahenger:")
cimke5.grid(row = 6, column = 1)
mezo5 = Entry(ablak)
mezo5.grid(row = 6, column = 2) 

ablak.mainloop()