#!/usr/bin/env python3

import subprocess
import platform
import socket
import re

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL).strip()
    except subprocess.CalledProcessError:
        return ""

hostname = socket.gethostname()
os_name = platform.platform()

idle = run("gsettings get org.gnome.desktop.session idle-delay")
lock = run("gsettings get org.gnome.desktop.screensaver lock-enabled")
updates = run("apt list --upgradable 2>/dev/null | tail -n +2 | wc -l")
unattended = run("systemctl is-enabled unattended-upgrades")
kernel = run("uname -r")

idle_seconds = int(re.search(r"uint32 ([0-9]+)", idle).group(1)) if re.search(r"uint32 ([0-9]+)", idle) else 0
update_count = int(updates) if updates.isdigit() else 0

print("=== ENDPOINT COMPLIANCE REPORT ===")
print(f"Hostname:              {hostname}")
print(f"OS:                    {os_name}")
print(f"Kernel:                {kernel}")
print()
print(f"Screen lock:           {'PASS' if lock == 'true' else 'FAIL'}")
print(f"Idle timeout:          {'PASS' if 0 < idle_seconds <= 900 else 'FAIL'} ({idle_seconds}s)")
print(f"Automatic updates:     {'PASS' if unattended == 'enabled' else 'FAIL'}")
print(f"Pending updates:       {'PASS' if update_count == 0 else 'FAIL'} ({update_count})")
print("Disk encryption:       NOT VERIFIABLE (WSL2)")
print()
print("Overall assessment:    REVIEW REQUIRED")
