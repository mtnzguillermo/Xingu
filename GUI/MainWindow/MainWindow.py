from tkinter import *
from GUI.XinguWindow import XinguWindow

class MainWindow(XinguWindow):

    def __init__(self):
        super().__init__()
        
        self.title("Xingú")
        self.resizable(False, False)
        self.StartFrame=Frame(self, bg="Purple", width=350, height=550)
        self.StartFrame.pack(fill="both", expand="True")