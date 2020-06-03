'''
EXPERIMENT No. : 2      PROGRAM: 03
Name : TAUSEEF MUSHTAQUE ALI SHAIKH
Roll No : 18CO63		Batch : B-3
Aim : Program to implement Functions in Python.
'''

'''
A function is a set of statements that take inputs, do some specific computation and produces output.
SYNTAX:
def FUNCTION_NAME():
  ARGUMENTS
'''

def fact(n):
    '''
    IT'S A FACTORIAL FUNCTION WHICH RETURNS THE FACTORIAL OF A GIVE NUMBER.
    INPUT:- INTEGER (int)
    '''
    """FUNCTION TO RETURN FACTORIAL VALUE OF GIVEN INTEGER"""
    if(type(n)==int):
        f=1
        for i in range(1,n+1):
            f=f*i
        return f
    else:
        return'CANNOT FIND THE FACTORIAL OF NON-INTEGER INPUT'

def fibo(n):
    '''
    IT'S A FIBONACCI FUNCTION WHICH RETURNS A LISTS CONTAINING FIBONACCI SERIES TILL GIVEN NUMBER.
    INPUT:- INTEGER (int)
    '''
    """FUNCTION TO RETURN LIST OF FIBONACCHI SERIES OF GIVEN INTEGER"""
    l = list()
    l.append(0)
    l.append(1)
    while (l[-1]+l[-2] <= n):
        l.append(l[-1]+l[-2])
    return l

def chkprime(n):
    '''
    IT'S A CHECK PRIMALITY FUNCTION IN WHICH A GIVEN NUMBER IS CHECKED, 
    WHETHER IT IS A PRIME NUMBER OR NOT.
    INPUT:- INTEGER (int)
    '''
    """FUNCTION TO CHECK THE PRIMALITY OF A GIVEN INTEGER"""
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    return True  

def sumfibo(n):
    l = fibo(n)
    sum = 0
    for i in l:
        sum+=i
    return sum

while True:
    print('\t\t\tMENU\n1. FACTORIAL OF A GIVEN NUMBER\n2. FIBONACCI OF GIVEN NUMBER\n3. SUMMATION OF FIBONACCI\n4. PRIMALITY\n0. EXIT')
    ch = int(input('ENTER YOUT CHOICE: '))
    if ch in range(1,5):
        n = int(input('ENTER THE NUMBER: '))
    if ch == 1:
        print('FACTORIAL OF',n,'IS',fact(n))
    elif ch == 2:
        print('FIBONACCI SERIES TILL',n,'IS',fibo(n))
    elif ch == 3:
        print('SUMMATION OF FIBONACCI SEIES TILL',n,'IS',sumfibo(n))
    elif ch == 4:
        print('PRIMALITY OF',n,'IS',chkprime(n))
    elif ch == 0:
        break
    else:
        print('ENTER A VALID INPUT!')

'''
OUTPUT:

                        MENU
1. FACTORIAL OF A GIVEN NUMBER
2. FIBONACCI OF GIVEN NUMBER
3. SUMMATION OF FIBONACCI
4. PRIMALITY
0. EXIT
ENTER YOUT CHOICE: 1
ENTER THE NUMBER: 6
FACTORIAL OF 6 IS 720
                        MENU
1. FACTORIAL OF A GIVEN NUMBER
2. FIBONACCI OF GIVEN NUMBER
3. SUMMATION OF FIBONACCI
4. PRIMALITY
0. EXIT
ENTER YOUT CHOICE: 2
ENTER THE NUMBER: 4
FIBONACCI SERIES TILL 4 IS [0, 1, 1, 2, 3]
                        MENU
1. FACTORIAL OF A GIVEN NUMBER
2. FIBONACCI OF GIVEN NUMBER
3. SUMMATION OF FIBONACCI
4. PRIMALITY
0. EXIT
ENTER YOUT CHOICE: 3
ENTER THE NUMBER: 7
SUMMATION OF FIBONACCI SEIES TILL 7 IS 12
                        MENU
1. FACTORIAL OF A GIVEN NUMBER
2. FIBONACCI OF GIVEN NUMBER
3. SUMMATION OF FIBONACCI
4. PRIMALITY
0. EXIT
ENTER YOUT CHOICE: 4
ENTER THE NUMBER: 9
PRIMALITY OF 9 IS False
                        MENU
1. FACTORIAL OF A GIVEN NUMBER
2. FIBONACCI OF GIVEN NUMBER
3. SUMMATION OF FIBONACCI
4. PRIMALITY
0. EXIT
ENTER YOUT CHOICE: 0
'''