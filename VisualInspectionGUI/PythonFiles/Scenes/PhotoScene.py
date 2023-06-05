#################################################################################

# importing necessary modules
import multiprocessing as mp
import logging, time
import tkinter as tk
import sys, time
from tkinter import *
from turtle import back
from PIL import ImageTk as iTK
from PIL import Image
import PythonFiles
import os
 

#################################################################################


logging.getLogger('PIL').setLevel(logging.WARNING)
logger = logging.getLogger('HGCAL_GUI')

FORMAT = '%(asctime)s|%(levelname)s|%(message)s|'
logging.basicConfig(filename="/home/{}/GUILogs/visual_gui.log".format(os.getlogin()), filemode = 'a', format=FORMAT, level=logging.DEBUG)


# creating the Photo Frame's class (called PhotoScene) to be instantiated in the GUIWindow
# instantiated as scan_frame by GUIWindow
# @param parent -> passes in GUIWindow as the parent.
# @param master_frame -> passes master_frame as the container for everything in the class.
# @param data_holder -> passes data_holder into the class so the data_holder functions can
#       be accessed within the class.
class PhotoScene(tk.Frame):
    
    #################################################

    # Runs upon creation
    def __init__(self, parent, master_frame, data_holder):
        self.data_holder = data_holder
        self.is_current_scene = False
        
        self.EXIT_CODE = 0
        # Runs the initilize_GUI function, which actually creates the frame
        # params are the same as defined above
        self.initialize_GUI(parent, master_frame)
        

       # Creates the GUI itself
    def initialize_GUI(self, parent, master_frame):
        
        self.master_frame = master_frame
        
        super().__init__(self.master_frame, width = 850, height = 500)

        logging.info("PhotoScene: Frame has been created.")
        # Create a photoimage object of the QR Code
        Engine_image = Image.open("{}/Images/EnginePhoto.png".format(PythonFiles.__path__[0]))
        Engine_PhotoImage = iTK.PhotoImage(Engine_image)
        Engine_label = tk.Label(self, image=Engine_PhotoImage)
        Engine_label.image = Engine_PhotoImage

        # the .grid() adds it to the Frame
        Engine_label.grid(column=1, row = 0)

        Scan_Board_Prompt_Frame = Frame(self)
        Scan_Board_Prompt_Frame.grid(column=0, row = 0)

        # creates a Label Variable, different customization options
        lbl_scan = tk.Label(
            master= Scan_Board_Prompt_Frame,
            text = "Insert Photo of Board",
            font = ('Arial', 18)
        )
        lbl_scan.pack(padx = 50, pady = 50)

        # Create a label to label the entry box
        lbl_snum = tk.Label(
            Scan_Board_Prompt_Frame,
            text = "Serial Number:",
            font = ('Arial', 16)
        )
        lbl_snum.pack(padx = 20)

        # Entry for the serial number to be displayed. Upon Scan, update and disable?
        global ent_snum
        
        # Creating intial value in entry box
        user_text = tk.StringVar(self)
        
        # Creates an entry box
        #self.ent_snum = tk.Entry(
        #    Scan_Board_Prompt_Frame,
        #    font = ('Arial', 16),
        #    textvariable= user_text, 
        #    )
        #self.ent_snum.pack(padx = 50)

        # Traces an input to show the submit button once text is inside the entry box
        #user_text.trace(
        #    "w", 
        #    lambda name, 
        #    index, 
        #    mode, 
        #    sv=user_text: self.show_submit_button()
        #    )

        # Rescan button creation
        #self.btn_rescan = tk.Button(
        #    Scan_Board_Prompt_Frame,
        #    text="Rescan",
        #    padx = 20,
        #    pady =10,
        #    relief = tk.RAISED,
        #    command = lambda:  self.scan_QR_code(self.master_window)
        #    )
        #self.btn_rescan.pack(pady=30)

        # Submit button creation
        self.btn_submit = tk.Button(
            Scan_Board_Prompt_Frame,
            text="Submit",
            padx = 20,
            pady = 10,
            relief = tk.RAISED,
            command= lambda:  self.btn_submit_action(parent)
            )
        self.btn_submit.pack()

        # Creating frame for logout button
        frm_logout = tk.Frame(self)
        frm_logout.grid(column = 1, row = 1, sticky= 'se')

        # Creating the logout button
        btn_logout = tk.Button(
            frm_logout,
            relief = tk.RAISED,
            text = "Logout",
            command = lambda: self.btn_logout_action(parent)
        )
        btn_logout.pack(anchor = 'se', padx = 0, pady = 80)
        # Locks frame size to the master_frame size
        self.grid_propagate(0)

    #################################################

    # Function for the submit button
    def btn_submit_action(self, _parent):
        self.data_holder.set_serial_ID(self.ent_snum.get())
        self.data_holder.check_if_new_board()
        _parent.set_frame_inspection_frame()


    #################################################

    # Function for the log out button
    def btn_logout_action(self, _parent):

         # Send user back to login frame
        _parent.set_frame_login_frame() 

    #################################################

    # Function to activate the submit button
    def show_submit_button(self):
        self.btn_submit["state"] = "active"

    #################################################

    # Function to disable to the submit button
    def hide_submit_button(self):
        self.btn_submit["state"] = "disabled"

    #################################################

    # Function to activate the rescan button
    def show_rescan_button(self):
        self.btn_rescan["state"] = "active"

    #################################################

    # Function to disable to the rescan button
    def hide_rescan_button(self):
        self.btn_rescan["state"] = "disabled"

    #################################################
        
    def update_frame(self, parent):
        return



    def kill_processes(self):
        logging.info("ScanScene: Terminating scanner proceses.")
        try:
            self.scanner.kill()
            self.listener.terminate()
            self.EXIT_CODE = 1
        except:
            logging.info("ScanScene: Processes could not be terminated.")
