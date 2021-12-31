nums = [0,3,7,2,5,8,4,6,0,1]

def longestConsecutive(nums):
    nums = sorted(nums)
    pHolder = []
    counter = 0
    
    for i in nums:
        if not pHolder:
            pHolder.append(i)
        
        if (pHolder[0] + 1) == i:
            pHolder.pop(0)
            pHolder.append(i)
            counter += 1
    
    return counter

print(longestConsecutive(nums))