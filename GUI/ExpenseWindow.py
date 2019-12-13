from tkinter import *
from GUI.XinguWindow import XinguWindow

class ExpenseWindow(XinguWindow):
        
    def __init__(self):
        super().__init__()
        
        self.title("New expense")
        self.mainframe=Frame(self,bg="Purple",width=150,height=200)
        self.mainframe.pack(fill="both",expand="True")