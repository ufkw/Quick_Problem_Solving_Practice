
def firstDuplicate(a):
# Find the first duplicate (the second number has the minimum index) in an array  
    size = len(a)
    
    min = size + 1
    hsh = dict()
    
    for i in range(size):
        
        if ((a[i] in hsh.keys()) and (i < min)):
            min = i
        
        hsh[(a[i])] = i
        
        
    if min == size + 1:
        return -1
    else:
        return a[min]
