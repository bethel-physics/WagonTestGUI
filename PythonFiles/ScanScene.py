# importing necessary modules
import threading
import time
import tkinter as tk
from tkinter import *
from turtle import back
from PIL import ImageTk as iTK
from PIL import Image
import tkinter.font as font
 
# Creating variable for testing QR Code entry
QRcode = "1090201033667425"


# creating the login frame
class ScanScene(tk.Frame):
    
    def __init__(self, parent, master_window, data_holder):
        self.data_holder = data_holder
        self.is_current_scene = False
        self.initialize_GUI(parent, master_window)

    def scan_QR_code(self):
        print("Begin to scan")
        ent_serial.config(state = 'normal')
        ent_serial.delete(0, END)
        self.QR_thread = threading.Thread(target=self.insert_QR_ID)
        self.QR_thread.daemon = True
        self.QR_thread.start()

    # Updates the QR ID in the task 
    def insert_QR_ID(self):
        ent_serial.delete(0, END)
        self.scanned_QR_value = 000
        for i in range(5):
            time.sleep(1)
            print(i + 1)
        time.sleep(0.5)
        print("Finished Scan")
        ent_serial.delete(0, END)
        ent_serial.insert(0, QRcode)
        ent_serial.config(state = 'readonly')

        

        if (not self.is_current_scene):
            self.scanned_QR_value = 0
        else:
            self.scanned_QR_value = QRcode
            self.data_holder.current_serial_ID = self.scanned_QR_value

        self.data_holder.print()


    def initialize_GUI(self, parent, master_window):
        
        self.master_window = master_window
        
        super().__init__(self.master_window, width = 850, height = 500)

        # Create a photoimage object of the QR Code
        QR_image = Image.open("./PythonFiles/QRimage.png")
        QR_PhotoImage = iTK.PhotoImage(QR_image)
        QR_label = tk.Label(self, image=QR_PhotoImage)
        QR_label.image = QR_PhotoImage

        # the place() method adds it to the Frame
        QR_label.grid(column=1, row = 0)

        Scan_Board_Prompt_Frame = Frame(self,)
        Scan_Board_Prompt_Frame.grid(column=0, row = 0)

        # creates a Label Variable, different customization options
        lbl_scan = tk.Label(
            master= Scan_Board_Prompt_Frame,
            text = "Scan the QR Code on the Board",
            font = ('Arial', 18)
        )
        lbl_scan.pack(padx = 50)

        # Entry for the serial number to be displayed. Upon Scan, update and disable?
        global ent_serial
        
        # Creating intial value in dropdown menu
        user_text = tk.StringVar(self)
        
        ent_serial = tk.Entry(
            Scan_Board_Prompt_Frame,
            font = ('Arial', 16),
            textvariable= user_text, 
            )
        ent_serial.pack(padx = 50, pady = 50)

        user_text.trace("w", lambda name, index, mode, sv=user_text: self.show_submit_button())

        # Submit button
        rescan_button = tk.Button(
            Scan_Board_Prompt_Frame,
            text="Rescan",
            padx = 50,
            pady =10,
            relief = tk.RAISED,
            command = lambda:  self.scan_QR_code()
            )
        rescan_button.pack(padx=10, pady=10)

        # Submit button
        self.btn_submit = tk.Button(
            Scan_Board_Prompt_Frame,
            text="Submit",
            padx = 50,
            pady = 10,
            relief = tk.RAISED,
            command= lambda:  self.submit_button_action(parent)
            )
        


        


        # Creating frame for logout button
        frm_logout = tk.Frame(self)
        frm_logout.grid(column = 1, row = 1, sticky= 'se')

        # Creating the logout button
        btn_logout = tk.Button(
            frm_logout,
            relief = tk.RAISED,
            text = "Logout",
            command = lambda: self.logout_button_action(parent)
        )
        btn_logout.pack(anchor = 'se', padx = 230, pady = 180)


        self.grid_propagate(0)


    def submit_button_action(self, _parent):
        _parent.set_frame(_parent.test1_frame)

    
    def logout_button_action(self, _parent):
        _parent.set_frame(_parent.login_frame)    

    def show_submit_button(self):
        print("SHowing SumBIt ButtON")
        self.btn_submit.pack(padx=10, pady=10)
        
        
        