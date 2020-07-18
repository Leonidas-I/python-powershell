dicrypted = {
    'a':'80', 'b':'50', 'c':'98', 'd':'71', 'e':'33', 'f':'36',
    'g':'68', 'h':'17', 'i':'41', 'j':'63', 'k':'75', 'l':'53',
    'm':'90', 'n':'10', 'o':'69', 'p':'79', 'q':'48', 'r':'31',
    's':'86', 't':'20', 'u':'65', 'v':'25', 'w':'93', 'x':'94',
    'y':'96', 'z':'39',
    'A':'47', 'B':'62', 'C':'83', 'D':'35', 'E':'24', 'F':'16',
    'G':'32', 'H':'84', 'I':'12', 'J':'97', 'K':'18', 'L':'21',
    'M':'64', 'N':'26', 'O':'13', 'P':'23', 'Q':'43', 'R':'44',
    'S':'95', 'T':'67', 'U':'87', 'V':'77', 'W':'46', 'X':'42',
    'Y':'28', 'Z':'70',
    '0':'K', '1':'D', '2':'z', '3':'t', '4':'i',
    '5':'N', '6':'S', '7':'m', '8':'q', '9':'V'
    }


def Encode(x):
    encrypted = []
    for i in x:
        if i in dicrypted:
            encrypted.append(dicrypted[i])
        else:
            encrypted.append(i)
    result = ''.join(encrypted)
    return (result , len(result), len(x))

def Decode(x):
    temp = ''
    decrypted = []
    while len(x) > 0:
        if x[0].isdigit():  #check value x tai index 0 co phai la number ko
            temp = x[0] + x[1]
            x = x[2:len(x)]
            for i in dicrypted:
                if temp == dicrypted[i]:
                    decrypted.append(i)
        elif x[0].isalpha():    #check value x tai index 0 co phai la string ko
            temp = x[0]
            x = x[1:len(x)]
            for i in dicrypted:
                if temp == dicrypted[i]:
                    decrypted.append(i)
        else:
            temp = x[0]
            x = x[1:len(x)]
            decrypted.append(temp)
    result = ''.join(decrypted)
    return result
   
#main    
option = raw_input('Do you want to encode or decode?: ')
lastpass = raw_input('Give it to me: ')
if option == 'encode':
    print Encode(lastpass)
elif option == 'decode':
    print Decode(lastpass)   
