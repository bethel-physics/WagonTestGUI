import tkinter as tk
from tkinter import ttk

# Creating the frame itself
class TestInProgressScene(tk.Frame):
    def __init__(self, parent, master_window):
        super().__init__(master_window, width=700, height=500, background='purple')

        # Creating grid frame to lay widgets onto
        frm_main = tk.Frame(self, width = 200, height = 200)
        frm_main.grid(column=0, row=0)

        # Creating the main title in the frame
        lbl_title = tk.Label(frm_main, text = "Test in progress. Please wait")
        lbl_title.pack(padx=200, pady=200)

        # Create a progress bar of some kind
        prgbar_progress = ttk.Progressbar(frm_main, orient = 'horizontal', mode = 'indeterminate', length = 280)
        prgbar_progress.pack()

        # A Button to start the progress bar
        btn_start = ttk.Button(frm_main, text='Start', command=prgbar_progress.start)
        btn_start.pack()

        # A Button To Stop the Progress Bar and Progress (Temporary until we link to actual progress)
        btn_stop = ttk.Button(frm_main, text='Stop', command=prgbar_progress.stop)
        btn_stop.pack()

        self.grid_propagate(0)