

import array
from constants import SUBJECT_NAMES, MAX_MARK_PER_SUBJECT, VALID_GRADES


class AcademicRecord:

    def init(self, student_id, marks_list, subject_tuple=SUBJECT_NAMES):
        self.student_id = student_id
        self.subjects = subject_tuple
        self.marks = array.array("f", marks_list)

    def calculatetotal(self):
        total = 0.0
        for mark in self.marks:
            total += mark
        return total

    def calculatepercentage(self):
        total = self.calculatetotal()
        count = len(self.marks)
        if count == 0:
            return 0.0
        percentage = (total / (count * MAX_MARK_PER_SUBJECT)) * 100.0
        return percentage

    def calculategrade(self):
        pct = self.calculatepercentage()

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
        if grade in VALID_GRADES:
            return grade
        return "F"

    def gethighestmark(self):
        if len(self.marks) == 0:
            return ("None", 0.0)

        max_idx = 0
        for i in range(1, len(self.marks)):
            if self.marks[i] > self.marks[max_idx]:
                max_idx = i

        return (self.subjects[max_idx], self.marks[max_idx])

    def getlowestmark(self):
        if len(self.marks) == 0:
            return ("None", 0.0)

        min_idx = 0
        for i in range(1, len(self.marks)):
            if self.marks[i] < self.marks[min_idx]:
                min_idx = i

        return (self.subjects[min_idx], self.marks[min_idx])

    def displaymarkscard(self):
        total = self.calculatetotal()
        percentage = self.calculatepercentage()
        grade = self.calculategrade()
        high_subj, high_mark = self.gethighestmark()
        low_subj, low_mark = self.getlowestmark()

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


def entermarks(academics_dict, student_id, marks_list, subject_tuple=SUBJECT_NAMES):
    record = AcademicRecord(student_id, marks_list, subject_tuple)
    academics_dict[student_id] = record
    return record


def getacademicrecord(academics_dict, student_id):
    if student_id in academics_dict:
        return academics_dict[student_id]
    return None


def displaystudentacademics(academics_dict, student_id):
    record = getacademicrecord(academics_dict, student_id)
    if record is None:
        print(f"\nNo academic marks found on record for Student ID {student_id}.")
        return

    record.displaymarkscard()
