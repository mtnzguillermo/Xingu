from tkinter import *

class XinguWindow(Tk):
    
    def __init__(self):
        super().__init__()

        # Menu
        self.menubar = Menu(self)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.newmenu = Menu(self.menubar, tearoff=0)
        self.newmenu.add_command(label="Data Base", command=self.NewDataBase)
        self.filemenu.add_cascade(label="New", menu=self.newmenu)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.config(menu=self.menubar)

    def donothing(self):
        pass

    def NewDataBase(self):   

        from GUI.NewDataBaseWindow import NewDataBaseWindow
        self.NewDataBaseW = NewDataBaseWindow(self)


    