import subprocess
from subprocess import PIPE

def read_barcode():
    print("Scan barcode now (CTRL-C to exit):")
    p = subprocess.Popen(["/usr/share/zebra-scanner/samples/console-app/bin/corescanner-console-app"], stdout=PIPE)

    output = p.communicate()[0]

    begin = output.find("<datalabel>") + len("<datalabel>")
    end = output.find("</datalabel>")

    raw_hex = output[begin:end].replace(" ","")

    payload = bytearray.fromhex(raw_hex).decode()

    print(payload)

    return "3203" + payload

if __name__ == "__main__":
    read_barcode()
