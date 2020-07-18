import random, time

def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)/2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)


def bisect_search2(L,e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)/2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, L[0], L[len(L) -1])


def normal_search(L, e):
    if e in L: return True
    return False


def compare_search(L, e):
    t0 = time.clock()
    a = bisect_search1(L, e)
    t1 = time.clock() - t0
    b = bisect_search2(L, e)
    t2 = time.clock() - t1
    c = normal_search(L,e)
    t3 = time.clock() - t2
    print 'Binary Search v1: ', a, 'Executed Time: ', t1*1000 , 'ms'
    print 'Binary Search v2: ', b, 'Executed Time: ', t2*1000 , 'ms'
    print 'Normal Search   : ', c, 'Executed Time: ', t3*1000 , 'ms'


Inputlist = [i for i in range(10000)]
target = 9872
compare_search(Inputlist, target)