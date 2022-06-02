# Importing all Modules
import tkinter as tk
from tk import *
from LoginScene import LoginScene
from ScanScene import ScanScene

# Create a class for creating the basic GUI Window
class GUIWindow():
    
    def __init__(self) -> None:       
               
        # Create the window named "master_window"
        master_window = tk.Tk()
        master_window.title("Bethel Interns' Window")
        master_window.geometry("700x500")

        login_frame = LoginScene(self, master_window)
        login_frame.pack()
        
        list_of_frames = [login_frame]



        master_window.mainloop()