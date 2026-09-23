"""
academic.py
Manages student subject marks, grade calculation, and academic statistics.

Course topics demonstrated:
- array module (array.array('f', ...) for numerical floating-point marks).
- Arithmetic operators, operator precedence and associativity.
- Comparison and logical operators.
- frozenset membership checking (VALID_GRADES).
- Identity operators (is None).
"""

import array
from constants import SUBJECT_NAMES, MAX_MARK_PER_SUBJECT, VALID_GRADES


class AcademicRecord:
    """
    Encapsulates numerical marks and academic evaluation for a student.
    Uses Python's array data structure for memory-efficient floating-point storage.
    """

    def __init__(self, student_id, marks_list, subject_tuple=SUBJECT_NAMES):
        self.student_id = student_id
        # Fixed subject tuple
        self.subjects = subject_tuple
        # Python array module storing floats ('f' code)
        self.marks = array.array("f", marks_list)

    def calculate_total(self):
        """
        Calculates total marks scored using an accumulator loop and += operator.
        """
        total = 0.0
        for mark in self.marks:
            total += mark
        return total

    def calculate_percentage(self):
        """
        Calculates overall percentage demonstrating operator precedence and associativity:
        Parenthesized multiplication and division occur before final scaling.
        """
        total = self.calculate_total()
        count = len(self.marks)
        if count == 0:
            return 0.0

        # Operator precedence: (count * MAX_MARK_PER_SUBJECT) computed first,
        # then total is divided by that product, and finally multiplied by 100.0.
        percentage = (total / (count * MAX_MARK_PER_SUBJECT)) * 100.0
        return percentage

    def calculate_grade(self):
        """
        Determines the student's letter grade based on percentage.
        Demonstrates relational operators and frozenset membership.
        """
        pct = self.calculate_percentage()

        if pct >= 85.0:
            grade = "A"
        elif pct >= 70.0:
            grade = "B"
        elif pct >= 55.0:
            grade = "C"
        elif pct >= 40.0:
            grade = "D"
        else:
            grade = "F"

        # Verify grade membership in the immutable frozenset
        if grade in VALID_GRADES:
            return grade
        return "F"

    def get_highest_mark(self):
        """
        Finds the maximum mark and corresponding subject.
        Returns a tuple: (subject_name, mark).
        """
        if len(self.marks) == 0:
            return ("None", 0.0)

        max_idx = 0
        for i in range(1, len(self.marks)):
            if self.marks[i] > self.marks[max_idx]:
                max_idx = i

        return (self.subjects[max_idx], self.marks[max_idx])

    def get_lowest_mark(self):
        """
        Finds the minimum mark and corresponding subject.
        Returns a tuple: (subject_name, mark).
        """
        if len(self.marks) == 0:
            return ("None", 0.0)

        min_idx = 0
        for i in range(1, len(self.marks)):
            if self.marks[i] < self.marks[min_idx]:
                min_idx = i

        return (self.subjects[min_idx], self.marks[min_idx])

    def display_marks_card(self):
        """
        Displays a structured marks card with subject-level breakdown and grades.
        """
        total = self.calculate_total()
        percentage = self.calculate_percentage()
        grade = self.calculate_grade()
        high_subj, high_mark = self.get_highest_mark()
        low_subj, low_mark = self.get_lowest_mark()

        max_possible = len(self.marks) * MAX_MARK_PER_SUBJECT

        print("=" * 55)
        print(f"            ACADEMIC MARKS CARD: ID {self.student_id}")
        print("=" * 55)
        print(f"{'Subject':<28} | {'Mark':<8} | {'Max Mark':<8}")
        print("-" * 55)

        for i in range(len(self.marks)):
            subj = self.subjects[i]
            mark = self.marks[i]
            print(f"{subj:<28} | {mark:<8.2f} | {MAX_MARK_PER_SUBJECT:<8.1f}")

        print("-" * 55)
        print(f"Total Marks Scored : {total:.2f} / {max_possible:.1f}")
        print(f"Overall Percentage : {percentage:.2f}%")
        print(f"Letter Grade       : {grade}")
        print(f"Highest Score      : {high_mark:.2f} ({high_subj})")
        print(f"Lowest Score       : {low_mark:.2f} ({low_subj})")
        print("=" * 55)


def enter_marks(academics_dict, student_id, marks_list, subject_tuple=SUBJECT_NAMES):
    """
    Creates or updates an AcademicRecord for a student.
    """
    record = AcademicRecord(student_id, marks_list, subject_tuple)
    academics_dict[student_id] = record
    return record


def get_academic_record(academics_dict, student_id):
    """
    Retrieves the AcademicRecord for a student, returning None if not found.
    """
    if student_id in academics_dict:
        return academics_dict[student_id]
    return None


def display_student_academics(academics_dict, student_id):
    """
    Displays the marks card for a student if the record exists.
    Demonstrates identity operator (is None).
    """
    record = get_academic_record(academics_dict, student_id)
    if record is None:
        print(f"\nNo academic marks found on record for Student ID {student_id}.")
        return

    record.display_marks_card()
