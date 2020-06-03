'''
EXPERIMENT No. : 1      PROGRAM: 03
Name : TAUSEEF MUSHTAQUE ALI SHAIKH
Roll No : 18CO63		Batch : B-3
Aim : Program to implement different data types such as List, Tuple, Dictionaries, Array.
'''

from array import *

print("-------------------- LIST ---------------------")

print("")

l = [12,23,-10,3.5,'PYTHON','CO']
print("PRINTING ORIGINAL LIST: ", l)
print("PRINTING FIRST THREE ELEMENTS OF A LIST: ",l[0:3])
print("PRINTING LAST ELEMENTS OF A LIST: ",l[-1])
print("PRINTING FIRST THREE ELEMENTS OF A LIST TWICE: ",l[0:3]*2)

print("")

print("-------------------- LIST FUNCTION -------------------- ")

print("")

l1 = list(range(1,8))
print("LIST OF RANGE 1 TO 7: ", l1)
l1.append(9)
print("APPEND 9: ",l1)
l1.sort(reverse = True)
print("DESCENDING SORT: ",l1)
l1.sort()
print("ASCENDING SORT: ",l1)
l1.reverse()
print("REVERSE: ",l1)
l1.sort()
l1.remove(9)
print("REMOVE 9: ",l1)
print("COUNT: ",l1.count(5))
print("MAX: ",max(l1))
print("MIN: ",min(l1))
print("INDEX OF 6: ",l1.index(6))

print("")

print("-------------------- MATRICES USING LISTS -------------------- ")

print("")

m1 = [[1,2,3],[4,5,6],[7,8,9]]
for r in m1:
    print(r)

print("")

print("-------------------- TUPLE DATA-TYPE -------------------- ")

print("")

tpl1 = (-3.5,10,20,'PYTHON','B-3')
print("CREATED TUPLE IS: ",tpl1)
print("TUPLE ELEMENTS 0 TO 2 IS: ",tpl1[0:2])

print("")

print("-------------------- TUPLE FUNCTION -------------------- ")

print("")

tpl2 = (3,5,6,9,4,8,5,9,5,9,1,2)
print("LENGTH: ",len(tpl2))
print("MIN: ",min(tpl2))
print("MAX: ",max(tpl2))
print("COUNT NOS. OF 5: ",tpl2.count(9))
print("REVERSE SORT: ",sorted(tpl2,reverse=True))

print("")

print("-------------------- DICTIONARIES i.e. KEY:VALUE PAIR -------------------- ")

print("")

d1 = {'NAME':"TAUSEEF",'GENDER':"MALE",'AGE':19,'COLLEGE':"AIKTC"}
print("PRINT DICTIONARY: ",d1)

print("")

print("--> KEYS: ",d1.keys())
print("--> values: ",d1.values())
print("--> KEYS & VALUES: ",d1.items())
d1.update({'COUNTRY':"INDIA"})
print("--> UPDATED DICTIONARY: ", d1)

print("")

print("-------------------- ARRAYS -------------------- ")

print("")

arr = array('i',[10,20,30,40,50])
print("THE ARRAY ELEMENTS ARE: ")
for i in arr:
    print(i)
print("LENGTH OF ARRAY IS: ",len(arr))

arrr = array('u',['a','b','c','d','e','f'])
for ch in arrr:
    print(ch)

'''
OUTPUT:

-------------------- LIST ---------------------

PRINTING ORIGINAL LIST:  [12, 23, -10, 3.5, 'PYTHON', 'CO']
PRINTING FIRST THREE ELEMENTS OF A LIST:  [12, 23, -10]
PRINTING LAST ELEMENTS OF A LIST:  CO
PRINTING FIRST THREE ELEMENTS OF A LIST TWICE:  [12, 23, -10, 12, 23, -10]

-------------------- LIST FUNCTION --------------------

LIST OF RANGE 1 TO 7:  [1, 2, 3, 4, 5, 6, 7]
APPEND 9:  [1, 2, 3, 4, 5, 6, 7, 9]
DESCENDING SORT:  [9, 7, 6, 5, 4, 3, 2, 1]
ASCENDING SORT:  [1, 2, 3, 4, 5, 6, 7, 9]
REVERSE:  [9, 7, 6, 5, 4, 3, 2, 1]
REMOVE 9:  [1, 2, 3, 4, 5, 6, 7]
COUNT:  1
MAX:  7
MIN:  1
INDEX OF 6:  5

-------------------- MATRICES USING LISTS --------------------

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

-------------------- TUPLE DATA-TYPE --------------------

CREATED TUPLE IS:  (-3.5, 10, 20, 'PYTHON', 'B-3')
TUPLE ELEMENTS 0 TO 2 IS:  (-3.5, 10)

-------------------- TUPLE FUNCTION --------------------

LENGTH:  12
MIN:  1
MAX:  9
COUNT NOS. OF 5:  3
REVERSE SORT:  [9, 9, 9, 8, 6, 5, 5, 5, 4, 3, 2, 1]

-------------------- DICTIONARIES i.e. KEY:VALUE PAIR --------------------

PRINT DICTIONARY:  {'NAME': 'TAUSEEF', 'GENDER': 'MALE', 'AGE': 19, 'COLLEGE': 'AIKTC'}

--> KEYS:  dict_keys(['NAME', 'GENDER', 'AGE', 'COLLEGE'])
--> values:  dict_values(['TAUSEEF', 'MALE', 19, 'AIKTC'])
--> KEYS & VALUES:  dict_items([('NAME', 'TAUSEEF'), ('GENDER', 'MALE'), ('AGE', 19), ('COLLEGE', 'AIKTC')])
--> UPDATED DICTIONARY:  {'NAME': 'TAUSEEF', 'GENDER': 'MALE', 'AGE': 19, 'COLLEGE': 'AIKTC', 'COUNTRY': 'INDIA'}

-------------------- ARRAYS --------------------

THE ARRAY ELEMENTS ARE:
10
20
30
40
50
LENGTH OF ARRAY IS:  5
a
b
c
d
e
f
'''