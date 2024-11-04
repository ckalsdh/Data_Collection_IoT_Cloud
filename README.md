# Data_Collection_IoT_Cloud

# Termux Sensor Data to Thingsboard Automation

This project automates the process of logging into an Android device running Termux via SSH, collecting sensor data (e.g., accelerometer), and posting this data to Thingsboard for visualization and analysis. The solution leverages `paramiko` for SSH connections and uses Termux's `termux-api` package for accessing Android sensors.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Prerequisites

- **Android Device** with [Termux](https://termux.dev/) installed
- **Termux:API Package** for accessing Android sensors:
  ```
  pkg install termux-api
  ```

## .env
Following credentials are needed to run the scripts. Please see `.env.example`.
```
THINGSBOARD_URL=<IP_ADDRESS>:8080/
ACCESS_TOKEN=<THINGSBOARD_DEVICE_ACCESS_TOKEN>
TERMUX_HOST=<TERMUX_IP_ADDRESS>
TERMUX_USER=<USER_NAME>
TERMUX_PASSWORD=<PASSWORD>
```

Make sure packages in `requirements.txt` are installed.
- Python 3.10.14

## Scripts
`sensor.py` is desinged to be ran directly inside Termux. Make sure python is installed in Termux.
This script will gather sensor and directly send it to AWS EC2 instance(Thingsboard).
  ```
  # inside Termux
  python3 sensor.py
  ```

`SSH_termux_thingsboard_connection.py` is a script to run on a PC(Mac) to SSH into Termux and run the same function as `sensor.py`.
  ```
  # on local PC(Mac)
  python3 SSH_termux_thingsboard_connection.py
  ```
