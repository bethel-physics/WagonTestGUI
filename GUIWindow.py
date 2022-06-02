# Importing all Modules
import tkinter as tk

# Create a class for creating the basic GUI Window
class GUIWindow():

    def show_frame(self, _frame):
        self.show_frame(_frame)


    login_frame = LoginScene()
    list_of_frames = [login_frame]

    # Create the window named "master_window"
    master_window = tk.Tk()
    master_window.title("Bethel Interns' Window")

    show_frame(login_frame)





    master_window.mainloop()