"""
main.py
Main entry point for the Student Academic Management System.
Provides a clear command-line interface with intuitive menus and sub-menus.

Course topics demonstrated:
- Procedural program structure, control flow (while loops, break, continue, conditionals).
- Functions, parameter passing, dictionary/set/tuple operations.
- User input handling, formatted console output, and modular integration.
"""

from constants import (
    SUBJECT_NAMES,
    MAX_MARK_PER_SUBJECT,
    FLAG_ACTIVE,
    FLAG_FEE_PAID,
    FLAG_SCHOLARSHIP,
)
from student import (
    Student,
    add_student,
    display_all_students,
    search_student,
    update_student,
    delete_student,
)
from academic import (
    AcademicRecord,
    enter_marks,
    display_student_academics,
)
from attendance import (
    AttendanceRecord,
    record_attendance,
    display_student_attendance,
)
from reports import (
    generate_student_report,
    display_class_summary,
    find_highest_scorer,
    calculate_class_average,
)
from validation import (
    get_valid_integer,
    get_valid_float,
    get_non_empty_string,
    get_menu_choice,
)


def seed_demo_data(students_dict, student_id_set, academics_dict, attendance_dict):
    """
    Populates the system with realistic initial student records
    so evaluators can immediately test reporting and analytics features.
    """
    demo_students = [
        Student(101, "Alice Smith", "Computer Science", FLAG_ACTIVE | FLAG_FEE_PAID | FLAG_SCHOLARSHIP),
        Student(102, "Bob Miller", "Electrical Engineering", FLAG_ACTIVE | FLAG_FEE_PAID),
        Student(103, "Charlie Davis", "Mechanical Engineering", FLAG_ACTIVE),
    ]

    for s in demo_students:
        add_student(students_dict, student_id_set, s)

    # Academic records (Array of floating-point marks)
    enter_marks(academics_dict, 101, [88.5, 92.0, 84.0])
    enter_marks(academics_dict, 102, [74.0, 68.5, 71.0])
    enter_marks(academics_dict, 103, [52.0, 48.0, 56.5])

    # Attendance records (Attended classes, total classes)
    record_attendance(attendance_dict, 101, 46, 50)  # 92% (Eligible)
    record_attendance(attendance_dict, 102, 38, 50)  # 76% (Eligible)
    record_attendance(attendance_dict, 103, 31, 50)  # 62% (Shortage)


