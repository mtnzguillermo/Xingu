from tkinter import *
from GUI.XinguWindow import XinguWindow
from datetime import datetime

class IncomeWindow(XinguWindow):

    def __init__(self, root_window):
        super().__init__()

        self.root_window = root_window
        
        self.title("Nuevo Ingreso")
        self.resizable(False, False)
        self.IncomeFrame=Frame(self,bg="Purple",width=450,height=450)
        self.IncomeFrame.pack() #fill="both",expand="True")

        #Date
        self.DateLabel = Label(self.IncomeFrame, text="Fecha:", bg="Purple", fg="White", font=("Calibri", 14))
        self.DateLabel.place(x=50, y=50)
        
        self.DateEntry = Entry(self.IncomeFrame, font=("Calibri", 14))
        self.DateEntry.place(x=200, y=50)

        #Field
        self.FieldLabel = Label(self.IncomeFrame, text="Tipo:", bg="Purple", fg="White", font=("Calibri", 14))
        self.FieldLabel.place(x=50, y=100)

        self.mode_field_list = ["Puntual", "Mensual"]
        self.mode_field = StringVar(self)
        self.mode_field.set(self.mode_field_list[0])
        self.ModeField = OptionMenu(self.IncomeFrame, self.mode_field, *self.mode_field_list)
        self.ModeField.config(width=18, font=('Calibri', 14))
        self.ModeField.place(x=200,y=100)

        #Value
        self.ValueLabel = Label(self.IncomeFrame, text="Valor:", bg="Purple", fg="White", font=("Calibri", 14))
        self.ValueLabel.place(x=50, y=150)
        
        self.ValueEntry = Entry(self.IncomeFrame, font=("Calibri", 14))
        self.ValueEntry.place(x=200, y=150)

        #Concept
        self.ConceptLabel = Label(self.IncomeFrame, text="Concepto:", bg="Purple", fg="White", font=("Calibri", 14))
        self.ConceptLabel.place(x=50, y=200)
        
        self.ConceptEntry = Entry(self.IncomeFrame, font=("Calibri", 14))
        self.ConceptEntry.place(x=200, y=200)

        #Observations
        self.ObservationsLabel = Label(self.IncomeFrame, text="Observaciones:", bg="Purple", fg="White", font=("Calibri", 14))
        self.ObservationsLabel.place(x=50, y=250)
        
        self.ObservationsText = Text(self.IncomeFrame, font=("Calibri", 14), height=3, width=20, xscrollcommand=TRUE)
        self.ObservationsText.place(x=200, y=250)

        #Button
        self.OKButton = Button(self.IncomeFrame, text="Introducir Ingreso", font=("Calibri", 14), height=2, width=20)
        self.OKButton.bind("<Button-1>",self.Send)
        self.OKButton.place(x=225, y=360, anchor=N)

        #Error 
        self.ErrorLabel = Label(self.IncomeFrame, text="Parámetros Incorrectos", bg="Purple", fg="Purple", font=("Calibri", 14))
        self.ErrorLabel.place(x=225, y=410, anchor=N)

    #Action of the button
    def Send(self, event):
        #imports
        from DB.DataManagement import InsertExpense
        
        self.date = self.DateEntry.get()
        self.field = self.mode_field.get()
        self.value = self.ValueEntry.get()
        self.concept = self.ConceptEntry.get()
        self.observations = self.ObservationsText.get("1.0",'end-1c')

        if self.CheckParameters() == TRUE:
            self.ErrorLabel.config(fg="Purple")
            self.datetime = datetime.strptime(self.date, '%d/%m/%Y')
            self.value = float(self.ValueEntry.get())

            InsertExpense(self.root_window.DB_Name, self.datetime, self.field, self.value, self.concept, self.observations)
        
        else:
            self.ErrorLabel.config(fg="White")
        #self.destroy()

    def CheckParameters(self):      
        
        try:
            datetime.strptime(self.date, '%d/%m/%Y')
            float(self.ValueEntry.get())

            if not self.field: raise Exception
            if not self.concept: raise Exception

            return(TRUE)

        except:
            return(FALSE)