strings = ['ab','ab','abc']
queries = ['ab','abc','bc']

def matchingStrings(strings, queries):
    pHolder = []
    
    for i in queries:
        counter = 0
        
        for j in strings:
            if i == j:
                counter += 1
            
        pHolder.append(counter)
        
    return pHolder

print(matchingStrings(strings, queries))