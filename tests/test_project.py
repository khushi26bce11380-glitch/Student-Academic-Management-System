"""
test_project.py
Verification suite using plain Python assert statements only (no unittest, no pytest).

Run via command:
    python tests/test_project.py
"""

import sys
import os

# Ensure modules can be imported when running from project root or tests/ directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import array
from constants import (
    SUBJECT_NAMES,
    MAX_MARK_PER_SUBJECT,
    FLAG_ACTIVE,
    FLAG_FEE_PAID,
    FLAG_SCHOLARSHIP,
    VALID_GRADES,
)
from student import (
    Student,
    add_student,
    search_student,
    update_student,
    delete_student,
)
from academic import (
    AcademicRecord,
    enter_marks,
    get_academic_record,
)
from attendance import (
    AttendanceRecord,
    record_attendance,
    get_attendance_record,
)
from reports import (
    find_highest_scorer,
    calculate_class_average,
)
from validation import (
    is_valid_integer,
    is_valid_float,
)


def test_student_and_bitwise_flags():
    """Tests Student creation, set uniqueness, and bitwise operations."""
    print("Running test_student_and_bitwise_flags...")

    s = Student(201, "Test Student", "CS", FLAG_ACTIVE)
    assert s.student_id == 201
    assert s.name == "Test Student"
    assert s.department == "CS"
    assert s.is_active() is True
    assert s.has_fee_paid() is False
    assert s.has_scholarship() is False

    # Test bitwise OR (enabling fee paid)
    s.set_fee_paid(True)
    assert s.has_fee_paid() is True
    assert (s.status_flags & FLAG_FEE_PAID) != 0

    # Test bitwise AND with NOT (clearing fee paid)
    s.set_fee_paid(False)
    assert s.has_fee_paid() is False

    # Test bitwise XOR (toggling scholarship)
    s.toggle_scholarship()
    assert s.has_scholarship() is True
    s.toggle_scholarship()
    assert s.has_scholarship() is False

    # Test tuple representation
    t = s.to_summary_tuple()
    assert type(t) is tuple
    assert t == (201, "Test Student", "CS")

    # Test set and dict management
    students_dict = {}
    id_set = set()
    acad_dict = {}
    att_dict = {}

    # Test addition
    assert add_student(students_dict, id_set, s) is True
    assert 201 in id_set
    assert 201 in students_dict

    # Test duplicate prevention (membership in set)
    dup = Student(201, "Duplicate", "CS")
    assert add_student(students_dict, id_set, dup) is False

    # Test search with identity check
    found = search_student(students_dict, 201)
    assert found is not None
    assert found.name == "Test Student"
    assert search_student(students_dict, 999) is None

    # Test update
    assert update_student(students_dict, 201, "Updated Name", "IT") is True
    assert students_dict[201].name == "Updated Name"
    assert students_dict[201].department == "IT"

    # Test delete
    assert delete_student(students_dict, acad_dict, att_dict, id_set, 201) is True
    assert 201 not in id_set
    assert 201 not in students_dict
    assert delete_student(students_dict, acad_dict, att_dict, id_set, 201) is False

    print("  -> PASSED: Student and Bitwise Flags")


def test_academic_record_and_array():
    """Tests AcademicRecord calculations and Python array data structure."""
    print("Running test_academic_record_and_array...")

    marks = [90.0, 80.0, 70.0]
    rec = AcademicRecord(301, marks, SUBJECT_NAMES)

    # Verify array data structure
    assert type(rec.marks) is array.array
    assert rec.marks.typecode == "f"
    assert len(rec.marks) == 3

    # Arithmetic total
    total = rec.calculate_total()
    assert abs(total - 240.0) < 1e-4

    # Percentage: (240 / 300) * 100 = 80.0%
    pct = rec.calculate_percentage()
    assert abs(pct - 80.0) < 1e-4

    # Grade calculation
    grade = rec.calculate_grade()
    assert grade == "B"
    assert grade in VALID_GRADES

    # Highest and Lowest marks
    high_subj, high_mark = rec.get_highest_mark()
    low_subj, low_mark = rec.get_lowest_mark()
    assert high_subj == SUBJECT_NAMES[0]
    assert abs(high_mark - 90.0) < 1e-4
    assert low_subj == SUBJECT_NAMES[2]
    assert abs(low_mark - 70.0) < 1e-4

    # Grade boundaries check
    rec_a = AcademicRecord(302, [95.0, 90.0, 88.0])
    assert rec_a.calculate_grade() == "A"

    rec_f = AcademicRecord(303, [30.0, 25.0, 35.0])
    assert rec_f.calculate_grade() == "F"

    print("  -> PASSED: Academic Record and Array")


