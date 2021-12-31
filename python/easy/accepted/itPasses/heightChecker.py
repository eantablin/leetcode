# Your runtime beats 14.27 % of python3 submissions.
# Your memory usage beats 45.77 % of python3 submissions.

def heightChecker(self, heights: List[int]) -> int:
    expected = sorted(heights)
    heightLen = len(heights)
    counter = 0
    i = 0
    
    while i < heightLen:
        if heights[i] != expected[i]:
            counter += 1
        i += 1
    
    return counter