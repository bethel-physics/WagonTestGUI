from Servers import SubscribeServer
import json

sub = SubscribeServer()

while True:
    topic, msg = sub.recv()
    if msg and topic == "print":
        print(msg)
    elif msg and topic == "json":
        with open("./example.json","w") as f:
            f.write(msg)
        f.close()
        break
    else:
        pass
