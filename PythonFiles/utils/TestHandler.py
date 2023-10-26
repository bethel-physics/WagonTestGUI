import yaml

# Class designed to identify and execute tests in a manner specified by the config file
# Three possible handlers are currently available:
#   - Local: Tests will be run on the current machine
#   - SSH: Tests will be run on another machine via SSH (key access required)
#   - ZMQ: Tests will be run on another machine/test stand via ZMQ requests (Some assembly required)
class TestHandler:

    def __init__(self, config):

        

