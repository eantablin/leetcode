# Runtime: 176 ms, faster than 78.58% of Python3 online submissions for Majority Element.
# Memory Usage: 15.5 MB, less than 80.56% of Python3 online submissions for Majority Element.

def majorityElement(nums: [int]) -> int:
    
    pHolder = {}
    numlen = len(nums)
    
    for i in nums:
        if i not in pHolder:
            pHolder[i] = 1
        else:
            pHolder[i] += 1
    
    counter = {}
    
    for i, j in pHolder.items():
        if j > numlen/2:
            return i

