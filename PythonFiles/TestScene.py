import tkinter as tk
import tkinter.font as font



# Creating class for the window
class TestScene(tk.Frame):
    def __init__(self, parent, master_frame, data_holder):
        super().__init__(master_frame, width=850, height=500)

        self.scan_frame = parent.scan_frame
        self.test2_frame = parent.test2_frame
        self.test3_frame = parent.test3_frame
        self.test4_frame = parent.test4_frame
        self.test_summary_frame = parent.test_summary_frame

        self.data_holder = data_holder
        
        self.update_frame(parent)

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
        ent_test = tk.Entry(
            frm_window, 
            font = font_scene
            )
        ent_test.pack(side = 'top')
        ent_test.config(state = "disabled")

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

        # # # # # # # # # 
        # Create a back button
        btn_back = tk.Button(
            frm_back, 
            text = "Back", 
            relief = tk.RAISED, 
            command = lambda: self.btn_back_action(parent))
        btn_back.pack(anchor = 'ne')
        # # # # # # # # # 

        # Create a rescan button
        btn_rescan = tk.Button(
            frm_back, 
            text = "Change Boards", 
            relief = tk.RAISED, 
            command = lambda: self.btn_rescan_action(parent))
        btn_rescan.pack(anchor = 'ne')


        

        self.grid_propagate(0)
    
    # Rescan button takes the user back to scanning in a new board
    def btn_rescan_action(self, _parent):
        _parent.set_frame(_parent.scan_frame)

    # # # # # # # # # 
    # Back button action takes the user back to the scanning device
    def btn_back_action(self, _parent):
        _parent.set_frame(self.back_frame)
    # # # # # # # # # 
   
    # Confirm button action takes the user to the test in progress scene
    def btn_confirm_action(self, _parent):

        _parent.set_frame(self.next_frame)

         #TODO EDIT THIS WITH ACTUAL TEST DATA
        self.data_holder.test1_completed = True
        self.data_holder.test1_pass = True
        self.data_holder.print()

    # functionality for the logout button
    def btn_logout_action(self, _parent):
        _parent.set_frame(_parent.login_frame)

class Test1Scene(TestScene):
    def __init__(self, parent, master_frame, data_holder):

        # Setting the confirm button's frame
        parent.next_frame = parent.test2_frame

        # Setting the back button's frame
        parent.back_frame = parent.scan_frame

        super.__init__(parent, master_frame, data_holder)

        # Entering the test name based on the test
        parent.ent_test.insert(0, "General Resistance Test")

class Test2Scene(TestScene):
    def __init__(self, parent, master_frame, data_holder):

        # Setting the confirm button's frame
        parent.next_frame = parent.test3_frame

        # Setting the back button's frame
        parent.back_frame = parent.test1_frame

        super.__init__(parent, master_frame, data_holder)

        # Entering the test name based on the test
        parent.ent_test.insert(0, "ID Resistor Test")

class Test3Scene(TestScene):
    def __init__(self, parent, master_frame, data_holder):

        # Setting the confirm button's frame
        parent.next_frame = parent.test4_frame

        # Setting the back button's frame
        parent.back_frame = parent.test2_frame

        super.__init__(parent, master_frame, data_holder)

        # Entering the test name based on the test
        parent.ent_test.insert(0, "I2C Comm. Test")

class Test4Scene(TestScene):
    def __init__(self, parent, master_frame, data_holder):

        # Setting the confirm button's frame
        parent.next_frame = parent.test_summary_frame

        # Setting the back button's frame
        parent.back_frame = parent.test3_frame

        super.__init__(parent, master_frame, data_holder)

        # Entering the test name based on the test
        parent.ent_test.insert(0, "Bit Rate Test")

