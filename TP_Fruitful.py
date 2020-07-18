def is_palindrome(x):
    if not isinstance(x, str):
        return 'x must be string'
    else:
        if len(x) <= 1:
            return True
        else:
            if x[0] == x[-1]:
                x = x[1:-1]
                return is_palindrome(x)
            else:
                return False

# var = raw_input('Type your word here: ')
# print is_palindrome(var)            

def is_power(a, b):
    if a == b**2:
        return True
    else:
        if a % b == 0:
            return is_power(a/b, b)

# print is_power(256, 4)

def gcd(a, b):
    r = b % a
    if r == 0:
        return a
    else:
        return gcd(b, r)

# print gcd(18, 72)            

def fibonacci(x):
    if x <= 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

print fibonacci(8)