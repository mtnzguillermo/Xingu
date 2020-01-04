from tkinter import *
import tkinter.ttk as ttk
from GUI.XinguWindow import XinguWindow
import DB.DataManagement as DB

class LoanWindow(XinguWindow):

    def __init__(self, root_window):
        super().__init__()

        self.root_window = root_window
        
        self.title("Nuevo Préstamo")
        self.LoanFrame=Frame(self,bg="Purple",width=450,height=500)
        self.LoanFrame.pack() #fill="both",expand="True")

        #Date
        self.DateLabel = Label(self.LoanFrame, text="Fecha:", bg="Purple", fg="White", font=("Calibri", 14))
        self.DateLabel.place(x=50, y=50)
        
        self.DateEntry = Entry(self.LoanFrame, font=("Calibri", 14))
        self.DateEntry.place(x=200, y=50)

        #Field
        self.FieldLabel = Label(self.LoanFrame, text="Tipo:", bg="Purple", fg="White", font=("Calibri", 14))
        self.FieldLabel.place(x=50, y=100)

        self.mode_field_list = ["Entrante", "Saliente"]
        self.mode_field = StringVar(self)
        self.mode_field.set("")
        self.ModeField = OptionMenu(self.LoanFrame, self.mode_field, *self.mode_field_list)
        self.ModeField.config(width=18, font=('Calibri', 14))
        self.ModeField.place(x=200,y=100)

        #Person
        self.PersonLabel = Label(self.LoanFrame, text="Persona:", bg="Purple", fg="White", font=("Calibri", 14))
        self.PersonLabel.place(x=50, y=150)

        self.PersonCombo = ttk.Combobox(self.LoanFrame)

        #PROVISIONAL    
        DB_Name = "Prueba"

        #self.PersonCombo["values"] = self.GetDebtPeople(DB_Name)
        self.PersonCombo["values"] = DB.GetDebtPeople(DB_Name)
        self.PersonCombo.config(width=18, font=('Calibri', 14))
        self.PersonCombo.place(x=200, y=150)

        #Value
        self.ValueLabel = Label(self.LoanFrame, text="Valor:", bg="Purple", fg="White", font=("Calibri", 14))
        self.ValueLabel.place(x=50, y=200)
        
        self.ValueEntry = Entry(self.LoanFrame, font=("Calibri", 14))
        self.ValueEntry.place(x=200, y=200)

        #Concept
        self.ConceptLabel = Label(self.LoanFrame, text="Concepto:", bg="Purple", fg="White", font=("Calibri", 14))
        self.ConceptLabel.place(x=50, y=250)
        
        self.ConceptEntry = Entry(self.LoanFrame, font=("Calibri", 14))
        self.ConceptEntry.place(x=200, y=250)

        #Observations
        self.ObservationsLabel = Label(self.LoanFrame, text="Observaciones:", bg="Purple", fg="White", font=("Calibri", 14))
        self.ObservationsLabel.place(x=50, y=300)
        
        self.ObservationsText = Text(self.LoanFrame, font=("Calibri", 14), height=3, width=20, xscrollcommand=TRUE)
        self.ObservationsText.place(x=200, y=300)

        #Button
        self.OKButton = Button(self.LoanFrame, text="Introducir Préstamo", font=("Calibri", 14), height=2, width=20)
        self.OKButton.bind("<Button-1>",self.Send)
        self.OKButton.place(x=225, y=410, anchor=N)

    #Action of the button
    def Send(self, event):
        #pass
        #imports
        from datetime import datetime

        self.date = self.DateEntry.get()
        self.datetime = datetime.strptime(self.date, '%d/%m/%Y')

        self.person = self.PersonCombo.get()

        if self.mode_field.get() == "Entrante":
            self.value = float(self.ValueEntry.get())
        elif self.mode_field.get() == "Saliente":
            self.value = - float(self.ValueEntry.get())

        self.concept = self.ConceptEntry.get()
        self.observations = self.ObservationsText.get("1.0",'end-1c')

        DB.InsertLoan(self.root_window.DB_Name, self.datetime, self.person, self.value, self.concept, self.observations)

        #self.destroy()
    
    