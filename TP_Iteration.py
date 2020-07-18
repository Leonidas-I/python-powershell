import math

def eval_loop():    #eval is built-in function to evaluate a string
    while True:
        a = raw_input('Type your equation here: ')  #Ex: 1 + 2 * 5
        if a == 'done':
            break
        print eval('math.sqrt(25)'), eval('type(math.pi)'), eval(a)
    print 'Done'

# eval_loop()    


def square_rootTP(a, epsilon):  #tinh sqrt theo Think Python
    a = float(a)
    x = 1                       #random first guess = 1
    ctr = 1
    while True:  
        y = (x + a/x)/2         #y is next guess
        if abs(y -x) < epsilon:
            break
        else:
            x = y
        ctr += 1
    print 'TP method. Num Iteration', ctr, 'Estimate', y
    return y
  

def square_rootBi(x, epsilon):  #tinh sqrt theo bisection method
    assert x > 0    
    assert epsilon > 0          #assume x & epsilon must be positive number
    low = 0
    high = max(x, 1.0)          #cover instance when x < 1.0 (Ex: sqrt(1/4) < 1/2)
    guess = (low + high)/2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        ctr += 1
    assert ctr <= 100           #make sure we not into infinitive iteration
    print 'Bi method. Num Iteration', ctr, 'Estimate', guess
    return guess


def square_rootNR(x, epsilon):  #tinh sqrt theo method of Newton (NR)
    assert x > 0                #NR: guess(i+1) = guess(i) - F(guess(i))/2*guess  
    assert epsilon > 0
    x = float(x)
    guess = x/2.0
    diff = guess**2 - x
    ctr = 1
    while abs(diff) > epsilon and ctr <= 100:
        guess = guess - diff/(2.0*guess)
        diff = guess**2 - x
        ctr += 1
    assert ctr <= 100
    print 'NR method. Num Iteration', ctr, 'Estimate', guess
    return guess


def square_root(a, epsilon):    #My method modify from Think Python method
    a = float(a)
    x = 1
    ctr = 1
    y = (x + a/x)/2
    while abs(y - x) > epsilon:
        x = y
        y = (x + a/x)/2
        ctr += 1
    print 'My method. Num Iteration', ctr, 'Estimate', y
    return y


numsqrt = 625
eps = 0.00000001
square_rootTP(numsqrt, eps); print
square_rootBi(numsqrt, eps); print
square_rootNR(numsqrt, eps); print
square_root(numsqrt, eps)