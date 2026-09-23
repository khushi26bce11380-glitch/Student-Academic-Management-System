"""
student.py
Defines the Student class and student profile management operations.

Course topics demonstrated:
- Classes and objects, constructors, attributes, methods (without magic methods).
- Bitwise operators (&, |, ^, ~) for student status tracking.
- Identity operators (is, is not) for genuine null checks.
- Membership operators (in, not in) with sets and dictionaries.
- Tuples, lists, dictionaries, and sets.
"""

from constants import FLAG_ACTIVE, FLAG_FEE_PAID, FLAG_SCHOLARSHIP


class Student:
    """
    Represents an individual student record.
    Uses normal attributes and beginner-level methods without any magic methods.
    """

    def __init__(self, student_id, name, department, status_flags=FLAG_ACTIVE):
        # Basic attribute assignment
        self.student_id = student_id
        self.name = name
        self.department = department
        # Bitmask integer storing student standing flags
        self.status_flags = status_flags

    def is_active(self):
        """Checks if student is active using bitwise AND."""
        return (self.status_flags & FLAG_ACTIVE) != 0

    def has_fee_paid(self):
        """Checks if tuition fee is paid using bitwise AND."""
        return (self.status_flags & FLAG_FEE_PAID) != 0

    def has_scholarship(self):
        """Checks if scholarship is awarded using bitwise AND."""
        return (self.status_flags & FLAG_SCHOLARSHIP) != 0

    def set_fee_paid(self, is_paid):
        """
        Updates the fee status flag using bitwise OR (to enable)
        or bitwise AND with bitwise NOT (to clear).
        """
        if is_paid:
            # Bitwise OR assignment
            self.status_flags = self.status_flags | FLAG_FEE_PAID
        else:
            # Bitwise AND with bitwise NOT inversion
            self.status_flags = self.status_flags & (~FLAG_FEE_PAID)

    def toggle_scholarship(self):
        """Toggles scholarship award status using bitwise XOR."""
        self.status_flags = self.status_flags ^ FLAG_SCHOLARSHIP

    def to_summary_tuple(self):
        """
        Returns a fixed tuple representation of core student details.
        Demonstrates meaningful tuple usage.
        """
        return (self.student_id, self.name, self.department)

    def display_info(self):
        """Displays formatted student profile and academic standing."""
        fee_status = "Paid" if self.has_fee_paid() else "Pending"
        scholarship_status = "Awarded" if self.has_scholarship() else "None"
        active_status = "Active" if self.is_active() else "Inactive"

        print("-" * 50)
        print(f"Student ID     : {self.student_id}")
        print(f"Name           : {self.name}")
        print(f"Department     : {self.department}")
        print(f"Enrollment     : {active_status}")
        print(f"Fee Status     : {fee_status}")
        print(f"Scholarship    : {scholarship_status}")
        print("-" * 50)


def add_student(students_dict, student_id_set, student_obj):
    """
    Registers a new student into the system.
    Uses set membership to enforce unique student IDs.
    """
    # Membership operator check on set
    if student_obj.student_id in student_id_set:
        return False

    # Store in dictionary and record in set
    students_dict[student_obj.student_id] = student_obj
    student_id_set.add(student_obj.student_id)
    return True


def display_all_students(students_dict):
    """
    Iterates through the student dictionary and displays all student records.
    """
    # Comparison operator with len()
    if len(students_dict) == 0:
        print("\nNo students currently registered in the system.")
        return

    print(f"\nTotal Registered Students: {len(students_dict)}")
    for student_id in students_dict:
        student = students_dict[student_id]
        student.display_info()


def search_student(students_dict, student_id):
    """
    Searches for a student by ID in the dictionary.
    Returns the Student object if found, or None if not found.
    """
    if student_id in students_dict:
        return students_dict[student_id]
    return None


def update_student(students_dict, student_id, new_name, new_dept):
    """
    Updates the name and department of an existing student.
    Demonstrates identity operator (is None).
    """
    student = search_student(students_dict, student_id)
    # Identity operator check
    if student is None:
        return False

    student.name = new_name
    student.department = new_dept
    return True


def delete_student(students_dict, academics_dict, attendance_dict, student_id_set, student_id):
    """
    Deletes student profile and cascades removal across marks and attendance.
    """
    # Membership check on set
    if student_id not in student_id_set:
        return False

    # Remove from primary records
    del students_dict[student_id]
    student_id_set.remove(student_id)

    # Clean up associated records if they exist
    if student_id in academics_dict:
        del academics_dict[student_id]

    if student_id in attendance_dict:
        del attendance_dict[student_id]

    return True
