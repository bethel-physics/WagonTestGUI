#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print ("started")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)
    if message == b"Test1":
        print("Received request for test 1")
        socket.send(b"Ran Test 1")
    elif message == b"Test2":
        print("Received request for test 2")
        socket.send(b"Ran Test 2")
    elif message == b"Test3":
        print("Received request for test 3")
        socket.send(b"Ran Test 3")
    elif message == b"Test4":
        print("Received request for test 4")
        socket.send(b"Ran Test 4")
    else:
        socket.send(b"Did not run a test")
    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    # socket.send(b"World")