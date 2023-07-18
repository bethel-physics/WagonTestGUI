import zmq
import json

class DBSendClient():

    def __init__(self):
        self.context = zmq.Context()

        print("Connecting with server...")
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://cmsfactory1.cmsfactorynet:5555")


    def send_request(self, message):

        #print("sending request: {}".format(message))

        self.socket.send_string(message)

        response = json.loads(self.socket.recv())

        #print("Got reply: {}".format(response))
        print(type(response))
    

if __name__ == "__main__":
    client = DBSendClient()

    client.send_request("get_usernames")
