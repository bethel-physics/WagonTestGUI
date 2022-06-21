import zmq, threading, time

class SUBClient():

    def __init__(self):
        self.message = ""
        pass

    # Creates a thread to start listening for the print statements
    def create_client(self):
        self.listen_thread = threading.Thread(target = self.listen_for_prints())
        self.listen_thread.daemon = True
        self.listen_thread.start()

    def listen_for_prints(self):
        # signal.signal(signal.SIGINT, signal.SIG_DFL)
        cxt = zmq.Context()
        listen_socket = cxt.socket(zmq.SUB)
        listen_socket.connect("tcp://localhost:5556")
        listen_socket.setsockopt(zmq.SUBSCRIBE, b'print')

        while 1 > 0:
            self.message = listen_socket.recv_multipart()
        
            if self.message == True:
                try:
                    self.message = self.message.decode("UTF-8")
                except:
                    self.message = "Message decode failed"
            else:
                self.message = "self.message != True"


    def get_message(self):
        return self.message

    def set_message(self, string):
        self.message = string



