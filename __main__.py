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
from PythonFiles.utils.LocalHandler import LocalHandler
import sys
import logging
import yaml

# Creates a task of creating the GUIWindow
def task_GUI(conn, conn_trigger, queue, board_cfg):
    # creates the main_window as an instantiation of GUIWindow
    main_window = GUIWindow(conn, conn_trigger, queue, board_cfg)

# Creates a task of creating the SUBClient
def task_SUBClient(conn, queue, board_cfg):
    # Creates the SUBSCRIBE Socket Client
    #try:
    sub_client = SUBClient(conn, queue, board_cfg)
    #except Exception as e:
    #    print("\n\n\n\n\nUh oh... an exception has been found...")
    #    print("Exception: {}\n\n\n".format(e))
    #    print("It looks like this has something to do with the SUBClient's instantiation\n\n") 

def task_LocalHandler(gui_cfg, conn_trigger):

    LocalHandler(gui_cfg, conn_trigger)

def task_SSHHandler(gui_cfg):

    SSHHandler(gui_cfg)

def run(board_cfg):    
    # Creates a Pipe for the SUBClient to talk to the GUI Window
    conn_SUB, conn_GUI = mp.Pipe()

    # Create another pipe to trigger the tests when needed
    if board_cfg["TestHandler"]["name"] != "ZMQ":
        conn_trigger_GUI, conn_trigger_Handler = mp.Pipe()
        
    queue = mp.Queue()

    logging.FileHandler(guiLogPath + "gui.log", mode='a')

    # Turns creating the GUI and creating the SUBClient tasks into processes
    if board_cfg["TestHandler"]["name"] == "Local":
        process_GUI = mp.Process(target = task_GUI, args=(conn_GUI, conn_trigger_GUI, queue, board_cfg))
        process_Handler = mp.Process(target = task_LocalHandler, args=(board_cfg, conn_trigger_Handler))
    elif board_cfg["TestHandler"]["name"] == "SSH":
        process_GUI = mp.Process(target = task_GUI, args=(conn_GUI, conn_trigger_GUI, queue, board_cfg))
        process_Handler = mp.Process(target = task_LocalHandler, args=(board_cfg, conn_trigger_Handler))
    else: 
        process_GUI = mp.Process(target = task_GUI, args=(conn_GUI, None, queue, board_cfg))
    process_SUBClient = mp.Process(target = task_SUBClient, args = (conn_SUB, queue, board_cfg))

    # Starts the processes
    process_GUI.start()
    if board_cfg["TestHandler"]["name"] == "Local":
        process_Handler.start()
    process_SUBClient.start()

    # Should hold the code at this line until the GUI process ends
    process_GUI.join()

    try:
        conn_SUB.close()
        conn_GUI.close()
        conn_trigger_GUI.close()
        conn_trigger_Handler.close()
    except:
        print("Pipe close is unnecessary.")

    try:
        # Cleans up the SUBClient process
        process_SUBClient.terminate()
        process_Handler.kill()
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

def import_yaml(config_path):

    return yaml.safe_load(open(config_path,"r"))

def main(args):
    pass

if __name__ == "__main__":

    try:
        if sys.argv[1] is not None:
            config_path = sys.argv[1]
            print(config_path)
    except:
        print("Opting for custom configuration setup called below")
        config_path = None

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

    if config_path is not None:
        board_cfg = import_yaml(config_path)

        run(board_cfg)
    else:
        board_config(None)
   