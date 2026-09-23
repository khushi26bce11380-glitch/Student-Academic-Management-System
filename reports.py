"""
reports.py
Generates individual student report cards, class summaries, top scorer identification,
and class-wide average marks.

Course topics demonstrated:
- Functions, parameters, and return statements.
- type() function and identity operators (is, is not).
- Meaningful tuple creation and unpacking.
- Loops, conditionals, arithmetic calculations, and string formatting.
"""

from student import Student
from academic import AcademicRecord
from attendance import AttendanceRecord
from constants import MAX_MARK_PER_SUBJECT


def generate_student_report(students_dict, academics_dict, attendance_dict, student_id):
    """
    Generates a unified, comprehensive academic and attendance report card.
    Demonstrates identity operators (is None, is not None) and type() function.
    """
    if student_id not in students_dict:
        print(f"\nStudent with ID {student_id} not found in the system.")
        return

    student = students_dict[student_id]
    acad_rec = academics_dict.get(student_id)
    att_rec = attendance_dict.get(student_id)

    # type() function demonstration checking valid class instance
    if type(student) is not Student:
        print("Error: Invalid student record type encountered.")
        return

    print("\n" + "=" * 62)
    print(f"            OFFICIAL STUDENT REPORT CARD: ID {student.student_id}")
    print("=" * 62)
    print(f"Full Name          : {student.name}")
    print(f"Department         : {student.department}")

    # Check status flags using bitwise helper methods
    fee_text = "Paid" if student.has_fee_paid() else "Pending / Due"
    scholarship_text = "Awarded (Merit)" if student.has_scholarship() else "Not Awarded"
    active_text = "Enrolled" if student.is_active() else "Withdrawn"
    print(f"Enrollment Status  : {active_text}")
    print(f"Fee Payment Status : {fee_text}")
    print(f"Scholarship Status : {scholarship_text}")
    print("-" * 62)

    # Academic Marks Breakdown
    if acad_rec is None:
        print("Academic Marks     : No marks recorded yet.")
    else:
        print("SUBJECT-WISE PERFORMANCE (Stored via Python Array):")
        for i in range(len(acad_rec.marks)):
            subj = acad_rec.subjects[i]
            mark = acad_rec.marks[i]
            print(f"  - {subj:<24} : {mark:>6.2f} / {MAX_MARK_PER_SUBJECT:.1f}")

        total = acad_rec.calculate_total()
        percentage = acad_rec.calculate_percentage()
        grade = acad_rec.calculate_grade()
        high_subj, high_mark = acad_rec.get_highest_mark()
        low_subj, low_mark = acad_rec.get_lowest_mark()

        print("-" * 62)
        print(f"Total Marks        : {total:.2f} / {len(acad_rec.marks) * MAX_MARK_PER_SUBJECT:.1f}")
        print(f"Percentage         : {percentage:.2f}%")
        print(f"Letter Grade       : {grade}")
        print(f"Best Subject       : {high_subj} ({high_mark:.2f})")
        print(f"Lowest Subject     : {low_subj} ({low_mark:.2f})")

    print("-" * 62)

    # Attendance Record Breakdown
    if att_rec is None:
        print("Attendance Record  : No attendance data recorded yet.")
    else:
        att_pct = att_rec.calculate_percentage()
        eligible = att_rec.is_eligible()
        verdict = "ELIGIBLE TO SIT FOR EXAMS" if eligible else "INELIGIBLE (ATTENDANCE SHORTAGE)"
        print("ATTENDANCE PERFORMANCE:")
        print(f"Classes Attended   : {att_rec.attended_classes} / {att_rec.total_classes}")
        print(f"Attendance Rate    : {att_pct:.2f}%")
        print(f"Exam Eligibility   : {verdict}")

    print("=" * 62)


def display_class_summary(students_dict, academics_dict, attendance_dict):
    """
    Displays a structured tabular overview of all students, their academic marks,
    percentages, grades, and attendance eligibility.
    """
    if len(students_dict) == 0:
        print("\nNo students found in the system.")
        return

    print("\n" + "=" * 80)
    print("                           CLASS PERFORMANCE SUMMARY TABLE")
    print("=" * 80)
    header = f"{'ID':<6} | {'Name':<18} | {'Total':<8} | {'% Score':<8} | {'Grade':<6} | {'Att. %':<8} | {'Status':<10}"
    print(header)
    print("-" * 80)

    for student_id in students_dict:
        student = students_dict[student_id]
        acad = academics_dict.get(student_id)
        att = attendance_dict.get(student_id)

        if acad is not None:
            total_str = f"{acad.calculate_total():.1f}"
            pct_str = f"{acad.calculate_percentage():.1f}%"
            grade_str = acad.calculate_grade()
        else:
            total_str = "N/A"
            pct_str = "N/A"
            grade_str = "N/A"

        if att is not None:
            att_pct_str = f"{att.calculate_percentage():.1f}%"
            eligible_str = "Eligible" if att.is_eligible() else "Shortage"
        else:
            att_pct_str = "N/A"
            eligible_str = "Pending"

        row = f"{student.student_id:<6} | {student.name:<18} | {total_str:<8} | {pct_str:<8} | {grade_str:<6} | {att_pct_str:<8} | {eligible_str:<10}"
        print(row)

    print("=" * 80)


def find_highest_scorer(students_dict, academics_dict):
    """
    Finds the student with the highest overall percentage.
    Returns a meaningful summary tuple: (student_id, name, percentage, grade)
    or None if no academic records exist.
    """
    if len(academics_dict) == 0:
        return None

    top_id = None
    top_pct = -1.0

    for s_id in academics_dict:
        record = academics_dict[s_id]
        pct = record.calculate_percentage()
        if pct > top_pct:
            top_pct = pct
            top_id = s_id

    if top_id is None:
        return None

    student = students_dict.get(top_id)
    student_name = student.name if student is not None else "Unknown"
    record = academics_dict[top_id]
    grade = record.calculate_grade()

    # Returns meaningful summary tuple
    return (top_id, student_name, top_pct, grade)


def calculate_class_average(academics_dict):
    """
    Calculates the arithmetic average percentage across all students with academic records.
    Demonstrates loops, arithmetic division, and comparison operators.
    """
    if len(academics_dict) == 0:
        return 0.0

    total_pct_sum = 0.0
    for record in academics_dict.values():
        total_pct_sum += record.calculate_percentage()

    average_percentage = total_pct_sum / len(academics_dict)
    return average_percentage
