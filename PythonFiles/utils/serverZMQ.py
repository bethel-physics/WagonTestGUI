#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print ("started")

try:
    while True:
        #  Wait for next request from client
        # string = socket.recv_string().lower()
        message = socket.recv()
        print("Received request: %s" % message)

        if message == b"Test1":
            print("Received request for test 1")
            time.sleep(3)
            socket.send(b"Unknown Error")

        elif message == b"Test2":
            print("Received request for test 2")
            time.sleep(3)
            current_JSON_file = open("./PythonFiles/utils/testingJSON.JSON")
            current_JSON_data = json.load(current_JSON_file)

            json_string = json.dumps(current_JSON_data)
            json_byte_string = bytes(json_string,'UTF-8')

            print(json_string)
        
            socket.send(json_byte_string)

        elif message == b"Test3":
            print("Received request for test 3")
            time.sleep(3)
            socket.send(b"Test Failed")

        elif message == b"Test4":
            print("Received request for test 4")
            time.sleep(3)
            current_JSON_file = open("./PythonFiles/utils/testingJSON.JSON")
            current_JSON_data = json.load(current_JSON_file)

            json_string = json.dumps(current_JSON_data)
            json_byte_string = bytes(json_string,'UTF-8')

            print(json_string)
        
            socket.send(json_byte_string)
        else:
            socket.send(b"Invalid request.")

except KeyboardInterrupt:
    print("Closing the server...")
    socket.close()
    context.term()