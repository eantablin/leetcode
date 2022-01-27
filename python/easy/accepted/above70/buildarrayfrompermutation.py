# Runtime: 236 ms, faster than 6.32% of Python3 online submissions for Build Array from Permutation.
# Memory Usage: 14.2 MB, less than 99.70% of Python3 online submissions for Build Array from Permutation.

nums = [0,2,1,5,3,4]

def buildArray(nums):
    pHolder = []
    
    for i in nums:
        pHolder.append(nums[i])
        
    return pHolder

# Runtime: 120 ms, faster than 76.19% of Python3 online submissions for Build Array from Permutation.
# Memory Usage: 14.5 MB, less than 40.29% of Python3 online submissions for Build Array from Permutation.

# nums = [0,2,1,5,3,4]

# def buildArray(nums):
#     pHolder = []
    
#     for i in range(len(nums)):
#         pHolder.append(nums[nums[i]])
    
#     return pHolder

print(buildArray(nums))