from Servers import SubscribeServer

sub = SubscribeServer()

while True:
    msg = sub.recv()
    if msg:
        print(msg)
    else:
        pass
