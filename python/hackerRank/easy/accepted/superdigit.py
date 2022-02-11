n = "1241"


def superDigit(n):
    sum = 0
    
    while len(n) != 1:
        
        for i in n:
            sum += int(i)
            
        n = str(sum)
    
    return sum
    # Write your code here


print(superDigit(n))















# n = 9875

# def superDigit(n):
    
#     n = str(n)

    
#     while(len(n) != 1):
#         counter = 0
#         for i in n:
#             counter += int(i)
        
#         n = str(counter)
    
#     return counter
    
# print(superDigit(n))