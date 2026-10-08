#!/usr/bin/env python3

import csv
import os
import platform
import socket
import subprocess
from datetime import datetime

OUTPUT = "endpoints/devices.csv"

def run(cmd):
    try:
        return subprocess.check_output(
            cmd, shell=True, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except subprocess.CalledProcessError:
        return ""

hostname = socket.gethostname()
os_name = platform.platform()
kernel = platform.release()
memory = run("free -h | awk '/^Mem:/ {print $2}'")
disk = run("df -h / | awk 'NR==2 {print $2}'")
timestamp = datetime.now().isoformat(timespec="seconds")

device = {
    "device_id": "D001",
    "hostname": hostname,
    "assigned_user": "U001",
    "os": "Ubuntu 24.04.4 LTS",
    "status": "assigned",
    "encryption": "unknown",
    "updates": "pending",
    "compliance": "review_required",
    "kernel": kernel,
    "memory": memory,
    "root_disk": disk,
    "last_inventory": timestamp
}

fields = list(device.keys())

with open(OUTPUT, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerow(device)

print("=== ENDPOINT INVENTORY COLLECTED ===")
for key, value in device.items():
    print(f"{key}: {value}")

print(f"\nInventory written to: {OUTPUT}")
