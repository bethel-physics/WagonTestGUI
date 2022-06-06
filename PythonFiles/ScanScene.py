# importing necessary modules
import tkinter as tk
from tkinter import *
from turtle import back
from PIL import ImageTk as iTK
from PIL import Image
import os
 

# creating the login frame
class ScanScene(tk.Frame):
    
    def __init__(self, parent, master_window):

        self.master_window = master_window
        
        super().__init__(self.master_window)

        self.config(height=500, width=700, background='blue')
        

        # Create a photoimage object of the QR Code
        QR_image = Image.open("./PythonFiles/QRimage.png")
        QR_PhotoImage = iTK.PhotoImage(QR_image)
        QR_label = tk.Label(self, image=QR_PhotoImage)
        QR_label.image = QR_PhotoImage

        # the place() method adds it to the Frame
        QR_label.grid(column=0, row=1)

        Scan_Board_Prompt_Frame = Frame(self, padx=10, pady=10)
        # creates a Label Variable, different customization options
        scan_prompt_label = tk.Label(
            master= Scan_Board_Prompt_Frame,
            text = "Scan the QR Code on the board...",
            foreground= "white",
            background= "#0a0a0a"
        )
        scan_text_field = tk.Entry(Scan_Board_Prompt_Frame)
        submit_button = tk.Button(Scan_Board_Prompt_Frame, text="Submit", command= lambda:  self.submit_button_action(parent))

        # the pack() method adds it to the window
        scan_prompt_label.pack()
        scan_text_field.pack()
        submit_button.pack()
        Scan_Board_Prompt_Frame.grid(row=1,column=1)
        self.grid_propagate(0)


    def submit_button_action(self, _parent):
        _parent.set_frame(_parent.test1_frame)


        