
from tkinter import *
import tkinter.ttk as ttk
from DB.DataManagement import *

class MonthPlotFrame(Frame):
    
    def __init__(self, root_window):

        # Saving root window as a class variable
        self.root_window = root_window

        # Setting frame dimensions
        self.frame_width = root_window.winfo_width() - root_window.OptFrame.winfo_width()
        self.frame_height = root_window.winfo_height()

        # Calling parent constructor, with the corresponding dimensions
        super().__init__(root_window, bg = "Green", width = self.frame_width, height = self.frame_height)

        # Introduction of the frame in MainWindow
        self.place(x = root_window.OptFrame.winfo_width(), y=0)