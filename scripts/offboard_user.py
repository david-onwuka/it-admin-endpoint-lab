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


def offboard_user(user_id):
    users = read_csv(USERS)
    access = read_csv(ACCESS)

    user = next((u for u in users if u["user_id"] == user_id), None)

    if not user:
        raise SystemExit(f"User {user_id} not found.")

    if user["status"] != "terminated":
        raise SystemExit(
            f"User {user_id} is not terminated. "
            "Refusing to perform offboarding."
        )

    revoked = 0

    for assignment in access:
        if assignment["user_id"] == user_id and assignment["status"] == "active":
            assignment["status"] = "revoked"
            revoked += 1

    write_csv(
        ACCESS,
        access,
        ["user_id", "app_id", "access_role", "status"],
    )

    AUDIT.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().isoformat(timespec="seconds")

    with open(AUDIT, "a") as f:
        f.write(
            f"{timestamp} | OFFBOARD | {user_id} | "
            f"{user['email']} | access_revoked={revoked}\n"
        )

    print(f"Offboarding completed for {user['email']}")
    print(f"Application access revoked: {revoked}")
    print(f"Audit record: {AUDIT}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(
            "Usage: python3 scripts/offboard_user.py USER_ID"
        )

    offboard_user(sys.argv[1])
