# Importing necessary modules
import zmq, threading, signal, time


class PUBServer():

    def __init__(self):
        pub_thread = threading.Thread(target = self.run_server())
        pub_thread.daemon = True
        pub_thread.start()

    def run_server(self):
        print("Publish Server starting up...")
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        cxt = zmq.Context()
        pub_socket = cxt.socket(zmq.PUB)
        pub_socket.bind("tcp://*:5556")

        try:
            while 1 > 0:
                try:
                    # Open might need to be fixed based on exact pathway to the file
                    ## Doesn't need to change as long as SERVER-MESSAGE-QUEUE stays in
                    ## the same folder as PUBServer

                    # Reads the file
                    with open('./PythonFiles/utils/SERVER-MESSAGE-QUEUE.txt', 'r') as read_function:
                        contents = read_function.read()
                        read_function.close()

                    # Sanity check
                    print(contents)

                    # Makes the file blank
                    with open('./PythonFiles/utils/SERVER-MESSAGE-QUEUE.txt', 'w') as overwrite:
                        overwrite.write('\n')
                        overwrite.close()
                    
                    # Sanity Check
                    # print("I have overwritten the file.")

                    # Sends the contents of the file to the SUB client
                    contents_byte_string = bytes(contents, 'UTF-8')  
                    # print("I have converted the string to bytes")
                    pub_socket.send(b'print')
                    # print('I have sent print')
                    pub_socket.send(contents_byte_string)
                    print('I have sent the contents')

                    # Sanity Check
                    # print("I have sent the information")

                    # Wait 1 second before trying again
                    time.sleep(5)

                except:
                    print("Waiting for messages to be added to the queue...")
                    time.sleep(5)

        except KeyboardInterrupt:
            print("Closing the server...")
            pub_socket.close()
            cxt.term()


        # Need to send a message that tells clients the topic before the payload (every message is 2 messages)
pub_server = PUBServer()
