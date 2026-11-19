# =====================================================================
# PERSON 2 - admin.py
# Admin side: login, add/remove PC, view faults, mark fixed.
# Uses: labs.py (Person 1), booking.py (Person 3), reports.py (Person 4)
# =====================================================================
from labs import load_labs, save_labs, view_pcs, lab_summary
from booking import view_all_bookings          # Person 3's function
from reports import report_fault               # Person 4's function
from storage import ask_nonempty

ADMIN_PASSWORD = "admin123"   # simple fixed password for the project


def admin_login():
    """Return True if the password is correct (3 tries)."""
    for _ in range(3):
        if input("Admin password: ").strip() == ADMIN_PASSWORD:
            return True
        print("  Wrong password.")
    return False


def add_pc(lab_name):
    labs = load_labs()
    pc_id = ask_nonempty("New PC id (e.g. PC21): ").upper()
    if any(p["pc_id"] == pc_id for p in labs[lab_name]):
        print("  That PC id already exists in this lab.")
        return
    labs[lab_name].append({"pc_id": pc_id, "status": "working", "fault": ""})
    save_labs(labs)
    print(f"  {pc_id} added to {lab_name}.")


def remove_pc(lab_name):
    labs = load_labs()
    pc_id = ask_nonempty("PC id to remove: ").upper()
    before = len(labs[lab_name])
    labs[lab_name] = [p for p in labs[lab_name] if p["pc_id"] != pc_id]
    if len(labs[lab_name]) == before:
        print("  PC not found.")
        return
    save_labs(labs)
    print(f"  {pc_id} removed.")


def view_faults(lab_name):
    faulty = [p for p in load_labs()[lab_name] if p["status"] == "faulty"]
    print(f"\n--- Fault reports: {lab_name} ---")
    if not faulty:
        print("  No faulty PCs.")
    for p in faulty:
        print(f"  {p['pc_id']:<8} {p['fault'] or 'no details'}")


def mark_fixed(lab_name):
    labs = load_labs()
    pc_id = ask_nonempty("PC id that is fixed: ").upper()
    for p in labs[lab_name]:
        if p["pc_id"] == pc_id and p["status"] == "faulty":
            p["status"], p["fault"] = "working", ""
            save_labs(labs)
            print(f"  {pc_id} marked working.")
            return
    print("  No faulty PC with that id.")


def admin_menu(lab_name):
    while True:
        print(f"\n===== ADMIN | {lab_name} =====")
        lab_summary(lab_name)
        print("1. View all PCs\n2. Add PC\n3. Remove PC\n4. View fault reports")
        print("5. Mark PC fixed\n6. View all bookings\n7. Back")
        c = input("Choice: ").strip()
        if c == "1":
            view_pcs(lab_name)
        elif c == "2":
            add_pc(lab_name)
        elif c == "3":
            remove_pc(lab_name)
        elif c == "4":
            view_faults(lab_name)
        elif c == "5":
            mark_fixed(lab_name)
        elif c == "6":
            view_all_bookings(lab_name)
        elif c == "7":
            return
        else:
            print("  Invalid choice.")
