arr = [1,2,3,4,5]

def miniMaxSum(arr):
    # Write your code here
    arr = sorted(arr)
    retVal = ""

    pHolder0 = arr[::] # holds max
    pHolder1 = arr[::] # holds min

    arrLen = len(arr)
    
    pHolder0.pop(arrLen-1)
    pHolder1.pop(0)
    
    maxNum = sum(pHolder0)
    minNum = sum(pHolder1)
    
    retVal += str(maxNum) + " " + str(minNum)
    
    return retVal

print(miniMaxSum(arr))