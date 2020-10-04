
from tkinter import *
import tkinter.ttk as ttk
from DB.DataManagement import *
from GUI.ExpenseWindow import *

class DataFrame(Frame):

    def __init__(self, root_window):

        # Saving root window as a class variable
        self.root_window = root_window

        # Setting frame dimensions
        self.frame_width = root_window.OptFrame.winfo_width()
        self.frame_height = root_window.winfo_height() - root_window.OptFrame.winfo_height()

        # Calling parent constructor, with the corresponding dimensions
        super().__init__(root_window, bg="Yellow", width=self.frame_width, height=self.frame_height)

        # Introduction of the frame in MainWindow
        self.place(x=0, y=root_window.OptFrame.winfo_height())

        self.title = Label(self, text= "Mes y Año", fg="White", background="Purple", font=("Calibri", 16))

        self.headers = ["Fecha", "Campo", "Tipo", "Valor", "Concepto", "Total", "Indicador", "Ahorro"]

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

        # Default view: current month expenses
        # root_window.OptFrame.VisualizeMonthMode(missing_args)
        
    def VisualizeMonthMode(self, year, month_string, month_integer):

        # Table (Monthly)

        self.title.config(text = month_string + " " + str(year))

        #for header in self.headers:
        #    self._tree.heading(header, text=header.title())
        #    self._tree.column(header, stretch=False, width=101)

        for i in self._tree.get_children():
            self._tree.delete(i)

        #Get parameters from DB
        self.visualization_data = GetMonthExpenses(self.root_window.DB_Name, year, month_integer)

        #cursor = [(str(self.contador), "Celda2"), ("Celda3", "Celda4")]
        
        self.index_tree = -1
        for row in self.visualization_data:
            self.index_tree  = self.index_tree + 1
            self.add_row(row[1:], self.index_tree)
    
    def VisualizeYearMode(self):
        pass

    def add_row(self, row, index_tree):

        self.item = 4
        self._tree.insert('', 'end', id=index_tree, values=row)
        for i, self.item in enumerate(row):
            col_width = 101
            if self._tree.column(self.headers[i], width=None) < col_width:
                    self._tree.column(self.headers[i], width=col_width)

    def DataDoubleClick(self, event):
        self.item = self._tree.selection()[0] # now you got the item on that tree
        #self.expense_window = ExpenseWindow(self.root_window)
        print ("you clicked on " + self.item)

        #self.item_int= self.item[1:]
        #print("you clicked on (int) " + self.item_int)

        #self.item_dec = int(self.item_int, 16)
        #print("you clicked on (dec) " + str(self.item_dec))

        #self.item_int = int(self.item[1:]) - 1 
        #self.clicked_code = self.visualization_data[self.item_dec][0]

        self.item_int = int(self.item) 
        self.clicked_code = self.visualization_data[self.item_int][0]

        self.EditExpenseWindow = EditExpenseWindow(self.root_window, self.clicked_code)

        #print ("Data " + str(self.visualization_data[self.item_int]))
        #print ("Code " + str(self.visualization_data[self.item_int][0]))