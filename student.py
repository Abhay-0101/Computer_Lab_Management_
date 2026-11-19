# =====================================================================
# PERSON 3 - student.py
# Student menu. Students can view, report, book. They CANNOT add/remove
# PCs or edit/clear fault reports.
# =====================================================================
from labs import view_pcs, lab_summary          # Person 1's functions
from reports import report_fault                # Person 4's function
from booking import book_session, my_bookings   # own functions


def student_menu(lab_name):
    while True:
        print(f"\n===== STUDENT | {lab_name} =====")
        lab_summary(lab_name)
        print("1. View available PCs\n2. Report a faulty PC")
        print("3. Book a lab session\n4. View my bookings\n5. Back")
        c = input("Choice: ").strip()
        if c == "1":
            view_pcs(lab_name, only_available=True)
        elif c == "2":
            report_fault(lab_name)
        elif c == "3":
            book_session(lab_name)
        elif c == "4":
            my_bookings()
        elif c == "5":
            return
        else:
            print("  Invalid choice.")
