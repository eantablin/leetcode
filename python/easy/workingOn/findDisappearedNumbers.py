# nums = [4,3,2,7,8,2,3,1]
nums = [1,1]

def findDisappearedNumbers(nums: [int]) -> [int]:
    pHolder = []
    numlen = len(nums)
    nums = sorted(nums)
    holdDict = {}
    
    for i in range(1, numlen+1):
        if i not in nums:
            pHolder.append(i)
    
    return pHolder


print(findDisappearedNumbers(nums))