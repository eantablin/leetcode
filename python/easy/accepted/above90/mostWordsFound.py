# Runtime: 36 ms, faster than 93.98% of Python3 online submissions for Maximum Number of Words Found in Sentences.
# Memory Usage: 14.3 MB, less than 41.67% of Python3 online submissions for Maximum Number of Words Found in Sentences.

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

def mostWordsFound(sentences):
    
    pHolder = []
    
    for i in sentences:
    
        counter = i.count(" ")
        
        pHolder.append(counter)
    
    return max(pHolder) + 1

print(mostWordsFound(sentences))