# =====================================================================
# PERSON 4 - main.py
# Entry point: role menu -> (admin login) -> select lab -> role menu.
# Run:  python main.py
# =====================================================================
from labs import select_lab
from admin import admin_login, admin_menu          # Person 2
from student import student_menu                   # Person 3


def main():
    while True:
        print("\n===== COMPUTER LAB MANAGEMENT =====")
        print("1. Admin\n2. Student\n3. Exit")
        c = input("Choice: ").strip()
        if c == "1":
            if admin_login():
                lab = select_lab()
                if lab:
                    admin_menu(lab)
        elif c == "2":
            lab = select_lab()
            if lab:
                student_menu(lab)
        elif c == "3":
            print("Goodbye!")
            break
        else:
            print("  Invalid choice.")


if __name__ == "__main__":
    main()
