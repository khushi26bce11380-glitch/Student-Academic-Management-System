

import array
from constants import SUBJECTNAMES, MAXMARKPERSUBJECT, VALIDGRADES


class AcademicRecord:

    def init(self, studentid, markslist, subjecttuple=SUBJECTNAMES):
        self.studentid = studentid
        self.subjects = subjecttuple
        self.marks = array.array("f", markslist)

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
        percentage = (total / (count * MAXMARKPERSUBJECT)) * 100.0
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
        if grade in VALIDGRADES:
            return grade
        return "F"

    def gethighestmark(self):
        if len(self.marks) == 0:
            return ("None", 0.0)

        maxidx = 0
        for i in range(1, len(self.marks)):
            if self.marks[i] > self.marks[maxidx]:
                maxidx = i

        return (self.subjects[maxidx], self.marks[maxidx])

    def getlowestmark(self):
        if len(self.marks) == 0:
            return ("None", 0.0)

        minidx = 0
        for i in range(1, len(self.marks)):
            if self.marks[i] < self.marks[minidx]:
                minidx = i

        return (self.subjects[minidx], self.marks[minidx])

    def displaymarkscard(self):
        total = self.calculatetotal()
        percentage = self.calculatepercentage()
        grade = self.calculategrade()
        highsubj, highmark = self.gethighestmark()
        lowsubj, lowmark = self.getlowestmark()

        maxpossible = len(self.marks) * MAXMARKPERSUBJECT

        print("=" * 55)
        print(f"            ACADEMIC MARKS CARD: ID {self.studentid}")
        print("=" * 55)
        print(f"{'Subject':<28} | {'Mark':<8} | {'Max Mark':<8}")
        print("-" * 55)

        for i in range(len(self.marks)):
            subj = self.subjects[i]
            mark = self.marks[i]
            print(f"{subj:<28} | {mark:<8.2f} | {MAXMARKPERSUBJECT:<8.1f}")

        print("-" * 55)
        print(f"Total Marks Scored : {total:.2f} / {maxpossible:.1f}")
        print(f"Overall Percentage : {percentage:.2f}%")
        print(f"Letter Grade       : {grade}")
        print(f"Highest Score      : {highmark:.2f} ({highsubj})")
        print(f"Lowest Score       : {lowmark:.2f} ({lowsubj})")
        print("=" * 55)


def entermarks(academicsdict, studentid, markslist, subjecttuple=SUBJECTNAMES):
    record = AcademicRecord(studentid, markslist, subjecttuple)
    academicsdict[studentid] = record
    return record


def getacademicrecord(academicsdict, studentid):
    if studentid in academicsdict:
        return academicsdict[studentid]
    return None


def displaystudentacademics(academicsdict, studentid):
    record = getacademicrecord(academicsdict, studentid)
    if record is None:
        print(f"\nNo academic marks found on record for Student ID {studentid}.")
        return

    record.displaymarkscard()
