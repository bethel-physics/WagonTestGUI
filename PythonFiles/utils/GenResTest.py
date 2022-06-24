import time


class GenResTest():

    def __init__(self, conn):
        for i in range(10):
            conn.send("Run:"+ str(i))
            time.sleep(0.25)

        conn.send("Done.")