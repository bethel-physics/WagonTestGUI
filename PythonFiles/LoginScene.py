# importing necessary modules
import tkinter as tk


# creating the login frame
class LoginScene(tk.Frame):
    def __init__(self, parent, master_window, data_holder):
        super().__init__(master_window, width=850, height=500)

        self.data_holder = data_holder


        # Creating the submit button
        # Need to add shift frame functionality later
        self.btn_submit = tk.Button(self, text="Submit", relief=tk.RAISED, command= lambda:  self.submit_button_action(parent))

        # Creating a list of users for dropdown menu
        # Eventually need to add a way for a database to have control over this array
        User_List = [
            "Bob Johnson",
            "Spencer Higgins",
            "Amanda Holmes"
        ]

        # Creating the title for the window
        lbl_title = tk.Label(self, text="Please Select Your Name", font=('Times', '24'))
        lbl_title.pack(pady=75)

        # Creating intial value in dropdown menu
        self.user_selected = tk.StringVar(self)
        self.user_selected.set("") # default value is empty

        # Creating the dropdown menu itself
        self.opt_user_dropdown = tk.OptionMenu(self, self.user_selected, *User_List)
        self.opt_user_dropdown.pack(pady=10)
        self.opt_user_dropdown.config(width = 20)

        
        self.user_selected.trace('w', lambda *args: self.show_submit_button())

        # # Creating logout button in grid
        # btn_logout = tk.Button(self, text = "Logout")
        # btn_logout.grid(column=1, row=1, sticky='se')

        self.pack_propagate(0)

    def submit_button_action(self, _parent):
        self.data_holder.user_ID = self.user_selected.get()
        current_scan_frame = _parent.get_scan_frame()
        _parent.set_frame(current_scan_frame)

    def show_submit_button(self):
        self.btn_submit.pack()

        