def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    arrLen = len(arr)
    
    for i in arr:
        if i < 0:
            negative += 1
        elif i > 0:
            positive += 1
        else:
            zero += 1
    
    positive /= arrLen
    negative /= arrLen
    zero /= arrLen
    
    print(positive)
    print(negative)
    print(zero)