def student_management_menu(students_dict, student_id_set, academics_dict, attendance_dict):
    """Sub-menu for managing student profiles and status flags."""
    while True:
        print("\n" + "=" * 45)
        print("          STUDENT MANAGEMENT MENU")
        print("=" * 45)
        print("1. Add New Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student Details")
        print("5. Manage Status Flags (Bitmask: Fee / Scholarship)")
        print("6. Delete Student")
        print("7. Return to Main Menu")
        print("-" * 45)

        choice = get_menu_choice("Enter choice (1-7): ", ("1", "2", "3", "4", "5", "6", "7"))

        if choice == "1":
            print("\n--- Add New Student ---")
            s_id = get_valid_integer("Enter Student ID (100 - 9999): ", 100, 9999)
            if s_id in student_id_set:
                print(f"Error: Student with ID {s_id} already exists!")
                continue

            name = get_non_empty_string("Enter Student Full Name: ")
            dept = get_non_empty_string("Enter Department: ")

            new_student = Student(s_id, name, dept, FLAG_ACTIVE)
            if add_student(students_dict, student_id_set, new_student):
                print(f"Success: Student '{name}' (ID: {s_id}) registered successfully!")

        elif choice == "2":
            print("\n--- All Registered Students ---")
            display_all_students(students_dict)

        elif choice == "3":
            print("\n--- Search Student ---")
            s_id = get_valid_integer("Enter Student ID to Search: ", 100, 9999)
            student = search_student(students_dict, s_id)
            if student is None:
                print(f"No student found with ID {s_id}.")
            else:
                student.display_info()

        elif choice == "4":
            print("\n--- Update Student Details ---")
            s_id = get_valid_integer("Enter Student ID to Update: ", 100, 9999)
            student = search_student(students_dict, s_id)
            if student is None:
                print(f"No student found with ID {s_id}.")
                continue

            new_name = get_non_empty_string(f"Enter New Name (Current: {student.name}): ")
            new_dept = get_non_empty_string(f"Enter New Department (Current: {student.department}): ")

            if update_student(students_dict, s_id, new_name, new_dept):
                print(f"Success: Student ID {s_id} updated successfully!")

        elif choice == "5":
            print("\n--- Manage Student Status Flags (Bitmask) ---")
            s_id = get_valid_integer("Enter Student ID: ", 100, 9999)
            student = search_student(students_dict, s_id)
            if student is None:
                print(f"No student found with ID {s_id}.")
                continue

            student.display_info()
            print("\nSelect Flag Operation:")
            print("1. Set Tuition Fee as Paid")
            print("2. Set Tuition Fee as Pending")
            print("3. Toggle Scholarship Award Status")
            print("4. Cancel")
            flag_choice = get_menu_choice("Choice (1-4): ", ("1", "2", "3", "4"))

            if flag_choice == "1":
                student.set_fee_paid(True)
                print(f"Success: Fee status updated to Paid for Student ID {s_id}.")
            elif flag_choice == "2":
                student.set_fee_paid(False)
                print(f"Success: Fee status updated to Pending for Student ID {s_id}.")
            elif flag_choice == "3":
                student.toggle_scholarship()
                current_sch = "Awarded" if student.has_scholarship() else "Removed"
                print(f"Success: Scholarship status is now {current_sch} for Student ID {s_id}.")

        elif choice == "6":
            print("\n--- Delete Student ---")
            s_id = get_valid_integer("Enter Student ID to Delete: ", 100, 9999)
            confirm = get_menu_choice(f"Are you sure you want to delete Student {s_id}? (y/n): ", ("y", "n", "Y", "N"))
            if confirm in ("y", "Y"):
                if delete_student(students_dict, academics_dict, attendance_dict, student_id_set, s_id):
                    print(f"Success: Student ID {s_id} and all related records deleted.")
                else:
                    print(f"Error: Student ID {s_id} was not found.")

        elif choice == "7":
            break


def academic_management_menu(students_dict, academics_dict):
    """Sub-menu for recording and viewing academic subject marks."""
    while True:
        print("\n" + "=" * 45)
        print("          ACADEMIC MANAGEMENT MENU")
        print("=" * 45)
        print("1. Enter / Update Subject Marks")
        print("2. View Student Marks Card")
        print("3. Return to Main Menu")
        print("-" * 45)

        choice = get_menu_choice("Enter choice (1-3): ", ("1", "2", "3"))

        if choice == "1":
            print("\n--- Enter Subject Marks ---")
            s_id = get_valid_integer("Enter Student ID: ", 100, 9999)
            if s_id not in students_dict:
                print(f"Error: Student ID {s_id} does not exist. Please register the student first.")
                continue

            marks_list = []
            for subject in SUBJECT_NAMES:
                mark = get_valid_float(f"Enter marks for {subject} (0.0 - {MAX_MARK_PER_SUBJECT}): ", 0.0, MAX_MARK_PER_SUBJECT)
                marks_list.append(mark)

            enter_marks(academics_dict, s_id, marks_list)
            print(f"Success: Marks recorded in Python Array for Student ID {s_id}!")

        elif choice == "2":
            print("\n--- View Marks Card ---")
            s_id = get_valid_integer("Enter Student ID: ", 100, 9999)
            display_student_academics(academics_dict, s_id)

        elif choice == "3":
            break


