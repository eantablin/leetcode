nums = [3,1,2,4]

# runtime beats 63.09 % of python3 submissions
# memory usage beats 57.10 % of python3 submissions

def sortArrayByParity(nums):
    evenHolder = []
    oddHolder = []
    
    for i in nums:
        if i % 2 == 0:
            evenHolder.append(i)
        else:
            oddHolder.append(i)
    
    nums = evenHolder + oddHolder
    
    return nums