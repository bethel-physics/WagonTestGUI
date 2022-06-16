#####################################################################
#                                                                   #
#  Currently a test client server to make sure this works correctly #
#                                                                   #
#####################################################################

# Importing necessary modules
import zmq
import json

# Making the Client Server a class
class ClientZMQ():
    def __init__(self, desired_test):
        
        self.desired_test = desired_test
        
        
        context = zmq.Context()

        # Creates a socket to talk to the server
        print("Connecting to the Hello World server...")
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")


        # Does 10 requests, waiting for a response each time

        socket.send(self.desired_test)

        # Get the reply
        message = socket.recv()
        # print("Received reply %s [ %s ]" % (request, message))

        valid_json_return = json.loads(message)

        print("\n", valid_json_return, "\n")