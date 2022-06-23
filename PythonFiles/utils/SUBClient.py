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
        listen_socket.setsockopt(zmq.SUBSCRIBE, b'JSON')

        while 1 > 0:
            self.topic, self.message = listen_socket.recv_string().split(" ; ")
            if self.topic == "print":
                print(self.topic)
                print(self.message)
                queue.put(self.message)
            elif self.topic == "JSON":
                print("JSON Received.")
                queue.put("JSON Received.")



    def get_message(self):
        return self.message

    def set_message(self, string):
        self.message = string



