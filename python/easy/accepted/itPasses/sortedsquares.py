# Runtime: 260 ms, faster than 69.91% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 16.3 MB, less than 15.70% of Python3 online submissions for Squares of a Sorted Array.

def sortedSquares(nums: [int]) -> [int]:
    pHolder = []
    
    for i in nums:
        pHolder.append(i**2)
    
    pHolder = sorted(pHolder)
    
    return pHolder