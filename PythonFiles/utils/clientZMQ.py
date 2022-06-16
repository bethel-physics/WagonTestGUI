#####################################################################
#                                                                   #
#  Currently a test client server to make sure this works correctly #
#                                                                   #
#####################################################################

# Importing necessary modules
import zmq

context = zmq.Context()

# Creates a socket to talk to the server
print("Connecting to the Hello World server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


# Does 10 requests, waiting for a response each time
for request in range(10):
    print("Sending request %s ..." % request)
    socket.send(b"THERE IT IS")

    # Get the reply
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))