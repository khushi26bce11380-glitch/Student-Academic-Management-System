"""
constants.py
Defines constant values, configuration tuples, sets, frozensets, and status bitmasks.

Course topics demonstrated:
- Fundamentals, tuples, frozensets, bitwise shift/masks, arithmetic/logical constants.
"""

# Fixed catalog of subjects (Tuple demonstrating an immutable ordered collection)
SUBJECT_NAMES = ("Python Programming", "Calculus", "Physics")

# Maximum marks per subject
MAX_MARK_PER_SUBJECT = 100.0

# Total maximum marks calculated using arithmetic operators (* and len)
TOTAL_MAX_MARKS = len(SUBJECT_NAMES) * MAX_MARK_PER_SUBJECT

# Minimum attendance percentage required for examination eligibility
MIN_ATTENDANCE_PERCENTAGE = 75.0

# Fixed collection of valid letter grades (frozenset demonstrating an immutable set)
VALID_GRADES = frozenset({"A", "B", "C", "D", "F"})

# Status bitmask flags for student academic standing (Bitwise operators)
# 1 in binary (0001): Student is actively enrolled
FLAG_ACTIVE = 1 << 0

# 2 in binary (0010): Student has cleared semester tuition fees
FLAG_FEE_PAID = 1 << 1

# 4 in binary (0100): Student is awarded a merit scholarship
FLAG_SCHOLARSHIP = 1 << 2
