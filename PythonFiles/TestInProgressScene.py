import tkinter as tk
from tkinter import ttk
from xml.dom.expatbuilder import parseFragmentString
import sys
import PythonFiles.ConsoleOutput
from PythonFiles.ConsoleOutput import *

# Creating the frame itself
class TestInProgressScene(tk.Frame):

    def __init__(self, parent, master_window, next_frame, data_holder):
        self.data_holder = data_holder
        self.is_current_scene = False
        self.initialize_scene(parent, master_window, next_frame)

    def initialize_console(self):
        # Creating a popup window for the console output
        global console_popup
        console_popup = tk.Tk()
        console_popup.geometry("500x500")
        console_popup.title("Console Output Window")

        # Creating a Frame For Console Output
        frm_console = tk.Frame(console_popup, width = 500, height = 500, bg = 'black')
        frm_console.pack_propagate(0)
        frm_console.pack()

        # Labeling frm_console
        global ent_console
        ent_console = tk.Text(frm_console, bg = 'black', fg = 'white', font = ('Arial', 8))
        ent_console.pack(anchor = 'center')

        # Instantiates the console writing class
        console = ConsoleOutput(ent_console)

        # replace sys.stdout with our object
        sys.stdout = console

        print("Hello World!")

    def console_destroy(self):
        console_popup.destroy()

    def initialize_scene(self, parent, master_window, next_frame):
        self.next_frame = next_frame
        super().__init__(master_window, width = 850, height = 500)


        # Creating the main title in the frame
        lbl_title = tk.Label(self, text = "Test in progress. Please wait.", font = ('Arial', 20))
        lbl_title.pack(padx = 0, pady = 100)

        # Create a progress bar of some kind
        prgbar_progress = ttk.Progressbar(
            self, 
            orient = 'horizontal', 
            mode = 'indeterminate', length = 350)
        prgbar_progress.pack(padx = 50)
        prgbar_progress.start()

        # A Button To Stop the Progress Bar and Progress Forward (Temporary until we link to actual progress)
        btn_stop = ttk.Button(self, text='Stop', command= lambda: self.stop_button_action(parent, self.next_frame))
        btn_stop.pack(padx = 0, pady = 100)




        self.pack_propagate(0)

    def stop_button_action(self, _parent, _next_frame):
        self.go_to_next_frame(_parent)
        self.console_destroy()

    # Goes to the next scene after the progress scene is complete
    def go_to_next_frame(self, _parent):
        _parent.set_frame(self.next_frame)