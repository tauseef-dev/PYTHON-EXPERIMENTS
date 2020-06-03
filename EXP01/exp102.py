'''
EXPERIMENT No. : 1      PROGRAM: 02
Name : TAUSEEF MUSHTAQUE ALI SHAIKH
Roll No : 18CO63		Batch : B-3
Aim : Program to implement byte array, range, set and string function.
'''

#BYTE-ARRAYS
'''
bytearray() method returns a bytearray object which is an array of given bytes.
It gives a mutable sequence of integers in the range 0 <= x < 256.
Syntax: bytearray(source, encoding, errors)

'''

print("\nILLUSTRATING BYTE-ARRAYS\n")

b = bytearray(3)
print(b[0],b[1],b[2])
c = b'HELLO'
print(c)
print(type(c)) 

#RANGE
'''
The range() function returns a sequence of numbers,
starting from 0 by default, and increments by 1 (by default),
and ends at a specified number.

Syntax: range(start, stop, step)

Parameter Values:
Parameter	Description
start	Optional. An integer number specifying at which position to start. Default is 0
stop	Required. An integer number specifying at which position to end.
step	Optional. An integer number specifying the incrementation. Default is 1

'''

print("\nILLUSTRATING RANGE\n")

r = range(5)
print(r[0],r[4])
r = list(range(10,20))
print(r)

#SET
''''
A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

'''

print("\nILLUSTRATING SET\n")

s1 = {1,2,3}
print("Set-1: ", s1)
s2 = {3,4,5,6}
print("Set-2", s2)
print("Union: ", s1.union(s2))
print("Intersection: ", s1.intersection(s2))
print("IS", s1.union(s2), "superset of: ",s1,"?",s1.union(s2).issuperset(s1))

#STRING FUNCTION
'''
Python has a set of built-in methods that you can use on strings.
Some of them are demonstrated below:

'''

print("\nILLUSTRATING STRING FUNCTION\n")

s = input("Enter String: ")
subs = input("Enter Substring: ")
print("Reverse String Is: ", s[::-1])
print("is", subs, "Substring of", s , "?", subs in s)       #Checks whether a string contains other string or not
print("uppercased: ", s.upper())        #Converts a string into upper case

'''
OUTPUT:

ILLUSTRATING BYTE-ARRAYS

0 0 0
b'HELLO'
<class 'bytes'>

ILLUSTRATING RANGE

0 4
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

ILLUSTRATING SET

Set-1:  {1, 2, 3}
Set-2 {3, 4, 5, 6}
Union:  {1, 2, 3, 4, 5, 6}
Intersection:  {3}
IS {1, 2, 3, 4, 5, 6} superset of:  {1, 2, 3} ? True

ILLUSTRATING STRING FUNCTION

Enter String: aiktc
Enter Substring: ktc
Reverse String Is:  ctkia
is ktc Substring of aiktc ? True
uppercased:  AIKTC
'''