def attendance_management_menu(students_dict, attendance_dict):
    """Sub-menu for recording and inspecting student attendance."""
    while True:
        print("\n" + "=" * 45)
        print("         ATTENDANCE MANAGEMENT MENU")
        print("=" * 45)
        print("1. Record / Update Attendance")
        print("2. View Student Attendance & Eligibility")
        print("3. Return to Main Menu")
        print("-" * 45)

        choice = get_menu_choice("Enter choice (1-3): ", ("1", "2", "3"))

        if choice == "1":
            print("\n--- Record Attendance ---")
            s_id = get_valid_integer("Enter Student ID: ", 100, 9999)
            if s_id not in students_dict:
                print(f"Error: Student ID {s_id} does not exist. Please register the student first.")
                continue

            total = get_valid_integer("Enter Total Classes Conducted (1 - 500): ", 1, 500)
            attended = get_valid_integer(f"Enter Classes Attended (0 - {total}): ", 0, total)

            record_attendance(attendance_dict, s_id, attended, total)
            print(f"Success: Attendance recorded for Student ID {s_id}!")

        elif choice == "2":
            print("\n--- View Attendance ---")
            s_id = get_valid_integer("Enter Student ID: ", 100, 9999)
            display_student_attendance(attendance_dict, s_id)

        elif choice == "3":
            break


def reports_menu(students_dict, academics_dict, attendance_dict):
    """Sub-menu for reports, class summaries, and analytics."""
    while True:
        print("\n" + "=" * 45)
        print("           REPORTS & ANALYTICS MENU")
        print("=" * 45)
        print("1. Individual Comprehensive Student Report")
        print("2. Class Performance Summary Table")
        print("3. View Highest Scorer")
        print("4. View Class Average Marks")
        print("5. Return to Main Menu")
        print("-" * 45)

        choice = get_menu_choice("Enter choice (1-5): ", ("1", "2", "3", "4", "5"))

        if choice == "1":
            print("\n--- Individual Student Report ---")
            s_id = get_valid_integer("Enter Student ID: ", 100, 9999)
            generate_student_report(students_dict, academics_dict, attendance_dict, s_id)

        elif choice == "2":
            display_class_summary(students_dict, academics_dict, attendance_dict)

        elif choice == "3":
            print("\n--- Class Highest Scorer ---")
            top_scorer = find_highest_scorer(students_dict, academics_dict)
            if top_scorer is None:
                print("No academic marks recorded in the system yet.")
            else:
                top_id, top_name, top_pct, top_grade = top_scorer
                print("-" * 45)
                print(f"Student ID : {top_id}")
                print(f"Name       : {top_name}")
                print(f"Score      : {top_pct:.2f}%")
                print(f"Grade      : {top_grade}")
                print("-" * 45)

        elif choice == "4":
            print("\n--- Class Average Marks ---")
            avg_pct = calculate_class_average(academics_dict)
            print("-" * 45)
            print(f"Total Students with Marks : {len(academics_dict)}")
            print(f"Overall Class Average     : {avg_pct:.2f}%")
            print("-" * 45)

        elif choice == "5":
            break


def main():
    """Main program entry point coordinating system data and menu loop."""
    print("=" * 60)
    print("      WELCOME TO STUDENT ACADEMIC MANAGEMENT SYSTEM")
    print("=" * 60)

    # In-memory storage structures
    students_dict = {}
    student_id_set = set()
    academics_dict = {}
    attendance_dict = {}

    # Seed realistic initial data for immediate evaluation and testing
    seed_demo_data(students_dict, student_id_set, academics_dict, attendance_dict)
    print("[System Initialized]: Loaded demo student records successfully.\n")

    while True:
        print("\n" + "=" * 50)
        print("                   MAIN MENU")
        print("=" * 50)
        print("1. Student Management")
        print("2. Academic Management")
        print("3. Attendance Management")
        print("4. Reports & Analytics")
        print("5. Exit System")
        print("-" * 50)

        choice = get_menu_choice("Enter your choice (1-5): ", ("1", "2", "3", "4", "5"))

        if choice == "1":
            student_management_menu(students_dict, student_id_set, academics_dict, attendance_dict)
        elif choice == "2":
            academic_management_menu(students_dict, academics_dict)
        elif choice == "3":
            attendance_management_menu(students_dict, attendance_dict)
        elif choice == "4":
            reports_menu(students_dict, academics_dict, attendance_dict)
        elif choice == "5":
            print("\nThank you for using the Student Academic Management System. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
