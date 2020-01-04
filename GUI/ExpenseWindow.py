from tkinter import *
from GUI.XinguWindow import XinguWindow

class ExpenseWindow(XinguWindow):
        
    def __init__(self):
        super().__init__()
        
        self.title("Nuevo Gasto")
        self.ExpenseFrame=Frame(self,bg="Purple",width=450,height=450)
        self.ExpenseFrame.pack() #fill="both",expand="True")

        #Date
        self.DateLabel = Label(self.ExpenseFrame, text="Fecha:", bg="Purple", fg="White", font=("Calibri", 14))
        self.DateLabel.place(x=50, y=50)
        
        self.DateEntry = Entry(self.ExpenseFrame, font=("Calibri", 14))
        self.DateEntry.place(x=200, y=50)

        #Field
        self.FieldLabel = Label(self.ExpenseFrame, text="Tipo:", bg="Purple", fg="White", font=("Calibri", 14))
        self.FieldLabel.place(x=50, y=100)

        self.mode_field_list = ["Comida", "Hogar", "Transporte", "Ocio", "Ropa", "Viajes", "Caprichos", "Regalos", "Gasto mensual", "Otros"]
        self.mode_field = StringVar(self)
        self.mode_field.set(self.mode_field_list[0])
        self.ModeField = OptionMenu(self.ExpenseFrame, self.mode_field, *self.mode_field_list)
        self.ModeField.config(width=18, font=('Calibri', 14))
        self.ModeField.place(x=200,y=100)

        #Value
        self.ValueLabel = Label(self.ExpenseFrame, text="Valor:", bg="Purple", fg="White", font=("Calibri", 14))
        self.ValueLabel.place(x=50, y=150)
        
        self.ValueEntry = Entry(self.ExpenseFrame, font=("Calibri", 14))
        self.ValueEntry.place(x=200, y=150)

        #Concept
        self.ConceptLabel = Label(self.ExpenseFrame, text="Concepto:", bg="Purple", fg="White", font=("Calibri", 14))
        self.ConceptLabel.place(x=50, y=200)
        
        self.ConceptEntry = Entry(self.ExpenseFrame, font=("Calibri", 14))
        self.ConceptEntry.place(x=200, y=200)

        #Observations
        self.ObservationsLabel = Label(self.ExpenseFrame, text="Observaciones:", bg="Purple", fg="White", font=("Calibri", 14))
        self.ObservationsLabel.place(x=50, y=250)
        
        self.ObservationsText = Text(self.ExpenseFrame, font=("Calibri", 14), height=3, width=20, xscrollcommand=TRUE)
        self.ObservationsText.place(x=200, y=250)

        #Button
        self.OKButton = Button(self.ExpenseFrame, text="Introducir Gasto", font=("Calibri", 14), height=2, width=20)
        self.OKButton.bind("<Button-1>",self.Send)
        self.OKButton.place(x=225, y=360, anchor=N)

    #Action of the button
    def Send(self, event):
        #pass
        #imports
        from DB.DataManagement import InsertExpense
        from datetime import datetime

        self.date = self.DateEntry.get()
        self.datetime = datetime.strptime(self.date, '%d/%m/%Y')

        self.field = self.mode_field.get()
        self.value = - float(self.ValueEntry.get())
        self.concept = self.ConceptEntry.get()
        self.observations = self.ObservationsText.get("1.0",'end-1c')

        InsertExpense("Prueba", self.datetime, self.field, self.value, self.concept, self.observations)

        #self.destroy()
