import time, json


class IDResTest():

    def __init__(self, conn):
        for i in range(10):
            conn.send("Run:"+ str(i))
            time.sleep(0.25)

        conn.send("Done.")
        time.sleep(0.25)
        # Test code to ensure json/text sending is working correctly
        current_JSON_file = open("./PythonFiles/JSONFiles/testingJSON.JSON")
        current_JSON_data = json.load(current_JSON_file)
        json_string = json.dumps(current_JSON_data)
        print(json_string)
        conn.send(json_string)