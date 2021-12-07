# Runtime: 28 ms, faster than 88.94% of Python3 online submissions for House Robber.
# Memory Usage: 14 MB, less than 93.42% of Python3 online submissions for House Robber.

nums = [1,2,3,1]

def rob(nums):
    
    l = r = 0
    for n in nums:
        l, r = r, max(n + l, r)
    return r

print(rob(nums))

# odd = []
# oddAdded = sum(odd)
# even = []
# evenSum = sum(even)
# for i in range(len(nums)):
#     if i %
# for i in nums:
#     if