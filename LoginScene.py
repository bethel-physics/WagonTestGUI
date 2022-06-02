# importing necessary modules
import tkinter as tk

# creating the login frame
class LoginScene(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        

        # Creating the title for the window
        label = tk.Label(self, text="Home Page", font=('Times', '20'))
        label.pack(pady=0,padx=0)

        # Creating a list of users for dropdown menu
        User_List = [
            "User 1",
            "User 2",
            "User 3"
        ]

        # # Creating intial value in dropdown menu
        # user_selected = tk.StringVar(master)
        # user_selected.set("") # default value is empty

        # opt_user_dropdown = tk.OptionMenu(master, user_selected, *User_List)
        # opt_user_dropdown.pack()