##################################
# script to run IN Termux
##################################
import requests
import json
import time
import subprocess
from pimux import scrip
from dotenv import load_dotenv
import os

load_dotenv()

# SSH connection details
HOST = os.getenv('TERMUX_HOST')
PORT = 8022
USERNAME = os.getenv('TERMUX_USER')
PASSWORD = os.getenv('TERMUX_PASSWORD')

# ThingsBoard details
THINGSBOARD_URL = os.getenv('THINGSBOARD_URL')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

headers = {"Content-Type": "application/json", "Authorization": f"Bearer {ACCESS_TOKEN}"}
url = f"http://{THINGSBOARD_URL}:8080/api/v1/{ACCESS_TOKEN}/telemetry"

while True:
    ts = time.time()

    # Run termux-audio-record to record audio for a fixed duration
    audio_file_path = f"/data/data/com.termux/files/home/audio_{ts}.wav"
    subprocess.run(["termux-audio-record", "-d", "5", "-o", audio_file_path], check=True)

    # Prepare data payload
    data = json.dumps({
        "ts": ts,
        "audio_file_path": audio_file_path  # Path to audio file recorded
    })
    
    # Send data to ThingsBoard
    resp = requests.post(url, headers=headers, data=data)
    print(f"Data sent: {data} - Response: {resp.status_code}")

    # Delay before next iteration
    time.sleep(10)
