n = 9875

def superDigit(n):
    
    n = str(n)

    
    while(len(n) != 1):
        counter = 0
        for i in n:
            counter += int(i)
        
        n = str(counter)
    
    return counter
    
print(superDigit(n))