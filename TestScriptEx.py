import threading
import time

class TestScriptEx():
    def __init__(self):
        
        self.incrementor = "Your console appears to be working"

        time.sleep(0.75)

        
    # def some_return_method(self):
    #     return "Some very odd and long string that has some content within it!"

    
    def run_inc_thread(self):
        self.inc_thread = threading.Thread(target=self.start_incrementing)
        self.inc_thread.daemon = True
        self.inc_thread.start()

    def start_incrementing(self):
        while True:
            time.sleep(3)
            self.incrementor = self.incrementor + "Here's another line for you"


    
    def get_current_status(self):
        temp = self.incrementor
        self.incrementor = ""
        return temp