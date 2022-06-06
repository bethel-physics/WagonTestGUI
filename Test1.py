import tkinter as tk
import ScanScene

# Creating class for the window
class Test1Scene(tk.Frame):
    def __init__(self, parent, master_window):
        self.master_window = master_window
        super().__init__(self.master_window, width=700, height=500, background='green')

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
        lbl_test1 = tk.Label(frm_window, text = "Current Test:")
        lbl_test1.pack(side = 'top', anchor = 'nw')

        # Create a entry for the test type
        ent_test1 = tk.Entry(frm_window)
        ent_test1.insert(0, "TEST #1")
        ent_test1.pack(side = 'top', anchor = 'nw')
        ent_test1.config(state = "disabled")

        # Create a label for confirming test
        lbl_confirm = tk.Label(frm_window, text = "Are you ready to begin the test?")
        lbl_confirm.pack(side = 'top', anchor = 'ne')

        # Create a button for confirming test
        btn_confirm = tk.Button(frm_window, text = "Confirm", relief = tk.RAISED, command = lambda:self.confirm_button_action(parent))
        btn_confirm.pack(side = 'top', anchor = 'ne')

        # Confirm button action takes the user to the test in progress scene
        def confirm_button_action(self, _parent):
            _parent.set_frame(_parent.in_progress_frame)

        # Create frame for logout button
        frm_logout = tk.Frame(self)
        frm_logout.grid(column = 2, row = 2)

        # Create a logout button
        btn_logout = tk.Button(frm_logout, text = "Logout", relief = tk.RAISED, command = lambda: self.logout_button_action(parent))
        btn_logout.pack()

        # Logout button action takes the user back to the login screen
        def logout_button_action(self, _parent):
            _parent.set_frame(_parent.login_frame)

        # Create a frame for the back button
        frm_back = tk.Frame(self)
        frm_back.grid(column = 2, row = 0)

        # Create a back button
        btn_back = tk.Button(frm_back, text = "Back", relief = tk.RAISED, command = lambda: self.back_button_action(parent))
        btn_back.pack()

        # Back button action takes the user back to the scanning device
        def back_button_action(self, _parent):
            _parent.set_frame(_parent.scan_frame)


        self.grid_propagate(0)