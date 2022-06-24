#####################################################################
#                                                                   #
#  This is the code for a client to send a request to a server to   #
#                   run specific test scripts.                      #
#                                                                   #
#####################################################################

#################################################################################

# Importing necessary modules
import zmq

#################################################################################

# Making the Client Server a class
class REQClient():

    #################################################

    # Ensures nothing happens on instantiantion
    def __init__(self, desired_test):
        self.message = ""
        
        # Establishing variable for use
        self.desired_test = desired_test
        test = desired_test.decode('UTF-8')
        # Necessary for zmqClient    
        context = zmq.Context()

        # Creates a socket to talk to the server
        # print("Connecting to the testing server...")
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")

        print("Sending request to REPServer for: ", test)
        # Tell the server what test to run
        socket.send(self.desired_test)
        print("Request sent. Waiting for confirmation receipt...")
        # Get the reply
        self.message = socket.recv()
        received = self.message.decode('UTF-8')
        print(received)

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