

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