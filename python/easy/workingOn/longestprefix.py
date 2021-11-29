strs = ["flower","flow","flight"]

def longestprefix(strs):
    common = {}

    pHolder = sorted(strs)
    prefix = pHolder[0[0]] # First character in first sorted string
    
    if len(strs) == 0 or len(strs) == 1:
        return ""

    while pHolder:
        for i in pHolder:
            if
    for i in pHolder:
        if i[0] == prefix:
            continue
        else:

                    


# def longestprefix(strs:List[str]):
#     pHolder = []

#     # if no common prefix, return ""
#     if not strs:
#         return ""
    
#     for i in strs:
#         for i in range


#     for i in range(0, len(strs)):
#         if strs[i[0]] == strs[i+1[0]]:
