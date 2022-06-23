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

        # # thread-safe data storage
        # self.the_queue = queue.Queue()

        # # create the data variable
        # self.data = []
        # for key in range(1):
        #     self.data.append(tk.StringVar())
        #     self.data[key].set('<default>')

        # # Button to start the asyncio tasks
        # new_button = tk.Button(
        #         master= self,
        #         text='Start Asyncio Tasks',
        #         command=lambda: self.do_asyncio())
        # new_button.pack()
        
        # # Frames to display data from the asyncio tasks
        # for key in range(1):
        #     tk.Label(master=self, textvariable=self.data[key]).pack()
        self.queue = queue
        self.data_holder = data_holder
        self.is_current_scene = False
        # self.initialize_scene(parent, master_frame)


    #################################################

    # Used to initialize the frame that is on the main window
    # next_frame is used to progress to the next scene and is passed in from GUIWindow
    # 
# def initialize_scene(self, parent, master_frame):
    #     super().__init__(master_frame, width = 850, height = 500)


    #     # Creating the main title in the frame
    #     lbl_title = tk.Label(self, 
    #         text = "Test in progress. Please wait.", 
    #         font = ('Arial', 20)
    #         )
    #     lbl_title.pack(padx = 0, pady = 100)

    #     # Create a progress bar that does not track progress but adds motion to the window
    #     prgbar_progress = ttk.Progressbar(
    #         self, 
    #         orient = 'horizontal',
    #         mode = 'indeterminate', length = 350)
    #     prgbar_progress.pack(padx = 50)
    #     prgbar_progress.start()

    #     # A Button To Stop the Progress Bar and Progress Forward (Temporary until we link to actual progress)
    #     btn_stop = ttk.Button(
    #         self, 
    #         text='Stop', 
    #         command= lambda: self.btn_stop_action(parent))
    #     btn_stop.pack(padx = 0, pady = 100)

    #     # Forces the frame to stay the size of the master_frame
    #     self.pack_propagate(0)
    #################################################

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



    # Method that is run when the button is clicked
    def do_asyncio(self):
        # """
        #     Button-Event-Handler starting the asyncio part in a separate
        #     thread.
        # """
        # # create fancy thread object
        # # Parameters: the queue that is storing the "updates", the maximum amount of data that can go in
        # self.thread = AsyncioThread(self.the_queue, len(self.data))

        # #  timer to refresh the gui with data from the asyncio thread
        # self.after(1000, self.refresh_data)  # called only once!

        # # start the thread
        # self.thread.start()
        pass



    
    # Recursive Method
    # Refreshes the data that will be put on the tkinter window
    def refresh_data(self):
        """
        """
        # do nothing if the aysyncio thread is dead
        # and no more data in the queue
        # Breaking statement of recursive loop
        if not self.thread.is_alive() and self.the_queue.empty():
            return

        # refresh the GUI with new data from the queue
        while not self.the_queue.empty():
            data = self.the_queue.get()
            self.data[0].set(data)

            to_display = self.data[0].get()
            to_display = to_display[5: -2]
            
            if len(to_display) > 0:
                print(to_display)

        # print('RefreshData...')

        #  timer to refresh the gui with data from the asyncio thread
        self.after(1000, self.refresh_data)  # called only once!






    # A function to be called within GUIWindow to create the console output
    # when the frame is being brought to the top
    def initialize_console(self, conn):

        global console_popup

        # Creating a popup window for the console output
        console_popup = tk.Tk()
        console_popup.geometry("300x300+975+200")
        console_popup.title("Console Output Window")
        # console_popup.wm_attributes('-toolwindow', 'True')

        # Used to tell the console window that its 
        # exit window button is being given a new function
        # console_popup.protocol('WM_DELETE_WINDOW', self.fake_destroy)

        # Creating a Frame For Console Output
        frm_console = tk.Frame(console_popup, width = 300, height = 300, bg = 'black')
        frm_console.pack_propagate(0)
        frm_console.pack()

        # Giving the console output a scroll bar
        scrollbar = tk.Scrollbar(frm_console)
        scrollbar.pack(side = "right", fill = 'y')


        # Placing an entry box in the frm_console
        global ent_console
        ent_console = tk.Text(
            frm_console, 
            bg = 'black', 
            fg = 'white', 
            font = ('Arial', 8),
            yscrollcommand = scrollbar.set
            )
        ent_console.pack(anchor = 'center', fill = tk.BOTH, expand = 1)

        # Adding scrollbar functionality
        scrollbar.config(command = ent_console.yview)

        try:
            while 1>0:
                if conn.recv is not None:
                    ent_console.insert(tk.END, conn.recv())
                else:
                    time.sleep(1)
        except:
            print("Your stupid code didn't work.")
        # # Instantiates the console writing class
        # console = ConsoleOutput(ent_console)

        # # replace sys.stdout with our new console object
        # sys.stdout = console

    #################################################

    # A pass function that the console window is being redirected to so its exit button
    # does not function
    # def fake_destroy(self):
    #     pass
    
    #################################################

    # A Function to be called when the console should be destroyed
    # def console_destroy(self):
        
    #     # Redirects any console readouts back to the actual console rather than the fake object
    #     sys.stdout = sys.__stdout__
        
    #     # Destroys the console output window
    #     console_popup.destroy()


    # Used to initialize the frame that is on the main window
    # next_frame is used to progress to the next scene and is passed in from GUIWindow
    def initialize_scene(self, parent, master_frame):

        # console_frm = tk.Frame(master_frame, width=850, height= 500, bg = 'black')
        # console_frm.grid(column = 1, row = 0, columnspan = 4)
        # console_frm.grid_propagate(0)

        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side = "right", fill = 'y')


        # Placing an entry box in the frm_console
        global ent_console
        ent_console = tk.Text(
            self, 
            bg = 'black', 
            fg = 'white', 
            font = ('Courier', 15),
            yscrollcommand = scrollbar.set
            )
        ent_console.pack(anchor = 'center', fill = tk.BOTH, expand = 1)

        # Adding scrollbar functionality
        scrollbar.config(command = ent_console.yview)
########################################################################################
        # # Creating the main title in the frame
        # lbl_title = tk.Label(self, 
        #     text = "Test in progress. Please wait.", 
        #     font = ('Arial', 20)
        #     )
        # lbl_title.pack(padx = 0, pady = 100)

        # # Create a progress bar that does not track progress but adds motion to the window
        # prgbar_progress = ttk.Progressbar(
        #     self, 
        #     orient = 'horizontal',
        #     mode = 'indeterminate', length = 350)
        # prgbar_progress.pack(padx = 50)
        # prgbar_progress.start()

        # # A Button To Stop the Progress Bar and Progress Forward (Temporary until we link to actual progress)
        # btn_stop = ttk.Button(
        #     self, 
        #     text='Stop', 
        #     command= lambda: self.btn_stop_action(parent))
        # btn_stop.pack(padx = 0, pady = 100)
##################################################################################################
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

    def begin_update(self, master_window, conn, queue):
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
                time.sleep(1)
            else:
                time.sleep(.01)
            
                # except:
                    # time.sleep(1)
        # except:
            # print("Your stupid code didn't work.")