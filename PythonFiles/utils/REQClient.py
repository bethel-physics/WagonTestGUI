#####################################################################
#                                                                   #
#  This is the code for a client to send a request to a server to   #
#                   run specific test scripts.                      #
#                                                                   #
#####################################################################

#################################################################################

# Importing necessary modules
import zmq, logging

#################################################################################

FORMAT = '%(asctime)s|%(levelname)s|%(message)s|'
logging.basicConfig(
    filename="/home/hgcal/WagonTest/WagonTestGUI/PythonFiles/logs/StressTest.log", 
    filemode = 'w', 
    format=FORMAT, 
    level=logging.INFO
    )

# Making the Client Server a class
class REQClient():

    #################################################

    # Ensures nothing happens on instantiantion
    def __init__(self, desired_test, serial, tester):
        self.message = ""
        self.serial = serial
        self.tester = tester
        sending_msg = desired_test + ";" + serial + ";" + tester
        # Establishing variable for use
        self.desired_test = desired_test
        # Necessary for zmqClient    
        context = zmq.Context()

        # Creates a socket to talk to the server
        # print("Connecting to the testing server...")
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://192.168.23.23:5555")

        debug_msg = "REQClient: Sending request to REPServer for: " + self.desired_test
        logging.debug(debug_msg)
        # Tell the server what test to run
        socket.send_string(sending_msg)
        logging.debug("REQClient: Request sent. Waiting for confirmation receipt...")
        # Get the reply
        self.message = socket.recv_string()
        print("REQClient: Request received.")

        # Closes the client so the code in the GUI can continue once the request is sent.
        socket.close()

    #################################################

    def get_message(self):
        return self.message

    #################################################

    def set_message(self, string):
        self.message = string

    #################################################
    
            
#################################################################################
