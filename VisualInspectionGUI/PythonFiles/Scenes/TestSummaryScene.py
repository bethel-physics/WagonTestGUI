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
        super().__init__(master_frame, width=850, height=500)

        logging.info("TestSummaryScene: Frame has been created.")

        self.data_holder = data_holder

        self.parent = parent
        # Setting weights of columns so the column 4 is half the size of columns 0-3
        #for i in range(self.data_holder.getNumTest()):
        #    self.columnconfigure(i, weight = 2)
        #self.columnconfigure(self.data_holder.getNumTest(), weight = 1)
        # Instantiates an updated table with the current data
        #self.create_updated_table(parent)


       
        self.create_results_table(parent)        

        # Fits the frame to set size rather than interior widgets
        self.grid_propagate(0)

    #################################################
    
    def create_results_table(self, parent):
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
        
        

        # Adds the title to the TestSummary Frame
        self.title = tk.Label(
                self, 
                fg='#0d0d0d', 
                text = "Visual Inspection Finished!",
                font=('Arial',18,'bold')
                )
        self.title.grid(row= 0, column= 1, pady = 20)
        

        logging.debug("TestSummaryScene: Creating the engine image.")
        
        # Create a photoimage object of the Engine
        Engine_image = Image.open("{}/Images/EnginePhoto.png".format(PythonFiles.__path__[0]))
        Engine_image = Engine_image.resize((200, 150), Image.ANTIALIAS)
        Engine_PhotoImage = iTK.PhotoImage(Engine_image)
        Engine_label = tk.Label(self, image=Engine_PhotoImage)
        Engine_label.image = Engine_PhotoImage

        # the .grid() adds it to the Frame
        Engine_label.grid(column=1, row = 1)





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
        for key,value in self.data_holder.inspection_data.items():
            key_count = key_count + 1
            print("\nKey: {}, Value: {}".format(key,value))
            
            key_label = tk.Label(
                    self.frm_table, 
                    text = key, 
                    relief = 'ridge', 
                    width=25, 
                    height=1, 
                    font=('Arial', 11, "bold")
                    )
            key_label.grid(row=key_count , column=0)
             
            
            result_label = tk.Label(
                    self.frm_table, 
                    text = value, 
                    relief = 'ridge', 
                    width=25, 
                    height=1, 
                    font=('Arial', 11, "bold")
                    )
            result_label.grid(row=key_count , column=1)
                    
            
 
 
        ## For the visual inspection component
        #self.inspection_data = { 
        #        'board_chipped_bent': False,
        #        'wagon_connection_pin_bent': False,
        #        'engine_connection_pin_bent': False,
        #        'visual_scratches': False,
        #        'inspection_comments': "_" 
        #        }





        
    
    #################################################

    def update_frame(self):
        self.create_results_table(self.parent)



#################################################################################
