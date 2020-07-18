def bubble_sort(L): #O(n**2) where n is len(L))
    swap = False
    while not swap: #O(len(L))
        print 'bubble_sort: '+ str(L)
        swap = True
        for i in range(1, len(L)): #O(len(L))
            if L[i-1] > L[i]:
                swap = False
                L[i], L[i-1] = L[i-1], L[i]

def selection_sort(L): #O(n**2)
    suffixSt = 0
    while suffixSt != len(L): #O(len(L))
        print 'selection_sort: ' + str(L)
        for i in range(suffixSt, len(L)): #O(len(L))
            if L[i] < L[suffixSt]:
                L[i], L[suffixSt] = L[suffixSt], L[i]
        suffixSt += 1

def merge(left, right):
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

def merge_sort(L): #O(nlog(n))
    print 'merge_sort: ' + str(L)
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)/2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def main():
    TestList = [1, 7, 5, 3, 2, 6, 25, 18, 13, 15, 30, 22, 28]   
    print TestList
    print 
    print bubble_sort(TestList)
    print TestList

    print '-'*50
    TestList = [1, 7, 5, 3, 2, 6, 25, 18, 13, 15, 30, 22, 28]   
    print selection_sort(TestList)
    print TestList

    print('')
    TestList = [1, 7, 5, 3, 2, 6, 25, 18, 13, 15, 30, 22, 28]   
    print merge_sort(TestList)


if __name__ == '__main__':
    main()    



               