#####################################################################
#                                                                   #
#  This is the code for a client to send a request to a server to   #
#                   run specific test scripts.                      #
#                                                                   #
#####################################################################

#################################################################################

# Importing necessary modules
import zmq, logging
import PythonFiles
import os

#################################################################################

FORMAT = '%(asctime)s|%(levelname)s|%(message)s|'
logging.basicConfig(
    filename="/home/{}/GUILogs/gui.log".format(os.getlogin()), 
    filemode = 'a', 
    format=FORMAT, 
    level=logging.INFO
    )

# Making the Client Server a class
class REQClient():

    ################################################

    # Ensures nothing happens on instantiantion
    def __init__(self, desired_test, serial, tester):
        with open("{}/utils/server_ip.txt".format(PythonFiles.__path__[0]),"r") as openfile:
            grabbed_ip = openfile.read()[:-1]
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
        socket.connect("tcp://{ip_address}:5555".format(ip_address = grabbed_ip))

        debug_msg = "REQClient: Sending request to REPServer for: " + self.desired_test
        logging.debug(debug_msg)
        # Tell the server what test to run
        socket.send_string(sending_msg)
        logging.debug("REQClient: Request sent. Waiting for confirmation receipt...")
        # Get the reply
    
        # Recording the number of tries to open the socket and receive a string
        tries = 0

        while (len(self.message)< 1) and tries < 1000:
            try:
                print("\nTrying to receive a message from the socket")
                logging.debug("REQClient: Trying to receive a message from the socket receive")
                self.message = socket.recv_string()
                print("\n\n\nSelf.message: {}\n\n\n".format(self.message))

            except:
                print("REQClient: couldn't get info - {}".format(tries))
                logging.debug("REQClient: No Message received from the request.")
                tries = tries + 1 
            #messagebox.showerror("No Message Received", "REQClient: No message received from the request.")

        print("REQClient: Request received.")

        # Closes the client so the code in the GUI can continue once the request is sent.
        try:
            logging.debug("REQClient: Trying to close the socket")
            socket.close()
        except:
            logging.debug("REQClient: Unable to close the socket")

    #################################################

    def get_message(self):
        return self.message

    #################################################

    def set_message(self, string):
        self.message = string

    #################################################
    
            
#################################################################################
