"""
attendance.py
Manages student attendance tracking, percentage calculations, and exam eligibility.

Course topics demonstrated:
- Classes and objects, constructors, methods.
- Arithmetic operators, integer conversion, comparison and logical operators.
- Identity operators (is, is not).
"""

from constants import MIN_ATTENDANCE_PERCENTAGE


class AttendanceRecord:
    """
    Represents an attendance record for a student across all academic sessions.
    """

    def __init__(self, student_id, attended_classes, total_classes):
        self.student_id = student_id
        self.attended_classes = attended_classes
        self.total_classes = total_classes

    def calculate_percentage(self):
        """
        Calculates attendance percentage.
        Demonstrates division and multiplication operators.
        """
        if self.total_classes == 0:
            return 0.0

        percentage = (self.attended_classes / self.total_classes) * 100.0
        return percentage

    def is_eligible(self, min_percentage=MIN_ATTENDANCE_PERCENTAGE):
        """
        Determines whether the student meets the minimum attendance requirement.
        Demonstrates comparison operator (>=).
        """
        return self.calculate_percentage() >= min_percentage

    def calculate_shortfall(self):
        """
        Calculates how many additional classes the student needed to attend
        to reach the minimum attendance requirement.
        Demonstrates arithmetic operators (+, -, *, /) and integer conversion.
        """
        required_classes = (MIN_ATTENDANCE_PERCENTAGE * self.total_classes) / 100.0
        if self.attended_classes < required_classes:
            # Need to ceil to whole class
            shortfall = int(required_classes - self.attended_classes + 0.9999)
            return shortfall
        return 0

    def display_attendance(self):
        """
        Displays structured attendance summary and eligibility verdict.
        """
        pct = self.calculate_percentage()
        eligible = self.is_eligible()
        status_text = "ELIGIBLE FOR EXAMS" if eligible else "SHORTAGE WARNING"
        shortfall = self.calculate_shortfall()

        print("=" * 55)
        print(f"            ATTENDANCE RECORD: ID {self.student_id}")
        print("=" * 55)
        print(f"Total Conducted Classes : {self.total_classes}")
        print(f"Classes Attended        : {self.attended_classes}")
        print(f"Attendance Percentage   : {pct:.2f}%")
        print(f"Minimum Required        : {MIN_ATTENDANCE_PERCENTAGE:.1f}%")
        print(f"Eligibility Verdict     : {status_text}")
        if not eligible and shortfall > 0:
            print(f"Shortfall Deficit       : {shortfall} class(es) below 75% limit")
        print("=" * 55)


def record_attendance(attendance_dict, student_id, attended, total):
    """
    Creates or updates an AttendanceRecord for a student.
    """
    record = AttendanceRecord(student_id, attended, total)
    attendance_dict[student_id] = record
    return record


def get_attendance_record(attendance_dict, student_id):
    """
    Retrieves the AttendanceRecord for a student, returning None if not found.
    """
    if student_id in attendance_dict:
        return attendance_dict[student_id]
    return None


def display_student_attendance(attendance_dict, student_id):
    """
    Displays the attendance details for a student.
    Demonstrates identity operator (is None).
    """
    record = get_attendance_record(attendance_dict, student_id)
    if record is None:
        print(f"\nNo attendance record found for Student ID {student_id}.")
        return

    record.display_attendance()
