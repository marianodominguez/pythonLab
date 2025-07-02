# url : http://www.pythonchallenge.com/pc/return/sequence.txt

#a = ['1', '11', '21', '1211', '111221']

a =['1', '11']

for i in range(2,31):
    seq = a[i-1]
    element = seq[0]
    count=0
    new = '';
      
    for c in seq:
        if element == c:
            count+=1
        else:
            new += str(count) + element	
            element = c
            count=1
      
    new += str(count) + element
    a.append(new)

print(a[0:15])
#print a[30]

print(len(a[30]))

