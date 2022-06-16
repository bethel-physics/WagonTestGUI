from utils.clientZMQ import ClientZMQ

# Creates a main function to initialize the GUI
def main():
    client1 = ClientZMQ(b"Test1")
    client2 = ClientZMQ(b"Test2")
    

if __name__ == "__main__":
    main()