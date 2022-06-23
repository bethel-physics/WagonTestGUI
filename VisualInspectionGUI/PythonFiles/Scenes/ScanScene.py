#################################################################################

# importing necessary modules
import threading, time
import tkinter as tk
from tkinter import *
from turtle import back
from PIL import ImageTk as iTK
from PIL import Image
import tkinter.font as font
 
#################################################################################


# Creating variable for testing QR Code entry
QRcode = "1090201033667425"


# creating the Scan Frame's class (called ScanScene) to be instantiated in the GUIWindow
# instantiated as scan_frame by GUIWindow
# @param parent -> passes in GUIWindow as the parent.
# @param master_frame -> passes master_frame as the container for everything in the class.
# @param data_holder -> passes data_holder into the class so the data_holder functions can
#       be accessed within the class.
class ScanScene(tk.Frame):
    
    #################################################

    # Runs upon creation
    def __init__(self, parent, master_frame, data_holder):
        self.data_holder = data_holder
        self.is_current_scene = False
        
        # Runs the initilize_GUI function, which actually creates the frame
        # params are the same as defined above
        self.initialize_GUI(parent, master_frame)


    # Creates a thread for the scanning of a barcode
    # Needs to be updated to run the read_barcode function in the original GUI
    def scan_QR_code(self):
        print("Begin to scan")
        ent_snum.config(state = 'normal')
        self.QR_thread = threading.Thread(target=self.insert_QR_ID)
        self.QR_thread.daemon = True
        self.QR_thread.start()

    # Updates the QR ID in the task
    # Place holder function to insert the QRcode into the textbox 
    def insert_QR_ID(self):

        # Clears the textbox of anything possibly in the box
        ent_snum.delete(0, END)

        # Disables the rescan button until after the scanning is complete
        self.hide_rescan_button()

        # Runs the hide_submit_button function and sets a default value to the QR_value
        self.hide_submit_button()
        self.scanned_QR_value = 000

        # Delay to simulate scanning a QRcode
        for i in range(1):
            time.sleep(1)
            print(i + 1)
        time.sleep(0.5)
        print("Finished Scan")
        ent_snum.insert(0, QRcode)
        ent_snum.config(state = 'disabled')

        # Restores access to the rescan button
        self.show_rescan_button()

        
        # Sets the scanned_QR_value to 0 when the function is not in use
        if (not self.is_current_scene):
            self.scanned_QR_value = 0
        else:
            self.scanned_QR_value = QRcode
            self.data_holder.current_serial_ID = self.scanned_QR_value

        self.data_holder.print()


    # Creates the GUI itself
    def initialize_GUI(self, parent, master_frame):
        
        self.master_frame = master_frame
        
        super().__init__(self.master_frame, width = 850, height = 500)

        # Create a photoimage object of the QR Code
        QR_image = Image.open("./PythonFiles/Images/QRimage.png")
        QR_PhotoImage = iTK.PhotoImage(QR_image)
        QR_label = tk.Label(self, image=QR_PhotoImage)
        QR_label.image = QR_PhotoImage

        # the .grid() adds it to the Frame
        QR_label.grid(column=1, row = 0)

        Scan_Board_Prompt_Frame = Frame(self,)
        Scan_Board_Prompt_Frame.grid(column=0, row = 0)

        # creates a Label Variable, different customization options
        lbl_scan = tk.Label(
            master= Scan_Board_Prompt_Frame,
            text = "Scan the QR Code on the Board",
            font = ('Arial', 18)
        )
        lbl_scan.pack(padx = 50, pady = 50)

        # Create a label to label the entry box
        lbl_snum = tk.Label(
            Scan_Board_Prompt_Frame,
            text = "Serial Number:",
            font = ('Arial', 16)
        )
        lbl_snum.pack()

        # Entry for the serial number to be displayed. Upon Scan, update and disable?
        global ent_snum
        
        # Creating intial value in entry box
        user_text = tk.StringVar(self)
        
        # Creates an entry box
        ent_snum = tk.Entry(
            Scan_Board_Prompt_Frame,
            font = ('Arial', 16),
            textvariable= user_text, 
            )
        ent_snum.pack(padx = 50)

        # Traces an input to show the submit button once text is inside the entry box
        user_text.trace(
            "w", 
            lambda name, 
            index, 
            mode, 
            sv=user_text: self.show_submit_button()
            )

        # Rescan button creation
        self.btn_rescan = tk.Button(
            Scan_Board_Prompt_Frame,
            text="Rescan",
            padx = 50,
            pady =10,
            relief = tk.RAISED,
            command = lambda:  self.scan_QR_code()
            )
        self.btn_rescan.pack(padx=10, pady=30)

        # Submit button creation
        self.btn_submit = tk.Button(
            Scan_Board_Prompt_Frame,
            text="Submit",
            padx = 50,
            pady = 10,
            relief = tk.RAISED,
            command= lambda:  self.btn_submit_action(parent)
            )
        self.btn_submit.pack(padx=10)

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
        btn_logout.pack(anchor = 'se', padx = 230, pady = 180)

        # Locks frame size to the master_frame size
        self.grid_propagate(0)

    #################################################

    # Function for the submit button
    def btn_submit_action(self, _parent):
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

    # Creates a thread for the scanning of a barcode
    # Needs to be updated to run the read_barcode function in the original GUI
    def scan_QR_code(self):
        print("Begin to scan")
        ent_snum.config(state = 'normal')
        self.QR_thread = threading.Thread(target=self.insert_QR_ID)
        self.QR_thread.daemon = True
        self.QR_thread.start()

    #################################################

    # Updates the QR ID in the task
    # Place holder function to insert the QRcode into the textbox 
    def insert_QR_ID(self):

        # Clears the textbox of anything possibly in the box
        ent_snum.delete(0, END)

        # Disables the rescan button until after the scanning is complete
        self.hide_rescan_button()

        # Runs the hide_submit_button function and sets a default value to the QR_value
        self.hide_submit_button()
        self.scanned_QR_value = 000

        # Delay to simulate scanning a QRcode
        
        time.sleep(1)
        print(1)
        time.sleep(0.5)
        print("Finished Scan")
        ent_snum.insert(0, QRcode)
        ent_snum.config(state = 'disabled')

        # Restores access to the rescan button
        self.show_rescan_button()

        
        # Sets the scanned_QR_value to 0 when the function is not in use
        if (not self.is_current_scene):
            self.scanned_QR_value = 0
        else:
            self.scanned_QR_value = QRcode
            self.data_holder.current_serial_ID = self.scanned_QR_value

        self.data_holder.print()

        #################################################
    
        
#################################################################################