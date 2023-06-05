#################################################################################

# Importing all neccessary modules
from pickle import NONE
import tkinter as tk
from turtle import bgcolor
from PythonFiles.GUIConfig import GUIConfig
from PythonFiles.Data.DataHolder import DataHolder
from PythonFiles.Scenes.LoginScene import LoginScene
from PythonFiles.Scenes.ScanScene import ScanScene
from PythonFiles.Scenes.SplashScene import SplashScene
from PythonFiles.Scenes.TestSummaryScene import TestSummaryScene
from PythonFiles.Scenes.InspectionScenes.Inspection1 import Inspection1
from PythonFiles.Scenes.AddUserScene import AddUserScene


#################################################################################


# Create a class for creating the basic GUI Window to be called by the main function to
# instantiate the actual object
class GUIWindow():

    #################################################

    def __init__(self, board_cfg):                     
        # Create the window named "master_window"
        # global makes master_window global and therefore accessible outside the function
        global master_window
        master_window = tk.Tk()
        master_window.title("Bethel Interns' Window")

        # Creates the size of the window and disables resizing
        master_window.geometry("850x500+25+100")
        master_window.resizable(0,0)

        # Removes the tkinter logo from the window
        # master_window.wm_attributes('-toolwindow', 'True')

        # Creates and packs a frame that exists on top of the master_frame
        master_frame = tk.Frame(master_window, width=850, height= 500)
        master_frame.grid(column = 0, row = 0, columnspan = 4)

        # Object for taking care of instantiation of different test types
        self.gui_cfg = GUIConfig(board_cfg)

        # Creates the "Storage System" for the data during testing
        self.data_holder = DataHolder(self.gui_cfg)


        #################################################
        #   Creates all the different frames in layers  #
        #################################################

        # At top so it can be referenced by other frames' code... Order of creation matters
        self.test_summary_frame = TestSummaryScene(self, master_frame, self.data_holder)
        self.test_summary_frame.grid(row=0, column=0)

        self.login_frame = LoginScene(self, master_frame, self.data_holder)
        self.login_frame.grid(row=0, column=0)
    
        self.scan_frame = ScanScene(self, master_frame, self.data_holder)
        self.scan_frame.grid(row=0, column=0)

        self.inspection_frame = Inspection1(self, master_frame, self.data_holder)
        self.inspection_frame.grid(row=0,column=0)

        self.add_user_frame = AddUserScene(self, master_frame, self.data_holder)
        self.add_user_frame.grid(row=0,column=0)


        # Near bottom so it can reference other frames with its code
        self.splash_frame = SplashScene(self, master_frame)
        self.splash_frame.grid(row=0, column=0)

        #################################################
        #              End Frame Creation               #
        #################################################
        
        # Tells the master window that its exit window button is being given a new function
        master_window.protocol('WM_DELETE_WINDOW', self.exit_function)

        # Sets the current frame to the splash frame
        self.set_frame_splash_frame()

        master_frame.after(500, self.set_frame_login_frame)

        master_window.mainloop()
    
    #################################################

    def set_frame_login_frame(self):  

        self.set_frame(self.login_frame)    

    #################################################

    def set_frame_inspection_frame(self):  
        self.inspection_frame.update_frame(self)
        self.set_frame(self.inspection_frame)    

    #################################################

    def set_frame_scan_frame(self):

        self.scan_frame.is_current_scene = True
        self.set_frame(self.scan_frame)
        self.scan_frame.scan_QR_code(master_window)
   
     #################################################

    def set_frame_splash_frame(self):

        self.set_frame(self.splash_frame)

    #################################################

    def set_frame_test_summary(self):
        self.test_summary_frame.update_frame()
        self.set_frame(self.test_summary_frame)

    def set_frame_add_user_frame(self):
        self.set_frame(self.add_user_frame)

    #################################################

    # Called to change the frame to the argument _frame
    def set_frame(self, _frame):
 
        #############################################################################
        #  The Following Code Determines What Buttons Are Visible On The Side Bar   #
        #############################################################################

            

        # Hides the submit button on scan frame until an entry is given to the computer
        if (_frame is not self.scan_frame):
            self.scan_frame.is_current_scene = False
            self.scan_frame.hide_submit_button()
            

        #############################################################################
        #                        End Button Visibility Code                         #
        #############################################################################

        # Raises the passed in frame to be the current frame
        _frame.tkraise()

    #################################################

    # New function for clicking on the exit button
    def exit_function(self):

        # Creates a popup to confirm whether or not to exit out of the window
        global popup
        popup = tk.Tk()
        # popup.wm_attributes('-toolwindow', 'True')
        popup.title("Exit Confirmation Window") 
        popup.geometry("300x150")
        popup.eval("tk::PlaceWindow . center")
       

        # Creates frame in the new window
        frm_popup = tk.Frame(popup)
        frm_popup.pack()

        # Creates label in the frame
        lbl_popup = tk.Label(frm_popup, text = "Are you sure you would like to exit?")
        lbl_popup.grid(column = 0, row = 0, columnspan = 2, pady = 25)

        # Creates yes and no buttons for exiting
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

    #################################################

    # Called when the no button is pressed to destroy popup and return you to the main window
    def destroy_popup(self):
        popup.destroy()

    #################################################

    # Called when the yes button is pressed to destroy both windows
    def destroy_function(self):

        # Destroys the popup and master window
        popup.destroy()
        master_window.destroy()

        # Ensures the application closes with the exit button
        exit()

    #################################################

    
#################################################################################
