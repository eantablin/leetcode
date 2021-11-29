A = [-4, 3, 6, 4, 1, 2,54,24,59]

def solution(A):
    pHolder = 1

    A = sorted(A)

    while pHolder in A:
        pHolder += 1
    
    return pHolder

print(solution(A))