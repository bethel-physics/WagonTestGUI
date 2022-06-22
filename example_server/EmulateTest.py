# Fake test that will print a bunch of output as if it is running a test

import time

def run_test(conn):
    for i in range(0, 100):
        conn.send("Test output for {}".format(i))
        time.sleep(0.1)

    conn.close()
