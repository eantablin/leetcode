# nums = [1,2,10,5,7]


# nums = [1,1]
# Leetcode says return for above should be True, when questions says "Strictly ascending"

def canBeIncreasing(nums):
        
        sortedArr = sorted(nums)
        if nums == sortedArr and min(nums) != max(nums):
            return True
        
        if min(nums) == max(nums):
            return False
        
        for i in nums:
            x = nums
            x.remove(i)
            

            if x == sorted(x) and min(x) != max(x):
                return True
        
        return False

print(canBeIncreasing(nums))