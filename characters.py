# -*- coding: iso-8859-1 -*-


def countChars(s):
    count = []
    letters = []
    for k in s:
        if k in letters:
            i = letters.index(k)
            num = count[i]
            num += 1
            count[i] = num
        else:
            letters.append(k)
            count.append(0)    
    return letters, count

def findFirstNonRepeating(s):
    index, count = countChars(s) 
    for i in range(len(index)):
        if count[i] == 0 :
            return index[i]
    return ''

def findFirstRepeating(s):
    index, count = countChars(s) 
    for i in range(len(index)):
        if count[i] > 0 :
            return index[i]
    return ''
            
s= 'test of string with repeating characters of w'
print(countChars(s))
print('first non repeating', findFirstNonRepeating(s))
print('first repeating', findFirstRepeating(s))