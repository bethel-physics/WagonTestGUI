import requests
import json
import socket
# from read_barcode import read_barcode


class DBSender():

    def __init__(self, gui_cfg):
        self.gui_cfg = gui_cfg

        # Predefined URL for the database
        self.db_url = self.gui_cfg.getDBInfo("baseURL")

        # If True, use database
        # If False, run in "offline" mode
        self.use_database = self.gui_cfg.get_if_use_DB()



    # Since we will have the tester in a separate room, we need to do modify the http requests
    # This proxy will be used to make http requests directly to cmslab3 via an ssh tunnel
    def getProxies(self):
        if (self.use_database):
            if "umncmslab" in socket.gethostname():
                return None
            
            return {"http": "http://127.0.0.1:8080"}

        # If not using the database, then...
        else:
            pass

    def add_new_user_ID(self, user_ID, passwd):
        
        if (self.use_database):

            try:
                r = requests.post('{}/add_tester2.py'.format(self.db_url), data= {'person_name':user_ID, 'password': passwd})
            except Exception as e:
                print("Unable to add the user to the database. Username: {}. Check to see if your password is correct.".format(user_ID))


        # If not using the database, use this...
        else:
            pass    
     

    # Returns an acceptable list of usernames from the database
    def get_usernames(self):
        if (self.use_database):
            r = requests.get('{}/get_usernames.py'.format(self.db_url))
            lines = r.text.split('\n')

            #print(lines)

            begin = lines.index("Begin") + 1
            end = lines.index("End")

            usernames = []

            for i in range(begin, end):
                temp = lines[i]
                usernames.append(temp)

            return usernames

        # If not using database...        
        else:
            
            return ['User1', 'User2', 'User3']


    def add_board_image(self, serial, image):
        pass
        

    # Returns a list of booleans
    # Whether test (by index) has been completed or not
    def get_test_completion_staus(self, serial_number):
        
        if (self.use_database):
            r = requests.post('{}/get_test_completion_status.py'.format(self.db_url), data= serial_number)
            
            lines = r.text.split('\n')
            begin = lines.index("Begin") + 1 
            end = lines.index("End")
            
            tests_completed = []
            for i in range(begin, end):
                temp = lines[i][1:-1].split(",")
                temp[0] = str(temp[0])
                temp[1] = int(temp[1])
                tests_completed.append(temp)

            return tests_completed

        # If not using the database...
        else:

            blank_completion = []
            for i in enumerate(self.gui_cfg.getNumTest()):
                blank_completion.append('False')

            return blank_completion




    # Returns a list of booleans
    # Whether or not DB has passing results 
    def get_previous_test_results(self, serial_number):
        
        if (self.use_database):
   
            r = requests.post('{}/get_previous_test_results.py'.format(self.db_url), data={'serial_number': str(serial_number)})
            
            lines = r.text.split('\n')

            begin = lines.index("Begin") + 1
            end = lines.index("End")

            tests_passed= []


            for i in range(begin, end):
                temp = lines[i][1:-1].split(",")
                temp[0] = str(temp[0])
                temp[1] = int(temp[1])
                tests_passed.append(temp)

            return tests_passed
        
        # If not using database...
        else:
            
            blank_results = []
            for i in enumerate(self.gui_cfg.getNumTest()):
                blank_results.append('False')

            return blank_results

    
    
    # #TODO Verify if a board has already been instantiated with SN
    # Posts a new board with passed in serial number
    def add_new_board(self, sn):
        
        if (self.use_database):
        
            r = requests.post('{}/add_module2.py'.format(self.db_url), data={"serial_number": str(sn)})
    
        else:
            
            pass

    def is_new_board(self, sn):
        
        if (self.use_database):

            r = requests.post('{}/is_new_board.py'.format(self.db_url), data={"serial_number": str(sn)})
            print(r.text)
            
            lines = r.text.split('\n')
       
            begin = lines.index("Begin") + 1
            end = lines.index("End")

    
            for i in range(begin, end): 
                
                if lines[i] == "True":
                    return True
                elif lines[i] == "False":
                    return False

        else:
            return True




    # Posts information via the "info" dictionary
    # Serial number is within the info dictionary
    def add_board_info(self, info):
        
        if (self.use_database):

            r = requests.post('{}/add_board_info2.py'.format(self.db_url), data = info)
        
        else:
            pass    

    def add_initial_tests(self, results):
        if (self.use_database):
    
            r = requests.post('{}/add_init_test.py'.format(self.db_url), data = results)
        
        else:
            pass        

    def add_general_test(self, results, files):
        if (self.use_database):
    
            r = requests.post('{}/add_test2.py'.format(self.db_url), data = results, files=files)

        else:
            pass

    def add_test_json(self, json_file, datafile_name):
        load_file = open(json_file)
        results = json.load(load_file)        
        load_file.close()

        datafile = open(datafile_name, "rb")        

        attach_data = {'attach1': datafile}
        #print("Read from json file:", results)

        if (self.use_database):
            r = requests.post('{}/add_test_json.py'.format(self.db_url), data = results, files = attach_data)

        else:
            pass

 # Returns a list of all different types of tests
    def get_test_list(self):
        if (self.use_database):
            r = requests.get('{}/get_test_types.py'.format(self.db_url))

            lines = r.text.split('\n')

            begin = lines.index("Begin") + 1
            end = lines.index("End")

            tests = []

            for i in range(begin, end):
                temp = lines[i][1:-1].split(",")
                temp[0] = str(temp[0][1:-1])
                temp[1] = int(temp[1])
                tests.append(temp)

            return tests

        else:
            
            blank_tests = []
            for i in enumerate(self.gui_cfg.getNumTest()):
                blank_tests.append("Test{}".format(i))

            return blank_tests

