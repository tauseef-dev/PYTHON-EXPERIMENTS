'''
EXPERIMENT No. : 2      PROGRAM: 01
Name : TAUSEEF MUSHTAQUE ALI SHAIKH
Roll No : 18CO63		Batch : B-3
Aim : Program to implement IF-ELSE loop.
'''

'''
Decision making is required when we want to execute a code only if a certain condition is satisfied.
The if…elif…else statement is used in Python for decision making.
Syntax:  if test expression:
             Body of if
         elif:
             Body of elif
         else:
            Body of else
'''
#IF-ELSE CONDITION

print("")

f = int(input("ENTER FIRST NO.: "))
s = int(input("ENTER SECOND NO.: "))
t = int(input("ENTER THIRD NO.: "))

print("")

if f>s:
    if f>t:
        print(str(f) + " IS THE LARGEST NUMBER!")
elif s>t:
    print(str(s) + " IS THE LARGEST NUMBER!")
else:
    print(str(t) + " IS THE LARGEST NUMBER!")

print("")

s1 = input("ENTER FIRST STRING: ")
s2 = input("ENTER SECONG STRING: ")

print("")

print("THE COMPARED STRINGS ARE "+ s1 + " & " + s2 )

print("")

s1 = s1.upper()
s2 = s2.upper()

if s1 == s2:
    print("STRINGS ARE SIMILAR!")
else:
    print("STRINGS ARE DIFFERENT!")

print("")

st1 = "HELLO"
print("ADRESS OF st1(HELLO) IS: " + str(id(st1)))

print("")

st1 = "WORLD"
st2 = "WORLD"

print("ADDRESS OF st1(WORLD) IS: " + str(id(st1)))
print("ADDRESS OF st2(WORLD) IS: " + str(id(st2)))

'''
OUTPUT:

ENTER FIRST NO.: 10
ENTER SECOND NO.: 20
ENTER THIRD NO.: 05

20 IS THE LARGEST NUMBER!

ENTER FIRST STRING: TAUSEEF
ENTER SECONG STRING: SHAIKH

THE COMPARED STRINGS ARE TAUSEEF & SHAIKH

STRINGS ARE DIFFERENT!

ADRESS OF st1(HELLO) IS: 2196469634864

ADDRESS OF st1(WORLD) IS: 2196469634736
ADDRESS OF st2(WORLD) IS: 2196469634736
'''