#####################################################################
#                                                                   #
#  This is the code for a client to send a request to a server to   #
#                   run specific test scripts.                      #
#                                                                   #
#####################################################################

#################################################################################

# Importing necessary modules
import zmq, json, threading

#################################################################################

# Making the Client Server a class
class ClientZMQ():

    #################################################

    # Ensures nothing happens on instantiantion
    def __init__(self):
        pass

    #################################################

    # Starts the test by creating a thread for the test to run inside of
    def run_test_thread(self, desired_test):
        self.test_thread = threading.Thread(target=self.ping_server(desired_test))
        self.test_thread.daemon = True
        self.test_thread.start()

    #################################################

    # The function used to run the test
    def ping_server(self, desired_test):

        # Establishing variable for use
        self.desired_test = desired_test

        # Necessary for zmqClient    
        context = zmq.Context()

        # Creates a socket to talk to the server
        print("Connecting to the testing server...")
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")

        # Tell the server what test to run
        socket.send(self.desired_test)

        # Get the reply
        message = socket.recv()

        # Try to interpret the response as a json
        try:
            message = socket.recv()
            valid_json_return = json.loads(message)
            print("\n", valid_json_return, "\n")
        # When it fails, print what the server sends back
        except:
            print("Server did not send json.")
            message.decode('UTF-8')
            print(message)
            print(message.decode('UTF-8'))
            self.message = message.decode('UTF-8')

    #################################################

    def get_message(self):
        return self.message

    #################################################

    def set_message(self, string):
        self.message = string

    #################################################
    
            
#################################################################################