'''
EXPERIMENT No. : 3      PROGRAM:02
Name : TAUSEEF MUSHTAQUE ALI SHAIKH
Roll No : 18CO63		Batch : B-3
Aim : Program to implement Constructors in Python.
'''

import datetime

class Student:
    '''
    A STUDENT CLASS TO MANAGE STUDENTS.
    '''
    no_of_courses = 5       #class variable
    credits = 25            #class variable

    def __init__(self,r='', n='', a='', m=0):
        '''
		"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
		'''
        self.rollno = r
        self.name = n
        self.addr = a
        self.mob = m

    def setval(self, rollno, name, addr, mob):
        '''
        METHOD TO SET THE PROPERTIES OF THE OBJECT.
        '''
        self.rollno = rollno 
        self.name = name 
        self.addr = addr 
        self.mob = mob
    
    def getval(self):
        print('SELF IS AT: ',id(self))
        return self.rollno, self.name, self. no_of_courses, self.credits, self.mob

    @classmethod
    def setcourses(cls,n):
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
print(s1.getval())
print()

s2 = Student()
Student.setcourses(9)
Student.setcredits(55)
s2.setval('18CO55', 'RAUF YOOSAF SHAIKH', 'MUMBAI', 9191919191)
print(s2.getval())
print()

s3 = Student()
s3.setval('19DCO06', 'SAMIR FAKRUDDIN SHAIKH', 'GOVANDI', 8080808080)
print(s3.getval())
print()

s4 = Student()
s4.setval('SOME-ROLLNO', 'SOME-NAME', 'SOME-PLACE', 7474747474)
print(s4.getval())
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
OUTPUT:

SELF IS AT:  2897071214216
('18CO63', 'TAUSEEF MUSHTAQUE ALI SHAIKH', 5, 25, 9898989898)

SELF IS AT:  2897071211400
('18CO55', 'RAUF YOOSAF SHAIKH', 9, 55, 9191919191)

SELF IS AT:  2897071214344
('19DCO06', 'SAMIR FAKRUDDIN SHAIKH', 9, 55, 8080808080)

SELF IS AT:  2897071214408
('SOME-ROLLNO', 'SOME-NAME', 9, 55, 7474747474)

SELF IS AT:  2897071214216
('18CO63', 'TAUSEEF MUSHTAQUE ALI SHAIKH', 9, 30, 9898989898)

ENTER DATE (DD): 12
ENTER MONTH (MM): 5
ENTER YEAR (YYYY): 2030
IS WORKING? False
'''
