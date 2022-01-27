arr = [10,20,20,10,10,30,50,10,20]
# arr = [1,1,3,1,2,1,3,3,3,3]

def sockMerchant(ar):
    # Write your code here
    dict = {}
    counter = 0

    for i, j in enumerate(ar):
        if j in dict:
            dict[j] += 1
        else:
            dict[j] = 1

    for i in dict.values():
        while i - 2 >= 0:
            counter += 1
            i -= 2
    
    return counter

print(sockMerchant(arr))