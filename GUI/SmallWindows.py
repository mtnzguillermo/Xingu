from tkinter import *
from GUI.XinguWindow import XinguWindow

class ConfirmWindow(XinguWindow):

    def __init__(self, caller_window, original_event):
        super().__init__()

        self.caller_window = caller_window
        self.original_event = original_event

        self.title("")
        self.resizable(False, False)
        ConfigWindowFrame=Frame(self,bg="White",width=200,height=200)
        ConfigWindowFrame.pack() #fill="both",expand="True")

        #Confirmation
        ConfirmLabel = Label(ConfigWindowFrame, text="¿Estás seguro?", bg="White", fg="Purple", font=("Calibri", 14))
        ConfirmLabel.place(x=100, y=50, anchor=N)

        #Confirm Button
        ConfirmButton = Button(ConfigWindowFrame, text="Sí", font=("Calibri", 14), height=2, width=10)
        ConfirmButton.bind("<Button-1>",self.Confirm)
        ConfirmButton.place(x=98, y=100, anchor=N)
        
        #self.destroy()

    #Action of the Confirm Button
    def Confirm(self, event):

        self.caller_window.ConfirmedAction(self.original_event)

        #self.destroy()

class PasswordWindow(XinguWindow):

    def __init__(self, caller_window, original_event):
        super().__init__()

        self.caller_window = caller_window
        self.original_event = original_event

        self.title("")
        self.resizable(False, False)
        PassWindowFrame=Frame(self,bg="White",width=300,height=200)
        PassWindowFrame.pack() #fill="both",expand="True")

        #Password Label
        PassLabel = Label(PassWindowFrame, text="Contraseña:", bg="White", fg="Purple", font=("Calibri", 14))
        PassLabel.place(x=150, y=30, anchor=N)

        #Password Entry
        self.PasswordEntry = Entry(PassWindowFrame, font=("Calibri", 18), show="·", bd=2)
        self.PasswordEntry.bind("<Return>", self.PassConfirm) 
        self.PasswordEntry.place(x=150, y=70, anchor=N)

        #Confirm Button
        ConfirmButton = Button(PassWindowFrame, text="Confirmar", font=("Calibri", 14), height=2, width=10)
        ConfirmButton.bind("<Button-1>",self.PassConfirm)
        ConfirmButton.place(x=150, y=130, anchor=N)
        
        #self.destroy()

    #Action of the Confirm Button
    def PassConfirm(self, event):

        pass