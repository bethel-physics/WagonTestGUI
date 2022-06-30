import string    
import random 
from random import randint


class StressScript():
    def __init__(self, conn):
        test_length = randint(500,1500)
        i = 0
        while i < test_length:
            S = 10  
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
            conn.send(ran)
            i += 1
        conn.send("Done.")
        conn.send("Run completed")
        