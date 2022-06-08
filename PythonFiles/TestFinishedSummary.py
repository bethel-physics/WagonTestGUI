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
        
        # Call to the super class's constructor
        # Super class is the tk.Frame class
        super().__init__(master_window, width=850, height=500)

        self.data_holder = data_holder

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



    '''
    Creates the table with the updated information from the data_holder
    @param parent -> 
    '''
    def create_updated_table(self, parent):
                
        
        self.list_of_tests = ["General Resistance Test", "ID Resistor Test", "I2C Comm. Test", "Bit Rate Test"]
        self.list_of_table_labels = ["Test Name", "Test Status", "Pass/Fail", "Retest?"]
        self.list_of_completed_tests = [self.data_holder.test1_completed, self.data_holder.test2_completed, self.data_holder.test3_completed, self.data_holder.test4_completed]
        self.list_of_pass_fail = [self.data_holder.test1_pass, self.data_holder.test2_pass, self.data_holder.test3_pass, self.data_holder.test4_pass]


        # Adds Board Serial Number to the TestSummaryFrame
        self.lbl_serial = tk.Label(
                self, 
                text = "Serial Number: " + str(self.data_holder.current_serial_ID),
                font=('Arial', 15)
                )
        self.lbl_serial.grid(column = 2, row = 0, pady = 20)

        # Adds Tester Name to the TestSummary Frame
        self.lbl_tester = tk.Label(
                self, 
                text = "Tester: " + self.data_holder.user_ID,
                font=('Arial', 15)
                )
        self.lbl_tester.grid(column = 0, row = 0, pady = 20)
        
        
        # Creates the "table" as a frame object
        self.table = tk.Frame(self)
        self.table.grid(row = 1, column= 0, columnspan = 4, rowspan = 4)


        
        # Adds the labels to the top of the table
        for index in range(len(self.list_of_table_labels)):
            _label = tk.Label(
                    self.table, 
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
                    self.table, 
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
                        self.table,
                        relief = 'ridge', 
                        width=25, 
                        height=5, 
                        font=('Arial',11)
                        )

            # if the test is completed, set the label to "Complete"
            if (self.list_of_completed_tests[index]):
                _label = tk.Label(
                        text = "COMPLETED"
                        )
            # else, set the label to "Unfinished"
            else:
                _label = tk.Label(
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
                GreenCheck_Label = tk.Label(self.table, image=Green_Check_PhotoImage, width=75, height=75)
                GreenCheck_Label.image = Green_Check_PhotoImage

                GreenCheck_Label.grid(row=index + 1, column=2)

            else:
                # Create a photoimage object of the QR Code
                Red_X_Image = Image.open("./PythonFiles/RedX.png")
                Red_X_Image = Red_X_Image.resize((75,75), Image.ANTIALIAS)
                Red_X_PhotoImage = iTK.PhotoImage(Red_X_Image)
                RedX_Label = tk.Label(self.table, image=Red_X_PhotoImage, width=75, height=75)
                RedX_Label.image = Red_X_PhotoImage

                RedX_Label.grid(row=index + 1, column=2)


        self.create_retest_btns(parent)
       

        self.grid_propagate(0)








    # Creates all of the retest button
    def create_retest_btns(self, parent):
        btn_retest1 = tk.Button(
                self.table, 
                text = "RETEST", 
                command = lambda: self.retest1_btn_action(parent)
                )
        btn_retest1.grid(column = 3, row = 1)
    
        btn_retest2 = tk.Button(
                self.table, 
                text = "RETEST", 
                command = lambda: self.retest2_btn_action(parent)
                )
        btn_retest2.grid(column = 3, row = 2)

        btn_retest3 = tk.Button(
                self.table, 
                text = "RETEST", 
                command = lambda: self.retest3_btn_action(parent)
                )
        btn_retest3.grid(column = 3, row = 3)

        btn_retest4 = tk.Button(
                self.table, 
                text = "RETEST", 
                command = lambda: self.retest4_btn_action(parent)
                )
        btn_retest4.grid(column = 3, row = 4)

        btn_next_test = tk.Button(
                self.table, 
                text = "NEXT TEST", 
                command = lambda: self.next_test_btn_action(parent)
                )
        btn_next_test.grid(column = 3, row = 5, columnspan = 2)



    # All of the different methods for what the retest buttons should do
    def retest1_btn_action(self, _parent):
        _parent.set_frame(_parent.test1_frame)
    
    def retest2_btn_action(self, _parent):
        _parent.set_frame(_parent.test2_frame)

    def retest3_btn_action(self, _parent):
        _parent.set_frame(_parent.test3_frame)

    def retest4_btn_action(self, _parent):
        _parent.set_frame(_parent.test4_frame)



    # Next test button action
    def next_test_btn_action(self, _parent):
        _parent.set_frame(_parent.scan_frame)
        



    # TODO Check what this is used for
    def add_new_test(self, _list_of_completed_tests, _list_of_pass_fail):
        self.list_of_completed_tests = _list_of_completed_tests
        self.list_of_pass_fail = _list_of_pass_fail