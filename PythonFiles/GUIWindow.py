# Importing all Modules
from pickle import NONE
import tkinter as tk
from turtle import bgcolor
from PythonFiles.LoginScene import LoginScene
from PythonFiles.ScanScene import ScanScene
from PythonFiles.TestFinishedSummary import TestFinishedSummary
from PythonFiles.TestFrames.Test1 import Test1Scene
from PythonFiles.TestFrames.Test2 import Test2Scene
from PythonFiles.TestFrames.Test3 import Test3Scene
from PythonFiles.TestFrames.Test4 import Test4Scene
from PythonFiles.TestInProgressScene import TestInProgressScene
from PythonFiles.DataHolder import DataHolder


# Create a class for creating the basic GUI Window
class GUIWindow():

    def __init__(self):                     
        # Create the window named "master_window"
        global master_window
        master_window = tk.Tk()
        master_window.title("Bethel Interns' Window")
        master_window.geometry("850x500")
        master_frame = tk.Frame(master_window, width=850, height= 500)
        master_window.resizable(0,0)
        master_frame.pack()


        # Creates the "Storage System" for the data during testing
        self.data_holder = DataHolder()
        

        # Creates all the different frames in layers
        self.testing_finished_frame = TestFinishedSummary(self, master_frame, self.data_holder)
        self.testing_finished_frame.grid(row=0, column=0)

        self.login_frame = LoginScene(self, master_frame, self.data_holder)
        self.login_frame.grid(row=0, column=0)
    
        self.scan_frame = ScanScene(self, master_frame, self.data_holder)
        self.scan_frame.grid(row=0, column=0)

        self.test1_frame= Test1Scene(self, master_frame, self.data_holder)
        self.test1_frame.grid(row=0, column=0)

        self.test2_frame= Test2Scene(self, master_frame, self.data_holder)
        self.test2_frame.grid(row=0, column=0)

        self.test3_frame= Test3Scene(self, master_frame, self.data_holder)
        self.test3_frame.grid(row=0, column=0)

        self.test4_frame= Test4Scene(self, master_frame, self.data_holder)
        self.test4_frame.grid(row=0, column=0)

        self.test1_in_progress = TestInProgressScene(self, master_frame, self.test2_frame)
        self.test1_in_progress.grid(row=0, column=0)

        self.test2_in_progress = TestInProgressScene(self, master_frame, self.test3_frame)
        self.test2_in_progress.grid(row=0, column=0)

        self.test3_in_progress = TestInProgressScene(self, master_frame, self.test4_frame)
        self.test3_in_progress.grid(row=0, column=0)

        self.test4_in_progress = TestInProgressScene(self, master_frame, self.testing_finished_frame)
        self.test4_in_progress.grid(row=0, column=0)

        # Used to tell the master window that its exit window button is being given a new function
        master_window.protocol('WM_DELETE_WINDOW', self.exit_function)

        # Sets the current frame to the login frame
        self.set_frame(self.login_frame)

        master_window.mainloop()
    

    # Changes which frame is currently shown
    def set_frame(self, _frame):
        if (_frame is self.scan_frame):
            self.scan_frame.is_current_scene = True
            self.scan_frame.scan_QR_code()

        if (_frame is not self.scan_frame):
            self.scan_frame.is_current_scene = False

        if(_frame is self.testing_finished_frame):
            self.testing_finished_frame.create_updated_table()
        
        _frame.tkraise()






    def exit_function(self):
        # Creates a popup to confirm whether or not to exit out of the window
        global popup
        popup = tk.Tk()
        popup.title("Exit Confirmation Window") 
        popup.geometry("300x150")
        popup.eval("tk::PlaceWindow . center")

        frm_popup = tk.Frame(popup)
        frm_popup.pack()

        lbl_popup = tk.Label(frm_popup, text = "Are you sure you would like to exit?")
        lbl_popup.grid(column = 0, row = 0, columnspan = 2, pady = 25)

        btn_yes = tk.Button(
             frm_popup,
             text = "Yes", 
             relief = tk.RAISED, 
             command = lambda: self.destroy_function()
             ) 
        btn_yes.grid(column = 0, row = 1)

        btn_no = tk.Button(
            frm_popup,
            text = "No",
            relief = tk.RAISED,
            command = lambda: self.destroy_popup()
        )
        btn_no.grid(column = 1, row = 1)

    # Called when the no button is pressed to destroy popup and return you to the main window
    def destroy_popup(self):
        popup.destroy()

    # Called when the yes button is pressed to destroy both windows
    def destroy_function(self):
        popup.destroy()
        master_window.destroy()

    def get_scan_frame(self):
        return self.scan_frame