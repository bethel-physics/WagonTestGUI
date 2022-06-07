# importing necessary modules
import threading
import time
import tkinter as tk
from tkinter import *
from turtle import back
from PIL import ImageTk as iTK
from PIL import Image
import os
import tkinter.font as font
 
# Creating variable for testing QR Code entry
QRcode = "1090201033667425"


# creating the login frame
class ScanScene(tk.Frame):
    
    def __init__(self, parent, master_window):
        self.GUI_thread = threading.Thread(target=self.initialize_GUI(parent, master_window), args=(10,))
        


    def start_QR_thread(self):
        self.QR_thread.start()

    def scan_QR_code(self):
        print("Begin to scan")
        self.QR_thread = threading.Thread(target=self.scan_QR_code(), args=(10,))
        time.sleep(5)
        self.insert_QR_ID()
        print("Scan Complete")

    # Updates the QR ID in the task 
    def insert_QR_ID(self):
        ent_serial.delete(0, END)
        ent_serial.insert(0, QRcode)
        ent_serial.config(state = 'disabled')

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
        ent_serial = tk.Entry(
            Scan_Board_Prompt_Frame,
            font = ('Arial', 16)
            )
        ent_serial.pack(padx = 50, pady = 50)

        # Submit button
        btn_submit = tk.Button(
            Scan_Board_Prompt_Frame,
            text="Submit",
            relief = tk.RAISED,
            command= lambda:  self.submit_button_action(parent)
            )
        btn_submit.pack()

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
        
        
        