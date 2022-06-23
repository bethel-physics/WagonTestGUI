#####################################################################
#                                                                   #
#  This code creates a server to be housed locally on the testing   #
#       station (at the moment this would be the raspberry pi)      #
#                                                                   #
#####################################################################

## MAYBE TURN THIS INTO A CLASS THAT IS INSTANTIATED IN THIS FILE ##

# importing necessary modules
from asyncore import write
import time, zmq, json
import multiprocessing as mp
from tkinter import NONE
# Should contain imports for the test scripts
from GenResTest import GenResTest
from PUBServer import PUBServer

# Makes the REPServer a class
class REPServer():

    def __init__(self):
        self.output = None
        
        # Creates a context class which contains the method to create a socket.
        cxt = zmq.Context()
        socket = cxt.socket(zmq.REP)

        # Server-side for talking to a network point. "Bind"   ## socket.connect() is only used for CLIENTS
        socket.bind("tcp://*:5555")

        print ("Reply Server has started.")
        time.sleep(1)


        try:
            # Sets up an infinite loop so the server is always on until a keyboard interrupt occurs
            while 1>0:
                #  Wait for next request from client
                # string = socket.recv_string().lower()
                print("Wating for request...")
                message = socket.recv_string().lower()
                print("Received request: %s " % message)


                # Testing to see what the request sent to the server was. The only requests we
                # care about are test1, test2, test3, & test4. Anything else will send back 
                # "invalid request" to the client.
                if message == "test1":

                    socket.send(b"Request receieved for Test 1. Starting test.")
                    self.begin_processes(message)
                    message = ''               
                    
                elif message == "test2":
                    print("Received request for test 2")

                    # Simulates the test running
                    # test2 = run_test2()
                    # test2.run_test()
                    time.sleep(3)

                    # Test code to ensure json/text sending is working correctly
                    current_JSON_file = open("./PythonFiles/utils/testingJSON.JSON")
                    current_JSON_data = json.load(current_JSON_file)

                    json_string = json.dumps(current_JSON_data)
                    json_byte_string = bytes(json_string,'UTF-8')

                    print(json_string)
                
                    socket.send(json_byte_string)

                elif message == "test3":
                    print("Received request for test 3")

                    # Simulates the test running
                    # test3 = run_test3()
                    # test3.run_test()
                    time.sleep(3)

                    # Test code to ensure json/text sending is working correctly
                    socket.send(b"Test Failed")

                elif message == "test4":
                    print("Received request for test 4")

                    # Simulates the test running
                    # test4 = run_test4()
                    # test4.run_test()
                    time.sleep(3)

                    # Test code to ensure json/text sending is working correctly
                    current_JSON_file = open("./PythonFiles/utils/testingJSON.JSON")
                    current_JSON_data = json.load(current_JSON_file)

                    json_string = json.dumps(current_JSON_data)
                    json_byte_string = bytes(json_string,'UTF-8')

                    print(json_string)
                
                    socket.send(json_byte_string)

                else:
                    socket.send(b"Invalid request.")

        # Keyboard interrupt with ZMQ has a bug when on BOTH Windows AND Python at the same time.
        # This code should allow for CTRL + C interrupt for the server on any non-windows system.
        except KeyboardInterrupt:
            print("Closing the server...")
            socket.close()
            cxt.term()

    # def passive_fxn(self):

    #     while 1>0:
    #         if self.output:
    #             try:
    #                 try:
    #                     write_function = open('./PythonFiles/utils/SERVER-MESSAGE-QUEUE.txt', 'a')
    #                     write_function.write(self.output)
    #                     write_function.close()
    #                 except:
    #                     break
    #             except:
    #                 pass
    #             self.output = None
    #         elif self.output == "Done.":
    #             try:
    #                 try:
    #                     write_function = open('./PythonFiles/utils/SERVER-MESSAGE-QUEUE.txt', 'a')
    #                     write_function.write(self.output)
    #                     write_function.close()
    #                 except:
    #                     break
    #             except:
    #                 pass
    #             self.output = None
    #             break
    #         else:
    #             time.sleep(.5)


    #         try:
    #                 try:
    #                     write_function = open('./PythonFiles/utils/SERVER-MESSAGE-QUEUE.txt', 'a')
    #                     write_function.write(self.output)
    #                     write_function.close()
    #                 except:
    #                     break
    #         except:
    #             pass

    def task_test(self, conn, desired_test):
        if desired_test == 'test1':
            test1 = GenResTest(conn)
        elif desired_test == 'test2':
            pass
        elif desired_test == 'test3':
            pass
        elif desired_test == 'test4':
            pass
        else:
            pass

    def task_PUBServer(self, conn):
        pub_server = PUBServer(conn)

    def begin_processes(self, desired_test):
        print("Starting processes")
        conn_test, conn_PUBServer = mp.Pipe()
        process_test = mp.Process(target = self.task_test, args=(conn_test, desired_test,))
        process_PUBServer = mp.Process(target = self.task_PUBServer, args=(conn_PUBServer,))
        
        process_test.start()
        process_PUBServer.start()

        process_test.join()
        process_PUBServer.join()

        print("Processes have ended.")

try:
    # Instantiates the server        
    REP_Server = REPServer()
except:
    print("REPServer already instantiated")
