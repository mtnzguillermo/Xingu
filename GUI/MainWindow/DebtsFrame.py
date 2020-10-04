
from tkinter import *
import tkinter.ttk as ttk
from DB.DataManagement import *

class DebtsFrame(Frame):
    
    def __init__(self, root_window):

        # Saving root window as a class variable
        self.root_window = root_window

        # Setting frame dimensions
        self.frame_width = root_window.winfo_width() - root_window.OptFrame.winfo_width() - root_window.winfo_height()/2
        self.frame_height = root_window.winfo_height()/2

        # Calling parent constructor, with the corresponding dimensions
        super().__init__(root_window, bg = "Cyan", width = self.frame_width, height = self.frame_height)

        # Introduction of the frame in MainWindow
        self.place(x=root_window.winfo_width()-self.frame_width, y=root_window.winfo_height()/2)

        self.title = Label(self, text= "Deudas", fg="White", background="Purple", font=("Calibri", 16))

        self.headers = ["Persona", "Valor"]

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
        
        #self._tree.bind("<Double-1>", self.DataDoubleClick)

        # Default view: current debts 
        # root_window.OptFrame.VisualizeMonthMode(missing_args)







    #def VisualizeDebts(self, year, month_string, month_integer):

        for i in self._tree.get_children():
           self._tree.delete(i)

        #Get parameters from DB
        self.visualization_data = GetAllDebts(self.root_window.DB_Name)
        #self.visualization_data = GetMonthExpenses(self.root_window.DB_Name, year, month_integer)
        
        self.index_tree = -1
        for row in self.visualization_data:
            self.index_tree  = self.index_tree + 1
            self.add_row(row[0:], self.index_tree)
    
    def add_row(self, row, index_tree):

        self.item = 4
        self._tree.insert('', 'end', id=index_tree, values=row)
        for i, self.item in enumerate(row):
            col_width = 101
            if self._tree.column(self.headers[i], width=None) < col_width:
                    self._tree.column(self.headers[i], width=col_width)
