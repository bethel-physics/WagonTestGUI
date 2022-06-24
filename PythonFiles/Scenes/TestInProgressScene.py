#################################################################################

# Imports all the necessary modules
import queue
import tkinter as tk
from tkinter import ttk
from xml.dom.expatbuilder import parseFragmentString
import sys, time
import multiprocessing as mp



#################################################################################


# Creating the frame itself
class TestInProgressScene(tk.Frame):
    def __init__(self, parent, master_frame, data_holder, queue):
        
        super().__init__(master_frame, width = 850, height = 500)


        self.queue = queue
        self.data_holder = data_holder
        self.is_current_scene = False


    ##################################################

    # A function for the stop button
    def btn_stop_action(self, _parent):

        _parent.go_to_next_test()

        
        # Destroys the console window
        self.console_destroy()
        
    #################################################    

    # Goes to the next scene after the progress scene is complete
    def go_to_next_frame(self, _parent):
        _parent.go_to_next_test()

    #################################################    

    # Used to bring the user back to the test that just failed
    def go_to_previous_frame(self, _parent, previous_frame):
        self.previous_frame = previous_frame
        _parent.set_frame(previous_frame)


    # Used to initialize the frame that is on the main window
    # next_frame is used to progress to the next scene and is passed in from GUIWindow
    def initialize_scene(self, parent, master_frame):

        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side = "right", fill = 'y')


        # Placing an entry box in the frm_console
        global ent_console
        ent_console = tk.Text(
            self, 
            bg = 'black', 
            fg = 'white', 
            height= 15,
            width= 400,
            font = ('Arial', 15),
            yscrollcommand = scrollbar.set
            )
        

        # Adding scrollbar functionality
        scrollbar.config(command = ent_console.yview)


        # Creating the main title in the frame
        lbl_title = tk.Label(self, 
            text = "Test in progress. Please wait.", 
            font = ('Arial', 20)
            )
        lbl_title.pack(padx = 0, pady = 50)

        # Create a progress bar that does not track progress but adds motion to the window
        prgbar_progress = ttk.Progressbar(
            self, 
            orient = 'horizontal',
            mode = 'indeterminate', length = 350)
        prgbar_progress.pack(padx = 50)
        prgbar_progress.start()

        # A Button To Stop the Progress Bar and Progress Forward (Temporary until we link to actual progress)
        btn_stop = ttk.Button(
            self, 
            text='Stop', 
            command= lambda: self.btn_stop_action(parent))
        btn_stop.pack(padx = 0, pady = 25)

        ent_console.pack(anchor = 'center')



        # Forces the frame to stay the size of the master_frame
        self.pack_propagate(0)

    # A function for the stop button
    def btn_stop_action(self, _parent):

        _parent.go_to_next_test()

        
        # Destroys the console window
        self.console_destroy()
        
        


    # Goes to the next scene after the progress scene is complete
    def go_to_next_frame(self, _parent):
        _parent.go_to_next_test()

        

    # Used to bring the user back to the test that just failed
    def go_to_previous_frame(self, _parent, previous_frame):
        self.previous_frame = previous_frame
        _parent.set_frame(previous_frame)

    

    # Dummy Script Function
    def run_test_gen_resist(self):
        print ("General Resistance Test Run")

    #################################################

    # Dummy Script Function
    def run_test_id_resistor(self):
        print ("ID Resistor Test Run")

    #################################################

    # Dummy Script Function
    def run_test_i2c_comm(self):
        print("I2C Comm. Test Run") 

    #################################################

    # Dummy Script Function
    def run_test_bit_rate(self):
         print("Bit Rate Test Run")

    #################################################

    def begin_update(self, _parent, master_window, conn, queue):
        print("started update loop")
        # try:
        while 1>0:
                # try:
            master_window.update()
            if not queue.empty():    
                print("Waiting for queue objects...")
                text = queue.get()
                print(text)
                ent_console.insert(tk.END, text)
                ent_console.insert(tk.END, "\n")
                self.entry.see('end')

                if text == "JSON Received.":
                    break
                
            else:
                time.sleep(.01)
                