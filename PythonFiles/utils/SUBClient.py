import zmq

class SUBClient():

    def __init__(self, conn, queue):
        self.conn = conn
        print("SUBClient has started")
        self.message = ""
        cxt = zmq.Context()
        listen_socket = cxt.socket(zmq.SUB)
        listen_socket.connect("tcp://localhost:5556")
        # Sets the topics that the server will listen for
        listen_socket.setsockopt(zmq.SUBSCRIBE, b'print')
        listen_socket.setsockopt(zmq.SUBSCRIBE, b'JSON')

        while 1 > 0:
            # Splits up every message that is received into topic and message
            # the space around the semi-colon is necessary otherwise the topic and messaage
            # will have extra spaces.
            self.topic, self.message = listen_socket.recv_string().split(" ; ")
            # Tests what topic was received and then does the appropriate code accordingly
            if self.topic == "print":

                # DEBUG
                print(self.topic)
                print(self.message)
                # END DEBUG

                # Places the message in the queue. the queue.get() is in 
                # TestInProgressScene's begin_update() method
                queue.put(self.message)
            elif self.topic == "JSON":

                # DEBUG
                print("JSON Received.")
                # END DEBUG

                # Places the message in the queue. the queue.get() is in 
                # TestInProgressScene's begin_update() method
                queue.put("JSON Received.")
            else:
                
                # DEBUG
                print("Invalid topic sent. Must be 'print' or 'JSON'.")
                # END DEBUG

                # Places the message in the queue. the queue.get() is in 
                # TestInProgressScene's begin_update() method
                queue.put("Invalid topic sent. Must be 'print' or 'JSON'.")