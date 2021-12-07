# Runtime: 129 ms, faster than 20.54% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14.7 MB, less than 23.98% of Python3 online submissions for Median of Two Sorted Arrays.

nums1 = [1,3]
nums2 = [2]

def findMedianSortedArrays(nums1, nums2):
    pHolder = nums1 + nums2
    pHolder = sorted(pHolder)

    pLen = len(pHolder)

    if pLen % 2 == 1:
        median = pLen // 2
        return pHolder[median]
    elif pLen % 2 == 0:
        firstHalf = pHolder[pLen//2-1]
        secHalf = pHolder[pLen//2]
        median = (firstHalf + secHalf) / 2
        return median

print(findMedianSortedArrays(nums1, nums2))

# No worky
# nums1 = [1,3]
# nums2 = [2]

# def findMedianSortedArrays(nums1, nums2):
        
#         pHolder = []
#         for i in nums1:
#             for j in nums2:
#                 if i > j:
#                     pHolder.append(i)
#                 elif i < j:
#                     pHolder.append(j)
#                 else:
#                     pHolder.append(i)
#                     pHolder.append(j)
            
#         pLen = len(pHolder)
        
#         if pLen % 2 == 1:
#             return pHolder[(pLen//2)-1]
#         else:
#             return pHolder[pLen//2]
            
# print(findMedianSortedArrays(nums1, nums2))