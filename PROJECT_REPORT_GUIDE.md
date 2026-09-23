# Academic Project Report & Design Documentation
## Project: Student Academic Management System

This document contains the complete **Academic Project Report Outline** (all 15 required sections) along with textual design diagrams ready for academic evaluation.

---

## Part 1: Design Diagrams (Textual & Structural)

### 1. System Architecture Diagram
The system follows a modular 3-tier CLI architecture:

```
+--------------------------------------------------------------------------+
|                        PRESENTATION LAYER (CLI)                          |
|  main.py (Menus: Student Mgmt, Academic Mgmt, Attendance, Reports)       |
+--------------------------------------------------------------------------+
                                    |
                                    v
+--------------------------------------------------------------------------+
|                          BUSINESS LOGIC LAYER                            |
|  student.py     academic.py       attendance.py       reports.py         |
|  - Student CRUD - Array Marks     - Attendance Track  - Report Card      |
|  - Bitmask Flags- Grade Logic     - Eligibility Check - Class Analytics  |
+--------------------------------------------------------------------------+
          |                    |                    |
          v                    v                    v
+--------------------------------------------------------------------------+
|                  DATA STORAGE & FOUNDATION LAYER                         |
|  constants.py                          validation.py                     |
|  - Subjects (tuple)                    - String inspection (.isdigit)    |
|  - Grade frozenset                     - Numerical bounds checking       |
|  - Status bitmasks (1, 2, 4)           - Zero try/except statements      |
|  In-Memory Data Structures:                                              |
|  - Dicts: {id: Student}, {id: AcademicRecord}, {id: AttendanceRecord}    |
|  - Sets: student_id_set {101, 102, ...}                                  |
|  - Arrays: array('f', marks)                                             |
+--------------------------------------------------------------------------+
```

---

### 2. Workflow Diagram
```
[Start Program]
       |
       v
[Initialize In-Memory Dicts & Seed Initial Demo Data]
       |
       +---> [Display Main Menu (1-5)]
                   |
     +-------------+-------------+-------------+-------------+
     |             |             |             |             |
     v             v             v             v             v
[1. Student]  [2. Academic] [3. Attendance] [4. Reports]  [5. Exit]
     |             |             |             |             |
     |--Add        |--Enter      |--Record     |--Individual |-> [End]
     |--Display    |  Marks      |  Attendance |--Class Table
     |--Search     |--View Card  |--Check      |--Top Scorer 
     |--Update     |             |  Eligibility|--Average    
     |--Bitmask    |             |             |             
     |--Delete     |             |             |             
     |             |             |             |             
     +-------------+-------------+-------------+             
                   |
                   v
         [Loop to Main Menu]
```

---

### 3. Use Case Diagram
```
                     +---------------------------------------+
                     |  Student Academic Management System   |
                     +---------------------------------------+
                                        |
       +--------------------------------+--------------------------------+
       |                                                                 |
       v                                                                 v
+-------------+                                                   +-------------+
| Instructor  |                                                   |  Student /  |
| / Faculty   |                                                   | Evaluator   |
+-------------+                                                   +-------------+
       |                                                                 |
       |-- (UC1: Register Student Profile)                               |
       |-- (UC2: Prevent Duplicate Student IDs via Set)                  |
       |-- (UC3: Record Subject Marks into Float Array)                  |
       |-- (UC4: Enter Session Attendance)                               |
       |-- (UC5: Toggle Fee & Scholarship Bitmask Flags)                 |
       |                                                                 |
       +-----------------------------------------------------------------+
       |
       |-- (UC6: View Individual Student Comprehensive Report Card)
       |-- (UC7: View Class-wide Tabular Summary)
       |-- (UC8: Determine Class Highest Scorer)
       |-- (UC9: Calculate Overall Class Average)
       |-- (UC10: Check Exam Attendance Eligibility & Deficit)
```

---

