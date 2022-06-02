# Importing all Modules
import tkinter as tk
from LoginScene import LoginScene
from ScanScene import ScanScene

# Create a class for creating the basic GUI Window
class GUIWindow():

    # Used for destroying windows
    # Use self.clear_window(window_name)
    def clear_window(self, window):
        for widget in window.winfo_children():
            widget.destroy()

    def __init__(self) -> None:       
               
        # Create the window named "master_window"
        master_window = tk.Tk()
        master_window.title("Bethel Interns' Window")
        master_window.geometry("700x500")

        login_frame = LoginScene(self, master_window)
        login_frame.pack()
        # scan_frame = ScanScene(self, master_window)
        # list_of_frames = [login_frame, scan_frame]
        # self.clear_window(master_window)
        scan_frame = ScanScene(self, master_window)
        scan_frame.pack()

        master_window.mainloop()