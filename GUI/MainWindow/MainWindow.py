from tkinter import *
from GUI.XinguWindow import XinguWindow
from DB.DataManagement import *
from GUI.MainWindow.DataFrame import DataFrame
from GUI.MainWindow.MonthPlotFrame import MonthPlotFrame
from GUI.MainWindow.CheesePlotFrame import CheesePlotFrame
from GUI.MainWindow.DebtsFrame import DebtsFrame
from GUI.MainWindow.OptionsFrame import OptionsFrame

#import tkinter.ttk as ttk


class MainWindow(XinguWindow):

    def __init__(self, DB_Name):
        super().__init__()

        self.DB_Name = DB_Name
        
        # Window configuration
        self.title("Xingú")

        # Setting fullscreen
        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))

        # Building options frame
        self.OptFrame = OptionsFrame(self)

        # Updating window, so all the elements have their actual size
        # and PlotFrame and DataFrame can be con figured accordingly
        self.update()

        # Building window-size-demependent frames
        self.DatFrame = DataFrame(self)
        self.MonthPlFrame = MonthPlotFrame(self) # As a default, the plots for the current month are displayed
        self.CheesePlFrame = CheesePlotFrame(self)
        self.DebFrame = DebtsFrame(self)

        # Menu
        self.editdb = Menu(self.menubar, tearoff=0)
        self.editdb.add_command(label="Edit", command=self.donothing)
        self.menubar.add_cascade(label="Data Base", menu=self.editdb)