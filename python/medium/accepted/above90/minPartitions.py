# Runtime: 192 ms, faster than 38.00% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
# Memory Usage: 14.9 MB, less than 33.72% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.

def minPartitions(self, n: str) -> int:
    counter = 0
    
    for i in n:
        i = int(i)
        if i > counter:
            counter = i
    
    return counter
    
# Runtime: 69 ms, faster than 66.42% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
# Memory Usage: 14.5 MB, less than 96.66% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.

def minPartitions(n):
        return max(n)