s = [2,2,1,3,2]
d = 4
m = 2

def birthday(s, d, m):
    sLen = len(s)
    pHolder = 0
    
    for i in range(sLen - (m-1)):
        if sum(s[i:i+m]) == d:
            pHolder += 1
    return pHolder

print(birthday(s, d, m))