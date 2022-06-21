# File to quickly start a client. Unnecessary file to be deleted at final stages of development

from utils.REQClient import REQClient

# Creates a main function to initialize the GUI
def main():
    client1 = REQClient()
    client1.run_test_thread(b"test1")
    

if __name__ == "__main__":
    main()