def diagonalDifference(arr):
    
    left = right = 0
    
    for i in range(n): # in range of number of rows and columns
        left += arr[i][i]
        right += arr[i][n-1-i] # [row] follow same as left [column] begins at end, inverts from left
        
    return abs(left-right) # Want to return the difference