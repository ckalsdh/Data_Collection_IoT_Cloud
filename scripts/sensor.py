##################################
# script to run IN Termux
##################################
import requests, json, time
from pimux import scrip

from dotenv import load_dotenv
import os

load_dotenv()

# SSH connection details
HOST = os.getenv('TERMUX_HOST')
PORT = 8022
USERNAME = os.getenv('TERMUX_USER')
PASSWORD = os.getenv('TERMUX_PASSWORD')

# Thingsboard details
THINGSBOARD_URL = os.getenv('THINGSBOARD_URL')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

headers = {"Content-Type": "application/json", "Authorization":f"Bearer {ACCESS_TOKEN}"}
url=f"http://{THINGSBOARD_URL}:8080/api/v1/{ACCESS_TOKEN}/telemetry"

while (1):
        ts = time.time()
        gpscmd = scrip.compute(f"termux-location -p passive -r last")
        senread = scrip.compute(f"termux-sensor -s 'K6DS3TR Accelerometer,BMP280 Barometer' -n 1")
        gps=json.loads(gpscmd["output"])
        sen=json.loads(senread["output"])
        tmp=sen["K6DS3TR Accelerometer"]
        tmp2=sen["BMP280 Barometer"]
        data=json.dumps({"ts":ts,"latitude":gps["latitude"],"longitude":gps["longitude"],"K6DS3TR Accelerometer":tmp["values"][0],"BMP280 Barometer":tmp2["values"][0]})
        resp=requests.post(url, headers=headers, data=data)