### 4. Class Diagram
```
+--------------------------------------------------------------------+
|                              Student                               |
+--------------------------------------------------------------------+
| - student_id    : int                                              |
| - name          : str                                              |
| - department    : str                                              |
| - status_flags  : int (bitmask)                                    |
+--------------------------------------------------------------------+
| + __init__(student_id: int, name: str, dept: str, flags: int)      |
| + is_active() : bool                                               |
| + has_fee_paid() : bool                                            |
| + has_scholarship() : bool                                         |
| + set_fee_paid(is_paid: bool) : void                               |
| + toggle_scholarship() : void                                      |
| + to_summary_tuple() : tuple                                       |
| + display_info() : void                                            |
+--------------------------------------------------------------------+

+--------------------------------------------------------------------+
|                           AcademicRecord                           |
+--------------------------------------------------------------------+
| - student_id : int                                                 |
| - subjects   : tuple (str)                                         |
| - marks      : array.array ('f')                                   |
+--------------------------------------------------------------------+
| + __init__(student_id: int, marks_list: list, subjects: tuple)     |
| + calculate_total() : float                                        |
| + calculate_percentage() : float                                   |
| + calculate_grade() : str                                          |
| + get_highest_mark() : tuple (str, float)                          |
| + get_lowest_mark() : tuple (str, float)                           |
| + display_marks_card() : void                                      |
+--------------------------------------------------------------------+

+--------------------------------------------------------------------+
|                          AttendanceRecord                          |
+--------------------------------------------------------------------+
| - student_id       : int                                           |
| - attended_classes : int                                           |
| - total_classes    : int                                           |
+--------------------------------------------------------------------+
| + __init__(student_id: int, attended: int, total: int)             |
| + calculate_percentage() : float                                   |
| + is_eligible(min_percentage: float) : bool                        |
| + calculate_shortfall() : int                                      |
| + display_attendance() : void                                      |
+--------------------------------------------------------------------+
```

---

### 5. Sequence Diagram: Recording Marks & Evaluating Academic Standing
```
User (Faculty)           main.py              academic.py          validation.py
     |                      |                      |                     |
     |-- 1. Select Marks -->|                      |                     |
     |   Menu Option        |                      |                     |
     |                      |-- get_valid_integer()--------------------->|
     |<-- Prompt for ID ----|                      |                     |-- Check .isdigit()
     |-- Enter 101 -------->|                      |                     |<-- Return 101
     |                      |                      |                     |
     |                      |-- Prompt Marks Loop ---------------------->|
     |<-- Prompt Subject ---|   (per subject in    |                     |-- Check float
     |-- Enter Score ------>|    SUBJECT_NAMES)    |                     |<-- Return float
     |                      |                      |                     |
     |                      |-- enter_marks(101, [88.5, 92.0, 84.0]) --->|
     |                      |                      |                     |
     |                      |                      |-- AcademicRecord()  |
     |                      |                      |   array('f', marks) |
     |                      |                      |   calculate_total() |
     |                      |                      |   calculate_pct()   |
     |                      |                      |   calculate_grade() |
     |<-- Display Success --|<-- Return Record ----|                     |
     |    Confirmation      |                      |                     |
```

---

## Part 2: 15-Section Project Report Outline

### Section 1: Cover Page
- **Project Title**: Student Academic Management System
- **Course**: Python Essentials (First-Year Foundation)
- **Author**: First-Year Undergraduate Student
- **Repository**: Hosted on GitHub
- **Submission Date**: Academic Term 2026

### Section 2: Introduction
The Student Academic Management System (SAMS) is a modular terminal application designed to automate student administration, numerical marks evaluation, and attendance compliance tracking. Developed to adhere strictly to foundational programming concepts, it bridges algorithmic problem-solving with object-oriented paradigms without relying on external packages.

### Section 3: Problem Statement
Manual student grading and record keeping suffer from computational errors, lack of verification, and administrative overhead. This project provides an in-memory, reproducible system that validates user inputs, guarantees unique student records, performs arithmetic calculations, and outputs formatted academic credentials.

### Section 4: Functional Requirements
1. **Student Management**: Adding, searching, listing, updating, and deleting student records.
2. **Academic Management**: Storing subject marks via Python `array`, computing sums, calculating percentages, and evaluating letter grades.
3. **Attendance Management**: Recording total and attended sessions, evaluating exam eligibility based on a 75% cutoff, and computing exact session shortfalls.
4. **Reports & Analytics**: Rendering individual report cards, generating class performance tables, identifying highest scorers, and calculating class averages.
5. **Bitmask Status Flags**: Managing enrollment, fee clearance, and scholarship attributes via bitwise flags.

