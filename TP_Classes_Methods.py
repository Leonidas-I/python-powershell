import math

class Time(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def is_valid(self):
        if self. hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True

    def time_to_int(self):
        minutes = self.hour*60 + self.minute
        seconds = minutes*60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def add_time(self, other):
        assert self.is_valid() and other.is_valid()
        ans = self.time_to_int() + other.time_to_int()
        return int_to_time(ans)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

def int_to_time(seconds):
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    ans = Time(hour, minute, second)
    return ans

def main():
    d1 = Time(23, 10, 40)
    print d1
    
    d2 = 5
    print d2

    print d1 + d2
    print d2 + d1

    d3 = Time(20, 7, 39)
    d4 = Time(3, 46, 21)
    print sum([d1, d3, d4])


if __name__ == '__main__':
    main()