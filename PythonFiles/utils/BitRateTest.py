import time, json


class BitRateTest():

    def __init__(self, conn):
        time.sleep(1)
        conn.send("One")
        time.sleep(2)
        conn.send("Two")
        time.sleep(2)
        conn.send("Three")
        time.sleep(2)
        conn.send("Done.")
        # Test code to ensure json/text sending is working correctly
        current_JSON_file = open("./PythonFiles/JSONFiles/testingJSON.JSON")
        current_JSON_data = json.load(current_JSON_file)
        json_string = json.dumps(current_JSON_data)
        print(json_string)
        conn.send(json_string)