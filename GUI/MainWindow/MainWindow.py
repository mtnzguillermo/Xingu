from tkinter import *
from GUI.XinguWindow import XinguWindow
from GUI.ExpenseWindow import *
from GUI.IncomeWindow import IncomeWindow
from GUI.LoanWindow import LoanWindow
from DB.DataManagement import *

import tkinter.ttk as ttk

class MainWindow(XinguWindow):

    def __init__(self, DB_Name):
        super().__init__()

        self.DB_Name = DB_Name
        
        # Window configurationm
        self.title("Xingú")

        # Setting fullscreen
        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))

        # Building frames
        self.DatFrame = DataFrame(self)
        self.OptFrame = OptionsFrame(self)
        
                

class OptionsFrame(Frame):

    def __init__(self, root_window):
        super().__init__(root_window, bg="Grey", width=725, height=75)

        self.root_window = root_window

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
        self.YearOM.config(width=7, font=('Calibri', 14))
        self.YearOM.place(x=370,y=10)

        # Visualization button

        self.ViewButton = Button(self, text="Visualizar", font=('Calibri', 14), width=50)
        print(root_window)
        self.ViewButton.bind("<Button-1>",self.Visualize)
        self.ViewButton.place(x=10, y=40)

        # Expense button

        self.ExpenseButton = Button(self, text="Nuevo\ngasto", font=('Calibri', 14), width=8, height=3)
        self.ExpenseButton.bind("<Button-1>",self.NewExpenseWindow)
        self.ExpenseButton.place(x=480, y=10) # anchor=N)

        # Income button

        self.IncomeButton = Button(self, text="Nuevo\ningreso", font=('Calibri', 14), width=8, height=3)
        self.IncomeButton.bind("<Button-1>",self.NewIncomeWindow)
        self.IncomeButton.place(x=560, y=10) # anchor=N)

        # Loan button

        self.LoanButton = Button(self, text="Nuevo\npréstamo", font=('Calibri', 14), width=8, height=3)
        self.LoanButton.bind("<Button-1>",self.NewLoanWindow)
        self.LoanButton.place(x=640, y=10) # anchor=N)

        # Introduction of the frame in MainWindow

        self.place(x=0, y=0)

    def Visualize(self,event):

        self.mode = self.mode_option.get()
        self.year = int(self.year_option.get())

        if self.mode == "Mes":
            self.month_string = self.month_option.get()
            self.month_integer = self.month_option_list.index(self.month_option.get()) + 1
            self.root_window.DatFrame.VisualizeMonthMode(self.year, self.month_string, self.month_integer)
        else:
            self.root_window.DatFrame.VisualizeYearMode(self.year)
     

    #def Visualization(self, event):

        #self.root_window.DatFrame.Visualize()

        #import sqlite3

        #self.connection = sqlite3.connect("DataBases/Prueba")
        #self.cursor = self.connection.cursor()
        #self.cursor.execute("SELECT * FROM EXPENSES;")
        #self.results = self.cursor.fetchall()

        #for row in self.results:
        #    print(row)

        #self.visualization_month = 1
        #self.visualization_year = 2020
        #self.visualization_codes = GetCodes(self.visualization_month, self.visualization_year)
        #self.visualization_expenses = GetExpenses(self.visualization_codes)

        #for expense in self.visualization_expenses:
        #    print(expense)

    def NewExpenseWindow(self, event):
        self.expense_window = ExpenseWindow(self.root_window)

    def NewIncomeWindow(self, event):
        self.income_window = IncomeWindow(self.root_window)

    def NewLoanWindow(self, event):
        self.loan_window = LoanWindow(self.root_window)

class DataFrame(Frame):

    def __init__(self, root_window):
        super().__init__(root_window, bg="Yellow", width=725, height=700)

        # Introduction of the frame in MainWindow
        self.place(x=0, y=75)

        self.root_window = root_window

        #root_window.OptFrame.Visualize()

        self.title = Label(self, text= "Mes y Año", fg="White", background="Purple", font=("Calibri", 16))

        self.headers = ["Fecha", "Campo", "Valor", "Concepto", "Total", "Indicador", "Ahorro"]

        self._tree = ttk.Treeview(self, height=25, columns=self.headers, show="headings")

        self.title.pack(side=TOP, fill="x")

        # Scrollbars 
        vsb = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)
        vsb.pack(side='right', fill='y')
        #hsb = ttk.Scrollbar(self, orient="horizontal", command=self._tree.xview)
        #hsb.pack(side='bottom', fill='x')
        #Not sure if hsb is necessary 

        #self._tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        self._tree.configure(yscrollcommand=vsb.set)
        self._tree.pack(side="left")

        for header in self.headers:
            self._tree.heading(header, text=header.title())
            self._tree.column(header, stretch=False, width=101)
        
        self._tree.bind("<Double-1>", self.DataDoubleClick)
        
    def VisualizeMonthMode(self, year, month_string, month_integer):

        # Table (Monthly)

        self.title.config(text = month_string + " " + str(year))

        #for header in self.headers:
        #    self._tree.heading(header, text=header.title())
        #    self._tree.column(header, stretch=False, width=101)

        for i in self._tree.get_children():
            self._tree.delete(i)

        #TO DO: Get parameters from DB
        self.visualization_data = GetMonthExpenses(self.root_window.DB_Name, year, month_integer)

        #cursor = [(str(self.contador), "Celda2"), ("Celda3", "Celda4")]
        
        for row in self.visualization_data:
            self.add_row(row[1:])
    
    def VisualizeYearMode(self):
        pass

    def add_row(self, row):

        self.item = 4
        self._tree.insert('', 'end', values=row)
        for i, self.item in enumerate(row):
            col_width = 101
            if self._tree.column(self.headers[i], width=None) < col_width:
                    self._tree.column(self.headers[i], width=col_width)

    def DataDoubleClick(self, event):
        self.item = self._tree.selection()[0] # now you got the item on that tree
        #self.expense_window = ExpenseWindow(self.root_window)
        #print ("you clicked on " + self.item)

        self.item_int = int(self.item[1:]) - 1 
        self.clicked_code = self.visualization_data[self.item_int][0]

        self.EditExpenseWindow = EditExpenseWindow(self.root_window, self.clicked_code)

        #print ("Data " + str(self.visualization_data[self.item_int]))
        #print ("Code " + str(self.visualization_data[self.item_int][0]))
