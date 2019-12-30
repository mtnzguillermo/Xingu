from tkinter import *
from GUI.XinguWindow import XinguWindow

class MainWindow(XinguWindow):

    def __init__(self):
        super().__init__()
        
        # Window configurationm
        self.title("Xingú")

        # Main frame configuration
        self.StartFrame=Frame(self, bg="Purple")
        self.StartFrame.pack(fill="both", expand="True")

        # Setting fullscreen
        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))