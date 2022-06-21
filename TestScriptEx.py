import threading
import time

from PythonFiles.utils.REQClient import REQClient
from PythonFiles.utils.SUBClient import SUBClient


class TestScriptEx():
    def __init__(self, _test_type):
        
        self.incrementor = "Your console appears to be working"
        self.test_type = bytes(_test_type,'UTF-8')

        time.sleep(0.75)

        
    # def some_return_method(self):
    #     return "Some very odd and long string that has some content within it!"

    
    def run_inc_thread(self):
        self.inc_thread = threading.Thread(target=self.start_incrementing)
        self.inc_thread.daemon = True
        self.inc_thread.start()

    def start_incrementing(self):
        
        self.reqclient = REQClient()
        self.subclient = SUBClient()
        self.subclient.create_client()
        time.sleep(2)
        self.reqclient.run_test_thread(self.test_type)
    
        self.incrementor = self.subclient.get_message()
        # while True:
        #     time.sleep(3)
        #     self.incrementor = self.incrementor + "Here's another line for you"


    
    def get_current_status(self):
        self.incrementor = self.subclient.get_message()
        self.subclient.set_message("")
        return self.incrementor