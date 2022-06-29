import requests
import json
# from read_barcode import read_barcode


class DBSender():

    def __init__(self) :
        pass


    def add_new_board(sn):
        r = requests.post('http://cmslab3.umncmslab/~cros0400/cgi-bin/add_module2.py', data={"serial_number": str(sn)})

    def add_board_info(info):
        r = requests.post('http://cmslab3.umncmslab/~cros0400/cgi-bin/add_board_info2.py', data = info)
    
    def add_initial_tests(results):
        r = requests.post('http://cmslab3.umncmslab/~cros0400/cgi-bin/add_init_test.py', data = results)
        
    def add_general_test(results, files):
        r = requests.post('http://cmslab3.umncmslab/~cros0400/cgi-bin/add_test2.py', data = results, files=files)

    def add_test_json(json_file, files):
        results = json.load(open(json_file))
        r = requests.post('http://cmslab3.umncmslab/~cros0400/cgi-bin/add_test_json.py', data = results, files = files)

    def get_test_list():
        r = requests.get('http://cmslab3.umncmslab/~cros0400/cgi-bin/get_test_types.py')

        lines = r.text.split('\n')

        begin = lines.index("Begin") + 1
        end = lines.index("End")

        tests = []

        for i in range(begin, end):
            temp = lines[i][1:-1].split(",")
            temp[0] = str(temp[0][1:-1])
            temp[1] = int(temp[1])
            tests.append(temp)

        return tests

    def verify_person(name):
        r = requests.post('http://cmslab3.umncmslab/~cros0400/cgi-bin/verify_person.py', data={'name': name})

        lines = r.text.split('\n')

        begin = lines.index("Begin") + 1
        end = lines.index("End")

        person_id = lines[begin]

        return person_id

    #add_test_json("example.json", {"attach1": open("test.txt","rb")})
