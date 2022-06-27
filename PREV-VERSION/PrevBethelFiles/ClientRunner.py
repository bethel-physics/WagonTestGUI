# File to quickly start a client. Unnecessary file to be deleted at final stages of development

from utils.REQClient import REQClient
from utils.SUBClient import SUBClient

# Creates a main function to initialize the GUI
def main():    
    client2 = SUBClient()
    client1 = REQClient()
    client1.run_test_thread(b"test1")


    

if __name__ == "__main__":
    main()