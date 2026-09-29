
from constants import MINATTENDANCEPERCENTAGE


class AttendanceRecord:

    def init(self, studentid, attendedclasses, totalclasses):
        self.studentid = studentid
        self.attendedclasses = attendedclasses
        self.totalclasses = totalclasses

    def calculatepercentage(self):
       
        if self.totalclasses == 0:
            return 0.0

        percentage = (self.attendedclasses / self.totalclasses) * 100.0
        return percentage

    def iseligible(self, minpercentage=MINATTENDANCEPERCENTAGE):

        return self.calculatepercentage() >= minpercentage

    def calculateshortfall(self):
        
        requiredclasses = (MINATTENDANCEPERCENTAGE * self.totalclasses) / 100.0
        if self.attendedclasses < requiredclasses:
            
            shortfall = int(requiredclasses - self.attendedclasses + 0.9999)
            return shortfall
        return 0

    def displayattendance(self):

        pct = self.calculatepercentage()
        eligible = self.iseligible()
        statustext = "ELIGIBLE FOR EXAMS" if eligible else "SHORTAGE WARNING"
        shortfall = self.calculateshortfall()

        print("=" * 55)
        print(f"            ATTENDANCE RECORD: ID {self.studentid}")
        print("=" * 55)
        print(f"Total Conducted Classes : {self.totalclasses}")
        print(f"Classes Attended        : {self.attendedclasses}")
        print(f"Attendance Percentage   : {pct:.2f}%")
        print(f"Minimum Required        : {MINATTENDANCEPERCENTAGE:.1f}%")
        print(f"Eligibility Verdict     : {statustext}")
        if not eligible and shortfall > 0:
            print(f"Shortfall Deficit       : {shortfall} class(es) below 75% limit")
        print("=" * 55)


def recordattendance(attendancedict, studentid, attended, total):
    
    record = AttendanceRecord(studentid, attended, total)
    attendancedict[studentid] = record
    return record


def getattendancerecord(attendancedict, studentid):
    
    if studentid in attendancedict:
        return attendancedict[studentid]
    return None


def displaystudentattendance(attendancedict, studentid):
    
    record = getattendancerecord(attendancedict, studentid)
    if record is None:
        print(f"\nNo attendance record found for Student ID {studentid}.")
        return

    record.displayattendance()
