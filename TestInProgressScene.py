import tkinter as tk
from tkinter import ttk
from GUIWindow import *
from xml.dom.expatbuilder import parseFragmentString

# Creating the frame itself
class TestInProgressScene(tk.Frame):

    def __init__(self, parent, master_window, next_frame):
        self.next_frame = next_frame
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
        prgbar_progress.start()

        # A Button To Stop the Progress Bar and Progress Forward (Temporary until we link to actual progress)
        btn_stop = ttk.Button(frm_main, text='Stop', command= lambda: self.stop_button_action(parent, self.next_frame))
        btn_stop.pack()

        self.grid_propagate(0)

    def stop_button_action(self, _parent, _next_frame):
        self.go_to_next_frame(_parent)

    # Goes to the next scene after the progress scene is complete
    def go_to_next_frame(self, _parent):
        _parent.set_frame(self.next_frame)