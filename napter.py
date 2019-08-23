from flask import Flask, escape, request, jsonify, render_template

from scooter import Device
from api import API

from time import sleep
from multiprocessing import Process

app = Flask(__name__)

app.debug = True

delayInSec = 5
mac = "f0:81:4f:ae:de:d3"

@app.route('/', methods=['GET', 'POST'])
def home():
    device = Device(mac)
    device.connect()
    device.getGPS()
    if request.method == 'GET':
        device.disconnect()
        return render_template('data.html', device=device)
    elif request.method == 'POST':
        return updateInUse(device)

def updateInUse(device):
    if request.json['inUse']:
        device.unlock()
    else:
        device.lock()
    device.disconnect()
    return jsonify({ 'message': 'device updated' })

@app.route('/lock')
def lock():
    device = Device(mac)
    device.connect()
    device.getGPS()
    device.lock()
    device.disconnect()
    return jsonify({ 'message': 'device updated' })

@app.route('/unlock')
def unlock():
    device = Device(mac)
    device.connect()
    device.getGPS()
    device.unlock()
    device.disconnect()
    return jsonify({ 'message': 'device updated' })

if __name__ == '__main__':
    app.run(host="0.0.0.0")
