# Runtime: 52 ms, faster than 73.86% of Python3 online submissions for Final Value of Variable After Performing Operations.
# Memory Usage: 14.4 MB, less than 16.41% of Python3 online submissions for Final Value of Variable After Performing Operations.

operations = ["--X","X++","X++"]

def finalValueAfterOperations(operations):
        pHolder = 0
        
        for i in operations:
            if i.__contains__("+"):
                pHolder += 1
            else:
                pHolder -= 1
        
        return pHolder

print(finalValueAfterOperations(operations))

# Runtime: 92 ms, faster than 14.58% of Python3 online submissions for Final Value of Variable After Performing Operations.
# Memory Usage: 13.8 MB, less than 99.91% of Python3 online submissions for Final Value of Variable After Performing Operations.

# operations = ["--X","X++","X++"]

# def finalValueAfterOperations(operations):
#         pHolder = 0
        
#         for i in operations:
#             if "+" in i:
#                 pHolder += 1
#             else:
#                 pHolder -= 1
        
#         return pHolder

# print(finalValueAfterOperations(operations))

