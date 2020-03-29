from tkinter import *
from GUI.XinguWindow import XinguWindow

class ConfirmWindow(XinguWindow):

    def __init__(self, caller_window, original_event):
        super().__init__()

        self.caller_window = caller_window
        self.original_event = original_event

        self.title("bla")
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
