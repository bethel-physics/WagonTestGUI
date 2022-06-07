

class DataHolder():

    def __init__(self):
        self.user_ID = ""
        self.current_serial_ID = 0
        self.test1_completed = False
        self.test2_completed = False
        self.test3_completed = False
        self.test4_completed = False
        self.test1_pass = False
        self.test2_pass = False
        self.test3_pass = False
        self.test4_pass = False

    def clear_DataHolder(self):
        self.__init__()

    
    def send_to_DB(self):
        pass

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