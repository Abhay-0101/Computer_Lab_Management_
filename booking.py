# =====================================================================
# PERSON 3 - booking.py
# Lab session booking: book a PC, view own, view all (admin uses last).
# Booking = lab + PC id + date + time + roll no + name. No live timing.
# =====================================================================
from storage import load_data, save_data, ask_nonempty, ask_date, ask_time
from labs import load_labs, view_pcs

BOOKINGS_FILE = "bookings.json"


def book_session(lab_name):
    """Show working PCs, ask which PC, then date, time, roll no, name.
    A PC can't be booked twice for the same date and time, and a
    student can't hold two PCs in the same slot."""
    view_pcs(lab_name, only_available=True)
    pc_id = ask_nonempty("PC id to book (e.g. PC01): ").upper()

    pc = next((p for p in load_labs()[lab_name] if p["pc_id"] == pc_id), None)
    if pc is None:
        print("  PC not found in this lab.")
        return
    if pc["status"] != "working":
        print("  That PC is faulty. Pick a working PC.")
        return

    date_ = ask_date("Date (e.g. 2026 12 22): ")
    time_ = ask_time("Time (HH:MM): ")
    roll = ask_nonempty("Full roll no.: ").upper()
    name = ask_nonempty("Full name: ")

    bookings = load_data(BOOKINGS_FILE, [])
    same_slot = [b for b in bookings
                 if b["lab"] == lab_name and b["date"] == date_ and b["time"] == time_]

    if any(b["pc_id"] == pc_id for b in same_slot):
        print(f"  {pc_id} is already booked for that date and time.")
        return
    if any(b["roll_no"] == roll for b in same_slot):
        print("  You already have a booking in this slot.")
        return

    bookings.append({"lab": lab_name, "pc_id": pc_id, "date": date_,
                     "time": time_, "roll_no": roll, "name": name})
    save_data(BOOKINGS_FILE, bookings)
    print(f"  Booked {pc_id} in {lab_name} on {date_} at {time_} for {name}.")


def my_bookings():
    """Student enters roll no and sees their bookings (all labs)."""
    roll = ask_nonempty("Full roll no.: ").upper()
    mine = [b for b in load_data(BOOKINGS_FILE, []) if b["roll_no"] == roll]
    print(f"\n--- Bookings for {roll} ---")
    if not mine:
        print("  No bookings found.")
    for b in mine:
        print(f"  {b['lab']} | {b['pc_id']} | {b['date']} {b['time']} | {b['name']}")


def view_all_bookings(lab_name):
    """Admin: all bookings of the selected lab."""
    rows = [b for b in load_data(BOOKINGS_FILE, []) if b["lab"] == lab_name]
    print(f"\n--- All bookings: {lab_name} ---")
    if not rows:
        print("  No bookings yet.")
    for b in sorted(rows, key=lambda x: (x["date"], x["time"])):
        print(f"  {b['date']} {b['time']} | {b['pc_id']} | {b['roll_no']} | {b['name']}")
