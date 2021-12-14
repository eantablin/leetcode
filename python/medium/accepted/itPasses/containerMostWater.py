# Runtime: 956 ms, faster than 15.67% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.8 MB, less than 5.40% of Python3 online submissions for Container With Most Water.

height = [1,8,6,2,5,4,8,3,7]

def maxArea(height):
    size = len(height)
    left, right = 0, size-1
    
    max_width = size-1
    
    area = 0
    
    for width in range(max_width, 0, -1):
        if height[left] < height[right]:
            area = max(area, width*height[left])
            left += 1
        else:
            area = max(area, width*height[right])
            right -= 1
    
    return area

print(maxArea(height))