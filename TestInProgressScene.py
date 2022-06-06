import tkinter as tk
from tkinter import ttk

# Creating the frame itself
class InProgressScene1(tk.Frame):
    def __init__(self, parent, master_window):
        super().__init__(master_window)

        # Creating grid frame to lay widgets onto
        frm_main = tk.Frame(self, width = 200, height = 200)
        frm_main.grid(column=0, row=0)

        # Creating the main title in the frame
        lbl_title = tk.Label(frm_main, text = "Test in progress. Please wait")
        lbl_title.pack(padx=200, pady=200)

        # Create a progress bar of some kind
        prgbar_progress = ttk.ProgressBar(frm_main)
        prgbar_progress.pack()

        self.grid_propagate(0)