def test_attendance_record():
    """Tests AttendanceRecord calculations and eligibility threshold."""
    print("Running test_attendance_record...")

    # 40 out of 50 classes = 80% (Eligible since >= 75%)
    att1 = AttendanceRecord(401, 40, 50)
    assert abs(att1.calculate_percentage() - 80.0) < 1e-4
    assert att1.is_eligible(75.0) is True
    assert att1.calculate_shortfall() == 0

    # 30 out of 50 classes = 60% (Ineligible since < 75%)
    att2 = AttendanceRecord(402, 30, 50)
    assert abs(att2.calculate_percentage() - 60.0) < 1e-4
    assert att2.is_eligible(75.0) is False
    # Required: 50 * 0.75 = 37.5 -> 38 classes, shortfall = 38 - 30 = 8 classes
    assert att2.calculate_shortfall() == 8

    print("  -> PASSED: Attendance Record")


def test_validation_helpers():
    """Tests input validation logic without try/except."""
    print("Running test_validation_helpers...")

    # Integer validation
    assert is_valid_integer("101") is True
    assert is_valid_integer("0") is True
    assert is_valid_integer("  450  ") is True
    assert is_valid_integer("abc") is False
    assert is_valid_integer("12.5") is False
    assert is_valid_integer("-5") is False
    assert is_valid_integer("") is False

    # Float validation
    assert is_valid_float("85.5") is True
    assert is_valid_float("100") is True
    assert is_valid_float("0.0") is True
    assert is_valid_float("  92.75  ") is True
    assert is_valid_float("85.5.2") is False
    assert is_valid_float("abc") is False
    assert is_valid_float("") is False
    assert is_valid_float(".") is False

    print("  -> PASSED: Validation Helpers")


def test_reports_and_analytics():
    """Tests analytics functions: class average and highest scorer."""
    print("Running test_reports_and_analytics...")

    students = {
        501: Student(501, "Alice", "CS"),
        502: Student(502, "Bob", "IT"),
    }
    academics = {
        501: AcademicRecord(501, [90.0, 95.0, 92.0]),  # avg = 92.33%
        502: AcademicRecord(502, [70.0, 75.0, 72.0]),  # avg = 72.33%
    }

    # Test highest scorer tuple
    top = find_highest_scorer(students, academics)
    assert top is not None
    assert type(top) is tuple
    top_id, top_name, top_pct, top_grade = top
    assert top_id == 501
    assert top_name == "Alice"
    assert top_grade == "A"
    assert top_pct > 92.0

    # Test class average
    avg = calculate_class_average(academics)
    assert abs(avg - 82.3333) < 0.1

    print("  -> PASSED: Reports and Analytics")


def run_all_tests():
    """Executes all test functions sequentially."""
    print("=" * 60)
    print("   RUNNING ACADEMIC MANAGEMENT SYSTEM TEST SUITE")
    print("=" * 60)

    test_student_and_bitwise_flags()
    test_academic_record_and_array()
    test_attendance_record()
    test_validation_helpers()
    test_reports_and_analytics()

    print("=" * 60)
    print(">>> ALL ASSERTION TESTS COMPLETED SUCCESSFULLY! <<<")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
