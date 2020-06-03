'''
EXPERIMENT No. : 1      PROGRAM: 01
Name : TAUSEEF MUSHTAQUE ALI SHAIKH
Roll No : 18CO63		Batch : B-3
Aim : Program to implement Comments, Data types, Expressions, Input and Output Functions.
'''

#SINGLE LINE COMMENT:
#Single line comment simply by beginning a line with the hash (#) Character, and they are automatically terminated as end of line.

'''
MULTI LINE COMMENT:
Comments that span multiple lines - used to explain things in more details - are crested by adding a
delimiter ('''  ''') on each end of a comment. Otherwise it is not recommended while developing any
application software.
''' 

#ILLUSTRATING DATA-TYPES
'''
Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

'''

print("\nILLUSTRATING DATA-TYPES\n")

i = 10
f = 20.5
s = "AN EXAMPLE OF A STRING."
c = 2+3j

print("\nINTEGER VALUE IS: ",i,"\nFLOAT VALUE IS: ",f,"\nSTRING VALUE IS: ",s,"\nCOMPLEX VALUE IS: ",c)
print("\nTYPE OF 'i' IS: ",type(i),"\nTYPE OF 'f' IS: ",type(f),"\nTYPE OF 's' IS: ",type(s),"\nTYPE OF 'c' IS: ",type(c))

#ILLUSTRATING EXPRESSIONS
'''
An expression is a combination of values, variables, operators, and calls to functions.
If you type an expression at the Python prompt,
the interpreter evaluates it and displays the result, which is always a value

'''

print("\nILLUSTRATING EXPRESSIONS\n")

print("\nDIVISION OF ' 2 by",i,"' IS: ",21/i)
print("\nQUOTIENT  ' 2 by",i,"' IS: ",21//i)
print("\nREMAINDER  ' 2 by",i,"' IS: ",21%i)
print("\nPOWER OF ' 2 to 3 ' IS: ",2**3)
x,y = divmod(5,2)
print("\nDIVMOD OF 5/2 IS: ",x,y)
#print("DIVMOD OF 5/2 IS: ",divmod(5,2))

#ILLUSTRATING INPUT-OUTPUT FUNCTIONS
'''
Python provides numerous built-in functions that are readily available to us at the Python prompt.

OUTPUT:
We use the print() function to output data to the standard output device (screen).

INPUT:
Up till now, our programs were static.
The value of variables were defined or hard coded into the source code.

To allow flexibility we might want to take the input from the user.
In Python, we have the input() function to allow this. The syntax for input() is
'''

print("\nILLUSTRATING INPUT-OUTPUT FUNCTIONS\n")

i = int(input("ENTER A INTEGER VALUE: "))
f = float(input("ENTER A FLOAT VALUE: "))
s = input("ENTER A STRING VALUE: ")
c = complex(input("ENTER A COMPLEX VALUE: "))
print("\nENTEREDINTEGER VALUE IS: ",i,"\nENTERED FLOAT VALUE IS: ",f,"\nENTERED STRING VALUE IS: ",s,"\nENTERED COMPLEX VALUE IS: ",c)


'''
OUTPUT:-

ILLUSTRATING DATA-TYPES


INTEGER VALUE IS:  10
FLOAT VALUE IS:  20.5
STRING VALUE IS:  AN EXAMPLE OF A STRING.
COMPLEX VALUE IS:  (2+3j)

TYPE OF 'i' IS:  <class 'int'>
TYPE OF 'f' IS:  <class 'float'>
TYPE OF 's' IS:  <class 'str'>
TYPE OF 'c' IS:  <class 'complex'>

ILLUSTRATING EXPRESSIONS


DIVISION OF ' 2 by 10 ' IS:  2.1

QUOTIENT  ' 2 by 10 ' IS:  2

REMAINDER  ' 2 by 10 ' IS:  1

POWER OF ' 2 to 3 ' IS:  8

DIVMOD OF 5/2 IS:  2 1

ILLUSTRATING INPUT-OUTPUT FUNCTIONS

ENTER A INTEGER VALUE: 5
ENTER A FLOAT VALUE: 5.5
ENTER A STRING VALUE: five
ENTER A COMPLEX VALUE: 5+5j

ENTEREDINTEGER VALUE IS:  5
ENTERED FLOAT VALUE IS:  5.5
ENTERED STRING VALUE IS:  five
ENTERED COMPLEX VALUE IS:  (5+5j)

'''