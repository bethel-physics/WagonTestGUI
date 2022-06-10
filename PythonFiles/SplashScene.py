# Importing necessary modules
import tkinter as tk
import tkinter.font as font
from PIL import ImageTk as iTK
from PIL import Image
import time
import threading



class SplashScene(tk.Frame):
    def __init__(self, parent, master_window):
        self.initialize_GUI(parent, master_window)

    def initialize_GUI(self, parent, master_window):
        super().__init__(master_window, width = 850, height = 500)

        # Creating Bethel Logo
        img_bethel_logo = Image.open("./PythonFiles/Images/Bethel_Logo.png")
        img_bethel_logo = img_bethel_logo.resize((250,100), Image.ANTIALIAS)
        phimg_bethel_logo = iTK.PhotoImage(img_bethel_logo)
        lbl_bethel_logo = tk.Label(self, image=phimg_bethel_logo, width=250, height=100)
        lbl_bethel_logo.image = phimg_bethel_logo

        lbl_bethel_logo.grid(row=0, column= 0, padx = 50, pady = 100)

        # Creating UMN Logo
        img_umn_logo = Image.open("./PythonFiles/Images/UMN_Logo.png")
        img_umn_logo = img_umn_logo.resize((250,100), Image.ANTIALIAS)
        phimg_umn_logo = iTK.PhotoImage(img_umn_logo)
        lbl_umn_logo = tk.Label(self, image=phimg_umn_logo, width=250, height=100)
        lbl_umn_logo.image = phimg_umn_logo

        lbl_umn_logo.grid(row = 0 , column = 2, padx = 50, pady = 100)

        # Creating label for names
        lbl_names = tk.Label(
            self,
            text = ' Created by:\n \n Andrew Kirzeder \n & \n Garrett Schindler',
            font = ('Arial', 15)
        )
        lbl_names.grid(row = 1, column = 1)

        self.grid_propagate(0)


        # Automatically passing on to login screen
    def thread_auto_set_frame(self, _parent):
        self.thread_auto_set = threading.Thread(target=self.auto_set_frame(_parent))
        self.thread_auto_set.daemon = True
        self.thread_auto_set.start()
    
    def auto_set_frame(self, __parent):
        for i in range(3):
            time.sleep(1)
            print(i + 1)
        time.sleep(0.5)
        __parent.set_frame(__parent.login_frame)