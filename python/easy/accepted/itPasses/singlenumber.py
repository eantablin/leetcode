# Runtime: 148 ms, faster than 74.24% of Python3 online submissions for Single Number.
# Memory Usage: 16.9 MB, less than 8.50% of Python3 online submissions for Single Number.

nums = [2,2,1]

def singleNumber(nums: [int]) -> int:
        pHolder = {}
        
        for i, j in enumerate(nums):
            if j not in pHolder:
                pHolder[j] = 1
            else:
                pHolder[j] += 1
        
        for i, j in pHolder.items():
            if j == 1:
                return i
            
print(singleNumber(nums))