from tkinter import *
from GUI.XinguWindow import XinguWindow

class StartWindow(XinguWindow):

    def __init__(self):
        super().__init__()
        
        self.title("Xingú")
        self.resizable(False, False)
        self.StartFrame = Frame(self, bg="Purple", width=350, height=550)
        self.StartFrame.pack() #(fill="both",expand="True")
        
        self.DataBaseLabel = Label(self.StartFrame, text="Base de datos:", bg="Purple", fg="White", font=("Calibri", 18))
        self.DataBaseLabel.place(x=50, y=250)
        
        self.DataBaseEntry = Entry(self.StartFrame, font=("Calibri", 18))
        self.DataBaseEntry.place(x=50, y=280)
        
        self.PasswordLabel = Label(self.StartFrame, text="Contraseña:", bg="Purple", fg="White", font=("Calibri", 18))
        self.PasswordLabel.place(x=50, y=340)
        
        self.PasswordEntry = Entry(self.StartFrame, font=("Calibri", 18), show="·")
        self.PasswordEntry.place(x=50, y=370)
        
        self.LoginButton = Button(self.StartFrame, text="Entrar", font=("Calibri", 18), height=2, width=10)
        self.LoginButton.bind("<Button-1>",self.Login)
        self.LoginButton.place(x=175, y=445, anchor=N)

        self.ErrorDBLabel = Label(self.StartFrame, text="DB no encontrada", bg="Purple", fg="Purple", font=("Calibri", 12))
        self.ErrorDBLabel.place(x=192, y=315)

        self.ErrorPassLabel = Label(self.StartFrame, text="Contraseña Incorrecta", bg="Purple", fg="Purple", font=("Calibri", 12))
        self.ErrorPassLabel.place(x=169, y=405)

    def Login(self,event):
        from GUI.MainWindow.MainWindow import MainWindow

        if self.DataBaseEntry.get() == "Prueba":

            self.ErrorDBLabel.config(fg="Purple")

            if self.PasswordEntry.get() == "Password":
                print("Correcto")
                self.ErrorPassLabel.config(fg="Purple")
                self.main_window = MainWindow("DataBases/Prueba")
                #self.withdraw()
                self.destroy()
                self.main_window.mainloop()
            else:
                print("La contraseña no es correcta")
                self.ErrorPassLabel.config(fg="White")
        else:
            print("El usuario no es correcto")
            self.ErrorDBLabel.config(fg="White")
            self.ErrorPassLabel.config(fg="Purple")