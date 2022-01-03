n = 3
trust = [[1,3],[2,3],[3,1]]

def findJudge(n, trust):
    # Everybody else must trust the town judge
    
    pHolder0 = []
    pHolder1 = []

    for i in trust:
        pHolder0.append(i[0])
        pHolder1.append(i[1])
    
    pHolder0 = sorted(pHolder0)
    pHolder1 = sorted(pHolder1)

    for i in pHolder1:
        if i not in pHolder0:
            return i
    
    return -1

    # seen = {}
    
    # for i in trust:
    #     peopleitTrusts = 0

    #     for j in trust:
    #         if i[1] != j[0]:
    #             peopleitTrusts = 0

    #         elif i[1] == j[0]:
    #             peopleitTrusts += 1
        
    #     if peopleitTrusts == 0:
    #         return i[1]
        
    #     seen[i[1]] = peopleitTrusts
        
    # return -1
        
print(findJudge(n, trust))