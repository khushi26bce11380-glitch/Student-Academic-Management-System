
from student import Student
from academic import AcademicRecord
from attendance import AttendanceRecord
from constants import MAXMARKPERSUBJECT


def generatestudentreport(studentsdict, academicsdict, attendancedict, studentid):
    if studentid not in studentsdict:
        print(f"\nStudent with ID {studentid} not found in the system.")
        return

    student = studentsdict[studentid]
    acadrec = academicsdict.get(studentid)
    attrec = attendancedict.get(studentid)

    if type(student) is not Student:
        print("Error: Invalid student record type encountered.")
        return

    print("\n" + "=" * 62)
    print(f"            OFFICIAL STUDENT REPORT CARD: ID {student.studentid}")
    print("=" * 62)
    print(f"Full Name          : {student.name}")
    print(f"Department         : {student.department}")
    
    feetext = "Paid" if student.hasfeepaid() else "Pending / Due"
    scholarshiptext = "Awarded (Merit)" if student.hasscholarship() else "Not Awarded"
    activetext = "Enrolled" if student.isactive() else "Withdrawn"
    print(f"Enrollment Status  : {activetext}")
    print(f"Fee Payment Status : {feetext}")
    print(f"Scholarship Status : {scholarshiptext}")
    print("-" * 62)
    
    if acadrec is None:
        print("Academic Marks     : No marks recorded yet.")
    else:
        print("SUBJECT-WISE PERFORMANCE (Stored via Python Array):")
        for i in range(len(acadrec.marks)):
            subj = acadrec.subjects[i]
            mark = acadrec.marks[i]
            print(f"  - {subj:<24} : {mark:>6.2f} / {MAXMARKPERSUBJECT:.1f}")

        total = acadrec.calculatetotal()
        percentage = acadrec.calculatepercentage()
        grade = acadrec.calculategrade()
        highsubj, highmark = acadrec.gethighestmark()
        lowsubj, lowmark = acadrec.getlowestmark()

        print("-" * 62)
        print(f"Total Marks        : {total:.2f} / {len(acadrec.marks) * MAXMARKPERSUBJECT:.1f}")
        print(f"Percentage         : {percentage:.2f}%")
        print(f"Letter Grade       : {grade}")
        print(f"Best Subject       : {highsubj} ({highmark:.2f})")
        print(f"Lowest Subject     : {lowsubj} ({lowmark:.2f})")

    print("-" * 62)

    if attrec is None:
        print("Attendance Record  : No attendance data recorded yet.")
    else:
        attpct = attrec.calculatepercentage()
        eligible = attrec.iseligible()
        verdict = "ELIGIBLE TO SIT FOR EXAMS" if eligible else "INELIGIBLE (ATTENDANCE SHORTAGE)"
        print("ATTENDANCE PERFORMANCE:")
        print(f"Classes Attended   : {attrec.attendedclasses} / {attrec.totalclasses}")
        print(f"Attendance Rate    : {attpct:.2f}%")
        print(f"Exam Eligibility   : {verdict}")

    print("=" * 62)


def display_class_summary(studentsdict, academicsdict, attendancedict):
    if len(studentsdict) == 0:
        print("\nNo students found in the system.")
        return

    print("\n" + "=" * 80)
    print("                           CLASS PERFORMANCE SUMMARY TABLE")
    print("=" * 80)
    header = f"{'ID':<6} | {'Name':<18} | {'Total':<8} | {'% Score':<8} | {'Grade':<6} | {'Att. %':<8} | {'Status':<10}"
    print(header)
    print("-" * 80)

    for studentid in studentsdict:
        student = studentsdict[studentid]
        acad = academicsdict.get(studentid)
        att = attendancedict.get(studentid)

        if acad is not None:
            totalstr = f"{acad.calculatetotal():.1f}"
            pctstr = f"{acad.calculatepercentage():.1f}%"
            gradestr = acad.calculategrade()
        else:
            totalstr = "N/A"
            pctstr = "N/A"
            gradestr = "N/A"

        if att is not None:
            attpctstr = f"{att.calculatepercentage():.1f}%"
            eligiblestr = "Eligible" if att.iseligible() else "Shortage"
        else:
            attpctstr = "N/A"
            eligiblestr = "Pending"

        row = f"{student.studentid:<6} | {student.name:<18} | {totalstr:<8} | {pctstr:<8} | {gradestr:<6} | {attpctstr:<8} | {eligiblestr:<10}"
        print(row)

    print("=" * 80)


def findhighestscorer(studentsdict, academicsdict):
    if len(academicsdict) == 0:
        return None

    topid = None
    toppct = -1.0

    for sid in academicsdict:
        record = academicsdict[sid]
        pct = record.calculatepercentage()
        if pct > toppct:
            toppct = pct
            topid = sid

    if topid is None:
        return None

    student = studentsdict.get(topid)
    studentname = student.name if student is not None else "Unknown"
    record = academicsdict[topid]
    grade = record.calculategrade()

    return (topid, studentname, toppct, grade)


def calculateclassaverage(academicsdict):

    if len(academicsdict) == 0:
        return 0.0

    totalpctsum = 0.0
    for record in academicsdict.values():
        totalpctsum += record.calculatepercentage()

    averagepercentage = totalpctsum / len(academicsdict)
    return averagepercentage
