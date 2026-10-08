# IT Administration & Endpoint Management Lab

*Built by Eme David Onwuka*



![Linux](https://img.shields.io/badge/Linux-Ubuntu%2024.04-E95420?logo=ubuntu&logoColor=white)




![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)




![Bash](https://img.shields.io/badge/Bash-Automation-4EAA25?logo=gnubash&logoColor=white)




![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?logo=git&logoColor=white)




![Environment](https://img.shields.io/badge/Environment-WSL2-4D4D4D?logo=linux&logoColor=white)




![Focus](https://img.shields.io/badge/Focus-IT%20Administration%20%26%20Endpoint%20Management-0A66C2)



> A local hands-on IT administration and endpoint management lab focused on employee lifecycle management, SaaS access administration, endpoint inventory, endpoint compliance, device lifecycle operations, automation, auditability, and IT support workflows.

---

## 1. Project Overview

This project was built as a practical simulation of junior IT administration and endpoint operations.

The objective was to move beyond theoretical knowledge and implement repeatable workflows for common IT administration tasks such as:

- Employee onboarding and offboarding
- Application access provisioning and revocation
- Role-based access assignments
- Access auditing
- Endpoint inventory collection
- Endpoint compliance assessment
- Device lifecycle management
- Linux endpoint troubleshooting
- IT support incident handling
- Root-cause analysis
- Operational documentation
- Python-based IT automation

The lab was intentionally designed to be *local, reproducible, and cost-free*, without requiring AWS infrastructure, paid SaaS platforms, or enterprise licensing.

The implementation uses a combination of Python, Bash, CSV-based operational records, Linux system commands, and Git.

---

## 2. Project Goals

The project was designed around several practical IT administration capabilities.

### Identity & Access Management

- Maintain employee records
- Track active and terminated users
- Provision application access
- Revoke access during offboarding
- Apply predefined application roles
- Prevent inappropriate offboarding actions
- Maintain an access audit trail

### Endpoint Administration

- Collect endpoint inventory
- Identify operating system and kernel
- Track assigned users and device status
- Evaluate endpoint compliance
- Check screen-lock configuration
- Check automatic update configuration
- Identify pending package updates
- Record endpoint limitations accurately

### Asset Lifecycle Management

Model a basic device lifecycle:

text
Assigned
   ↓
Maintenance
   ↓
Retired


### IT Operations

Implement a basic operational workflow:

text
Detection
   ↓
Investigation
   ↓
Root Cause Analysis
   ↓
Remediation Plan
   ↓
Verification
   ↓
Documentation


### Automation

Automate repetitive administrative tasks using Python rather than relying entirely on manual CSV editing.

---

## 3. Architecture

The lab is divided into three primary operational areas:

text
                    IT ADMINISTRATION LAB
                            |
          +-----------------+-----------------+
          |                 |                 |
       IDENTITY          ENDPOINTS        IT SUPPORT
          |                 |                 |
          |                 |                 |
     Users / Apps      Inventory /       Tickets / RCA
     Access Records    Compliance
          |                 |
     +----+----+       +----+-----+
     |         |       |          |
  Onboard   Offboard  Inventory  Compliance
     |         |       |          |
 Access      Access   Collection  Checks
  Grant      Revocation    |        |
     |         |           |        |
     +----+----+           +----+---+
          |                     |
          +----------+----------+
                     |
               Audit / Records


The project deliberately keeps the data layer simple so the administrative workflows can be inspected and understood easily.

---

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Ubuntu 24.04.4 LTS | Linux administration environment |
| WSL2 | Local endpoint environment |
| Python 3 | IT administration automation |
| Bash | Linux system inspection and operations |
| CSV | Local identity, application, and endpoint records |
| Git | Version control |
| Linux system utilities | Endpoint discovery and compliance checks |

---

## 5. Repository Structure

text
it-admin-endpoint-lab/
│
├── endpoints/
│   └── devices.csv
│
├── identity/
│   ├── access_assignments.csv
│   ├── applications.csv
│   └── users.csv
│
├── scripts/
│   ├── check_endpoint_compliance.py
│   ├── collect_endpoint_inventory.py
│   ├── offboard_user.py
│   ├── onboard_user.py
│   └── update_device_status.py
│
├── tickets/
│   ├── IT-001-endpoint-compliance.md
│   └── access_audit.log
│
├── screenshots/
│
└── README.md


---

## 6. Identity & Access Administration

The identity layer uses structured records to represent employees, applications, and application access.

### User Inventory

identity/users.csv contains employee records including:

- User ID
- Full name
- Email
- Department
- Role
- Employment status

Example lifecycle states include:

text
active
terminated


### Application Inventory

identity/applications.csv maintains the applications available within the simulated organization.

The lab includes example SaaS applications such as:

- GitHub
- Slack
- Google Workspace
- Jira

These records are *simulated SaaS inventory data*.

They do not represent production administration of these services.

---

## 7. Automated User Onboarding

The onboard_user.py script automates application access assignment for active users.

The workflow:

text
User identified
      ↓
Verify user exists
      ↓
Verify user is active
      ↓
Determine default application access
      ↓
Check for duplicate assignments
      ↓
Assign missing access
      ↓
Record audit event


Example:

bash
python3 scripts/onboard_user.py U005


The automation is designed to be idempotent.

If a user already has the expected access, the script does not create duplicate assignments.

This was also tested against an existing active user.

---

## 8. Automated User Offboarding

The offboard_user.py script automates access revocation when an employee is terminated.

The workflow:

text
User identified
      ↓
Verify user exists
      ↓
Verify user is terminated
      ↓
Find active application assignments
      ↓
Revoke active access
      ↓
Write audit record


Example:

bash
python3 scripts/offboard_user.py U005


The script includes a safety control that refuses to perform offboarding on an active employee.

For example, attempting to offboard an active user results in the operation being rejected rather than silently revoking access.

This demonstrates a basic least-privilege and administrative-safety principle.

---

## 9. Access Audit Trail

All onboarding and offboarding automation is recorded in:

text
tickets/access_audit.log


The audit trail records:

- Timestamp
- Operation
- User ID
- User email
- Number of access assignments or revocations

A tested employee lifecycle included:

text
Active User
    ↓
Onboarding
    ↓
3 Application Access Assignments
    ↓
User Terminated
    ↓
Offboarding
    ↓
3 Application Access Revocations
    ↓
Audit Log


This provides evidence that the access lifecycle is not only documented but also automated and auditable.

---

## 10. Endpoint Inventory Management

The endpoint inventory component is implemented by:

text
scripts/collect_endpoint_inventory.py


The script collects information directly from the local Linux environment.

Collected information includes:

- Device ID
- Hostname
- Operating system
- Kernel
- Assigned user
- Device status
- Encryption state
- Update state
- Compliance state
- Available memory
- Root filesystem capacity
- Inventory timestamp

Example:

bash
python3 scripts/collect_endpoint_inventory.py


The resulting inventory is stored in:

text
endpoints/devices.csv


The actual tested endpoint reported:

text
Hostname: DESKTOP-06P9THF
OS: Ubuntu 24.04.4 LTS
Kernel: 6.18.40.1-microsoft-standard-WSL2
Memory: approximately 3.7 GiB
Root filesystem: approximately 1007 GiB


---

## 11. Endpoint Compliance Automation

The endpoint compliance checker is implemented by:

text
scripts/check_endpoint_compliance.py


It evaluates several endpoint controls:

### Screen Lock

Checks whether screen locking is enabled.

### Idle Timeout

Checks the configured GNOME idle timeout.

The tested endpoint reported:

text
300 seconds


which corresponds to a five-minute timeout.

### Automatic Updates

Checks whether unattended-upgrades is enabled.

### Pending Updates

Counts packages currently available for upgrade.

### Disk Encryption

Checks whether encryption can be established from the available Linux environment.

Because this project runs under WSL2, disk encryption cannot be independently verified as a Linux LUKS configuration.

The lab therefore deliberately reports:

text
NOT VERIFIABLE (WSL2)


rather than incorrectly marking the control as compliant.

---

## 12. Actual Compliance Test

The automated compliance report produced:

text
=== ENDPOINT COMPLIANCE REPORT ===
Hostname:              DESKTOP-06P9THF
OS:                    Linux-6.18.40.1-microsoft-standard-WSL2-x86_64-with-glibc2.39
Kernel:                6.18.40.1-microsoft-standard-WSL2

Screen lock:           PASS
Idle timeout:          PASS (300s)
Automatic updates:     PASS
Pending updates:       FAIL (53)
Disk encryption:       NOT VERIFIABLE (WSL2)

Overall assessment:    REVIEW REQUIRED


This demonstrates an important operational principle:

> Compliance automation should report the actual state of the endpoint, including failures and verification limitations, rather than artificially producing a PASS result.

---

## 13. Endpoint Security Findings

The compliance investigation identified two important findings.

### Finding 1: Pending Updates

The endpoint had:

text
53 pending package updates


Automatic updates were enabled, but the endpoint was still not fully update-compliant.

### Finding 2: Repository Signing-Key Problem

During apt update, the HashiCorp repository reported a missing public signing key:

text
NO_PUBKEY FC9CA96ACA026560


This prevented successful repository signature verification.

The issue was documented rather than bypassed.

No unsafe repository configuration or unverified package installation was performed.

---

## 14. Device Lifecycle Management

Device lifecycle operations are automated using:

text
scripts/update_device_status.py


Supported states:

text
assigned
maintenance
retired


Example:

bash
python3 scripts/update_device_status.py D001 maintenance


Then:

bash
python3 scripts/update_device_status.py D001 retired


The actual lab test demonstrated:

text
assigned
    ↓
maintenance
    ↓
retired


Each status change records the previous state, new state, and timestamp.

This models a basic IT asset lifecycle from device assignment through maintenance and eventual retirement.

---

## 15. IT Support Ticket & RCA

The project includes a documented IT support incident:

text
tickets/IT-001-endpoint-compliance.md


### Incident

The endpoint was reported as non-compliant during a routine compliance assessment.

### Impact

The endpoint had 53 pending package updates.

### Detection

The automated compliance checker identified:

text
Automatic updates: PASS
Screen lock: PASS
Idle timeout: PASS
Pending updates: FAIL
Disk encryption: Not verifiable in WSL2


### Investigation

The investigation examined:

bash
apt list --upgradable
systemctl is-enabled unattended-upgrades
gsettings
lsblk


### Root Cause

The endpoint had pending package updates despite automatic update functionality being enabled.

A separate repository signing-key issue was also identified during package repository validation.

### Remediation Plan

The documented remediation process is:

1. Review the pending packages.
2. Validate the repository signing key.
3. Apply approved updates during a maintenance window.
4. Re-run the compliance checker.
5. Verify the final endpoint state.
6. Close the incident only after verification.

The project intentionally did *not* perform a blanket system upgrade simply to force the compliance report to PASS.

---

## 16. Operational Workflow

The lab models a simplified IT operations workflow:

text
                 USER / DEVICE EVENT
                         |
                         v
                    Detection
                         |
                         v
                    Investigation
                         |
                         v
                 Root Cause Analysis
                         |
                         v
                 Remediation Planning
                         |
                         v
                     Resolution
                         |
                         v
                    Verification
                         |
                         v
                 Documentation / Audit


This approach is applicable to common junior IT support and administration scenarios such as:

- User onboarding
- User offboarding
- Access requests
- Access removal
- Endpoint compliance failures
- Device maintenance
- Device retirement
- Update failures
- Configuration issues

---

## 17. Security & Administrative Controls

The project incorporates several basic administrative safeguards.

### Offboarding Safety

Active users cannot be offboarded by the offboarding automation.

### Idempotent Provisioning

Running onboarding against an already provisioned user does not create duplicate access assignments.

### Auditability

Identity lifecycle operations are written to an audit log.

### Explicit Compliance Failures

Failed controls are reported as failures rather than hidden.

### Configuration Verification

Repository signature failures are treated as issues requiring investigation rather than bypassed.

### Environment Transparency

WSL2 limitations are explicitly documented.

---

## 18. Evidence

The project produced practical evidence during implementation.

Suggested evidence includes:

| Evidence | Purpose |
|---|---|
| Endpoint compliance report | Demonstrates automated endpoint assessment |
| Endpoint inventory collection | Demonstrates asset discovery |
| Device lifecycle maintenance | Demonstrates device state management |
| Device lifecycle retirement | Demonstrates asset retirement workflow |
| User onboarding/offboarding | Demonstrates identity lifecycle automation |
| Access audit log | Demonstrates administrative auditability |
| IT-001 ticket/RCA | Demonstrates troubleshooting and documentation |

---

## 19. Project Limitations

This is a *local technical lab*, not a production enterprise IT environment.

Several limitations are intentionally documented.

### Google Workspace

The Google Workspace entry in the application inventory is a simulated SaaS record.

The project does *not* claim production Google Workspace administration.

### MDM

This lab does not claim enterprise MDM deployment or management.

The endpoint-management work demonstrates inventory, compliance assessment, lifecycle management, and automation using the available local environment.

### Disk Encryption

The endpoint runs inside WSL2.

A physical workstation or appropriately configured virtual machine would be required to independently demonstrate Linux LUKS or Windows BitLocker enforcement.

### SaaS Platforms

GitHub, Slack, Jira, and Google Workspace records are simulated application inventory/access records rather than live enterprise tenants.

These limitations are documented deliberately to keep the project technically honest.

---

## 20. What This Project Demonstrates

### Identity & Access

- User lifecycle management
- Application provisioning
- Access revocation
- Role assignment
- Basic RBAC concepts
- Audit logging
- Offboarding controls

### Endpoint Administration

- Endpoint discovery
- Inventory collection
- Compliance assessment
- Screen-lock verification
- Update-state verification
- Endpoint security checks
- Device lifecycle tracking

### IT Operations

- Incident detection
- Troubleshooting
- Root-cause analysis
- Remediation planning
- Verification
- Operational documentation

### Automation

- Python scripting
- Bash/Linux command integration
- CSV data management
- Idempotent workflows
- Automated reporting

### Linux Administration

- Ubuntu administration
- Package management
- Repository troubleshooting
- System configuration inspection
- Filesystem and device inspection
- WSL2 troubleshooting

---

## 21. Skills Demonstrated

text
IT Administration
Endpoint Management
Identity & Access Management
User Lifecycle Management
SaaS Access Administration
RBAC
Endpoint Inventory
Endpoint Compliance
Asset Lifecycle Management
Linux Administration
Ubuntu
Python
Bash
Git
Automation
Audit Logging
Incident Management
Root Cause Analysis
Technical Documentation
Troubleshooting


---

## 22. Key Takeaways

The lab demonstrates how common IT administration activities can be converted into repeatable, auditable workflows.

Rather than relying solely on manual administration, the project uses automation to:

text
Discover
   ↓
Record
   ↓
Evaluate
   ↓
Act
   ↓
Audit
   ↓
Verify


The most important design principle was maintaining an accurate distinction between:

- What was actually implemented
- What was simulated
- What could not be verified
- What would require an enterprise environment

This makes the lab suitable as a technical demonstration of junior IT administration, endpoint operations, Linux support, automation, and troubleshooting skills.

---

## 23. Author

*Eme David Onwuka*

Junior DevOps / Technical Support Engineer
Focus areas: IT Administration, Linux, Cloud Infrastructure, DevOps, Endpoint Operations, Automation, and Technical Support.

GitHub: **[github.com/david-onwuka](https://github.com/david-onwuka)**

---

## Project Status

*Completed: Local IT Administration & Endpoint Management Lab*

The core implementation covers:

- [x] Identity inventory
- [x] Application inventory
- [x] User onboarding automation
- [x] User offboarding automation
- [x] Access provisioning
- [x] Access revocation
- [x] Access audit logging
- [x] Endpoint inventory automation
- [x] Endpoint compliance automation
- [x] Endpoint security checks
- [x] Device lifecycle automation
- [x] IT support ticket
- [x] Root-cause analysis
- [x] Remediation workflow
- [x] Operational documentation
- [x] Evidence capture
