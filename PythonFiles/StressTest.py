import logging, time
import multiprocessing as mp

from PythonFiles.utils.REQClient import REQClient

FORMAT = '%(asctime)s|%(levelname)s|%(message)s|'
logging.basicConfig(filename="/home/hgcal/WagonTest/WagonTestGUI/PythonFiles/logs/StressTest.log", filemode = 'w', format=FORMAT, level=logging.DEBUG)

class StressTest():
    def __init__(conn, queue):
        test_active = False
        try:
            while 1 > 0:
                if test_active == False:
                    req_client = REQClient("STRESS", "000000", "STRESS")
                    test_active = True
                    while 1 > 0:
                        try:
                            if not queue.empty():    
                                logging.info("TestInProgressScene: Waiting for queue objects...")
                                text = queue.get()
                                logging.info("Message: %s" % text)
                                if text == "Run completed":
                                    logging.info("Run complete. Beginning next run...")
                                    test_active = False                
                            else:
                                time.sleep(.01)
                        except Exception as e:
                            logging.error(e)
                            logging.error("An error has occurred inside the nested while loop.")
                else:
                    pass
        except Exception as e:
            logging.error(e)
            logging.error("An error has occurred in the outer while loop.")