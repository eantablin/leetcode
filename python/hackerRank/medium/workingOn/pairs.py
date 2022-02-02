# Passes 9/18

k = 1
arr = [1,2,3,4]

def pairs(k, arr):
    
    pHolder = []
    
    for i in arr:
        for j in arr:
            sortedvals = sorted([i, j])
            if ((i - j == k) or (j - i == k)) and sortedvals not in pHolder:
                pHolder.append(sortedvals)
                
    return len(pHolder)

print(pairs(k, arr))