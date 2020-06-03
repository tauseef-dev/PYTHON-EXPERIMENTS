'''
EXPERIMENT No. : 4  PROGRAM : 02
Name : TAUSEEF MUSHTAQUE ALI SHAIKH
Roll No : 18CO63    Batch : B-3
Aim : Program to perform exception handeling in Python.
'''

from exp401 import Student

class SECO(Student):
	'''
    A INHERIT CALSS OF MAIN CLASS 'SECO'
	'''
	courses = list()
	skills = list()

	def __int__(self):
		'''
		"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
		'''
        try:
			'''
			The try block lets you test a block of code for errors.
			'''
            Student.__init__(self)

        except NameError:
			name = myname
            print('THIS IS NAME ERROR')

        except Exception as e:
            '''
            The except block lets you handle the error.
            '''
            print('ERROR:', e)

        else:
			'''
			The 'else:' keyword is used to define a block of code to be executed if no errors were raised.
			'''
            pass

        finally:
			'''
			The finally block lets you execute code, regardless of the result of the try- and except blocks.
			'''
            pass

    def setprop(self,c,s):
		'''
		A METHOD TO ADD PROPERTIES LIKE SKILLS AND COURSES TO THEIR RESPECTIVE LISTS.
		'''
        self.courses.append(c)
        self.skills.append(s)

    def getprop(self):
		'''
		A METHOD TO GET THE VALUES OF A STUDENT
		'''
        self.getval()
        print(self.courses)
        print(self.skills)
        return 'DONE'


s = SECO()
s.setval('18CO63', 'TAUSEEF MUSHTAQUE ALI SHAIKH', 'MUMBAI', 9898989898)
s.setprop('OSTL','PYTHON')
s.setprop('AOA','DESIGN ALGORITHM')

print(s.getprop())

'''
OUTPUT:

ROLLNO: 18CO63
NAME: TAUSEEF MUSHTAQUE ALI SHAIKH
NO. OF COURSES: 5
CREDITS: 25
MOBILE: 9898989898
['OSTL','AOA']
['PYTHON','DESIGN ALGORITHM']
DONE
'''
