# Class for monitoring requests from nodes and sending DB data back from cmslab3

import requests
import json
import socket
import zmq
import sys
from SSHTunnel import Tunnel
from DBSender import DBSender

sys.path.append("../")
sys.path.append("../../TestConfigs/")

from GUIConfig import GUIConfig
import Engine_cfg
import Wagon_cfg

class DBSendServer():
    
    def __init__(self, board_type):

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:5555")

        if board_type == "wagon":
            gui_cfg = GUIConfig(Wagon_cfg.masterCfg)
        elif board_type == "engine":
            gui_cfg = GUIConfig(Engine_cfg.masterCfg)

        # Create DB sender object
        self.db = DBSender(gui_cfg)

        # Create SSHTunnel (password and username prompt)
        self.tunnel = Tunnel()

        print("Server created!")

        self.loop()

    def loop(self):
        
        while True:
            message = self.socket.recv().decode('utf-8')
            print("Received request: {}".format(message))

            response = json.dumps(self.handle_request(message))

            self.socket.send_string(response)

    def handle_request(self, message):

        # Reference DB sender to determine what the inputs are
        # All inputs are given after the semi-colon in the request
        # loads the json and use this to call DBSender functions
        rep = None
        if ";" in message:
            argstr = message.split(";")[1]
            args = json.loads(argstr)

        if "add_new_user_ID" in message:
            rep = self.db.add_new_user_ID(args["user_ID"], args["passwd"])

        if "get_usernames" in message:
            rep = self.db.get_usernames()

        if "get_test_completion_staus" in message:
            rep = self.db.get_test_completion_staus(args["serial_number"])

        if "get_previous_test_results" in message:
            rep = self.db.get_previous_test_results(args["serial_number"])

        if "add_new_board" in message:
            rep = self.db.add_new_board(args["sn"])

        if "is_new_board" in message:
            rep = self.db.is_new_board(args["sn"])

        if "add_board_info" in message:
            rep = self.db.add_board_info(args["info"])

        if "add_initial_tests" in message:
            rep = self.db.add_initial_tests(args["results"])

        if "add_general_test" in message:
            rep = self.db.add_general_test(args["results"], args["files"])

        if "add_test_json" in message:
            rep = self.db.add_test_json(args["json_file"], args["datafile_name"])

        if "get_test_list" in message:
            rep = self.db.get_test_list()

        if rep == None:
            print("Bad request...")

        return rep

if __name__ == "__main__":

    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument('--board', type=str, default="wagon", help="Specify which board to start the server for (wagon or engine)")

    args = parser.parse_args()

    serv = DBSendServer(args.board)

