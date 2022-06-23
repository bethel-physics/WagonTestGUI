import zmq

class SUBClient():

    def __init__(self, conn, queue):
        self.conn = conn
        print("SUBClient has started")
        self.message = ""
        cxt = zmq.Context()
        listen_socket = cxt.socket(zmq.SUB)
        listen_socket.connect("tcp://localhost:5556")
        listen_socket.setsockopt(zmq.SUBSCRIBE, b'print')

        while 1 > 0:
            self.topic, self.message = listen_socket.recv_string().split(";")
            print(self.message)
            queue.put(self.message)


    def get_message(self):
        return self.message

    def set_message(self, string):
        self.message = string



