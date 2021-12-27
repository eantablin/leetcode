a = [1, 2, 3]
b = [3, 2, 1]

def compareTriplets(a, b):
    pHolderArr = []
    aPoints, bPoints = 0,0
    arrLen = len(a)

    for i in range(arrLen):
        if a[i] > b[i]:
            aPoints += 1
        elif a[i] < b[i]:
            bPoints += 1
    
    pHolderArr.append(aPoints)
    pHolderArr.append(bPoints)
    
    return pHolderArr

print(compareTriplets(a, b))