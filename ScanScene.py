# importing necessary modules
import tkinter as tk

# creating the login frame
class ScanScene(tk.Frame):
    def __init__(self, parent, master_window):
        super().__init__(master_window)
    
        # Creating the title for the window
        lbl_title = tk.Label(self, text="THIS IS DIFFERENT")
        lbl_title.pack()
