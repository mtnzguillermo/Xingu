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

        self.mode_option_list = ["Mes", "Año"]
        self.mode_option = StringVar()
        self.mode_option.set(self.mode_option_list[0])
        self.ModeOM = OptionMenu(self, self.mode_option, *self.mode_option_list)
        #self.ModeOM.config(width=50, height=15, font=('Helvetica', 12), fg="Black")
        self.ModeOM.place(x=50,y=10)

        self.ExpenseButton = Button(self, text="Nuevo gasto")
        self.ExpenseButton.bind("<Button-1>",self.NewExpenseWindow)
        self.ExpenseButton.place(x=700, y=10) # anchor=N)

        self.place(x=0, y=0)

    def NewExpenseWindow(self,event):
        self.expense_window = ExpenseWindow()




