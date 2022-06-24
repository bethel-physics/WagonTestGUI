#################################################################################

# Importing Necessary Modules
import tkinter as tk
import tkinter.font as font

# Importing Necessary Files
from PythonFiles.utils.REQClient import REQClient

#################################################################################


# Creating class for the window
class TestScene(tk.Frame):

    #################################################

    def __init__(self, parent, master_frame, data_holder, test_name, queue):
        super().__init__(master_frame, width=850, height=500)
        self.queue = queue
        self.test_name = test_name
        self.data_holder = data_holder
        
        self.update_frame(parent)

    #################################################

    def update_frame(self, parent):

        # Creates a font to be more easily referenced later in the code
        font_scene = ('Arial', 15)

        # Create a centralized window for information
        frm_window = tk.Frame(self, width = 850, height = 500)
        frm_window.grid(column=1, row=1, padx = 235, pady = 97)

        # Create a label for the tester's name
        lbl_tester = tk.Label(
            frm_window, 
            text = "Tester: ", 
            font = font_scene
            )
        lbl_tester.pack(side = 'top')

        # Create an entry for the tester's name
        ent_tester = tk.Entry(
            frm_window, 
            font = font_scene
            )
        ent_tester.insert(0, self.data_holder.user_ID)
        ent_tester.pack(side = 'top')
        ent_tester.config(state = "disabled")

        # Create a label for the serial number box
        lbl_snum = tk.Label(
            frm_window, 
            text = "Serial Number: ", 
            font = font_scene
            )
        lbl_snum.pack(side = 'top')

        # Create a entry for the serial number box
        ent_snum = tk.Entry(
            frm_window, 
            font = font_scene
            )
        ent_snum.insert(0, self.data_holder.current_serial_ID)
        ent_snum.pack(side = 'top')
        ent_snum.config(state = "disabled")

        # Create a label for the test about to be run
        lbl_test = tk.Label(
            frm_window, 
            text = "Current Test: ", 
            font = font_scene
            )
        lbl_test.pack(side = 'top')


        # Create a entry for the test type
        self.ent_test = tk.Entry(
            frm_window, 
            font = font_scene
            )
        self.ent_test.pack(side = 'top')
        self.ent_test.insert(0, self.test_name)
        self.ent_test.config(state = "disabled")

        # Create a label for confirming test
        lbl_confirm = tk.Label(
            frm_window, 
            text = "Are you ready to begin the test?", 
            font = font_scene
            )
        lbl_confirm.pack(side = 'top')

        # Create a button for confirming test
        btn_confirm = tk.Button(
            frm_window, 
            text = "Confirm", 
            relief = tk.RAISED, 
            command = lambda:self.btn_confirm_action(parent)
            )
        btn_confirm.pack(side = 'top')
        btn_confirm['font'] = font.Font(family = 'Arial', size = 13)

        # Create frame for logout button
        frm_logout = tk.Frame(self)
        frm_logout.grid(column = 2, row = 2, sticky = 'ne')

        # Create a logout button
        btn_logout = tk.Button(
            frm_logout, 
            text = "Logout", 
            relief = tk.RAISED, 
            command = lambda: self.btn_logout_action(parent))
        btn_logout.pack(anchor = 'se')

        # Create a frame for the back button
        frm_back = tk.Frame(self)
        frm_back.grid(column = 2, row = 0, sticky = 'ne')

        # Create a rescan button
        btn_rescan = tk.Button(
            frm_back, 
            text = "Change Boards", 
            relief = tk.RAISED, 
            command = lambda: self.btn_rescan_action(parent))
        btn_rescan.pack(anchor = 'ne')


        

        self.grid_propagate(0)
        
    #################################################

    # Rescan button takes the user back to scanning in a new board
    def btn_rescan_action(self, _parent):
        _parent.set_frame_scan_frame()
    
    #################################################

    # Confirm button action takes the user to the test in progress scene
    def btn_confirm_action(self, _parent):
        # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #   ++ GOAL CODE ++                                 #
        # def confirm():                                    #
        #       set_frame_TIPS()                            #
        #       Runs_Test()   # Might include multithread   #
        #       Get_Results()                               #
        #       Update_Dataholder()                         #
        #       Go_To_Next_Test()                           #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        # _parent.set_frame_test_in_progress(self.queue)
        pass

    #################################################

    # functionality for the logout button
    def btn_logout_action(self, _parent):
        _parent.set_frame_login_frame()

    #################################################


#################################################################################


class Test1Scene(TestScene):
    # Override to add specific functionality
    def btn_confirm_action(self, _parent):

        self.data_holder.test1_completed = True
        self.data_holder.test1_pass = True
        self.data_holder.print()
        super().btn_confirm_action(_parent)
        test_1_client = REQClient(b'test1')
        _parent.set_frame_test_in_progress(self.queue)
         #TODO EDIT THIS WITH ACTUAL TEST DATA

        
#################################################################################


class Test2Scene(TestScene):
    # Override to add specific functionality
    def btn_confirm_action(self, _parent):
        self.data_holder.test2_completed = True
        self.data_holder.test2_pass = True
        self.data_holder.print()
        super().btn_confirm_action(_parent)
        test_2_client = REQClient(b'test2')
        _parent.set_frame_test_in_progress(self.queue)
         #TODO EDIT THIS WITH ACTUAL TEST DATA
        
        


#################################################################################


class Test3Scene(TestScene):
    # Override to add specific functionality
    def btn_confirm_action(self, _parent):

        self.data_holder.test3_completed = True
        self.data_holder.test3_pass = True
        self.data_holder.print()
        super().btn_confirm_action(_parent)
        test_3_client = REQClient(b'test3')
        _parent.set_frame_test_in_progress(self.queue)
         #TODO EDIT THIS WITH ACTUAL TEST DATA


#################################################################################


class Test4Scene(TestScene):
    # Override to add specific functionality
    def btn_confirm_action(self, _parent):

        self.data_holder.test4_completed = True
        self.data_holder.test4_pass = True
        self.data_holder.print()
        super().btn_confirm_action(_parent)
        test_4_client = REQClient(b'test4')
        _parent.set_frame_test_in_progress(self.queue)
         #TODO EDIT THIS WITH ACTUAL TEST DATA

#################################################################################