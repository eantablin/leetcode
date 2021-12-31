arr = [0,3,2,1]

def validMountainArray(arr):
        N = len(arr)
        i = 0
        
        while i+1 < N and arr[i] < arr[i+1]:
            i += 1
        
        if i == 0 or i == N-1:
            return False
        
        while i+1 < N and arr[i] > arr[i+1]:
            i += 1
        
        return i == N-1

print(validMountainArray(arr))