# Runtime: 44 ms, faster than 79.37% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15.1 MB, less than 9.58% of Python3 online submissions for Valid Anagram.

s = "anagram"
t = "nagaram"

def isAnagram(s, t):
        
        sortedS = sorted(s)
        sortedT = sorted(t)
        
        if sortedS == sortedT:
            return True
        else:
            return False

print(isAnagram(s, t))


# Runtime: 48 ms, faster than 70.38% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.9 MB, less than 17.98% of Python3 online submissions for Valid Anagram.

def isAnagram(s, t):
        
        sortedS = sorted(s)
        sortedT = sorted(t)

        return True if sortedS == sortedT else False