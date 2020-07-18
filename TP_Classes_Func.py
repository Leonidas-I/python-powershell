import math
from datetime import datetime

class Time(object):
    '''Tao class Time'''

def is_after(t1, t2):
    print (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

def print_time(time):
    print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)    

def time_to_int(time):
    minute = time.hour * 60 + time.minute
    second = minute * 60 + time.second
    return second

def int_to_time(seconds):    #time quy doi theo base 60, apply method for don vi quy 
    time = Time()           #doi khac nhu (weight, height, ...) theo base 10, ...
    minute, second = divmod(seconds, 60)
    hour, minute = divmod(minute, 60)
    time.hour = hour
    time.minute = minute
    time.second =second
    return time

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def increment(time, second):
    second += time_to_int(time)
    return int_to_time(second)

def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    newtime = time_to_int(t1) + time_to_int(t2)
    return int_to_time(newtime)

def mul_time(time, number):
    assert valid_time(time)
    result = time_to_int(time) * number
    return int_to_time(result) 

def exercise6():
    runtime = Time()
    runtime.hour = 8
    runtime.minute = 35
    runtime.second = 49
    distance = 25.0   #km, must be float
    Avgspeed = mul_time(runtime, 1/distance)
    print 'Average speed = ',
    print_time(Avgspeed) 

def next_birthday(birthday):
    today = datetime.today()
    next_birthday = datetime(today.year, birthday.month, birthday.day)
    return next_birthday - today

def n_times_day(birthday1, birthday2, n):
    assert birthday1 < birthday2    #1989 < 1991 but age 1989 > age 1991
    delta1 = birthday1 - birthday1  #code in command line + read document about
    delta2 = birthday2 - birthday1  #modult datetime to see why use delta1, delta2
    result = (n*delta2 - delta1)/(n-1) + birthday1    
    return result

def exercise7():
    today = datetime.today()
    print 'Today is ',
    # print today.weekday()     #return number from 0 to 6 (0 is Monday)
    print today.strftime('%A')  #read library datetime python

    birthday = datetime(1989, 10, 23)
    print 'Your next birthday countdown: ',
    print next_birthday(birthday)

    age = today.year - birthday.year
    print 'Your age in %s is: ' % today.year ,age

    birthday1 = datetime(1989, 10, 23)
    birthday2 = datetime(1991, 7, 20)
    n = 3
    print 'The day when birthday1 is n time birthday2: ',
    print n_times_day(birthday1, birthday2, n)

def main():
    t1 = Time()
    t1.hour = 1
    t1.minute = 25
    t1.second = 30
    print_time(t1)

    t2 = Time()
    t2.hour = 7
    t2.minute = 7
    t2.second = 59
    print 'Compare time: ',
    is_after(t1, t2);

    second = 200
    incretime = increment(t1, second)
    print 'Add second = ',
    print_time(incretime)

    print 'Add 2 times = ',
    print_time(add_time(t1, t2))

    exercise6()

    exercise7()


if __name__ == '__main__':
    main()    