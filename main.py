

from constants import (
    SUBJECTNAMES,
    MAXMARKPERSUBJECT,
    FLAGACTIVE,
    FLAGFEEPAID,
    FLAGSCHOLARSHIP,
)
from student import (
    Student,
    addstudent,
    displayallstudents,
    searchstudent,
    updatestudent,
    deletestudent,
)
from academic import (
    AcademicRecord,
    entermarks,
    displaystudentacademics,
)
from attendance import (
    AttendanceRecord,
    recordattendance,
    displaystudentattendance,
)
from reports import (
    generatestudentreport,
    displayclasssummary,
    findhighestscorer,
    calculateclassaverage,
)
from validation import (
    getvalidinteger,
    getvalidfloat,
    getnonemptystring,
    getmenuchoice,
)


def seed_demo_data(studentsdict, studentidset, academicsdict, attendancedict):
    demostudents = [
        Student(101, "Alice Smith", "Computer Science", FLAGACTIVE | FLAGFEEPAID | FLAGSCHOLARSHIP),
        Student(102, "Bob Miller", "Electrical Engineering", FLAGACTIVE | FLAGFEEPAID),
        Student(103, "Charlie Davis", "Mechanical Engineering", FLAGACTIVE),
    ]

    for s in demostudents:
        addstudent(studentsdict, studentidset, s)

    
    entermarks(academicsdict, 101, [88.5, 92.0, 84.0])
    entermarks(academicsdict, 102, [74.0, 68.5, 71.0])
    entermarks(academicsdict, 103, [52.0, 48.0, 56.5])

    
    recordattendance(attendancedict, 101, 46, 50)  
    recordattendance(attendancedict, 102, 38, 50)  
    recordattendance(attendancedict, 103, 31, 50)  


def studentmanagementmenu(studentsdict, studentidset, academicsdict, attendancedict):
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

        choice = getmenuchoice("Enter choice (1-7): ", ("1", "2", "3", "4", "5", "6", "7"))

        if choice == "1":
            print("\n--- Add New Student ---")
            sid = getvalidinteger("Enter Student ID (100 - 9999): ", 100, 9999)
            if sid in studentidset:
                print(f"Error: Student with ID {s_id} already exists!")
                continue

            name = getnonemptystring("Enter Student Full Name: ")
            dept = getnonemptystring("Enter Department: ")

            newstudent = Student(sid, name, dept, FLAGACTIVE)
            if addstudent(studentsdict, studentidset, newstudent):
                print(f"Success: Student '{name}' (ID: {sid}) registered successfully!")

        elif choice == "2":
            print("\n--- All Registered Students ---")
            displayallstudents(studentsdict)

        elif choice == "3":
            print("\n--- Search Student ---")
            sid = getvalidinteger("Enter Student ID to Search: ", 100, 9999)
            student = searchstudent(studentsdict, sid)
            if student is None:
                print(f"No student found with ID {sid}.")
            else:
                student.displayinfo()

        elif choice == "4":
            print("\n--- Update Student Details ---")
            sid = getvalidinteger("Enter Student ID to Update: ", 100, 9999)
            student = searchstudent(studentsdict, sid)
            if student is None:
                print(f"No student found with ID {sid}.")
                continue

            newname = getnonemptystring(f"Enter New Name (Current: {student.name}): ")
            newdept = getnonemptystring(f"Enter New Department (Current: {student.department}): ")

            if updatestudent(studentsdict, sid, newname, newdept):
                print(f"Success: Student ID {sid} updated successfully!")

        elif choice == "5":
            print("\n--- Manage Student Status Flags (Bitmask) ---")
            sid = getvalidinteger("Enter Student ID: ", 100, 9999)
            student = searchstudent(studentsdict, sid)
            if student is None:
                print(f"No student found with ID {sid}.")
                continue

            student.displayinfo()
            print("\nSelect Flag Operation:")
            print("1. Set Tuition Fee as Paid")
            print("2. Set Tuition Fee as Pending")
            print("3. Toggle Scholarship Award Status")
            print("4. Cancel")
            flagchoice = getmenuchoice("Choice (1-4): ", ("1", "2", "3", "4"))

            if flagchoice == "1":
                student.setfeepaid(True)
                print(f"Success: Fee status updated to Paid for Student ID {sid}.")
            elif flagchoice == "2":
                student.setfeepaid(False)
                print(f"Success: Fee status updated to Pending for Student ID {sid}.")
            elif flagchoice == "3":
                student.togglescholarship()
                currentsch = "Awarded" if student.hasscholarship() else "Removed"
                print(f"Success: Scholarship status is now {currentsch} for Student ID {sid}.")

        elif choice == "6":
            print("\n--- Delete Student ---")
            sid = getvalidinteger("Enter Student ID to Delete: ", 100, 9999)
            confirm = getmenuchoice(f"Are you sure you want to delete Student {sid}? (y/n): ", ("y", "n", "Y", "N"))
            if confirm in ("y", "Y"):
                if deletestudent(studentsdict, academicsdict, attendancedict, studentid_set, sid):
                    print(f"Success: Student ID {sid} and all related records deleted.")
                else:
                    print(f"Error: Student ID {sid} was not found.")

        elif choice == "7":
            break


