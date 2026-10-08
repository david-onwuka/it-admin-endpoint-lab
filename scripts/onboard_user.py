import csv
import sys
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
USERS = BASE / "identity/users.csv"
ACCESS = BASE / "identity/access_assignments.csv"
AUDIT = BASE / "tickets/access_audit.log"


def read_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fieldnames):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def onboard_user(user_id):
    users = read_csv(USERS)
    access = read_csv(ACCESS)

    user = next((u for u in users if u["user_id"] == user_id), None)

    if not user:
        raise SystemExit(f"User {user_id} not found.")

    if user["status"] != "active":
        raise SystemExit(
            f"User {user_id} is not active. "
            "Refusing to perform onboarding."
        )

    existing = {
        (a["user_id"], a["app_id"])
        for a in access
    }

    default_apps = [
        ("APP001", "member"),
        ("APP002", "member"),
        ("APP003", "user"),
    ]

    assigned = 0

    for app_id, role in default_apps:
        if (user_id, app_id) not in existing:
            access.append({
                "user_id": user_id,
                "app_id": app_id,
                "access_role": role,
                "status": "active",
            })
            assigned += 1

    write_csv(
        ACCESS,
        access,
        ["user_id", "app_id", "access_role", "status"],
    )

    AUDIT.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().isoformat(timespec="seconds")

    with open(AUDIT, "a") as f:
        f.write(
            f"{timestamp} | ONBOARD | {user_id} | "
            f"{user['email']} | access_assigned={assigned}\n"
        )

    print(f"Onboarding completed for {user['email']}")
    print(f"Application access assigned: {assigned}")
    print(f"Audit record: {AUDIT}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(
            "Usage: python3 scripts/onboard_user.py USER_ID"
        )

    onboard_user(sys.argv[1])
