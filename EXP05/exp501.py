'''
EXPERIMENT No. : 5  PROGRAM : 01
Name : TAUSEEF MUSHTAQUE ALI SHAIKH
Roll No : 18CO63    Batch : B-3
Aim : Program to perform file operatiobn in Python.
'''

def readf():
    '''
    A METHOD TO READ A FILE.
    '''
    try:
        f = open(input('ENTER FILE NAME: '))
        s = f.readlines()
        for l in s:
            print(l,end = '')
    except:
        print('THE FILE NAME: DOES NOT EXIST, ENTER A VALID FILE NAME!')
        f = open(input('ENTER FILE NAME: '))
        s = f.readlines()
        for l in s:
            print(l,end = '')
    f.close()

def writef():
    '''
    A METHOD TO CREATE OR REPLACE (WRITE) A FILE.
    '''
    f = open(input('ENTER FILE NAME: '), 'w+')
    while True:
        data = input('ENTER DATA: ')
        f.write(data + '\n')
        ch = input('WANT TO ENTER MORE DATA (Y/N): ')
        if (ch == 'y' or ch == 'Y'):
            continue
        else: 
            break
    f.close

def appendf():
    '''
    A METHOD TO APPEND INFROMATION INTO AN EXISTING FILE.
    '''
    f = open(input('ENTER FILE NAME: '), 'a')
    while True:
        data = input('ENTER DATA: ')
        f.write(data + '\n')
        ch = input('WANT TO ENTER MORE DATA (Y/N): ')
        if (ch == 'y' or ch == 'Y'):
            continue
        else: 
            break
    f.close

def main():
    '''
    A MAIN METHOD WHCH WILL BE EXECUTED ONLY WHEN THE FILE IS EXECUTED BY ITSELF AND NOT IMPORTED.
    '''
    while True:
        print('\t\t\tMENU')
        print('\n 1. DISPLAY CONTAINS OF FILE\n 2. WRITE A FILE\n 3. APPPEND FILE\n 0. QUIT')
        ch = int(input('ENTER YOUR CHOICE: '))
        if ch == 0:
            break
        elif ch == 1:
            readf()
        elif ch == 2:
            writef()
        elif ch == 3:
            appendf()
        else:
            print('PLEASE ENTER A VALID CHOICE!')

if __name__ == '__main__':
    main()

'''
OUTPUT:

                        MENU

 1. DISPLAY CONTAINS OF FILE
 2. WRITE A FILE
 3. APPPEND FILE
 0. QUIT
ENTER YOUR CHOICE: 2
ENTER FILE NAME: exp501sam.txt
ENTER DATA: TAUSEEF MUSHTAQUE ALI SHAIKH
WANT TO ENTER MORE DATA (Y/N): Y
ENTER DATA: SE [CO]
WANT TO ENTER MORE DATA (Y/N): n
                        MENU

 1. DISPLAY CONTAINS OF FILE
 2. WRITE A FILE
 3. APPPEND FILE
 0. QUIT
ENTER YOUR CHOICE: 3
ENTER FILE NAME: exp501sam.txt
ENTER DATA: 18CO63
WANT TO ENTER MORE DATA (Y/N): N
                        MENU

 1. DISPLAY CONTAINS OF FILE
 2. WRITE A FILE
 3. APPPEND FILE
 0. QUIT
ENTER YOUR CHOICE: 1
ENTER FILE NAME: exp501sam.txt
TAUSEEF MUSHTAQUE ALI SHAIKH
SE [CO]
18CO63
                        MENU

 1. DISPLAY CONTAINS OF FILE
 2. WRITE A FILE
 3. APPPEND FILE
 0. QUIT
ENTER YOUR CHOICE: 0
'''