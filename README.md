# Student Academic Management System (SAMS)

A command-line Student Academic Management System developed using Python to manage student records, marks, attendance and academic reports for VITYarthi Project:Python Essential.  The project demonstrates Python Essentials concepts such as data structures, operators, control flow, functions, modules, arrays and object-oriented programming.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Objectives](#objectives)
4. [Features](#features)
5. [Technologies & Course Topics Used](#technologies--course-topics-used)
6. [Project Structure](#project-structure)
7. [How to Run the Project](#how-to-run-the-project)
8. [How to Test the Project](#how-to-test-the-project)
9. [Example Usage & Console Walkthrough](#example-usage--console-walkthrough)
10. [Academic Report & Design Diagrams](#academic-report--design-diagrams)

---

## Project Overview
The **Student Academic Management System** manages student profiles, numerical academic marks, and session attendance entirely within the command line. It computes student percentages, assigns letter grades, evaluates exam eligibility based on attendance thresholds, and generates formatted reports.

This project is tailored to demonstrate authentic mastery of introductory Python concepts, avoiding both over-engineering and superficial implementations.

---

## Problem Statement
Traditional academic record keeping often relies on manual logs or complex enterprise database software. For academic evaluation in a foundational Python course, there is a need for a lightweight, transparent, and robust command-line application that models student records, performs arithmetic and logical computations, ensures unique identifiers, and validates user input using fundamental control flow.

---

## Objectives
- Implement a 100% standard-Python, command-line system free of external packages or database engines.
- Authentically showcase all 22 topics of the *Python Essentials* curriculum.
- Build robust input validation without `try/except` using string inspection and relational checks.
- Utilize low-level bitwise operations (`&`, `|`, `^`, `~`) to manage student academic standing flags.
- Employ Python's built-in `array` module for storing and computing numerical floating-point marks.
- Provide a full automated test suite using standard Python `assert` statements.

---

## Features

### 1. Student Management Module
- **Add Student**: Registers student ID, name, and department. Enforces ID uniqueness via Python sets.
- **Display All Students**: Tabular display of all registered students with status details.
- **Search Student**: Look up student profiles by ID.
- **Update Student**: Modify name and department information.
- **Bitwise Status Flags**: Update and toggle student standing (Active, Tuition Fee Paid, Merit Scholarship).
- **Delete Student**: Cascading removal of student profile, academic marks, and attendance data.

### 2. Academic Management Module
- **Enter / Update Marks**: Record numerical scores for predefined core subjects.
- **Numerical Array Storage**: Stores marks in native `array.array('f')` contiguous memory.
- **Total & Percentage Computation**: Accurate floating-point arithmetic demonstrating operator precedence.
- **Automated Grading**: Categorizes students into `'A'`, `'B'`, `'C'`, `'D'`, or `'F'` verified against a `frozenset`.
- **Subject Analytics**: Identifies highest and lowest scoring subjects for each student.

### 3. Attendance Management Module
- **Track Sessions**: Record total conducted classes and attended sessions.
- **Percentage Evaluation**: Calculates attendance rate and compares against the mandatory 75% cutoff.
- **Shortfall Deficit**: Calculates the exact number of classes required to reach exam eligibility.

### 4. Reports & Class Analytics Module
- **Comprehensive Report Card**: Consolidated view of student profile, status bitmask, subject marks, percentage, grade, and attendance eligibility.
- **Class Performance Summary**: Tabular overview of all students.
- **Highest Scorer**: Identifies top performer in the class.
- **Class Average**: Computes arithmetic mean across all students.

---

## Technologies & Course Topics Used

The system strictly employs standard Python 3 and maps directly to the 22 syllabus topics:

| # | Course Topic | Implementation in SAMS |
|---|---|---|
| 1 | Python fundamentals | Script structure, comments, variables, indentation across 7 modules |
| 2 | Input and output | Formatted console output with `print()` and user prompts with `input()` |
| 3 | Arithmetic operators | `+`, `-`, `*`, `/`, `//`, `%`: totals, percentages, shortfall deficits |
| 4 | Assignment operators | `=`, `+=`, `-=`, `*=`, `/=`, `&=`, `|=`, `^=`: totals and bitmasks |
| 5 | Comparison operators | `==`, `!=`, `<`, `>`, `<=`, `>=`: marks limits, attendance thresholds |
| 6 | Logical operators | `and`, `or`, `not`: compound conditions and input boundary checks |
| 7 | Membership operators | `in`, `not in`: verifying student IDs in sets and grades in `frozenset` |
| 8 | Identity operators | `is`, `is not`: legitimate `None` checking (`if student is None:`) |
| 9 | Bitwise operators | Real-world status bitmask: Active (`1`), Fees Paid (`2`), Scholarship (`4`) |
| 10 | `type()` function | Type inspection in reports and test assertions |
| 11 | Type conversion | `int()` for IDs/counts, `float()` for marks, `str()` for formatting |
| 12 | Precedence & associativity | Natural grade/attendance math: `(total / (count * 100.0)) * 100.0` |
| 13 | Lists | Dynamic input collection for marks and student rankings |
| 14 | Tuples | Fixed subjects `("Python Programming", "Calculus", "Physics")` and summary records |
| 15 | Sets | Unique `student_id_set` for fast duplicate verification |
| 16 | Dictionaries | Primary storage: `students_dict`, `academics_dict`, `attendance_dict` |
| 17 | frozenset | `VALID_GRADES = frozenset({"A", "B", "C", "D", "F"})` |
| 18 | Control flow | `if/elif/else`, `while True:` interactive loops, `for`, `break`, `continue` |
| 19 | Functions | Modular functions with parameters and return values across modules |
| 20 | Modules & packages | Multi-file architecture importing custom modules (`from student import ...`) |
| 21 | Array module | `import array`; `marks = array.array('f', marks_list)` in `AcademicRecord` |
| 22 | OOP | Clean beginner classes: `Student`, `AcademicRecord`, `AttendanceRecord` |

---

## Project Structure

```
student-academic-management-system/
│
├── constants.py              # Subject tuples, grade thresholds, bitwise masks, frozensets
├── student.py                # Student class & profile management functions (CRUD)
├── academic.py               # AcademicRecord class (array.array('f') marks, grade logic)
├── attendance.py             # AttendanceRecord class & attendance calculation functions
├── reports.py                # Report card generation and class-level analytics
├── validation.py             # Pure non-exception validation (loops, isdigit, string checks)
├── main.py                   # Main CLI menu loop and application entry point
│
├── tests/
│   └── test_project.py       # Plain assert-based testing suite (no external frameworks)
│
├── README.md                 # Complete project documentation and guide
├── statement.md              # Problem statement, scope, target users, features
└── PROJECT_REPORT_GUIDE.md   # Complete 15-section report outline and all design diagrams
```

---

## How to Run the Project

The application runs directly in any standard terminal with Python 3.

```bash
# 1. Navigate to the project directory
cd student-academic-management-system

# 2. Launch the application
python main.py
```

*(Note: On systems where Python is registered under a specific path or launcher, run `python main.py` or `py main.py`)*.

---

## How to Test the Project

Testing is conducted using plain Python `assert` statements. No third-party test libraries (such as `unittest` or `pytest`) are required.

```bash
# Run the automated test suite
python tests/test_project.py
```

### Test Suite Output:
```text
============================================================
   RUNNING ACADEMIC MANAGEMENT SYSTEM TEST SUITE
============================================================
Running test_student_and_bitwise_flags...
  -> PASSED: Student and Bitwise Flags
Running test_academic_record_and_array...
  -> PASSED: Academic Record and Array
Running test_attendance_record...
  -> PASSED: Attendance Record
Running test_validation_helpers...
  -> PASSED: Validation Helpers
Running test_reports_and_analytics...
  -> PASSED: Reports and Analytics
============================================================
>>> ALL ASSERTION TESTS COMPLETED SUCCESSFULLY! <<<
============================================================
```

---

## Example Usage & Console Walkthrough

### 1. Main Navigation Menu
```text
==================================================
                   MAIN MENU
==================================================
1. Student Management
2. Academic Management
3. Attendance Management
4. Reports & Analytics
5. Exit System
--------------------------------------------------
Enter your choice (1-5): 4
```

### 2. Comprehensive Student Report Card
```text
==============================================================
            OFFICIAL STUDENT REPORT CARD: ID 101
==============================================================
Full Name          : Alice Smith
Department         : Computer Science
Enrollment Status  : Enrolled
Fee Payment Status : Paid
Scholarship Status : Awarded (Merit)
--------------------------------------------------------------
SUBJECT-WISE PERFORMANCE (Stored via Python Array):
  - Python Programming       :  88.50 / 100.0
  - Calculus                 :  92.00 / 100.0
  - Physics                  :  84.00 / 100.0
--------------------------------------------------------------
Total Marks        : 264.50 / 300.0
Percentage         : 88.17%
Letter Grade       : A
Best Subject       : Calculus (92.00)
Lowest Subject     : Physics (84.00)
--------------------------------------------------------------
ATTENDANCE PERFORMANCE:
Classes Attended   : 46 / 50
Attendance Rate    : 92.00%
Exam Eligibility   : ELIGIBLE TO SIT FOR EXAMS
==============================================================
```

### 3. Class Performance Summary Table
```text
================================================================================
                           CLASS PERFORMANCE SUMMARY TABLE
================================================================================
ID     | Name               | Total    | % Score  | Grade  | Att. %   | Status    
--------------------------------------------------------------------------------
101    | Alice Smith        | 264.5    | 88.2%    | A      | 92.0%    | Eligible  
102    | Bob Miller         | 213.5    | 71.2%    | B      | 76.0%    | Eligible  
103    | Charlie Davis      | 156.5    | 52.2%    | D      | 62.0%    | Shortage  
================================================================================
```

### 4. Non-Exception Input Validation
```text
Enter Student ID (100 - 9999): text_input
Invalid input! Please enter whole numerical digits only.
Enter Student ID (100 - 9999): 50
Value out of bounds! Must be between 100 and 9999.
Enter Student ID (100 - 9999): 104
```

---

## Academic Report & Design Diagrams

For complete architectural specifications, workflow diagrams, use case diagrams, class diagrams, sequence diagrams, and a 15-section project report outline, refer to:
- [`statement.md`](statement.md)
- [`PROJECT_REPORT_GUIDE.md`](PROJECT_REPORT_GUIDE.md)