def academicmanagementmenu(studentsdict, academicsdict):
    while True:
        print("\n" + "=" * 45)
        print("          ACADEMIC MANAGEMENT MENU")
        print("=" * 45)
        print("1. Enter / Update Subject Marks")
        print("2. View Student Marks Card")
        print("3. Return to Main Menu")
        print("-" * 45)

        choice = getmenuchoice("Enter choice (1-3): ", ("1", "2", "3"))

        if choice == "1":
            print("\n--- Enter Subject Marks ---")
            sid = getvalidinteger("Enter Student ID: ", 100, 9999)
            if sid not in studentsdict:
                print(f"Error: Student ID {sid} does not exist. Please register the student first.")
                continue

            markslist = []
            for subject in SUBJECTNAMES:
                mark = getvalidfloat(f"Enter marks for {subject} (0.0 - {MAXMARKPERSUBJECT}): ", 0.0, MAXMARKPERSUBJECT)
                markslist.append(mark)

            entermarks(academicsdict, sid, markslist)
            print(f"Success: Marks recorded in Python Array for Student ID {sid}!")

        elif choice == "2":
            print("\n--- View Marks Card ---")
            sid = getvalidinteger("Enter Student ID: ", 100, 9999)
            displaystudentacademics(academicsdict, sid)

        elif choice == "3":
            break


def attendancemanagementmenu(studentsdict, attendancedict):

    while True:
        print("\n" + "=" * 45)
        print("         ATTENDANCE MANAGEMENT MENU")
        print("=" * 45)
        print("1. Record / Update Attendance")
        print("2. View Student Attendance & Eligibility")
        print("3. Return to Main Menu")
        print("-" * 45)

        choice = getmenuchoice("Enter choice (1-3): ", ("1", "2", "3"))

        if choice == "1":
            print("\n--- Record Attendance ---")
            sid = getvalidinteger("Enter Student ID: ", 100, 9999)
            if sid not in studentsdict:
                print(f"Error: Student ID {sid} does not exist. Please register the student first.")
                continue

            total = getvalidinteger("Enter Total Classes Conducted (1 - 500): ", 1, 500)
            attended = getvalidinteger(f"Enter Classes Attended (0 - {total}): ", 0, total)

            recordattendance(attendancedict, sid, attended, total)
            print(f"Success: Attendance recorded for Student ID {sid}!")

        elif choice == "2":
            print("\n--- View Attendance ---")
            sid = getvalidinteger("Enter Student ID: ", 100, 9999)
            displaystudentattendance(attendancedict, sid)

        elif choice == "3":
            break


def reportsmenu(studentsdict, academicsdict, attendancedict):
    
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

        choice = getmenuchoice("Enter choice (1-5): ", ("1", "2", "3", "4", "5"))

        if choice == "1":
            print("\n--- Individual Student Report ---")
            sid = getvalidinteger("Enter Student ID: ", 100, 9999)
            generatestudentreport(studentsdict, academicsdict, attendancedict, sid)

        elif choice == "2":
            display_class_summary(studentsdict, academicsdict, attendancedict)

        elif choice == "3":
            print("\n--- Class Highest Scorer ---")
            topscorer = findhighestscorer(studentsdict, academicsdict)
            if topscorer is None:
                print("No academic marks recorded in the system yet.")
            else:
                topid, topname, toppct, topgrade = topscorer
                print("-" * 45)
                print(f"Student ID : {topid}")
                print(f"Name       : {topname}")
                print(f"Score      : {toppct:.2f}%")
                print(f"Grade      : {topgrade}")
                print("-" * 45)

        elif choice == "4":
            print("\n--- Class Average Marks ---")
            avgpct = calculateclassaverage(academicsdict)
            print("-" * 45)
            print(f"Total Students with Marks : {len(academicsdict)}")
            print(f"Overall Class Average     : {avgpct:.2f}%")
            print("-" * 45)

        elif choice == "5":
            break


def main():
    print("=" * 60)
    print("      WELCOME TO STUDENT ACADEMIC MANAGEMENT SYSTEM")
    print("=" * 60)

   
    studentsdict = {}
    studentidset = set()
    academicsdict = {}
    attendancedict = {}

    
    seed_demo_data(studentsdict, studentidset, academicsdict, attendancedict)
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

        choice = getmenuchoice("Enter your choice (1-5): ", ("1", "2", "3", "4", "5"))

        if choice == "1":
            studentmanagementmenu(studentsdict, studentidset, academicsdict, attendancedict)
        elif choice == "2":
            academic_management_menu(studentsdict, academicsdict)
        elif choice == "3":
            attendance_management_menu(studentsdict, attendancedict)
        elif choice == "4":
            reports_menu(studentsdict, academicsdict, attendancedict)
        elif choice == "5":
            print("\nThank you for using the Student Academic Management System. Goodbye!\n")
            break


if name == "main":
    main()