### Section 5: Non-Functional Requirements
1. **Zero External Dependencies**: Uses only standard Python libraries (`array`, `sys`, `os`).
2. **Deterministic Input Validation**: All validations run without exception handling (`try/except`), avoiding program crashes through defensive control flow.
3. **Memory Efficiency**: Numerical marks are maintained in native C-style floating-point arrays (`array.array('f')`).
4. **Maintainability**: Clean separation into 7 focused Python modules.

### Section 6: System Architecture
A 3-layer architecture comprising Presentation (CLI), Business Logic (`student`, `academic`, `attendance`, `reports`), and Foundation/Storage (`constants`, `validation`, in-memory collections).

### Section 7: Design Diagrams
*(Refer to Part 1 of this document for Architecture, Workflow, Use Case, Class, and Sequence Diagrams).*

### Section 8: Design Decisions and Rationale
- **Why no `try/except`?** Exception handling was outside the foundational syllabus. Using loops, `.isdigit()`, and decimal counting teaches explicit data validation.
- **Why Python's `array` module?** Demonstrates contiguous, fixed-type numerical memory management over heterogeneous lists for floating-point marks.
- **Why Bitmask Status Flags?** Bitwise operators (`&`, `|`, `^`, `~`) provide an authentic, hardware-aligned mechanism for tracking student flags (Enrolled, Fee Paid, Scholarship) without artificial mathematical puzzles.
- **Why `frozenset` for Grades?** Ensures letter grade definitions are immutable and supports $O(1)$ membership checks (`grade in VALID_GRADES`).

### Section 9: Implementation Details
Details of the 7 modules:
- `constants.py`: Immutables, bitmasks, configuration.
- `validation.py`: Pure algorithmic input verification.
- `student.py`: Class `Student`, bitmask methods, CRUD helpers.
- `academic.py`: Class `AcademicRecord`, `array('f')`, percentage, grade logic.
- `attendance.py`: Class `AttendanceRecord`, eligibility logic.
- `reports.py`: Analytics algorithms and formatted rendering.
- `main.py`: Interactive CLI flow and sub-menu dispatchers.

### Section 10: Screenshots / Results
*(Capture and embed console outputs from Section 8 of the README)*:
- Main menu view.
- Student profile view with bitwise status.
- Marks card with array-backed scores.
- Class performance summary table.
- Highest scorer and class average metrics.

### Section 11: Testing Approach
- Built on plain Python `assert` statements (`tests/test_project.py`).
- 5 comprehensive test functions covering bitwise flags, array math, attendance deficit, validation logic, and analytics.
- Executed via standard terminal command: `python tests/test_project.py`.

### Section 12: Challenges Faced
1. **Validating Floats Without Exceptions**: Designing an algorithm to validate inputs like `"88.5"` without `try/float()` using `.count(".")`, `.replace()`, and `.isdigit()`.
2. **Bitwise Flag Manipulation**: Implementing bitwise clearing (`flags & ~FLAG_FEE_PAID`) and toggling (`flags ^ FLAG_SCHOLARSHIP`) cleanly.
3. **Accurate Shortfall Calculation**: Formulating the ceiling deficit formula for attendance shortfall without importing the `math` module.

### Section 13: Learnings and Key Takeaways
- Mastery of operator precedence in academic calculations.
- Practical understanding of when to use `list`, `tuple`, `set`, `dict`, `frozenset`, and `array`.
- Experience in structuring multi-file Python applications.
- Writing testable code with assertions.

### Section 14: Future Enhancements
- Addition of CSV/JSON file persistence when file I/O is introduced in subsequent semesters.
- Graphical User Interface (GUI) using Tkinter or PyQt in advanced courses.
- Dynamic subject enrollment allowing students to register for elective courses.

### Section 15: References
1. Python Software Foundation. *Python 3 Standard Library Documentation: array, built-in types*.
2. Python Essentials Course Curriculum & Lecture Notes (Topics 1–22).
