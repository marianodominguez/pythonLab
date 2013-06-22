forbidden=[[0,1,1,1] , [1,0,1,1], [9,9,5,8]]

def moveDigit(initial, final, i):
    if (final[i] - initial[i]) % 10 < 5:
        initial[i] = (initial[i] + 1) %10
    else:
        initial[i] = (initial[i] - 1) %10

def moveDisks(initial, final):
    current = initial
    movements = []
    index = 0
    
    while(current != final):
        print current;
        previous = current[:]
        if(current[index] != final[index]):
            moveDigit(current, final, index)
        else:
            index = (index +1) %4
        # reached a forbidden combination
        if current in forbidden:
            current = previous
            if index < 3: 
                index = index +1
            else:
                index=0
    print current;
        
moveDisks([1,5,1,7],[9,9,5,9])    