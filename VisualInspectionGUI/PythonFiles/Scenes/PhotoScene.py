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


        self.master_frame = master_frame

        self.data_holder = data_holder
        self.is_current_scene = False
        
        self.EXIT_CODE = 0
        # Runs the initilize_GUI function, which actually creates the frame
        # params are the same as defined above
        self.initialize_GUI(parent, master_frame)
        

       # Creates the GUI itself
    def initialize_GUI(self, parent, master_frame):
        
        
        super().__init__(self.master_frame, width = 850, height = 500)

        logging.info("PhotoScene: Frame has been created.")
        # Create a photoimage object of the Engine
        Engine_image = Image.open("{}/Images/EnginePhoto.png".format(PythonFiles.__path__[0]))
        Engine_image = Engine_image.resize((400, 300), Image.ANTIALIAS)
        Engine_PhotoImage = iTK.PhotoImage(Engine_image)
        Engine_label = tk.Label(self, image=Engine_PhotoImage)
        Engine_label.image = Engine_PhotoImage

        # the .grid() adds it to the Frame
        Engine_label.grid(column=1, row = 1)

        Scan_Board_Prompt_Frame = Frame(self)
        Scan_Board_Prompt_Frame.grid(column=1, row = 0)

        Blank_Frame = Frame(self)
        Blank_Frame.grid(column = 0, row = 1, padx = 100, pady = 10)

        # creates a Label Variable, different customization options
        lbl_scan = tk.Label(
            master= Scan_Board_Prompt_Frame,
            text = "Insert Photo of Board",
            font = ('Arial', 18)
        )
        lbl_scan.pack(padx = 50, pady = 50)

        # Create a label to label the entry box
        lbl_correct = tk.Label(
            Scan_Board_Prompt_Frame,
            text = "Does this look correct?",
            font = ('Arial', 16)
        )
        lbl_correct.pack(padx = 20)

        # Entry for the serial number to be displayed. Upon Scan, update and disable?
        global ent_correct
        
        # Creating intial value in entry box
        user_text = tk.StringVar(self)
        
        # Creates an entry box
        #self.ent_correct = tk.Entry(
        #    Scan_Board_Prompt_Frame,
        #    font = ('Arial', 16),
        #    textvariable= user_text, 
        #    )
        #self.ent_correct.pack(padx = 50)

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
        self.btn_submit.pack(padx = 8, pady = 5)

        # Creating frame for logout button
        frm_logout = tk.Frame(self)
        frm_logout.grid(column = 2, row = 1, sticky= 'se')


        # Creating the logout button
        btn_logout = tk.Button(
            frm_logout,
            relief = tk.RAISED,
            text = "Logout",
            command = lambda: self.btn_logout_action(parent)
        )
        btn_logout.pack(anchor = 'se', padx = 10, pady = 20)

        # Creating the help button
        btn_help = tk.Button(
            frm_logout,
            relief = tk.RAISED,
            text = "Help",
            command = lambda: self.help_action(parent)
        )
        btn_help.pack(anchor = 's', padx = 10, pady = 20)


        # Locks frame size to the master_frame size
        self.grid_propagate(0)

    #################################################

    # Function for the submit button
    def btn_submit_action(self, _parent):
        
        #TODO Do something with the dataholder here with the photo
        
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
        
    def remove_widgets(self, parent):
        for widget in self.winfo_children():
            widget.destroy()


    def kill_processes(self):
        return
