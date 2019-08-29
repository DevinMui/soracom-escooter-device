# soracom-escooter-app
This repository accompanies the tutorial for building an escooter app using SORACOM services (Link coming soon). You'll need to have also completed the steps in the first article (Link coming soon) to connect the GPS module and SORACOM Air SIM.     
Clone this repository and run the various `.py` files on the Raspberry Pi to see it interact with the electric scooter and your [AWS Lambda functions](https://github.com/DevinMui/soracom-escooter-server). 

## Setup    
You'll need to complete this step once you've cloned the repository. This step mainly consists of downloading packages that aren't already on the Raspberry Pi. All the commands listed below are run in a terminal opened at the root of this directory (i.e. `/{where you cloned}/soracom-escooter-device`).         

1. Install Python 3 and Vim    
  You'll need Python 3 to run the `.py` files. You'll also need to make some edits to the files add your scooter's MAC address. Though you can use any text editor, we recommend Vim.
    - Install Python 3 with     
    ```
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install python3.6
    ```
    - Install Vim with `sudo apt-get install vim`
2. Install additional Python packages
   - Run the following commands
   ```
   pip install -r requirements.txt
   pip install git+https://github.com/AntonHakansson/m365py.git#egg=m365py
   ```
   Python comes with its own package manager `pip` that grabs the neccessary packages for us from `requirements.txt`. The GPS module requires a package off GitHub, so we download it with the second line above.
3. Turn on the GPS module
   - The GPS module needs to be turned on each time you reboot the Raspberry Pi. If you've been following the series of articles and have not powered off your Raspberry Pi, you can skip this step. Otherwise, run the following commands to restart the GPS module.
     ```
     sudo systemctl stop gpsd.socket
     sudo systemctl disable gpsd.socket
     sudo killall gpsd
     sudo systemctl stop gpsd.socket
     sudo systemctl disable gpsd.socket
     sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock
     ```
  4. Change the included MAC address to match your electric scooter's Bluetooth MAC address. If you need to find the MAC address again, power on the scooter and run `sudo python3 -m m365py`.    
     - Using a text editor, change line 7 in `harvest.py` and `funk.py` to `mac = "{YOUR MAC ADDRESS}"`
     - Using a text editor, change line 14 in `napter.py` to `mac = "{YOUR MAC ADDRESS}"`
    
**Congratulations!** Your Raspberry Pi is now ready.

## Explanation of the Python files
  #### `api.py`
  This file helps package eScooter data before it is sent to SORACOM Harvest or Funk. Though you won't be interacting with this file directly, it is used in both `harvest.py` and `funk.py` to create HTTP requests.
  #### `funk.py`
  This file communicates with SORACOM Funk, which allows data to be sent securely to AWS (or another clou provider) without much setup. You'll set up the endpoint for Funk and run this file in the third part of the series.
  #### `harvest.py`
  This file communicates with SORACOM Harvest, which collects data sent through the SIM card. It packages eScooter data neatly in a JSON object in an HTTP request before sending it to the Harvest endpoint. You'll set up Harvest (and its visualization with Lagoon) in the second part of the series.
  #### `napter.py`
  This file enables Napter on the Raspberry Pi. It exposes a Flask server, which can be accessed remotely by a specific range of IP addresses. It will let you lock and unlock the eScooter remotely. The pages created by the server will let you see eScooter data and commands through a web browser. You'll set up Napter and run this file in the fourth part of the series.
  #### `requirements.txt`
  This file is created by Python's package manager `pip`. It organizes required packages and their versions into a single file so that installing them during setup is easy. Simply ask `pip` to install it with `pip install -r requirements.txt`. 
  #### `scooter.py`
  This file exposes a `Device` class for managing the electric scooter. It uses [the m365 module](https://github.com/AntonHakansson/m365py) to connect to the scooter, retrieve data, and send commands through Bluetooth. Though you won't be interacting with this file directly, it is used in the other Python files to manage the eScooter.
  #### `/templates/`
  This folder contains HTML documents which are rendered by the Flask server created by `napter.py`.
  
