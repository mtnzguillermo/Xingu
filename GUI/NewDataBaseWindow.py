from tkinter import *
from GUI.XinguWindow import XinguWindow

class NewDataBaseWindow(XinguWindow):

    def __init__(self, root_window):
        super().__init__()

        self.root_window = root_window
        
        self.title("Nueva Base de Datos")
        self.resizable(False, False)
        self.DBFrame=Frame(self,bg="Purple",width=350,height=550)
        self.DBFrame.pack() #fill="both",expand="True")
        
        self.NewDataBaseLabel = Label(self.DBFrame, text="Nombre:", bg="Purple", fg="White", font=("Calibri", 18))
        self.NewDataBaseLabel.place(x=50, y=50)
        
        self.NewDataBaseEntry = Entry(self.DBFrame, font=("Calibri", 18))
        self.NewDataBaseEntry.bind("<Return>", self.CreateDB) 
        self.NewDataBaseEntry.place(x=50, y=80)
        
        self.NewPasswordLabel1 = Label(self.DBFrame, text="Contraseña:", bg="Purple", fg="White", font=("Calibri", 18))
        self.NewPasswordLabel1.place(x=50, y=140)
        
        self.NewPasswordEntry1 = Entry(self.DBFrame, font=("Calibri", 18), show="·")
        self.NewPasswordEntry1.bind("<Return>", self.CreateDB) 
        self.NewPasswordEntry1.place(x=50, y=170)
        
        self.NewPasswordLabel2 = Label(self.DBFrame, text="Repetir Contraseña:", bg="Purple", fg="White", font=("Calibri", 18))
        self.NewPasswordLabel2.place(x=50, y=230)
        
        self.NewPasswordEntry2 = Entry(self.DBFrame, font=("Calibri", 18), show="·")
        self.NewPasswordEntry2.bind("<Return>", self.CreateDB) 
        self.NewPasswordEntry2.place(x=50, y=260)

        self.InitMoneyLabel = Label(self.DBFrame, text="Dinero Inicial:", bg="Purple", fg="White", font=("Calibri", 18))
        self.InitMoneyLabel.place(x=50, y=320)
        
        self.InitMoneyEntry = Entry(self.DBFrame, font=("Calibri", 18))
        self.InitMoneyEntry.bind("<Return>", self.CreateDB) 
        self.InitMoneyEntry.place(x=50, y=350)

        self.CreateButton = Button(self.DBFrame, text="Crear", font=("Calibri", 18), height=2, width=10)
        self.CreateButton.bind("<Button-1>",self.CreateDB)
        self.CreateButton.place(x=175, y=445, anchor=N)

        self.ErrorDBLabel = Label(self.DBFrame, text="Las contraseñas no coinciden", bg="Purple", fg="Purple", font=("Calibri", 12))
        self.ErrorDBLabel.place(x=175, y=500, anchor=N)

    def CreateDB(self,event):

        
        if self.NewPasswordEntry1.get() != self.NewPasswordEntry2.get():

            self.ErrorDBLabel.config(fg="White")
        
        else: 

            self.ErrorDBLabel.config(fg="Purple")

        
