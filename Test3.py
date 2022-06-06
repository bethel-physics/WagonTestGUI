import tkinter as tk
import ScanScene

# Creating class for the window
class Test3Scene(tk.Frame):
    def __init__(self, parent, master_window):
        
        super().__init__(master_window)

        self.config(height=500, width=700, background='yellow')

        # Create a centralized window for information
        frm_window = tk.Frame(self, width = 300, height = 300)
        frm_window.grid(column=1, row=1, padx = 50, pady =50)

        # Create a label for the serial number box
        lbl_snum = tk.Label(frm_window, text = "  Serial Number:  ")
        lbl_snum.pack(side = 'top', anchor = 'nw')

        # Create a entry for the serial number box
        ent_snum = tk.Entry(frm_window)
        ent_snum.insert(0, "0000111122223333") # Need a way to fetch the serial number, make this uneditable?
        ent_snum.pack(side = 'top', anchor = 'nw')
        ent_snum.config(state = "disabled")

        # Create a label for the test about to be run
        lbl_test3 = tk.Label(frm_window, text = "Current Test:")
        lbl_test3.pack(side = 'top', anchor = 'nw')

        # Create a entry for the test type
        ent_test3 = tk.Entry(frm_window)
        ent_test3.insert(0, "TEST #3")
        ent_test3.pack(side = 'top', anchor = 'nw')
        ent_test3.config(state = "disabled")

        # Create a label for confirming test
        # Need to add command function
        lbl_confirm = tk.Label(frm_window, text = "Are you ready to begin the test?")
        lbl_confirm.pack(side = 'top', anchor = 'ne')

        # Create a button for confirming test
        btn_confirm = tk.Button(frm_window, text = "Confirm", command= lambda: self.confirm_button_action(parent))
        btn_confirm.pack(side = 'top', anchor = 'ne')
        btn_confirm.config(relief = tk.RAISED)

        # Create frame for logout button
        frm_logout = tk.Frame(self)
        frm_logout.grid(column = 2, row = 2)

        # Create a logout button
        # Need to add command function
        btn_logout = tk.Button(frm_logout, text = "Logout", command= lambda: self.logout_button_action(parent))
        btn_logout.pack()
        btn_logout.config(relief = tk.RAISED)

        # Create a frame for the back button
        frm_back = tk.Frame(self)
        frm_back.grid(column = 2, row = 0)

        # Create a back button
        # Need to add command function
        btn_back = tk.Button(frm_back, text = "Back", command= lambda: self.back_button_action(parent))
        btn_back.pack()
        btn_logout.config(relief = tk.RAISED)


        self.grid_propagate(0)



    # Back button action takes the user back to the scanning device
    def back_button_action(self, _parent):
        _parent.set_frame(_parent.test2_frame)

        
    # Confirm button action takes the user to the test in progress scene
    def confirm_button_action(self, _parent):
        _parent.set_frame(_parent.test3_in_progress)

    # Logout button that takes the user back to the login scene
    def logout_button_action(self, _parent):
        _parent.set_frame(_parent.login_frame)