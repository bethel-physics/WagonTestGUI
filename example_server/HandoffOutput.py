from EmulateTest import run_test
from multiprocessing import Process, Pipe
from Servers import PublishServer

import time

def listener(conn):
    pub = PublishServer()

    print("Starting listener in a separate process")
    while True:
        output = parent_conn.recv()
        if output.find("{") is not -1:
            pub.send("json",output)
            return
        elif output:
            pub.send("print",output)
        else:
            return
        time.sleep(0.01)

parent_conn, child_conn = Pipe()
p1 = Process(target=run_test, args=(child_conn,))
p2 = Process(target=listener, args=(parent_conn,))

print("Starting Test Now...")

p1.start()
p2.start()

p1.join()
p2.join()

print("Ending Test")
