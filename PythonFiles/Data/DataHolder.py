#################################################################################
import json, logging
from PythonFiles.Data.DBSender import DBSender

FORMAT = '%(asctime)s|%(levelname)s|%(message)s|'
logging.basicConfig(filename="/home/hgcal/WagonTest/WagonTestGUI/PythonFiles/logs/GUIWindow.log", filemode = 'w', format=FORMAT, level=logging.DEBUG)

class DataHolder():

    #################################################

    # List of the variables being held by data holder
    def __init__(self):


        # Object that sends information to the database
        self.data_sender = DBSender()
        
        self.user_ID = ""                 # Tester's Name
        self.test_stand = ""              # Test stand for the unit
        self.current_serial_ID = -1        # Unit Serial Number
        self.test1_completed = False      # Whether the test has been completed
        self.test2_completed = False      # Whether the test has been completed
        self.test3_completed = False      # Whether the test has been completed
        self.test4_completed = False      # Whether the test has been completed
        self.test1_pass = False           # Whether the test has been passed
        self.test2_pass = False           # Whether the test has been passed
        self.test3_pass = False           # Whether the test has been passed
        self.test4_pass = False           # Whether the test has been passed

    #################################################

    def set_user_ID(self, user_ID):

        self.data_sender.verify_person(user_ID)
        self.user_ID = user_ID
        logging.debug("DataHolder: User ID has been set.")

    ##################################################

    def set_serial_ID(self, sn):
        # TODO
        # self.data_sender.add_new_board(sn)

        self.current_serial_ID = sn
        logging.info("DataHolder: Serial Number has been set.")

    ##################################################

    def get_serial_ID(self):
        # TODO
        # self.data_sender.add_new_board(sn)

        return self.current_serial_ID

    #################################################

    # Clears the data by reseting all the values to the initial state
    def clear_DataHolder(self):
        self.__init__()
        logging.info("DataHolder: DataHolder has been fully reset.")
    #################################################

    # Future method to send data to the database
    def send_to_DB(self):
        pass
    
    #################################################

    # Prints all the variable values inside data_holder
    def print(self):
        print("user_ID: ", self.user_ID)
        print("test_stand: ", self.test_stand)
        print("current_serial_ID: ", self.current_serial_ID)
        print("test1_completed: ", self.test1_completed)
        print("test2_completed: ", self.test2_completed)
        print("test3_completed: ", self.test3_completed)
        print("test4_completed: ", self.test4_completed)
        print("test1_pass: ", self.test1_pass)
        print("test2_pass: ", self.test2_pass)
        print("test3_pass: ", self.test3_pass)
        print("test4_pass: ", self.test4_pass)

    #################################################

    # Gets all the variables from data_holder
    def get(self):
        return (
                self.user_ID + 
                self.test_stand +
                str(self.current_serial_ID) +
                str(self.test1_completed) +
                str(self.test2_completed) +
                str(self.test3_completed) +
                str(self.test4_completed) +
                str(self.test1_pass) +
                str(self.test2_pass) +
                str(self.test3_pass) +
                str(self.test4_pass) 
        )

    ################################################



    def update_from_json_string(self, imported_json_string):
        json_dict = json.loads(imported_json_string)

        
        test_type = json_dict["name"]
        if test_type == "GenRes Test":
            with open("/home/hgcal/WagonTest/WagonTestGUI/PythonFiles/JSONFiles/Current_GenRes_JSON.json", "w") as file:
                json.dump(json_dict, file)

            self.user_ID = json_dict["tester"]
            self.current_serial_ID = json_dict["board_sn"] 
            self.test1_completed = True
            self.test1_pass = json_dict["pass"]

        elif test_type == "IDRes Test":
            with open("/home/hgcal/WagonTest/WagonTestGUI/PythonFiles/JSONFiles/Current_IDRes_JSON.json", "w") as file:
                json.dump(json_dict, file)

            self.user_ID = json_dict["tester"]
            self.current_serial_ID = json_dict["board_sn"] 
            self.test2_completed = True
            self.test2_pass = json_dict["pass"]


        elif test_type == "IIC Test":
            with open("/home/hgcal/WagonTest/WagonTestGUI/PythonFiles/JSONFiles/Current_IIC_JSON.json", "w") as file:
                json.dump(json_dict, file)

            self.user_ID = json_dict["tester"]
            self.current_serial_ID = json_dict["board_sn"] 
            self.test3_completed = True
            self.test3_pass = json_dict["pass"]

        elif test_type == "Bit Error Rate Test":
            with open("/home/hgcal/WagonTest/WagonTestGUI/PythonFiles/JSONFiles/Current_BERT_JSON.json", "w") as file:
                json.dump(json_dict, file)
            self.user_ID = json_dict["tester"]
            self.current_serial_ID = json_dict["board_sn"] 
            self.test4_completed = True
            self.test4_pass = json_dict["pass"]

        logging.info("DataHolder: Test results have been saved")

    # Keeps the login information stored
    def data_holder_new_test(self):    
        self.test_stand = ""        
        self.current_serial_ID = -1  
        self.test1_completed = False
        self.test2_completed = False
        self.test3_completed = False
        self.test4_completed = False
        self.test1_pass = False     
        self.test2_pass = False     
        self.test3_pass = False     
        self.test4_pass = False 

        logging.info("DataHolder: DataHolder Information has been reset for a new test.")        

    ################################################



#################################################################################
