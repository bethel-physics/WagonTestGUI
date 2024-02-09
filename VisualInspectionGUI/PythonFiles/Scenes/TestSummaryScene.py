#################################################################################

import PythonFiles
import json, logging
import tkinter as tk
from PIL import ImageTk as iTK
from PIL import Image
from matplotlib.pyplot import table
from pyparsing import col
import PythonFiles
import os

#################################################################################

logging.getLogger('PIL').setLevel(logging.WARNING)


logger = logging.getLogger('HGCAL_GUI')
FORMAT = '%(asctime)s|%(levelname)s|%(message)s|'
logging.basicConfig(filename="/home/{}/GUILogs/gui.log".format(os.getlogin()), filemode = 'a', format=FORMAT, level=logging.DEBUG)

# Frame that shows all of the final test results
# @param parent -> References a GUIWindow object
# @param master_frame -> Tkinter object that the frame is going to be placed on
# @param data_holder -> DataHolder object that stores all relevant data

class TestSummaryScene(tk.Frame):

    #################################################

    def __init__(self, parent, master_frame, data_holder):
    
        # Call to the super class's constructor
        # Super class is the tk.Frame class
        super().__init__(master_frame, width = 1105, height = 850)

        logging.info("TestSummaryScene: Frame has been created.")

        self.data_holder = data_holder

        self.parent = parent
        # Setting weights of columns so the column 4 is half the size of columns 0-3
        #for i in range(self.data_holder.getNumTest()):
        #    self.columnconfigure(i, weight = 2)
        #self.columnconfigure(self.data_holder.getNumTest(), weight = 1)
        # Instantiates an updated table with the current data
        #self.create_updated_table(parent)


       
        self.create_frame(parent)        

        # Fits the frame to set size rather than interior widgets
        self.grid_propagate(0)

    #################################################
    
    def create_frame(self, parent):
        logging.debug("TestSummaryScene: Destroying old widgets on the TestSummaryScene.")
        print("TestSummaryScene: Destroying old widgets on the TestSummaryScene.")
        try:
            for widget in self.winfo_children():
                widget.destroy()
        except:
            logging.warning("TestSummaryScene: Widgets could not be found and/or destroyed (making room for new widgets.")
        else:
            logging.info("TestSummaryScene: Widgets destroyed successfully (making room for new widgets).")
        

        logging.debug("TestSummaryScene: Table is being created with the results.")
        print("\n\nTestSummaryScene: Table is being created with the results.")
        
        self.blank_frame = tk.Frame(self)
        self.blank_frame.grid(row = 0, column = 0, padx = 80, pady = 20)

        # Adds the title to the TestSummary Frame
        self.title = tk.Label(
                self, 
                fg='#0d0d0d', 
                text = "Visual Inspection Finished!",
                font=('Arial',18,'bold')
                )
        self.title.grid(row= 0, column= 1, pady = 20)


        # Tries to add all of the images to the final screen
        # TODO This is not scalable as it just appends the images horizontally
        for i, photo in enumerate(self.data_holder.get_photo_list()):
            
            try:
                # Create a photoimage object of the Board
                Board_image = Image.open("{}/Images/captured_image{}.png".format(PythonFiles.__path__[0], i))
                Board_image = Board_image.resize((222, 125), Image.LANCZOS)
                Board_PhotoImage = iTK.PhotoImage(Board_image)
                Board_label = tk.Label(self, image=Board_PhotoImage)
                Board_label.image = Board_PhotoImage

                # the .grid() adds it to the Frame
                Board_label.grid(column=0 + i, row = 1)

            except Exception as e:
                print("TestSummaryScene: Could not find captured_image.")
                logging.debug("TestSummaryScene: Could not find captured_image.")
                logging.debug("Exception: {}".format(e))
                next


        
        logging.debug("TestSummaryScene: Creating the board image.")
        


       # Adds Board Serial Number to the TestSummaryFrame
        self.lbl_snum = tk.Label(
                self, 
                text = "Serial Number: " + str(self.data_holder.data_dict['current_serial_ID']),
                font=('Arial', 14) 
                )
        self.lbl_snum.grid(column = 1, row = 2, pady = 10) 

        # Adds Tester Name to the TestSummary Frame
        self.lbl_tester = tk.Label(
                self, 
                text = "Tester: " + self.data_holder.data_dict['user_ID'],
                font=('Arial', 14) 
                )
        self.lbl_tester.grid(column = 1, row = 3, pady = 10)


        # Creates the "table" as a frame object
        self.frm_table = tk.Frame(self)
        self.frm_table.grid(row = 4, column= 1) 

        # Where to start putting the JSON information
        starting_row = 4
        # Number of keys the data_holder.inspection_data dictionary
        key_count = 0
        
        # Loop through all of the keys in the data_holder.inspection_data dictionary
        for index,box in enumerate(self.data_holder.all_checkboxes[0]):
            key_count = key_count + 1
            print("\nIndex: {}, Box: {}".format(index, box))
        
            key_label = tk.Label(
                    self.frm_table, 
                    text = box['text'], 
                    relief = 'ridge', 
                    width=40, 
                    height=1, 
                    font=('Arial', 11, "bold")
                    )
            key_label.grid(row=key_count , column=0, padx = 2)
             

            # Correctly displays the booleans
            # If not a string, show as a boolean true/false
            l_text = "UNDEFINED"
            if not isinstance(box['value'], str):
                if (box['value']):
                    l_text = "True"
                else:
                    l_text = "False"
            else:
                l_text = value['value']    

            result_label = tk.Label(
                    self.frm_table, 
                    text = l_text, 
                    relief = 'ridge', 
                    width=40, 
                    height=1, 
                    font=('Arial', 11, "bold")
                    )
            result_label.grid(row=key_count, column=1)
                    
        comment_index = 0
        comment_title_text = "Comments:"
        comment_title = tk.Label(
               self.frm_table, 
               text = comment_title_text, 
               relief = 'ridge', 
               width=40, 
               height=2, 
               font=('Arial', 11, "bold")
               )
        comment_title.grid(row=key_count + 1, column=0)

        comment_text = str(self.data_holder.get_comment_dict(comment_index))
        comment_label = tk.Label(
               self.frm_table, 
               text = comment_text, 
               relief = 'ridge', 
               width=40, 
               height=2, 
               font=('Arial', 11, "bold")
               )
        comment_label.grid(row=key_count + 1, column=1)

 
        # Creating frame for logout button
        frm_logout = tk.Frame(self)
        frm_logout.grid(column = 4, row = starting_row, sticky= 'se')
        

        # Creating the next board button
        next_board_button = tk.Button(
            frm_logout,
            relief = tk.RAISED,
            text = "Next Board",
            command = lambda: self.btn_NextBoard_action(parent)
        )
        next_board_button.pack(anchor = 'ne', padx = 10, pady = 10)
 

        # Creating the logout button
        btn_logout = tk.Button(
            frm_logout,
            relief = tk.RAISED,
            text = "Logout",
            command = lambda: self.btn_logout_action(parent)
        )
        btn_logout.pack(anchor = 'se', padx = 10, pady = 20)
 
    


    #################################################

    def btn_NextBoard_action(self, parent):
        parent.set_frame_scan_frame()

    def btn_logout_action(self, parent):
        parent.set_frame_login_frame() 

        
    
    #################################################

    def update_frame(self):
        self.create_frame(self.parent)



#################################################################################
