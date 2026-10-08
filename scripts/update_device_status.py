#!/usr/bin/env python3

import csv
import sys
from datetime import datetime

FILE = "endpoints/devices.csv"

if len(sys.argv) != 3:
    print("Usage: python3 scripts/update_device_status.py DEVICE_ID STATUS")
    print("Allowed: assigned, maintenance, retired")
    sys.exit(1)

device_id = sys.argv[1]
new_status = sys.argv[2]

allowed = {"assigned", "maintenance", "retired"}

if new_status not in allowed:
    print(f"Invalid status: {new_status}")
    sys.exit(1)

with open(FILE, newline="") as f:
    rows = list(csv.DictReader(f))
    fields = rows[0].keys() if rows else []

found = False

for row in rows:
    if row["device_id"] == device_id:
        old_status = row["status"]
        row["status"] = new_status
        row["last_status_change"] = datetime.now().isoformat(timespec="seconds")
        found = True
        break

if not found:
    print(f"Device {device_id} not found")
    sys.exit(1)

with open(FILE, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print("=== DEVICE LIFECYCLE UPDATE ===")
print(f"Device:       {device_id}")
print(f"Previous:     {old_status}")
print(f"New status:   {new_status}")
print(f"Updated:      {datetime.now().isoformat(timespec='seconds')}")
