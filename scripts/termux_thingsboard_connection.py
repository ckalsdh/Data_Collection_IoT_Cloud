import subprocess
import requests
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

THINGSBOARD_URL = os.getenv('THINGSBOARD_URL')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

def get_sensor_data(sensor_type="K6DS3TR Accelerometer"):
    # use termux-sensor to get accelerometer data
    command = ["termux-sensor", "-s", sensor_type, "-n", "1"]
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("Error retrieving sensor data.")
        return None

    try:
        data_json = json.loads(result.stdout)
        sensor_values = data_json.get(sensor_type, {}).get('values', [0, 0, 0])
        
        sensor_data = {
            "accelerometer_x": sensor_values[0],
            "accelerometer_y": sensor_values[1],
            "accelerometer_z": sensor_values[2]
        }
        return sensor_data
    except (ValueError, KeyError) as e:
        print("Parsing error:", e)
        return None

def post_to_thingsboard(data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    url = f"{THINGSBOARD_URL}/api/v1/{ACCESS_TOKEN}/telemetry"
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response

# loop to automate continuous data fetching and posting
while True:
    data = get_sensor_data()
    if data:
        response = post_to_thingsboard(data)
        if response.status_code == 200:
            print("Data posted successfully:", data)
        else:
            print("Failed to post data:", response.status_code, response.text)
    else:
        print("No data available.")
    
    # Adjust sleep time based on desired data collection frequency
    time.sleep(5)