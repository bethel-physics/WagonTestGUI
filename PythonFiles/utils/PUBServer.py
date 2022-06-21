# Importing necessary modules
import zmq, threading, signal


class PUBServer():

    def __init__(self):
        pub_thread = threading.Thread(target = self.run_server())
        pub_thread.daemon = True
        pub_thread.start()

    def run_server():
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        cxt = zmq.Context()
        pub_socket = cxt.socket(zmq.PUB)
        pub_socket.bind("tcp://localhost:5556")


        # Need to send a message that tells clients the topic before the payload (every message is 2 messages)
pub_server = PUBServer()
