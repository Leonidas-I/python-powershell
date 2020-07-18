# Think Python - Excercise - Function

def right_justify(s):
    leading_space = 70 - len(s)
    return ' ' * leading_space + s
# t = 'Lilly Allen'
# print right_justify(t)

def do_twice(f, x):
    f(x)
    f(x)
def print_spam(x):
    print x
def do_four(f, x):
    do_twice(f, x)
    do_twice(f, x)    

# s = 'sphere of influence'
# do_four(print_spam, s)


x = '+ ' + '- ' * 5
y = ' ' * 11
z = '| ' + '  ' * 5
def draw_row(a, b, c):    
    print a; print b; print c; print b; print c
    print b; print c; print b; print c; print b
def draw_row_end(a):
    print a 
def draw_col_end():
    print '+'; print ''; print '|'; print ''; print '|'
    print ''; print '|'; print ''; print '|'; print ''; print '+'
def draw_cell(a, b, c):
    draw_row(a, b, c)
    draw_row_end()
    draw_col_end()

draw_cell(x, y, z)
