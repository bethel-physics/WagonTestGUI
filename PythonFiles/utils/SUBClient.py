# Importing necessary modules
import zmq, logging
import PythonFiles
import os

logger = logging.getLogger('HGCALTestGUI.PythonFiles.utils.SUBClient')

#FORMAT = '%(asctime)s|%(levelname)s|%(message)s|'
#logging.basicConfig(filename="/home/{}/GUILogs/gui.log".format(os.getlogin()), filemode = 'a', format=FORMAT, level=logging.INFO)


# Creating a class for the SUBSCRIBE socket-type Client
class SUBClient():

    def __init__(self, conn, queue, gui_cfg):
        with open("{}/utils/server_ip.txt".format(PythonFiles.__path__[0]), "r") as openfile:
            grabbed_ip = openfile.read()[:-1]
        logger.info("SUBClient has started") 
        # Instantiates variables       
        self.conn = conn
        self.message = ""

        self.SUB_ZMQ(conn, queue, gui_cfg)

    # Responsible for listening for ZMQ messages from teststand
    def SUB_ZMQ(self, conn, queue, gui_cfg):
        grabbed_ip = gui_cfg["TestHandler"]["remoteip"]
        # Creates the zmq.Context object
        cxt = zmq.Context()
        # Creates the socket as the SUBSCRIBE type
        listen_socket = cxt.socket(zmq.SUB)
        listen_socket.connect("tcp://{ip_address}:5556".format(ip_address = grabbed_ip))
        # Sets the topics that the server will listen for
        listen_socket.setsockopt(zmq.SUBSCRIBE, b'print')
        listen_socket.setsockopt(zmq.SUBSCRIBE, b'JSON')

        try:
            while 1 > 0:
                # Splits up every message that is received into topic and message
                # the space around the semi-colon is necessary otherwise the topic and messaage
                # will have extra spaces.
                try:
                    print("Waiting")
                    self.topic, self.message = listen_socket.recv_string().split(" ; ")
                    print(self.topic, self.message)
                except Exception as e:
                    print("\nThere was an error trying to get the topic and/or message from the socket\n")
                    logger.info("SUBClient: There was an error trying to get the topic and/or message from the socket")
                                     

                poller = zmq.Poller()
                poller.register(listen_socket, zmq.POLLIN)
                #if not poller.poll(7*1000):
                #    print("Poller being bad")
                #    
                #    raise Exception("The SUBClient has failed to receive a topic and message")

                logger.debug("The received topic is: %s" % self.topic)
                logger.debug("The received message is: %s" % self.message)

                # Tests what topic was received and then does the appropriate code accordingly
                if self.topic == "print":

                    # Places the message in the queue. the queue.get() is in 
                    # TestInProgressScene's begin_update() method
                    queue.put(self.message)
                    logger.debug("SUBClient: The print message has been placed into the queue.")

                elif self.topic == "JSON":
                    
                    # Places the message in the queue. the queue.get() is in 
                    # TestInProgressScene's begin_update() method
                    queue.put("Results received successfully.")
                    logger.info("SUBClient: Informed the user that the results have been received.")

                    # Sends the JSON to GUIWindow on the pipe.
                    self.conn.send(self.message)
                    logger.info("SUBClient: The JSON has been sent to the GUIWindow along the pipe.")

                elif self.topic == "LCD":
                    logger.info("SUBClient: The topic of LCD has been selected. This method is empty")
                    pass

                else:
                    logger.error("SUBClient: Invalid topic sent. Must be 'print' or 'JSON'.")

                    # Places the message in the queue. the queue.get() is in 
                    # TestInProgressScene's begin_update() method
                    queue.put("SUBClient: An error has occurred. Check logs for more details.")

        except Exception as e:
            print("Outer Try: {}".format(e))
            logger.debug(e)
            logger.critical("SUBClient: SUBClient has crashed. Please restart the software.")
