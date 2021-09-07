import numpy as np

def rotateImage(a):
# rotate array with O(1) additional memory  
    arr = np.array(a)
    arr = np.rot90(arr,k = 3)
    
    return arr
