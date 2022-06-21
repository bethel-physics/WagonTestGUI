
import zmq, threading, signal

class SUBClient():

    def __init__(self):
        pass

    # Creates a thread to start listening for the print statements
    def create_client(self):
        self.listen_thread = threading.Thread(target = self.listen_for_prints())
        self.listen_thread.daemon = True
        self.listen_thread.start()

    def listen_for_prints(self):
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        cxt = zmq.Context()
        sub_socket = cxt.Socket(zmq.SUB)
        sub_socket.connect("tcp://localhost:5556")
        sub_socket.setsockopt(zmq.SUBSCRIBE, b'print')

        self.message = sub_socket.recv_multipart()
        
        try:
            if self.message == True:
                try:
                    self.message = self.message.decode("UTF-8")
                except:
                    self.message = "Message decode failed"
        except:
            pass

    def get_message(self):
        return self.message

