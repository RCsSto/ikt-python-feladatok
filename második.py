from tkinter import * 
ablak1 = Tk()
gyoker = "H:\\programózás\\IKT python xddd"
ablak1.geometry("450x450")
ablak1.title("IKT Tkinter")
icon = PhotoImage(file = gyoker + "H:\\programózás\\IKT python xddd\\china.png")
ablak1.iconphoto(True, icon)
ablak1.config(background = "black")
elsokep = PhotoImage(file = gyoker + "Mao_Zedong_portrait.png")
cimke = Label(ablak1,
            text = "Üdvözlöm!",
            fg = "#553388",
            bg = "#c3cee0", 
            font = ("Arial", 45, "bold"),
            bd = 10, 
            relief = RAISED,
            padx = 25, 
            pady = 30, 
            image = elsokep,
            compound = "center").pack()

ablak1.mainloop()
