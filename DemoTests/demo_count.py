import time

# Simple test counting from 1 to 10 for demo purposes
# This is an example of how a test can be written to run locally
class count:

    def __init__(self):
        self.run_test()


    def run_test(self):
        print("Beginning count test:")

        for i in range(1,11):
            print(i)
            time.sleep(1)

        print("Test completed")

        return True


count()
