# Runtime: 69 ms, faster than 20.31% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Running Sum of 1d Array.

nums = [1, 2, 3, 4]

def runningSum():
    counter = 0
    numslen = len(nums)
    
    for i in range(numslen):
        counter += nums[i]
        nums[i] = counter
    
    return nums

print(runningSum())

# Runtime: 36 ms, faster than 84.76% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.5 MB, less than 43.91% of Python3 online submissions for Running Sum of 1d Array.

# nums = [1, 2, 3, 4]

# def runningSum():
#     runNum = 0

#     for i, j in enumerate(nums):
#         runNum += j
#         nums[i] = runNum
    
#     return nums

# runningSum()

