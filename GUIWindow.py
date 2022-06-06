# Importing all Modules
from pickle import NONE
import tkinter as tk
from turtle import bgcolor
from LoginScene import LoginScene
from ScanScene import ScanScene
from Test1 import Test1Scene
from Test2 import Test2Scene
from Test3 import Test3Scene
from Test4 import Test4Scene



# Create a class for creating the basic GUI Window
class GUIWindow():

    def __init__(self):                     
        # Create the window named "master_window"
        self.master_window = tk.Tk()
        self.master_window.title("Bethel Interns' Window")
        self.master_window.geometry("700x500")
        self.master_frame = tk.Frame(self.master_window, width=700, height= 500)
        self.master_frame.pack()
        

        self.login_frame = LoginScene(self, self.master_frame)
        self.login_frame.grid(row=0, column=0)
    
        self.scan_frame = ScanScene(self, self.master_frame)
        self.scan_frame.grid(row=0, column=0)

        self.test1_frame= Test1Scene(self, self.master_frame)
        self.test1_frame.grid(row=0, column=0)

        self.test2_frame= Test2Scene(self, self.master_frame)
        self.test2_frame.grid(row=0, column=0)

        self.test3_frame= Test3Scene(self, self.master_frame)
        self.test3_frame.grid(row=2, column=0)

        self.test4_frame= Test4Scene(self, self.master_frame)
        self.test4_frame.grid(row=0, column=0)

        self.in_progress_frame = TestInProgressScene(self, self.master_frame)
        self.in_progress_frame.grid(row=0, column=0)

        self.set_frame(self.login_frame)

        self.master_window.mainloop()
    

    def set_frame(self, _frame):
        _frame.tkraise()


        

        
        