def lonelyinteger(a):
    
    pHolder = {}
    
    for i in a: # Loop through entirety of array, using current value
        if i not in pHolder: # Add value to dictionary
            pHolder[i] = 1
        else: # Value is in dictionary, increase it's count
            pHolder[i] += 1
    
    for k, v in pHolder.items():
        if v == 1: # If this key contains the lonely value
            return k