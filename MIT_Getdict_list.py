def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram_get(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

h = histogram_get('brontosaurus')
print h

def genSubsets(L):
    #res = []
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small+extra)
    return (smaller, new, small, extra)

Li = [1, 2, 3]
print genSubsets(Li)