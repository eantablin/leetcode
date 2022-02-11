arr = [1,1,4,1,1]

def balancedSums(arr):
    pHolder = []
    arrlen = len(arr)
    
    for i in range(arrlen):
        if i == arrlen-1:
            return "NO"
        elif sum(pHolder) == sum(arr[i+1::]):
            return "YES"
        pHolder.append(arr[i])
            
print(balancedSums(arr))