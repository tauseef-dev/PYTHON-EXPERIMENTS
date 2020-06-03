'''
EXPERIMENT No. : 3      PROGRAM: 01
Name : TAUSEEF MUSHTAQUE ALI SHAIKH
Roll No : 18CO63		Batch : B-3
Aim : Program to implement Classes in Python.
'''

import datetime

class Student:
    '''
    A STUDENT CLASS TO MANAGE STUDENTS.
    '''
    no_of_courses = 5       #class variable
    credits = 25            #class variable

    def setval(self,rollno,name,addr,mob):
        '''
        METHOD TO SET THE PROPERTIES OF THE OBJECT.
        '''
        self.rollno = rollno   #instance variable
        self.name = name
        self.mob = mob
    
    def getval(self):
        '''
        METHOD TO PRINT THE ADDRESS OF THE OBJECT INVOKING IT AND RETURNING THE VALUE OF IT. 
        '''
        print('SELF IS AT: ',id(self))
        return self.rollno, self.name, self. no_of_courses, self.credits, self.mob

    @classmethod
    def setcourses(cls,n):
        '''

        '''
        cls.no_of_courses = n
    
    @classmethod
    def setcredits(cls,c):
        cls.credits = c

    @staticmethod
    def is_workday(day):
        if(day.weekday()==6):
            return False
        return True
    
s1 = Student()
s1.setval('18CO63', 'TAUSEEF MUSHTAQUE ALI SHAIKH', 'MUMBAI', 9898989898)
print('S1 IS AT: ', id(s1))
print(s1.getval())
print()

s2 = Student()
s2.no_of_courses = 6
print('S2 IS AT: ',id(s2))
s2.setval('18CO55', 'RAUF YOOSAF SHAIKH', 'MUMBAI', 9191919191)
print(s2.getval())
print()

print(s1.getval())
print()
print('S1 = ', s1.__dict__)
print()
print('S2 = ', s2.__dict__)
print()

Student.setcredits(30)
print(s1.getval())
print()

date = int(input('ENTER DATE (DD): '))
month = int(input('ENTER MONTH (MM): '))
year = int(input('ENTER YEAR (YYYY): '))
d = datetime.date(year,month,date)
print('IS WORKING?', Student.is_workday(d))

'''
OUTPUT:-

S1 IS AT:  2310392089736
SELF IS AT:  2310392089736
('18CO63', 'TAUSEEF MUSHTAQUE ALI SHAIKH', 5, 25, 9898989898)

S2 IS AT:  2310392090056
SELF IS AT:  2310392090056
('18CO55', 'RAUF YOOSAF SHAIKH', 6, 25, 9191919191)

SELF IS AT:  2310392089736
('18CO63', 'TAUSEEF MUSHTAQUE ALI SHAIKH', 5, 25, 9898989898)

S1 =  {'rollno': '18CO63', 'name': 'TAUSEEF MUSHTAQUE ALI SHAIKH', 'mob': 9898989898}

S2 =  {'no_of_courses': 6, 'rollno': '18CO55', 'name': 'RAUF YOOSAF SHAIKH', 'mob': 9191919191}

SELF IS AT:  2310392089736
('18CO63', 'TAUSEEF MUSHTAQUE ALI SHAIKH', 5, 30, 9898989898)

ENTER DATE (DD): 10
ENTER MONTH (MM): 10
ENTER YEAR (YYYY): 2010
IS WORKING? False
'''