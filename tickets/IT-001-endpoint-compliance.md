# IT-001 — Endpoint Compliance Failure

## Issue
Endpoint reported as non-compliant during routine IT compliance check.

## Impact
The endpoint has 53 pending package updates, so it does not meet the lab's update-compliance requirement.

## Detection
The automated endpoint compliance checker reported:

- Automatic updates: PASS
- Screen lock: PASS
- Idle timeout: PASS
- Pending updates: FAIL (53)
- Disk encryption: Not verifiable in WSL2

## Investigation

The endpoint was checked using:

- `apt list --upgradable`
- `systemctl is-enabled unattended-upgrades`
- `gsettings` screen-lock configuration
- `lsblk` disk configuration

The investigation confirmed that automatic security updates are enabled, but outstanding packages remain.

## Root Cause

The endpoint has pending package updates despite automatic security updates being enabled.

A separate repository configuration issue was also detected during `apt update`: the HashiCorp repository could not be verified because its signing key was unavailable.

## Current Status

REVIEW REQUIRED.

No full system upgrade was performed because this lab intentionally avoids unnecessary package changes.

## Recommended Remediation

1. Review the 53 pending packages.
2. Validate the HashiCorp repository signing key.
3. Apply approved updates during a maintenance window.
4. Re-run the compliance checker.
5. Confirm the endpoint reaches the required compliance state.

## Verification

Re-run:

`python3 scripts/check_endpoint_compliance.py`

The ticket should remain open until the compliance result is verified after remediation.
