#!/TestingEnv/bin/python

# Including information about both Engine and Wagon GUIs


# Need to make the log file path before any imports
import os
guiLogPath = "/home/{}/GUILogs/".format(os.getlogin())

if not os.path.exists(guiLogPath):
    os.makedirs(guiLogPath)

# Importing necessary modules
import multiprocessing as mp
import socket
# Imports the GUIWindow
from PythonFiles.GUIWindow import GUIWindow
from PythonFiles.utils.SUBClient import SUBClient
from PythonFiles.update_config import update_config
import sys
import logging

# Creates a task of creating the GUIWindow
def task_GUI(conn, queue, board_cfg):
    # creates the main_window as an instantiation of GUIWindow
    main_window = GUIWindow(conn, queue, board_cfg)

# Creates a task of creating the SUBClient
def task_SUBClient(conn, queue):
    # Creates the SUBSCRIBE Socket Client
    try:
        sub_client = SUBClient(conn, queue)
    except Exception as e:
        print("\n\n\n\n\nUh oh... an exception has been found...")
        print("Exception: {}\n\n\n".format(e))
        print("It looks like this has something to do with the SUBClient's instantiation\n\n") 

def run(board_cfg):    
    # Creates a Pipe for the SUBClient to talk to the GUI Window
    conn_SUB, conn_GUI = mp.Pipe()

    queue = mp.Queue()

    logging.FileHandler(guiLogPath + "gui.log", mode='a')

    # Turns creating the GUI and creating the SUBClient tasks into processes
    process_GUI = mp.Process(target = task_GUI, args=(conn_GUI, queue, board_cfg))
    process_SUBClient = mp.Process(target = task_SUBClient, args = (conn_SUB, queue,))
    

    # Starts the processes
    process_GUI.start()
    process_SUBClient.start()

    # Should hold the code at this line until the GUI process ends
    process_GUI.join()

    try:
        conn_SUB.close()
        conn_GUI.close()
    except:
        print("Pipe close is unnecessary.")

    try:
        # Cleans up the SUBClient process
        process_SUBClient.terminate()
    except:
        print("Terminate is unnecessary.")
        pass


def board_config(sn):

    board_cfg = None
    
    if sn == None:
        if any(node in y for y in  wagon_GUI_computers):
            from TestConfigs.Wagon_cfg import masterCfg

            print("Hostname setup for wagon testing. Initializing Wagon Test GUI...")

            board_cfg = masterCfg
        
        if any(node in y for y in engine_GUI_computers):
            from TestConfigs.Engine_cfg import masterCfg

            print("Hostname setup for engine testing. Initializing Engine Test GUI...")

            board_cfg = masterCfg


        run(board_cfg)

    else:
        update_config(sn)
def main(args):
    pass

if __name__ == "__main__":

    if sys.argv[1] is not None:
        config_path = sys.argv[1]
        print(config_path)
        exit(0)

    curpath = os.path.abspath(os.curdir)
    print( "Current path is: %s" % (curpath))

    node = socket.gethostname()
    print(socket.gethostname())
    wagon_GUI_computers = [
        "cmsfactory1.cmsfactorynet",
        "cmsfactory5.cmsfactorynet",
        "cmslab4.umncmslab",
        "cmsfactory2.cmsfactorynet",
    ]
    engine_GUI_computers = [
        "cmsfactory4.cmsfactorynet",
    ]

    board_config(None)
   
