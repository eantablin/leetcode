s = "babad"

def longestPalindrome(s):
    strLen = len(s)

    if not s:
        return False
    
    if s == s[::-1]:
        return s
    
    for i in range(strLen, 0, -1):
        
        jRange = strLen-i+1

        for j in range(0, jRange):
            pHolder = s[j:j+i]

            if pHolder == pHolder[::-1]:
                return pHolder

print(longestPalindrome(s))

# # Sample code
# def longestPalindrome(s):
#     res = ""
#     for i in range(len(s)):
#         # odd case, like "aba"
#         tmp = helper(s, i, i)
#         if len(tmp) > len(res):
#             res = tmp
#         # even case, like "abba"
#         tmp = helper(s, i, i+1)
#         if len(tmp) > len(res):
#             res = tmp
#     return res
 
# # get the longest palindrome, l, r are the middle indexes   
# # from inner to outer
# def helper(s, l, r):
#     while l >= 0 and r < len(s) and s[l] == s[r]:
#         l -= 1; r += 1
#     return s[l+1:r]

# s = "babad"

# print(longestPalindrome(s))

# s = "babad"
# s = "cbbd"
# s = "ac"

# def longestPalindrome(s):
#     if len(s) < 2:
#         return s
    
#     pHolder = ""

#     for i in s:
        