# =====================================================================
# PERSON 4 - reports.py
# Fault reporting. Used by BOTH admin and student menus.
# =====================================================================
from labs import load_labs, save_labs
from storage import ask_nonempty


def report_fault(lab_name):
    """Anyone can report. The PC becomes 'faulty' with a short note.
    Only the admin can clear it later (admin.mark_fixed)."""
    labs = load_labs()
    pc_id = ask_nonempty("PC id to report (e.g. PC03): ").upper()
    for p in labs[lab_name]:
        if p["pc_id"] == pc_id:
            note = input("Short fault note (or press Enter for 'faulty'): ").strip()
            p["status"] = "faulty"
            p["fault"] = note or "faulty"
            save_labs(labs)
            print(f"  {pc_id} marked FAULTY. Thank you for reporting.")
            return
    print("  PC not found in this lab.")
