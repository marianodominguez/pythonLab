from random import randint
from functools import reduce

def oddsMaxSum(a):
    #a = [randint(0,10) for x in range(size)]
    size = 20
    a = list(range(size))
    odds = [a[x] for x in range(1,len(a),2) ]
    oddsums = reduce(lambda x,y: x+y, odds )
    evens = [a[x] for x in range(0, len(a),2) ]
    evensums = reduce(lambda x,y: x+y, evens )
    print(a)
    print("odd index", odds)
    print(oddsums)
    print("even index", evens)
    print(evensums)
    return max(oddsums, evensums)

def secondLargest(a = []):
    if not a: return 0;
    if len(a) == 1: return a[0]
    largest = a[0]
    secondLargest = a[0]
    for item in a:
        if item > largest:
            secondLargest = largest
            largest = item
        if item > secondLargest and item < largest:
            secondLargest = item
    return secondLargest
        
print(oddsMaxSum([10,12,6,7,8,9,11]));
print(oddsMaxSum([10,12]));
print(oddsMaxSum([1,2,3,4,5,6,7,8,9,0]));

print(secondLargest([10,12,6,7,8,9,11]));
print(secondLargest([10,12]));
print(secondLargest([1,2,3,4,5,6,7,8,9,0]));

