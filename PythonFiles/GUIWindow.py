#################################################################################

# Importing all neccessary modules
from pickle import NONE
import tkinter as tk
from turtle import bgcolor
import multiprocessing as mp
#from pyparsing import trace_parse_action

# Importing all the neccessary files and classes from them
from PythonFiles.Scenes.SidebarScene import SidebarScene
from PythonFiles.Scenes.LoginScene import LoginScene
from PythonFiles.Scenes.ScanScene import ScanScene
from PythonFiles.TestFailedPopup import TestFailedPopup
from PythonFiles.Scenes.TestSummaryScene import TestSummaryScene
from PythonFiles.Scenes.TestScene import *
from PythonFiles.Scenes.TestInProgressScene import TestInProgressScene
from PythonFiles.Data.DataHolder import DataHolder
from PythonFiles.Scenes.SplashScene import SplashScene
from PythonFiles.Scenes.TestInProgressScene import *

#################################################################################



FORMAT = '%(asctime)s|%(levelname)s|%(message)s|'
logging.basicConfig(filename="/home/hgcal/WagonTest/WagonTestGUI/PythonFiles/logs/GUIWindow.log", filemode = 'w', format=FORMAT, level=logging.DEBUG)

# Create a class for creating the basic GUI Window to be called by the main function to
# instantiate the actual object
class GUIWindow():

    #################################################

    def __init__(self, conn, queue):
        self.conn = conn
        self.queue = queue
                             
        # Create the window named "self.master_window"
        # global makes self.master_window global and therefore accessible outside the function
        self.master_window = tk.Tk()
        self.master_window.title("Bethel Interns' Window")
        # Creates the size of the window and disables resizing
        self.master_window.geometry("1063x500+25+100")
        self.master_window.resizable(0,0)

        # Removes the tkinter logo from the window
        # self.master_window.wm_attributes('-toolwindow', 'True')

        # Creates and packs a frame that exists on top of the master_frame
        self.master_frame = tk.Frame(self.master_window, width=850, height= 500)
        self.master_frame.grid(column = 1, row = 0, columnspan = 4)

        # Creates a frame to house the sidebar on self.master_window
        sidebar_frame = tk.Frame(self.master_window, width = 213, height = 500)
        sidebar_frame.grid(column = 0 , row = 0)

        # Creates the "Storage System" for the data during testing
        self.data_holder = DataHolder()

        # Creates all the widgets on the sidebar
        self.sidebar = SidebarScene(self, sidebar_frame, self.data_holder)
        self.sidebar.pack()

        #################################################
        #   Creates all the different frames in layers  #
        #################################################

        # At top so it can be referenced by other frames' code... Order of creation matters

        self.test_summary_frame = TestSummaryScene(self, self.master_frame, self.data_holder)
        self.test_summary_frame.grid(row=0, column=0)

        self.login_frame = LoginScene(self, self.master_frame, self.data_holder)
        self.login_frame.grid(row=0, column=0)
    
        self.scan_frame = ScanScene(self, self.master_frame, self.data_holder)
        self.scan_frame.grid(row=0, column=0)

        self.test1_frame= Test1Scene(self, self.master_frame, self.data_holder, 
                            "General Resistance Test",
                            queue
                            )
        self.test1_frame.grid(row=0, column=0)

        self.test2_frame= Test2Scene(self, self.master_frame, self.data_holder,
                            "ID Resistor Test", 
                            queue
                            )
        self.test2_frame.grid(row=0, column=0)

        self.test3_frame= Test3Scene(self, self.master_frame, self.data_holder, 
                            "I2C Comm. Test", 
                            queue
                            )
        self.test3_frame.grid(row=0, column=0)

        self.test4_frame= Test4Scene(self, self.master_frame, self.data_holder, 
                            "Bit Rate Test", 
                            queue
                            )
        self.test4_frame.grid(row=0, column=0)

        self.test_in_progress_frame = TestInProgressScene(self, self.master_frame, self.data_holder, queue)
        self.test_in_progress_frame.grid(row=0, column=0)


        # Near bottom so it can reference other frames with its code
        self.splash_frame = SplashScene(self, self.master_frame)
        self.splash_frame.grid(row=0, column=0)

        #################################################
        #              End Frame Creation               #
        #################################################
        
        logging.info("All frames have been created.")


        # Tells the master window that its exit window button is being given a new function
        self.master_window.protocol('WM_DELETE_WINDOW', self.exit_function)
        
        # Sets the current frame to the splash frame
        self.set_frame_splash_frame()

        self.master_frame.after(500, self.set_frame_login_frame)
        
        self.master_frame.after(1000, logging.info("The window mainloop has run.")

        self.master_window.mainloop()
        

    #################################################

    def set_frame_login_frame(self):  

        self.set_frame(self.login_frame)    

    #################################################

    def set_frame_scan_frame(self):

        self.scan_frame.is_current_scene = True
        self.set_frame(self.scan_frame)
        self.scan_frame.scan_QR_code(self.master_window)

    #################################################

    def set_frame_splash_frame(self):

        self.set_frame(self.splash_frame)

        # Disables all buttons when the splash frame is the only frame
        self.sidebar.disable_all_btns()

    #################################################

    def set_frame_test_summary(self):
        self.test_summary_frame.update_frame()
        self.check_if_test_passed()
        self.set_frame(self.test_summary_frame)

    #################################################

    def set_frame_test1(self):
        self.test1_frame.update_frame(self)
        self.set_frame(self.test1_frame)

    #################################################

    def set_frame_test2(self):
        self.test2_frame.update_frame(self)
        self.set_frame(self.test2_frame)

    #################################################

    def set_frame_test3(self):
        self.test3_frame.update_frame(self)
        self.set_frame(self.test3_frame)

    #################################################

    def set_frame_test4(self):
        self.test4_frame.update_frame(self)
        self.set_frame(self.test4_frame)

    #################################################

    def set_frame_test_in_progress(self, queue):
        print("first set_frame called")
        
        self.set_frame(self.test_in_progress_frame)
        print("tk.raise called")
        self.sidebar.disable_all_btns()
        print("Buttons disabled")
        self.test_in_progress_frame.begin_update(self.master_window, queue)
        print("after command called")
        self.go_to_next_test()   

    #################################################

    def check_if_test_passed(self):
        pass
    #################################################

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

        
        self.check_if_test_passed()
    #################################################

    # Called to change the frame to the argument _frame
    def set_frame(self, _frame):
        
        # Updates the sidebar every time the frame is set
        self.sidebar.update_sidebar(self)

        # If frame is test_in_progress frame, disable the close program button
        # Tells the master window that its exit window button is being given a new function
        if _frame is self.test_in_progress_frame:
            self.master_window.protocol('WM_DELETE_WINDOW', self.unable_to_exit)
        else:
            # Tells the master window that its exit window button is being given a new function
            self.master_window.protocol('WM_DELETE_WINDOW', self.exit_function)
 
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

        # Brings up the test_failed popup if the test is false, continues on if not
        if _frame == self.test2_frame:
            if self.data_holder.test1_pass == False:
                TestFailedPopup(self, self.test1_frame)
        if _frame == self.test3_frame:
            if self.data_holder.test2_pass == False:
                TestFailedPopup(self, self.test2_frame)
        if _frame == self.test4_frame:
            if self.data_holder.test3_pass == False:
                TestFailedPopup(self, self.test3_frame)
        if _frame == self.test_summary_frame:
            if self.data_holder.test4_pass == False:
                TestFailedPopup(self, self.test4_frame)

        # Raises the passed in frame to be the current frame
        _frame.tkraise()

    #################################################


    def unable_to_exit(self):
        # Creates a popup to confirm whether or not to exit out of the window
        self.popup = tk.Toplevel()
        # popup.wm_attributes('-toolwindow', 'True')
        self.popup.title("Exit Window") 
        self.popup.geometry("300x150+500+300")
        self.popup.grab_set()
       

        # Creates frame in the new window
        frm_popup = tk.Frame(self.popup)
        frm_popup.pack()

        # Creates label in the frame
        lbl_popup = tk.Label(
            frm_popup, 
            text = " You cannot exit the program \n during a test! ",
            font = ('Arial', 13)
            )
        lbl_popup.grid(column = 0, row = 0, columnspan = 2, pady = 25)


        btn_ok = tk.Button(
            frm_popup,
            width = 12,
            height = 2,
            text = "OK",
            font = ('Arial', 12),
            relief = tk.RAISED,
            command = lambda: self.destroy_popup()
        )
        btn_ok.grid(column = 0, row = 1, columnspan=2)

    #################################################

    # Called when the no button is pressed to destroy popup and return you to the main window
    def destroy_popup(self):
        self.popup.destroy()


    # New function for clicking on the exit button
    def exit_function(self):

        # Creates a popup to confirm whether or not to exit out of the window
        self.popup = tk.Toplevel()
        # popup.wm_attributes('-toolwindow', 'True')
        self.popup.title("Exit Window") 
        self.popup.geometry("300x150+500+300")
        self.popup.grab_set()
       

        # Creates frame in the new window
        frm_popup = tk.Frame(self.popup)
        frm_popup.pack()

        # Creates label in the frame
        lbl_popup = tk.Label(
            frm_popup, 
            text = "Are you sure you would like to exit?",
            font = ('Arial', 13)
            )
        lbl_popup.grid(column = 0, row = 0, columnspan = 2, pady = 25)

        # Creates yes and no buttons for exiting
        btn_yes = tk.Button(
            frm_popup,     
            width = 12,
            height = 2,
            text = "Yes", 
            relief = tk.RAISED,
            font = ('Arial', 12), 
            command = lambda: self.destroy_function()
            )
        btn_yes.grid(column = 0, row = 1)

        btn_no = tk.Button(
            frm_popup,
            width = 12,
            height = 2,
            text = "No",
            relief = tk.RAISED,
            font = ('Arial', 12),
            command = lambda: self.destroy_popup()
        )
        btn_no.grid(column = 1, row = 1)

    #################################################

    # Called when the no button is pressed to destroy popup and return you to the main window
    def destroy_popup(self):
        self.popup.destroy()

    #################################################


    # Called when the yes button is pressed to destroy both windows
    def destroy_function(self):
        #self.master_window.eval('::ttk::CancelRepeat')

        self.master_window.update()
        self.popup.update()
       
        #popup.quit()
        #self.master_window.quit()

        if self.scan_frame.is_current_scene == True:
            self.test_in_progress_frame.close_prgbar()
            self.scan_frame.kill_processes()

        # Destroys the popup and master window
        self.popup.destroy()
        self.popup.quit()

        self.master_window.destroy()
        self.master_window.quit()

        # Ensures the application closes with the exit button
        #exit_main()

        print("Leaving tester. Goodbye!")

    #################################################

    
#################################################################################
