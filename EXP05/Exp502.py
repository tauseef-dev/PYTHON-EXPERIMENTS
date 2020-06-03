'''
EXPERIMENT No. : 5  PROGRAM : 02
Name : TAUSEEF MUSHTAQUE ALI SHAIKH
Roll No : 18CO63    Batch : B-3
Aim : Program to perform lambda with filter, map and reduce functions.
'''

from functools import reduce

def main():
    while True:
        print('\t\t\tMENU')
        print(
            '1. LAMBDA WITH FILTER.\n2. LAMDA WITH MAP.\n3. LAMBDA WITH REDUCE.\n0. EXIT.')
        ch = int(input('ENTER YOUR CHOICE: '))
        if ch == 0:
            break
        elif ch == 1:
            li = list()
            n = int(input('HOW MANY ELEMENT YOU WANT IN A LIST?: '))
            for i in range(n):
                li.append(int(input('ENTER ELEMENT: ')))
            oddli = list(filter(lambda x: (x % 2 != 0), li))
            print('LIST OF ODD ELEMENTS: ', oddli)
        elif ch == 2:
            li = list()
            n = int(input('HOW MANY ELEMENT YOU WANT IN A LIST?: '))
            for i in range(n):
                li.append(int(input('ENTER ELEMENT: ')))
            sqrli = list(map(lambda x: x**2, li))
            print('LIST OF SQUARED ELEMENTS: ', sqrli)
        elif ch == 3:
            li = list()
            n = int(input('HOW MANY ELEMENT YOU WANT IN A LIST?: '))
            for i in range(n):
                li.append(int(input('ENTER ELEMENT: ')))
            varmax = reduce(lambda x,y:x if x > y else y, li)
            print('MAXIMUM ELEMENT IN THE LIST IS: ', varmax)
        else:
            print('PLEASE ENTER A VALID CHOICE')


if __name__ == '__main__':
    main()


'''
OUTPUT:

                        MENU
1. LAMBDA WITH FILTER.
2. LAMDA WITH MAP.
3. LAMBDA WITH REDUCE.
0. EXIT.
ENTER YOUR CHOICE: 1
HOW MANY ELEMENT YOU WANT IN A LIST?: 3
ENTER ELEMENT: 4
ENTER ELEMENT: 6
ENTER ELEMENT: 5
LIST OF ODD ELEMENTS:  [5]
                        MENU
1. LAMBDA WITH FILTER.
2. LAMDA WITH MAP.
3. LAMBDA WITH REDUCE.
0. EXIT.
ENTER YOUR CHOICE: 2
HOW MANY ELEMENT YOU WANT IN A LIST?: 3
ENTER ELEMENT: 7
ENTER ELEMENT: 8
ENTER ELEMENT: 9
LIST OF SQUARED ELEMENTS:  [49, 64, 81]
                        MENU
1. LAMBDA WITH FILTER.
2. LAMDA WITH MAP.
3. LAMBDA WITH REDUCE.
0. EXIT.
ENTER YOUR CHOICE: 3
HOW MANY ELEMENT YOU WANT IN A LIST?: 3
ENTER ELEMENT: 7
ENTER ELEMENT: 5
ENTER ELEMENT: 1
MAXIMUM ELEMENT IN THE LIST IS:  7
                        MENU
1. LAMBDA WITH FILTER.
2. LAMDA WITH MAP.
3. LAMBDA WITH REDUCE.
0. EXIT.
ENTER YOUR CHOICE: 0
'''