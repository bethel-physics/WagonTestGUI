# Importing all neccessary modules
from pickle import NONE
import tkinter as tk
from turtle import bgcolor

# Importing all the neccessary files and classes from them
from PythonFiles.SidebarScene import SidebarScene
from PythonFiles.LoginScene import LoginScene
from PythonFiles.ScanScene import ScanScene
from PythonFiles.TestFailedPopup import TestFailedPopup
from PythonFiles.TestSummary import TestSummaryScene
from PythonFiles.TestScene import *
from PythonFiles.TestInProgressScene import TestInProgressScene
from PythonFiles.DataHolder import DataHolder
from PythonFiles.SplashScene import SplashScene
from PythonFiles.TestInProgressScene import *


# Create a class for creating the basic GUI Window to be called by the main function to
# instantiate the actual object
class GUIWindow():

    def __init__(self):                     
        # Create the window named "master_window"
        # global makes master_window global and therefore accessible outside the function
        global master_window
        master_window = tk.Tk()
        master_window.title("Bethel Interns' Window")

        # Creates the size of the window and disables resizing
        master_window.geometry("1063x500+25+100")
        master_window.resizable(0,0)

        # Removes the tkinter logo from the window
        master_window.wm_attributes('-toolwindow', 'True')

        # Creates and packs a frame that exists on top of the master_frame
        master_frame = tk.Frame(master_window, width=850, height= 500)
        master_frame.grid(column = 1, row = 0, columnspan = 4)

        # Creates a frame to house the sidebar on master_window
        sidebar_frame = tk.Frame(master_window, width = 213, height = 500)
        sidebar_frame.grid(column = 0 , row = 0)

        # Creates the "Storage System" for the data during testing
        self.data_holder = DataHolder()

        # Creates all the widgets on the sidebar
        self.sidebar = SidebarScene(self, sidebar_frame, self.data_holder)
        self.sidebar.pack()

        # Creates all the different frames in layers

        # At top so it can be referenced by other frames' code... Order of creation matters
        self.test_summary_frame = TestSummaryScene(self, master_frame, self.data_holder)
        self.test_summary_frame.grid(row=0, column=0)

        self.login_frame = LoginScene(self, master_frame, self.data_holder)
        self.login_frame.grid(row=0, column=0)
    
        self.scan_frame = ScanScene(self, master_frame, self.data_holder)
        self.scan_frame.grid(row=0, column=0)

        self.test1_frame= Test1Scene(self, master_frame, self.data_holder, "General Resistance Test")
        self.test1_frame.grid(row=0, column=0)

        self.test2_frame= Test2Scene(self, master_frame, self.data_holder,  "ID Resistor Test")
        self.test2_frame.grid(row=0, column=0)

        self.test3_frame= Test3Scene(self, master_frame, self.data_holder, "I2C Comm. Test")
        self.test3_frame.grid(row=0, column=0)

        self.test4_frame= Test4Scene(self, master_frame, self.data_holder, "Bit Rate Test")
        self.test4_frame.grid(row=0, column=0)

        self.test_in_progress_frame = TestInProgressScene(self, master_frame, self.data_holder)
        self.test_in_progress_frame.grid(row=0, column=0)


        # Near bottom so it can reference other frames with its code
        self.splash_frame = SplashScene(self, master_frame)
        self.splash_frame.grid(row=0, column=0)

        # Tells the master window that its exit window button is being given a new function
        master_window.protocol('WM_DELETE_WINDOW', self.exit_function)

        # Sets the current frame to the splash frame
        self.set_frame_splash_frame()

        master_frame.after(1500, self.set_frame_login_frame)

        master_window.mainloop()
    




    def set_frame_login_frame(self):  

        self.set_frame(self.login_frame)    


    def set_frame_scan_frame(self):

        self.scan_frame.is_current_scene = True
        self.scan_frame.scan_QR_code()
        self.set_frame(self.scan_frame)


    def set_frame_splash_frame(self):

        self.set_frame(self.splash_frame)

        # Disables all buttons when the splash frame is the only frame
        self.sidebar.disable_all_btns()


    def set_frame_test_summary(self):
        self.test_summary_frame.update_frame()
        self.check_if_test_passed()
        self.set_frame(self.test_summary_frame)

    
    def set_frame_test1(self):
        self.test1_frame.update_frame(self)
        self.set_frame(self.test1_frame)


    def set_frame_test2(self):
        self.test2_frame.update_frame(self)
        self.set_frame(self.test2_frame)


    def set_frame_test3(self):
        self.test3_frame.update_frame(self)
        self.set_frame(self.test3_frame)


    def set_frame_test4(self):
        self.test4_frame.update_frame(self)
        self.set_frame(self.test4_frame)


    def set_frame_test_in_progress(self):
        self.test_in_progress_frame.tkraise()
        self.sidebar.disable_all_btns()
        self.test_in_progress_frame.update_frame(self)


    def check_if_test_passed(self):
        # Brings up the test_failed popup if the test is false, continues on if not
        if self.data_holder.test1_pass == False:
            TestFailedPopup(self)

        elif self.data_holder.test2_pass == False:
            TestFailedPopup(self)

        elif self.data_holder.test3_pass == False:
            TestFailedPopup(self)

        elif self.data_holder.test4_pass == False:
            TestFailedPopup(self)

    





    def go_to_next_test(self):

        # Array of potentially uncompleted tests
        test_completed_list = [
            self.data_holder.test1_completed,
            self.data_holder.test2_completed,
            self.data_holder.test3_completed,
            self.data_holder.test4_completed
        ]
        

        test_incomplete = False

        # Checks tells the function which frame to set based on what frame is currently up
        for index, test in enumerate(test_completed_list):
            if test == True:
                pass

            else:
                test_incomplete = True
                if (index ==0):
                    self.set_frame_test1()
                elif (index == 1):
                    self.set_frame_test2()
                elif (index == 2):
                    self.set_frame_test3()
                elif (index == 3):
                    self.set_frame_test4()
                break


        # Tests if all the tests have been completed
        # if true, brings user to Test Summary Frame rather than the next test
        if (not test_incomplete):
            self.set_frame_test_summary()





    # Called to change the frame to the argument _frame
    def set_frame(self, _frame):
        
        # Updates the sidebar every time the frame is set
        self.sidebar.update_sidebar(self)
 
        #############################################################################
        #  The Following Code Determines What Buttons Are Visible On The Side Bar   #
        #############################################################################

        # Disables all but login button when on login_frame
        if _frame is self.login_frame:
            self.sidebar.disable_all_btns_but_login()

        # Disables all but scan button when on scan_frame
        if _frame is self.scan_frame:
            self.sidebar.disable_all_btns_but_scan()

        # Disables the sidebar login button when the login frame is not the current frame
        # or when scan_frame is not the current frame
        if (_frame is not self.login_frame):
            self.sidebar.disable_login_button()
            

        # Hides the submit button on scan frame until an entry is given to the computer
        if (_frame is not self.scan_frame):
            self.scan_frame.is_current_scene = False
            self.scan_frame.hide_submit_button()
            
            # Disables the sidebar scan button when the scan frame is not the current frame
            self.sidebar.disable_scan_button()

        #############################################################################
        #                        End Button Visibility Code                         #
        #############################################################################

        # Raises the passed in frame to be the current frame
        _frame.tkraise()




    # New function for clicking on the exit button
    def exit_function(self):

        # Creates a popup to confirm whether or not to exit out of the window
        global popup
        popup = tk.Tk()
        popup.wm_attributes('-toolwindow', 'True')
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

    # Called when the no button is pressed to destroy popup and return you to the main window
    def destroy_popup(self):
        popup.destroy()

    # Called when the yes button is pressed to destroy both windows
    def destroy_function(self):

        # If statements are to destroy console windows if they exist
        if(self.test_in_progress_frame.is_current_scene):
            self.test_in_progress_frame.console_destroy()

        # Destroys the popup and master window
        popup.destroy()
        master_window.destroy()

        # Ensures the application closes with the exit button
        exit()

    

