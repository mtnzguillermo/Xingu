from tkinter import *
from GUI.XinguWindow import XinguWindow
from GUI.ExpenseWindow import ExpenseWindow

class MainWindow(XinguWindow):

    def __init__(self):
        super().__init__()
        
        # Window configurationm
        self.title("Xingú")

        # Main frame configuration
        #self.StartFrame=Frame(self, bg="Purple")
        #self.StartFrame.pack(fill="both", expand="True")

        # Setting fullscreen
        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))

        # Building options' frame
        self.OptFrame = OptionsFrame(self)

class OptionsFrame(Frame):

    def __init__(self, root_window):
        super().__init__(root_window, bg="Grey", width=800, height=150)

        # Introduction of the view mode

        self.ModeLabel = Label(self, text="Modo:", font=("Calibri", 14))
        self.ModeLabel.place(x=10,y=10)

        self.mode_option_list = ["Mes", "Año"]
        self.mode_option = StringVar(self)
        self.mode_option.set(self.mode_option_list[0])
        self.ModeOM = OptionMenu(self, self.mode_option, *self.mode_option_list)
        self.ModeOM.config(width=7, font=('Calibri', 14))
        self.ModeOM.place(x=60,y=10)

        # Month selection

        self.MonthLabel = Label(self, text="Mes:", font=("Calibri", 14))
        self.MonthLabel.place(x=160,y=10)

        self.month_option_list = ["Enero", "Febrero", "Marzo", "Abril",
                                "Mayo", "Junio", "Julio", "Agosto",
                                "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        self.month_option = StringVar(self)
        self.month_option.set(self.month_option_list[0])
        self.MonthOM = OptionMenu(self, self.month_option, *self.month_option_list)
        self.MonthOM.config(width=10, font=('Calibri', 14))
        self.MonthOM.place(x=200,y=10)

        # Year selection

        self.YearLabel = Label(self, text="Año:", font=("Calibri", 14))
        self.YearLabel.place(x=330,y=10)

        self.year_option_list = ["2019", "2020", "2021", "2022",
                                "2023", "2024", "2025", "2026",
                                "2027", "2028", "2029", "2030"]
        self.year_option = StringVar(self)
        self.year_option.set(self.year_option_list[0])
        self.YearOM = OptionMenu(self, self.year_option, *self.year_option_list)
        self.YearOM.config(width=10, font=('Calibri', 14))
        self.YearOM.place(x=370,y=10)

        # Expense button

        self.ExpenseButton = Button(self, text="Nuevo gasto")
        self.ExpenseButton.bind("<Button-1>",self.NewExpenseWindow)
        self.ExpenseButton.place(x=700, y=10) # anchor=N)
        self.place(x=0, y=0)

    def NewExpenseWindow(self,event):
        self.expense_window = ExpenseWindow()




