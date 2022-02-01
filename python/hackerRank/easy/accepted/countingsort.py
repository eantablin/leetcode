def countingSort(arr):
    pHolder = [0]*100 # Initialize arr len 100 initialized to 0
    
    for i in arr: # Each slot in parameter array
        pHolder[i] += 1 # # Increment that position in our array
        
    return pHolder