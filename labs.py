# =====================================================================
# PERSON 1 - labs.py
# Lab selection + viewing PCs + lab summary.
# view_pcs() is SHARED: admin and student both call it.
# =====================================================================
from storage import load_data, save_data

LABS_FILE = "labs.json"


def load_labs():
    """Return the whole labs dict: {"Lab 1": [pc, pc, ...], ...}"""
    return load_data(LABS_FILE, {})


def save_labs(labs):
    save_data(LABS_FILE, labs)


def select_lab():
    """Show all registered labs; user picks by NAME. Returns lab name or None."""
    labs = load_labs()
    if not labs:
        print("No labs registered.")
        return None
    while True:
        print("\n--- Select Lab ---")
        for name in labs:
            print("  -", name)
        choice = input("Enter lab name (or 'back'): ").strip().lower()
        if choice == "back":
            return None
        for name in labs:
            if name.lower() == choice:
                return name
        print("  Lab not found. Type the name exactly as listed.")


def view_pcs(lab_name, only_available=False):
    """Print PCs of a lab. only_available=True shows working PCs only
    (student view). Admin uses only_available=False to see faulty ones too."""
    pcs = load_labs().get(lab_name, [])
    if only_available:
        pcs = [p for p in pcs if p["status"] == "working"]
    print(f"\n--- {lab_name}: {'Available' if only_available else 'All'} PCs ---")
    if not pcs:
        print("  (none)")
        return
    for p in pcs:
        if p["status"] == "working":
            print(f"  {p['pc_id']:<8} working")
        else:
            print(f"  {p['pc_id']:<8} FAULTY - {p['fault'] or 'no details'}")


def lab_summary(lab_name):
    """One-line summary: 'Lab 2: 18 working, 2 faulty'."""
    pcs = load_labs().get(lab_name, [])
    working = sum(1 for p in pcs if p["status"] == "working")
    faulty = len(pcs) - working
    print(f"[{lab_name}: {working} working, {faulty} faulty]")
