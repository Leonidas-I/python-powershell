import random
from collections import Counter
"""
newlist = []
while len(newlist) < 52:
    a = random.randint(10, 99)
    if a not in newlist:
        newlist.append(a)

print Counter(newlist), len(newlist)
print newlist
"""    

dic_test = {
    'a':'80', 'b':'50', 'c':'98', 'd':'71', 'e':'33', 'f':'36',
    'g':'68', 'h':'17', 'i':'41', 'j':'63', 'k':'75', 'l':'53',
    'm':'90', 'n':'10', 'o':'69', 'p':'79', 'q':'48', 'r':'31',
    's':'86', 't':'20', 'u':'65', 'v':'25', 'w':'93', 'x':'94',
    'y':'96', 'z':'39',
    'A':'47', 'B':'62', 'C':'83', 'D':'35', 'E':'24', 'F':'16',
    'G':'32', 'H':'84', 'I':'12', 'J':'97', 'K':'18', 'L':'21',
    'M':'64', 'N':'26', 'O':'13', 'P':'45', 'Q':'43', 'R':'44',
    'S':'95', 'T':'67', 'U':'87', 'V':'77', 'W':'46', 'X':'42',
    'Y':'28', 'Z':'70',
    '0':'K', '1':'D', '2':'z', '3':'t', '4':'i',
    '5':'N', '6':'S', '7':'m', '8':'q', '9':'V'
    }
target = '1095505395Dz6826NN97t3316469420'
numbers = '0123456789'
temp = ''
listv1 = []

while len(target) > 0:
    if target[0] in numbers:
        temp = target[0] + target[1]
        target = target[2:len(target)]
        for i in dic_test:
            if temp == dic_test[i]:
                listv1.append(i)
        print temp
    else:
        temp = target[0]
        target = target[1:len(target)]
        for i in dic_test:
            if temp == dic_test[i]:
                listv1.append(i)
            else:
                listv1.append(temp)
        print temp
    

print ''.join(listv1)
