import tkinter as tk
from tkinter import ttk
from PythonFiles.GUIWindow import *
from xml.dom.expatbuilder import parseFragmentString

# Creating the frame itself
class TestInProgressScene(tk.Frame):

    def __init__(self, parent, master_window, next_frame):
        self.next_frame = next_frame
        super().__init__(master_window, width = 850, height = 500)

        # Creating grid frame to lay widgets onto
        frm_main = tk.Frame(self, width = 425, height = 500)
        frm_main.grid(column=0, row=0, sticky = 'nsew')
        frm_main.grid_propagate(0)

        # Creating the main title in the frame
        lbl_title = tk.Label(frm_main, text = "Test in progress. Please wait.", font = ('Arial', 20))
        lbl_title.pack(padx = 0, pady = 100)

        # Create a progress bar of some kind
        prgbar_progress = ttk.Progressbar(
            frm_main, 
            orient = 'horizontal', 
            mode = 'indeterminate', length = 350)
        prgbar_progress.pack(padx = 50)
        prgbar_progress.start()

        # A Button To Stop the Progress Bar and Progress Forward (Temporary until we link to actual progress)
        btn_stop = ttk.Button(frm_main, text='Stop', command= lambda: self.stop_button_action(parent, self.next_frame))
        btn_stop.pack(padx = 0, pady = 125)

        # Creating a Frame For Console Output
        frm_console = tk.Frame(self, width = 425, height = 500, bg = 'black')
        frm_console.grid_propagate(0)
        frm_console.grid(column = 1, row = 0, sticky = 'nsew')

        # Labeling frm_console
        lbl_console = tk.Label(frm_console, text = 'Console Output', bg = 'black', fg = 'white', font = ('Arial', 30))
        lbl_console.pack(anchor = 'center', padx = 50)

        self.grid_propagate(0)

    def stop_button_action(self, _parent, _next_frame):
        self.go_to_next_frame(_parent)

    # Goes to the next scene after the progress scene is complete
    def go_to_next_frame(self, _parent):
        _parent.set_frame(self.next_frame)