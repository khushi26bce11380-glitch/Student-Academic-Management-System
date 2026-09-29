
from constants import FLAGACTIVE, FLAGFEEPAID, FLAGSCHOLARSHIP


class Student:
    def init(self, studentid, name, department, statusflags=FLAGACTIVE):
       
        self.studentid = studentid
        self.name = name
        self.department = department

        self.statusflags = statusflags

    def isactive(self):
     
        return (self.statusflags & FLAGACTIVE) != 0

    def hasfeepaid(self):
       
        return (self.statusflags & FLAGFEEPAID) != 0

    def hasscholarship(self):
        
        return (self.statusflags & FLAGSCHOLARSHIP) != 0

    def setfeepaid(self, ispaid):
     
        if ispaid:
          
            self.statusflags = self.statusflags | FLAGFEEPAID
        else:
           
            self.statusflags = self.statusflags & (~FLAGFEEPAID)

    def togglescholarship(self):
       
        self.statusflags = self.statusflags ^ FLAGSCHOLARSHIP

    def to_summarytuple(self):
    
        return (self.studentid, self.name, self.department)

    def displayinfo(self):
        
        feestatus = "Paid" if self.hasfeepaid() else "Pending"
        scholarshipstatus = "Awarded" if self.hasscholarship() else "None"
        activestatus = "Active" if self.isactive() else "Inactive"

        print("-" * 50)
        print(f"Student ID     : {self.studentid}")
        print(f"Name           : {self.name}")
        print(f"Department     : {self.department}")
        print(f"Enrollment     : {activestatus}")
        print(f"Fee Status     : {feestatus}")
        print(f"Scholarship    : {scholarshipstatus}")
        print("-" * 50)


def add_student(studentsdict, studentidset, studentobj):
 
    if studentobj.studentid in studentidset:
        return False
    studentsdict[studentobj.studentid] = studentobj
    studentidset.add(studentobj.studentid)
    return True


def displayallstudents(studentsdict):

    if len(studentsdict) == 0:
        print("\nNo students currently registered in the system.")
        return

    print(f"\nTotal Registered Students: {len(studentsdict)}")
    for studentid in studentsdict:
        student = studentsdict[studentid]
        student.displayinfo()


def searchstudent(studentsdict, studentid):

    if studentid in studentsdict:
        return studentsdict[studentid]
    return None


def updatestudent(studentsdict, studentid, newname, newdept):
    student = searchstudent(studentsdict, studentid)
    if student is None:
        return False

    student.name = newname
    student.department = newdept
    return True


def deletestudent(studentsdict, academicsdict, attendancedict, studentidset, studentid):
  
    if studentid not in studentidset:
        return False

    del studentsdict[studentid]
    studentidset.remove(studentid)

    if studentid in academicsdict:
        del academicsdict[studentid]

    if studentid in attendancedict:
        del attendancedict[studentid]

    return True
