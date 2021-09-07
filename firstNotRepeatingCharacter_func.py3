def firstNotRepeatingCharacter(s):
    # find first char in a string that is no where else in the string
    
    hsh = dict()
    len_s = len(s)
    min_i = len_s + 1
    min_c = ''
    #hsh[s[0]] = 1
    for i in range(len_s):
        
        if s[i] not in hsh.keys():
            hsh[s[i]] = [1, i]
            
        else:
            count = hsh[s[i]][0]
            hsh[s[i]][0] = count + 1
            hsh[s[i]].append(i)
    
    
    for x in hsh.keys():
        if hsh[x][0] == 1 and hsh[x][1] < min_i:
            min_i = hsh[x][1]
            min_c = x
    
   
    
    if min_c == '':
        return '_'
    else:
        return min_c
            
