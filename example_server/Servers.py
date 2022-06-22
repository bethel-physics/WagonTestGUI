import zmq

class PublishServer:
    
    def __init__(self):
        ctx = zmq.Context.instance()
        self.pub = ctx.socket(zmq.PUB)
        self.pub.bind("tcp://*:5555")

    def send(self, msg):
        self.pub.send_string(msg.encode('utf-8'))


class SubscribeServer:
    
    def __init__(self):
        ctx = zmq.Context.instance()
        self.sub = ctx.socket(zmq.SUB)
        self.sub.connect("tcp://localhost:5555")
        self.sub.setsockopt(zmq.SUBSCRIBE, b"")


    def recv(self):
        return self.sub.recv_string()
