

class DataHolder():

    # List of the variables being held by data holder
    def __init__(self):
        self.user_ID = ""                 # Tester's Name
        self.current_serial_ID = 0        # Unit Serial Number
        self.test1_completed = False      # Whether the test has been completed
        self.test2_completed = False      # Whether the test has been completed
        self.test3_completed = False      # Whether the test has been completed
        self.test4_completed = False      # Whether the test has been completed
        self.test1_pass = False           # Whether the test has been passed
        self.test2_pass = False           # Whether the test has been passed
        self.test3_pass = False           # Whether the test has been passed
        self.test4_pass = False           # Whether the test has been passed

    # Clears the data by reseting all the values to the initial state
    def clear_DataHolder(self):
        self.__init__()

    # Future method to send data to the database
    def send_to_DB(self):
        pass

    # Prints all the variable values inside data_holder
    def print(self):
        print("self.user_ID: ", self.user_ID)
        print("self.current_serial_ID: ", self.current_serial_ID)
        print("self.test1_completed: ", self.test1_completed)
        print("self.test2_completed: ", self.test2_completed)
        print("self.test3_completed: ", self.test3_completed)
        print("self.test4_completed: ", self.test4_completed)
        print("self.test1_pass: ", self.test1_pass)
        print("self.test2_pass: ", self.test2_pass)
        print("self.test3_pass: ", self.test3_pass)
        print("self.test4_pass: ", self.test4_pass)

    # Set of commands for getting all the variables from data_holder
    def get(self):
        return (self.user_ID + 
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