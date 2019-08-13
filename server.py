from flask import Flask, escape, request, jsonify

from scooter import Device
from api import API

from time import sleep
from argparse import ArgumentParser
from multiprocessing import Process

app = Flask(__name__)

app.debug = True

parser = ArgumentParser(description='Control Xiaomi M365 and talk to SORACOM and AWS Lambda')
parser.add_argument('-m', '--mac', type=str, required=True, help='Xiaomi M365 bluetooth MAC address') 
args = parser.parse_args()

delayInSec = 5

device = Device(args.mac)
device.connect()

def updateLoop():
    while True:
        res = API.funk(device)
        API.harvest(device)

        sleep(delayInSec)

    device.disconnect()

@app.route('/')
def updateInUse():
    if request.json.inUse:
        device.unlock()    
    else:
        device.lock()
    return jsonify({ 'message': 'device updated' })

if __name__ == '__main__':
    p = Process(target=updateLoop)
    p.start()
    app.run()
    p.join()
