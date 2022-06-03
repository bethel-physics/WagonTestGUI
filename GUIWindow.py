# Importing all Modules
from pickle import NONE
import tkinter as tk
from turtle import bgcolor
from LoginScene import LoginScene
from ScanScene import ScanScene



# Create a class for creating the basic GUI Window
class GUIWindow():

    def __init__(self):                     
        # Create the window named "master_window"
        self.master_window = tk.Tk()
        self.master_window.title("Bethel Interns' Window")
        self.master_window.geometry("700x500")
        self.master_frame = tk.Frame(self.master_window, width=700, height= 500)
        # self.master_frame.config(background='red')
        self.master_frame.pack()
        

        self.login_frame = LoginScene(self, self.master_frame)
        self.login_frame.grid(row=0, column=0)
        # scan_frame = ScanScene(self, master_window)
        # list_of_frames = [login_frame, scan_frame]
        # self.clear_window(master_window)
        self.scan_frame = ScanScene(self, self.master_frame)
        self.scan_frame.grid(row=0, column=0)

        self.master_window.mainloop()
    

    def set_frame(self, _frame):
        _frame.tkraise()


        

        
        