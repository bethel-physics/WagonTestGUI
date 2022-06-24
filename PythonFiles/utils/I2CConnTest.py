import time


class I2CConnTest():

    def __init__(self, conn):
        time.sleep(1)
        conn.send("One")
        time.sleep(2)
        conn.send("Two")
        time.sleep(2)
        conn.send("Three")
        time.sleep(2)
        conn.send("Done.")