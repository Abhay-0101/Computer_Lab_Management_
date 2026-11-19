# =====================================================================
# PERSON 4 - storage.py
# Shared helpers: load/save JSON files + input validation.
# Everyone imports from here. Do NOT change function names without
# telling the team.
# =====================================================================
import json
import os
import re
from datetime import datetime, date

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def load_data(filename, default):
    """Read a JSON file from data/. Return `default` if missing/broken."""
    path = os.path.join(DATA_DIR, filename)
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def save_data(filename, data):
    """Write data to a JSON file in data/."""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(os.path.join(DATA_DIR, filename), "w") as f:
        json.dump(data, f, indent=2)


# ---------------- input validation helpers ----------------

def ask_nonempty(prompt):
    """Keep asking until the user types something."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Input cannot be empty.")


def ask_date(prompt):
    """Ask for a date. Accepts 2026-12-22, 2026 12 22, 2026/12/22, 2026.12.22.
    Returns it as YYYY-MM-DD. Past dates are rejected."""
    while True:
        parts = re.split(r"[\s\-/.]+", input(prompt).strip())
        try:
            d = date(int(parts[0]), int(parts[1]), int(parts[2]))
            if len(parts) != 3:
                raise ValueError
        except (ValueError, IndexError):
            print("  Type year month day, e.g. 2026 12 22 (or 2026-12-22).")
            continue
        if d < date.today():
            print("  Date is in the past.")
            continue
        return d.isoformat()


def ask_time(prompt):
    """Ask for a time as HH:MM (24-hour)."""
    while True:
        value = input(prompt).strip()
        try:
            return datetime.strptime(value, "%H:%M").strftime("%H:%M")
        except ValueError:
            print("  Use format HH:MM (example: 10:00).")
