import time, sys, os

sys.path.append("{}/Tests/".format(os.getcwd()))

from Test import Test

# Simple test counting from 1 to 10 for demo purposes
# This is an example of how a test can be written to run locally
# Note the inheritance of the test demo class for full functionality
class counting(Test):

    def __init__(self, conn, board_sn=-1, tester="Jane Doe"):

        # Test metadata for storage
        self.info_dict = {'name': "Count to 10", 'board_sn': board_sn, 'tester': tester}

        # One end of a multiprocessing pipe to send output to GUI console
        self.conn = conn

        # Initialization of the parent test object handles result saving,
        # message passing between tests and GUI
        # Note that tests are run on initialization of the Test object
        Test.__init__(self, self.run_count, self.info_dict, conn)

    def initialization(self):

        # Do some initialization of test setup
        time.sleep(3)

    def run_count(self, **kwargs):

        self.initialization()

        self.conn.send("Beginning count test:")

        try: 
            for i in range(1,11):
                self.conn.send("{}".format(i))
                time.sleep(1)
        except:
            self.conn.send("Something went wrong while counting to 10...")
            test_passed = False
            data = {"StartVal": 1, "EndVal": i}
            return test_passed, data

        test_passed = True
        data = {"StartVal": 1, "EndVal": i}
        self.conn.send("Done.")

        return test_passed, data

