# Imports all the necessary modules
import tkinter as tk
from tkinter import ttk
from xml.dom.expatbuilder import parseFragmentString
import sys

# Imports the ConsoleOutput class and its functions
from PythonFiles.ConsoleOutput import *

# Creating the frame itself
class TestInProgressScene(tk.Frame):

    def __init__(self, parent, master_window, next_frame, data_holder):
        self.data_holder = data_holder
        self.is_current_scene = False
        self.initialize_scene(parent, master_window, next_frame)

    # A function to be called within GUIWindow to create the console output
    # when the frame is being brought to the top
    def initialize_console(self):
        
        # Creating a popup window for the console output
        global console_popup
        console_popup = tk.Tk()
        console_popup.geometry("500x500+0+100")
        console_popup.title("Console Output Window")
        console_popup.wm_attributes('-toolwindow', 'True')

        # Used to tell the console window that its 
        # exit window button is being given a new function
        console_popup.protocol('WM_DELETE_WINDOW', self.fake_destroy)

        # Creating a Frame For Console Output
        frm_console = tk.Frame(console_popup, width = 500, height = 500, bg = 'black')
        frm_console.pack_propagate(0)
        frm_console.pack()

        # Placing an entry box in the frm_console
        global ent_console
        ent_console = tk.Text(
            frm_console, 
            bg = 'black', 
            fg = 'white', 
            font = ('Arial', 8)
            )
        ent_console.pack(anchor = 'center', fill = tk.BOTH, expand = 1)

        # Instantiates the console writing class
        console = ConsoleOutput(ent_console)

        # replace sys.stdout with our new console object
        sys.stdout = console

    # A pass function that the console window is being redirected to so its exit button
    # does not function
    def fake_destroy(self):
        pass

    # A Function to be called when the console should be destroyed
    def console_destroy(self):
        # Destroys the console output window
        console_popup.destroy()
        # Redirects any console readouts back to the actual console rather than the fake object
        sys.stdout = sys.__stdout__

    # Used to initialize the frame that is on the main window
    # next_frame is used to progress to the next scene and is passed in from GUIWindow
    def initialize_scene(self, parent, master_window, next_frame):
        self.next_frame = next_frame
        super().__init__(master_window, width = 850, height = 500)


        # Creating the main title in the frame
        lbl_title = tk.Label(self, 
            text = "Test in progress. Please wait.", 
            font = ('Arial', 20)
            )
        lbl_title.pack(padx = 0, pady = 100)

        # Create a progress bar that does not track progress but adds motion to the window
        prgbar_progress = ttk.Progressbar(
            self, 
            orient = 'horizontal', 
            mode = 'indeterminate', length = 350)
        prgbar_progress.pack(padx = 50)
        prgbar_progress.start()

        # A Button To Stop the Progress Bar and Progress Forward (Temporary until we link to actual progress)
        btn_stop = ttk.Button(
            self, 
            text='Stop', 
            command= lambda: self.stop_button_action(parent, self.next_frame))
        btn_stop.pack(padx = 0, pady = 100)

        # Forces the frame to stay the size of the master_window
        self.pack_propagate(0)

    # A function for the stop button
    def stop_button_action(self, _parent, _next_frame):

        # Destroys the console window
        self.console_destroy()

        # Progresses to the next frame
        self.go_to_next_frame(_parent)



    # Goes to the next scene after the progress scene is complete
    def go_to_next_frame(self, _parent):
        # Testing to see which frame you currently are in
        if self == _parent.test1_in_progress:
            current = 1
        if self == _parent.test2_in_progress:
            current = 2
        if self == _parent.test3_in_progress:
            current = 3
        if self == _parent.test4_in_progress:
            current = 4
        # Array of potentially uncompleted tests
        test_list = [
            self.data_holder.test2_completed,
            self.data_holder.test3_completed,
            self.data_holder.test4_completed
        ]
        for index, test in enumerate(test_list):
            if test == True:
                pass
            else:
                if index == 0 and current == 1:
                    _parent.set_frame(_parent.test2_frame)
                    break
                elif index == 1 and current < 3:
                    _parent.set_frame(_parent.test3_frame)
                    break
                else:
                    _parent.set_frame(_parent.test4_frame)

        # Tests if all the tests have been completed
        # if true, brings user to Test Summary Frame rather than the next test
        if (self.data_holder.test1_completed == True and 
            self.data_holder.test2_completed == True and 
            self.data_holder.test3_completed == True and 
            self.data_holder.test4_completed == True):

            _parent.set_frame(_parent.testing_finished_frame)
            
        # Otherwise takes the user to the next test
        # else:
        #     _parent.set_frame(self.next_frame)