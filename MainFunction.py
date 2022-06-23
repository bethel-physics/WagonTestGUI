# Importing necessary modules
from audioop import mul
import multiprocessing as mp
import time
from numpy import multiply
# Imports the GUIWindow
from PythonFiles.GUIWindow import GUIWindow
from PythonFiles.utils.SUBClient import SUBClient
from PythonFiles.CreateConsole import OutputConsole



# Creates a task of creating the GUIWindow
def task_GUI(conn, queue):
    # creates the main_window as an instantiation of GUIWindow
    main_window = GUIWindow(conn, queue)
    # print("object sent")

# Creates a task of creating the SUBClient
def task_SUBClient(conn, queue):
    # Creates the SUBSCRIBE Socket Client
    sub_client = SUBClient(conn, queue)

# def task_Console(conn):
#     print("console code started")
#     time.sleep(2)
#     object = conn.recv()
#     print("object received")
#     console = OutputConsole(conn, object)

def run():    
    # Creates a Pipe for the SUBClient to talk to the GUI Window
    conn_SUB, conn_GUI = mp.Pipe()

    queue = mp.Queue()

    # Turns creating the GUI and creating the SUBClient tasks into processes
    process_GUI = mp.Process(target = task_GUI, args=(conn_GUI, queue,))
    process_SUBClient = mp.Process(target = task_SUBClient, args = (conn_SUB, queue,))
    # process_console = mp.Process(target = task_Console, args=(conn_GUI,))
    

    # Starts the processes
    process_GUI.start()
    process_SUBClient.start()
    # process_console.start()

    # Should hold the code at this line until the GUI process ends
    process_GUI.join()

    try:
        # Cleans up the SUBClient process
        process_SUBClient.terminate()
    except:
        print("Terminate is unnecessary.")
        pass
    # try:
    #     # Cleans up the Console process
    #     # process_console.terminate()
    # except:
    #     print("Terminate is unnecessary.")
    #     pass

if __name__ == "__main__":
    run()