# Importing necessary modules
import zmq, threading, signal, time


class PUBServer():

    def __init__(self, conn):
        self.conn = conn
        print("Publish Server starting up...")
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        cxt = zmq.Context()
        pub_socket = cxt.socket(zmq.PUB)
        pub_socket.bind("tcp://*:5556")

        # try:
        while 1 > 0:
        # try:
            prints = conn.recv()
            if prints == "Done.":
                prints = "print ; " + prints
                # prints_byte_string = bytes(prints, 'UTF-8')  
                pub_socket.send_string(prints)
                break
            else:
        # try:
                prints = "print ; " + prints
                # prints_byte_string = bytes(prints, 'UTF-8')  
                pub_socket.send_string(prints)

            time.sleep(1)

        print("PUBServer Closing")    
        pub_socket.close()
        
        # except:
        #     print("Failed to convert to bytes.")
        #     pass

                    # Sanity Check
                    # print("I have sent the information")

                    # Wait 1 second before trying again
           

                # except:
                #     print("Waiting for messages to be added to the queue...")
                #     time.sleep(5)

        # except KeyboardInterrupt:
        #     print("Closing the server...")
        #     pub_socket.close()
        #     cxt.term()


