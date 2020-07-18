#Think Python - Exercise - Condition and Recursion

def countdown(x): 
    if x <= 0:
        print 'Go off! = Blast off!'
    else:
        print x
        countdown(x-1)

# n = 5
# countdown(n)

def factorial1(x): #O(n)
    if not isinstance(x, int): #built-in function to check whether x is int 
        return 'Wrong Input'
    else:
        prod = 1
        for i in range(1, (x+1)):
            prod *= i
        return prod

def factorial2(x): #O(n)
    if not isinstance(x, int): #similar to isinstance(x, float/str) 
        return 'x must be int'
    else:    
        if x == 0 or x == 1:
            return 1
        else:
            return x * factorial2(x-1)

a = 5
print factorial1(a)
print factorial2(a)

def check_fermat(a, b, c, n):
    if n > 2:
        if a**n + b**n != c**n:
            print 'No, that doesn\'t work'
        else:
            print 'Holyshit, Fermat was wrong'
    else:
        print 'n must greater than 2'

# x = int(raw_input('Nhap gia tri x: '))
# y = int(raw_input('Nhap gia tri y: '))
# z = int(raw_input('Nhap gia tri z: '))
# n = int(raw_input('Nhap gia tri n: '))
# check_fermat(x, y, z, n)
