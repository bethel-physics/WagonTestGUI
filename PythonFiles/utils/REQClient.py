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
        
        print("Before send")
        # Tell the server what test to run
        socket.send_string(sending_msg)
        
        print("After send")

        # Timeout feature for the socket
        # The poller is responsible for stopping the socket send after a certain time
        # Poller is in milliseconds
        #poller = zmq.Poller()
        #poller.register(socket, zmq.POLLIN)
        #if not poller.poll(6*1000):   
        #    raise IOError("Timeout processing the REQClient request from socket")
            

        print("After poller")

        logging.debug("REQClient: Request sent. Waiting for confirmation receipt...")
        # Get the reply
    
        # Recording the number of tries to open the socket and receive a string
        tries = 0


        REQUEST_TIMEOUT = 2500
        REQUEST_RETRIES = 3
        # socket.connect("tcp://{ip_address}:5555".format(ip_address = grabbed_ip))

        retries_left = REQUEST_RETRIES
        while (len(self.message)< 1) and tries < 1000:
            
            try:
                #print("\nTrying to receive a message from the socket")
                #logging.debug("REQClient: Trying to receive a message from the socket receive")
                #self.message = socket.recv_string()
                #print("\n\n\nSelf.message: {}\n\n\n".format(self.message))

                if(socket.poll(REQUEST_TIMEOUT) &  zmq.POLLIN) != 0:
                    self.message = socket.recv_string()
                    retries_left = REQUEST_RETRIES
                    print("REQClient: Request received.")
                    logging.info("REQClient: Request received.")
                    break

                retries_left -= 1
                logging.warning("REQClient: No response from server")
                print("\n\nREQCLIENT WARNING: NO RESPONSE FROM THE SERVER\n\n")
                socket.setsockopt(zmq.LINGER, 0)
                socket.close()
                
                # Out of retries
                if retries_left == 0:
                    logging.error("REQClient: Server seems to be offline, abandoning...")
                    print("REQClient: Server seems to be offline, abandoning...")
                    break
                
                logging.info("REQClient: Attempts remaining...Reconnecting to the server...")

                socket = context.socket(zmq.REQ)
                
                socket.connect("tcp://{ip_address}:5555".format(ip_address = grabbed_ip))
        
                logging.info("REQClient: Resending...")

                socket.send_string(sending_msg)
                

            except:
                print("REQClient: couldn't get info - {}".format(tries))
                logging.debug("REQClient: No Message received from the request.")
                tries = tries + 1 
            #messagebox.showerror("No Message Received", "REQClient: No message received from the request.")


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
