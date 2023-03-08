
# Class to handle creation of different types of GUIs based on which board we want to test
# This class will hold all of the frame information and order them accordingly

class GUIConfig():

    # Loads in a config file with board type name
    # Information about board tests and database are stored within the config
    def __init__(self, board_cfg):
        self.board_cfg = board_cfg

        self.configure()


    # Create the GUI instance based off testing information
    def configure(self):

        # Possibly do something special here if need be

        print("Instance of {} GUI created.".format(self.getGUIType()))

    # Get number of tests to define order of scenes and sidebar
    def getNumTest(self):
        return len(self.board_cfg["Test"])

    # Get number of tests to define order of scenes and sidebar
    def getTests(self):
        return self.board_cfg["Test"]

    # Get database info for getting and posting test results
    def getDBInfo(self, key=None):
        if key is None:
            return self.board_cfg["DBInfo"]
        else:
            return self.board_cfg["DBInfo"][key]

    def getGUIType(self):
        return self.board_cfg["GUIType"]


