import tkinter as tk
import tkinter.font as font

# Creating class for the window
class Test3Scene(tk.Frame):
    def __init__(self, parent, master_window):     
        super().__init__(master_window, width=850, height = 500)

        # Create a centralized window for information
        frm_window = tk.Frame(self, width = 850, height = 500)
        frm_window.grid(column=1, row=1, padx = 235, pady = 125)

        # Create a label for the serial number box
        lbl_snum = tk.Label(frm_window, text = "Serial Number:  ", font = ('Arial', 15))
        lbl_snum.pack(side = 'top')

        # Create a entry for the serial number box
        ent_snum = tk.Entry(frm_window, font = ('Arial', 15))
        ent_snum.insert(0, "0000111122223333") # Need a way to fetch the serial number, make this uneditable?
        ent_snum.pack(side = 'top')
        ent_snum.config(state = "disabled")

        # Create a label for the test about to be run
        lbl_test3 = tk.Label(frm_window, text = "Current Test:", font = ('Arial', 15))
        lbl_test3.pack(side = 'top')

        # Create a entry for the test type
        ent_test3 = tk.Entry(frm_window, font = ('Arial', 15))
        ent_test3.insert(0, "TEST #3")
        ent_test3.pack(side = 'top')
        ent_test3.config(state = "disabled")

        # Create a label for confirming test
        # Need to add command function
        lbl_confirm = tk.Label(frm_window, text = "Are you ready to begin the test?", font = ('Arial', 15))
        lbl_confirm.pack(side = 'top')

        # Create a button for confirming test
        btn_confirm = tk.Button(
            frm_window, 
            relief = tk.RAISED, 
            text = "Confirm", 
            command= lambda: self.confirm_button_action(parent))
        btn_confirm.pack(side = 'top')
        btn_confirm['font'] = font.Font(family = 'Arial', size = 13)

        # Create frame for logout button
        frm_logout = tk.Frame(self)
        frm_logout.grid(column = 2, row = 2, sticky = 'ne')

        # Create a logout button
        # Need to add command function
        btn_logout = tk.Button(
            frm_logout, 
            relief = tk.RAISED, 
            text = "Logout", 
            command= lambda: self.logout_button_action(parent))
        btn_logout.pack(anchor = 'se')

        # Create a frame for the top right of frame
        frm_back = tk.Frame(self)
        frm_back.grid(column = 2, row = 0)

        # Create a back button
        btn_back = tk.Button(
            frm_back, 
            relief = tk.RAISED, 
            text = "Back", 
            command= lambda: self.back_button_action(parent))
        btn_back.pack(anchor = 'ne')

        # Create a rescan button
        btn_rescan = tk.Button(
            frm_back, 
            text = "Change Boards", 
            relief = tk.RAISED, 
            command = lambda: self.rescan_button_action(parent))
        btn_rescan.pack(anchor = 'ne')

        self.grid_propagate(0)
    
    # Rescan button takes the user back to scanning in a new board
    def rescan_button_action(self, _parent):
        _parent.set_frame(_parent.scan_frame)

    # Back button action takes the user back to the scanning device
    def back_button_action(self, _parent):
        _parent.set_frame(_parent.test2_frame)

        
    # Confirm button action takes the user to the test in progress scene
    def confirm_button_action(self, _parent):
        _parent.set_frame(_parent.test3_in_progress)

    # Logout button that takes the user back to the login scene
    def logout_button_action(self, _parent):
        _parent.set_frame(_parent.login_frame)