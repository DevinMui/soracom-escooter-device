import requests
import time
from api import API
from scooter import Device

delay = 5
device = Device("f0:81:4f:ae:de:d3")
device.connect()

while True:

    device.getGPS()
    print("Harvesting data")
    print(device.lat)
    print(device.lng)
    json =  API.harvest(device)
    print(json.text)
    time.sleep(5)

device.disconnect()
