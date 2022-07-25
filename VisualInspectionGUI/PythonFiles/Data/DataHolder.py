#################################################################################


class DataHolder():

    #################################################

    # List of the variables being held by data holder
    def __init__(self):
        self.user_ID = ""                 # Tester's Name
        self.test_stand = ""              # Test stand for the unit
        self.current_serial_ID = 0        # Unit Serial Number
        self.test1_completed = False      # Whether the test has been completed
        self.test2_completed = False      # Whether the test has been completed
        self.test3_completed = False      # Whether the test has been completed
        self.test4_completed = False      # Whether the test has been completed
        self.test1_pass = False           # Whether the test has been passed
        self.test2_pass = False           # Whether the test has been passed
        self.test3_pass = False           # Whether the test has been passed
        self.test4_pass = False           # Whether the test has been passed
        self.board_chipped_bent = False
        self.wagon_connection_pin_bent = False
        self.engine_connection_pin_bent = False
        self.visual_scratches = False

    #################################################

    # Clears the data by reseting all the values to the initial state
    def clear_DataHolder(self):
        self.__init__()

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
        print("board_chipped_bent: ", self.board_chipped_bent)
        print("wagon_connection_pin_bent: ", self.wagon_connection_pin_bent)
        print("engine_connection_pin_bent: ", self.engine_connection_pin_bent)
        print("visual_scratches: ", self.visual_scratches)

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


#################################################################################
