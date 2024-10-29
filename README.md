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
  ```bash
  pkg install termux-api