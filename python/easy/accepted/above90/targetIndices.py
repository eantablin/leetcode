# Runtime: 40 ms, faster than 95.83% of Python3 online submissions for Find Target Indices After Sorting Array.
# Memory Usage: 14 MB, less than 99.18% of Python3 online submissions for Find Target Indices After Sorting Array.

nums = [1,2,5,2,3]
target = 2

def targetIndices(nums, target):
    
    if target not in nums:
        return []
    
    pHolder = nums[::]
    pHolder = sorted(pHolder)
    
    retHolder = []
    
    for i, j in enumerate(pHolder):
        if j == target:
            retHolder.append(i)
        
    return retHolder