'''
EXPERIMENT No. : 4  PROGRAM : 01
Name : TAUSEEF MUSHTAQUE ALI SHAIKH
Roll No : 18CO63    Batch : B-3
Aim : Program to perform INHERITANCE in Python.
'''
class Student:
	'''
	A MAIN CLASS TO STORE DATA OF STUDENTS.
	'''
    no_of_courses = 5
    credits = 25

    def __init__(self,*args):
        if args.__len__()==0:
            self.rollno = self.name = self.adr = self.mob = None
        elif isinstance(args[0],Student):
            self.rollno = args[0].rollno
            self.name = args[0].name
            self.addr = args[0].addr
            self.mob = args[0].mob
        else:
            self.setval(args[0],args[1],args[2],args[3])
    
    def setval(self, rollno, name, addr,mob):
		'''
		A METHOD TO SAT DATA OF STUDENT.
		'''
        self.rollno = rollno
        self.name = name
        self.addr=addr
        self.mob = mob
    
    def getval(self):
		'''
		A METHOD TO PRINT DATA OF STUDENT
		'''
        print('ROLLNO:',self.rollno,'\nNAME:',self.name,'\nNO. OF COURSES:',self.no_of_courses,'\nCREDITS:',self.credits, '\nMOBILE:',self.mob)


class Info(Student):
	'''
	AN INHERIT CLASS FROM MAIN CLASS 'STUDENT' TO GET INFORMATION OF THE STUDENT.
	'''
    def getprop(self):
        self.getval()

def main():
	'''
	A MAIN FUNCTION.
	'''        
	s = Info()
	s.setval('18CO63', 'TAUSEEF MUSHTAQUE ALI SHAIKH', 'MUMBAI', 9898989898)

	print(s.getprop())
	
if __name__ == '__main__':
	main()

'''
OUTPUT:

ROLLNO: 18CO63
NAME: TAUSEEF MUSHTAQUE ALI SHAIKH
NO. OF COURSES: 5
CREDITS: 25
MOBILE: 9898989898
None
'''
