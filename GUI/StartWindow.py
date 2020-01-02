from tkinter import *
from GUI.XinguWindow import XinguWindow

class StartWindow(XinguWindow):

    def __init__(self):
        super().__init__()
        
        self.title("Xingú")
        self.resizable(False, False)
        self.StartFrame = Frame(self, bg="Purple", width=350, height=550)
        self.StartFrame.pack() #(fill="both",expand="True")
        
        self.DataBaseLabel=Label(self.StartFrame, text="Base de datos:", bg="Purple", fg="White", font=("Calibri", 18))
        self.DataBaseLabel.place(x=50, y=250)
        
        self.DataBaseEntry=Entry(self.StartFrame, font=("Calibri", 18))
        self.DataBaseEntry.place(x=50, y=280)
        
        self.PasswordLabel = Label(self.StartFrame, text="Contraseña:", bg="Purple", fg="White", font=("Calibri", 18))
        self.PasswordLabel.place(x=50, y=340)
        
        self.PasswordEntry = Entry(self.StartFrame, font=("Calibri", 18, "bold"), show="·")
        self.PasswordEntry.place(x=50, y=370)
        
        self.LoginButton = Button(self.StartFrame, text="Entrar", font=("Calibri", 18), height=2, width=10)
        self.LoginButton.bind("<Button-1>",self.Login)
        self.LoginButton.place(x=175, y=445, anchor=N)

    def Login(self,event):
        from GUI.MainWindow.MainWindow import MainWindow

        if self.DataBaseEntry.get() == "Prueba":
            if self.PasswordEntry.get() == "Password":
                print("Correcto")
                self.main_window = MainWindow()
                self.withdraw()
                #main_window.mainloop()
            else:
                print("La contraseña no es correcta")
        else:
            print("El usuario no es correcto")