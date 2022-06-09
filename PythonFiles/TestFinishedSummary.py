import json
import tkinter as tk
from PIL import ImageTk as iTK
from PIL import Image
from matplotlib.pyplot import table
from pyparsing import col


'''
Frame that shows all of the final test results
@param parent -> References a GUIWindow object
@param master_window -> Tkinter object that the frame is going to be placed on
@param data_holder -> DataHolder object that stores all relevant data
'''
class TestFinishedSummary(tk.Frame):
    def __init__(self, parent, master_window, data_holder):
    
        self.parent = parent
        
        # Call to the super class's constructor
        # Super class is the tk.Frame class
        super().__init__(master_window, width=850, height=500)

        self.data_holder = data_holder

        # Setting weights of columns so the column 4 is half the size of columns 0-3
        self.columnconfigure(0, weight = 2)
        self.columnconfigure(1, weight = 2)
        self.columnconfigure(2, weight = 2)
        self.columnconfigure(3, weight = 2)
        self.columnconfigure(4, weight = 1)
        # Instantiates an updated table with the current data
        self.create_updated_table(parent)

        # Adds the title to the TestSummary Frame
        self.title = tk.Label(
                self, 
                fg='#0d0d0d', 
                text = "Testing Finished!",
                font=('Arial',18,'bold')
                )
        self.title.grid(row= 0, column= 1, pady = 20)

        # Fits the frame to set size rather than interior widgets
        self.grid_propagate(0)


    # A function to be called within GUIWindow to create the console output
    # when the frame is being brought to the top
    def create_JSON_popup(self, JSON_String):
        
        # Creating a popup window for the JSON Details
        self.JSON_popup = tk.Tk()
        self.JSON_popup.geometry("500x500+0+100")
        self.JSON_popup.title("JSON Details")
        self.JSON_popup.wm_attributes('-toolwindow', 'True')

    

        # Creating a Frame For Console Output
        JSON_frame = tk.Frame(self.JSON_popup, width = 500, height = 500, bg = 'green')
        JSON_frame.pack_propagate(0)
        JSON_frame.pack()

        # Placing an entry box in the frm_console
        self.JSON_entry_box = tk.Text(
            JSON_frame, 
            bg = '#6e5e5d', 
            fg = 'white', 
            font = ('Arial', 14)
            )
        self.JSON_entry_box.pack(anchor = 'center', fill=tk.BOTH, expand=1)

        current_JSON_file = open(JSON_String)
        current_JSON_data = json.load(current_JSON_file)


        temp = ""
        for key, value in current_JSON_data.items():
            temp = temp + "{} : {}".format(key, value) + "\n"


        self.JSON_entry_box.delete(1.0,"end")
        self.JSON_entry_box.insert(1.0, temp)


    '''
    Creates the table with the updated information from the data_holder
    @param parent -> References the GUIWindow object that creates the class
    '''
    def create_updated_table(self, parent):
                
        
        self.list_of_tests = ["General Resistance Test", "ID Resistor Test", "I2C Comm. Test", "Bit Rate Test"]
        self.list_of_table_labels = ["Test Name", "Test Status", "Pass/Fail"]
        self.list_of_completed_tests = [self.data_holder.test1_completed, self.data_holder.test2_completed, self.data_holder.test3_completed, self.data_holder.test4_completed]
        self.list_of_pass_fail = [self.data_holder.test1_pass, self.data_holder.test2_pass, self.data_holder.test3_pass, self.data_holder.test4_pass]


        # Adds Board Serial Number to the TestSummaryFrame
        self.lbl_serial = tk.Label(
                self, 
                text = "Serial Number: " + str(self.data_holder.current_serial_ID),
                font=('Arial', 14)
                )
        self.lbl_serial.grid(column = 2, row = 0, pady = 20)

        # Adds Tester Name to the TestSummary Frame
        self.lbl_tester = tk.Label(
                self, 
                text = "Tester: " + self.data_holder.user_ID,
                font=('Arial', 14)
                )
        self.lbl_tester.grid(column = 0, row = 0, pady = 20)
       
        
        # Creates the "table" as a frame object
        self.frm_table = tk.Frame(self)
        self.frm_table.grid(row = 1, column= 0, columnspan = 4, rowspan = 4)
        
        # Setting weights of columns so the column 4 is half the size of columns 0-3
        self.frm_table.columnconfigure(0, weight = 2)
        self.frm_table.columnconfigure(1, weight = 2)
        self.frm_table.columnconfigure(2, weight = 2)
        self.frm_table.columnconfigure(3, weight = 1)
        self.frm_table.columnconfigure(4, weight = 1)
        

        
        # Adds the labels to the top of the table
        for index in range(len(self.list_of_table_labels)):
            _label = tk.Label(
                    self.frm_table, 
                    text = self.list_of_table_labels[index], 
                    relief = 'ridge', 
                    width=25, 
                    height=1, 
                    font=('Arial', 11, "bold")
                    )
            _label.grid(row= 0, column=index)
            

        # Adds the test names to the first column
        for index in range(len(self.list_of_tests)):
            _label= tk.Label(
                    self.frm_table, 
                    text = self.list_of_tests[index], 
                    relief = 'ridge', 
                    width=25, 
                    height=5, 
                    font=('Arial', 11)
                    )
            _label.grid(row=index + 1, column=0)
            


        # Create Labels that tell whether or not a test was completed
        for index in range(len(self.list_of_completed_tests)):
            
            # Instantiates a Label
            _label = tk.Label(
                        self.frm_table,
                        relief = 'ridge', 
                        width=25, 
                        height=5, 
                        font=('Arial',11)
                        )

            # if the test is completed, set the label to "Complete"
            if (self.list_of_completed_tests[index]):
                _label.config(
                        text = "COMPLETED"
                        )
            # else, set the label to "Unfinished"
            else:
                _label.config(
                        text = "UNFINISHED"
                        )

            # Puts the completed/unfinished label into the table       
            _label.grid(row=index + 1, column=1)


        # Adds the Image as to whether the test was completed or not
        for index in range(len(self.list_of_pass_fail)):
            if(self.list_of_pass_fail[index]):
                # Create a photoimage object of the QR Code
                Green_Check_Image = Image.open("./PythonFiles/GreenCheckMark.png")
                Green_Check_Image = Green_Check_Image.resize((75,75), Image.ANTIALIAS)
                Green_Check_PhotoImage = iTK.PhotoImage(Green_Check_Image)
                GreenCheck_Label = tk.Label(self.frm_table, image=Green_Check_PhotoImage, width=75, height=75)
                GreenCheck_Label.image = Green_Check_PhotoImage

                GreenCheck_Label.grid(row=index + 1, column=2)

            else:
                # Create a photoimage object of the QR Code
                Red_X_Image = Image.open("./PythonFiles/RedX.png")
                Red_X_Image = Red_X_Image.resize((75,75), Image.ANTIALIAS)
                Red_X_PhotoImage = iTK.PhotoImage(Red_X_Image)
                RedX_Label = tk.Label(self.frm_table, image=Red_X_PhotoImage, width=75, height=75)
                RedX_Label.image = Red_X_PhotoImage

                RedX_Label.grid(row=index + 1, column=2)


        self.create_retest_more_info_btns(parent)
       
        self.grid_propagate(0)



    # Creates all of the retest button
    def create_retest_more_info_btns(self, parent):
        
        row1 = tk.Frame(self.frm_table)
        row1.grid(column = 3, row = 1)
        
        btn_retest1 = tk.Button(
                row1, 
                text = "RETEST",
                padx= 5,
                pady=5,  
                command = lambda: self.retest1_btn_action(parent)
                )
        btn_retest1.grid(column = 1, row = 0, padx=5, pady=5)

        btn_more_info1 = tk.Button(
                row1, 
                text = "MORE INFO", 
                padx= 5,
                pady=5, 
                command = lambda: self.btn_more_info1_action(parent)
                )
        btn_more_info1.grid(column=0, row = 0)
    



        row2 = tk.Frame(self.frm_table)
        row2.grid(column = 3, row = 2)
        
        btn_retest2 = tk.Button(
                row2, 
                text = "RETEST",
                padx= 5,
                pady=5,  
                command = lambda: self.retest2_btn_action(parent)
                )
        btn_retest2.grid(column = 1, row = 0, padx=5, pady=5)

        btn_more_info2 = tk.Button(
                row2, 
                text = "MORE INFO", 
                padx= 5,
                pady=5, 
                command = lambda: self.btn_more_info2_action(parent)
                )
        btn_more_info2.grid(column=0, row = 0)




        row3 = tk.Frame(self.frm_table)
        row3.grid(column = 3, row = 3)
        
        btn_retest3 = tk.Button(
                row3, 
                text = "RETEST",
                padx= 5,
                pady=5,  
                command = lambda: self.retest3_btn_action(parent)
                )
        btn_retest3.grid(column = 1, row = 0, padx=5, pady=5)

        btn_more_info3 = tk.Button(
                row3, 
                text = "MORE INFO", 
                padx= 5,
                pady=5, 
                command = lambda: self.btn_more_info3_action(parent)
                )
        btn_more_info3.grid(column=0, row = 0)

        
        
        
    
        
        row4 = tk.Frame(self.frm_table)
        row4.grid(column = 3, row = 4)
        
        btn_retest4 = tk.Button(
                row4, 
                text = "RETEST",
                padx= 5,
                pady=5, 
                command = lambda: self.retest4_btn_action(parent)
                )
        btn_retest4.grid(column = 1, row = 0, padx=5, pady=5)

        btn_more_info4 = tk.Button(
                row4, 
                text = "MORE INFO", 
                padx= 5,
                pady=5, 
                command = lambda: self.btn_more_info4_action(parent)
                )
        btn_more_info4.grid(column=0, row = 0)




        btn_next_test = tk.Button(
                self.frm_table, 
                text = "NEXT TEST",
                font = ('Arial', 15), 
                command = lambda: self.next_test_btn_action(parent)
                )
        btn_next_test.grid(column = 3, row = 5)



    # All of the different methods for what the retest buttons should do
    def retest1_btn_action(self, _parent):
        _parent.set_frame(_parent.test1_frame)
    
    def retest2_btn_action(self, _parent):
        _parent.set_frame(_parent.test2_frame)

    def retest3_btn_action(self, _parent):
        _parent.set_frame(_parent.test3_frame)

    def retest4_btn_action(self, _parent):
        _parent.set_frame(_parent.test4_frame)


    def btn_more_info1_action(self, _parent):
        self.create_JSON_popup(".\PythonFiles\DummyJSONTest.JSON")

    def btn_more_info2_action(self, _parent):
        self.create_JSON_popup(".\PythonFiles\GarrettJSONTest.JSON")

    def btn_more_info3_action(self, _parent):
        self.create_JSON_popup(".\PythonFiles\DummyJSONTest.JSON")
    
    def btn_more_info4_action(self, _parent):
        self.create_JSON_popup(".\PythonFiles\GarrettJSONTest.JSON")



    # Next test button action
    def next_test_btn_action(self, _parent):
        _parent.set_frame(_parent.scan_frame)
        

    # Updates the frame to show current data
    def update_frame(self):
        self.create_updated_table(self.parent)



    # TODO Check what this is used for
    def add_new_test(self, _list_of_completed_tests, _list_of_pass_fail):
        self.list_of_completed_tests = _list_of_completed_tests
        self.list_of_pass_fail = _list_of_pass_fail