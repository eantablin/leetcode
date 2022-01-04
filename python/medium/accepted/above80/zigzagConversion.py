# Runtime: 69 ms, faster than 40.45% of Python3 online submissions for Zigzag Conversion.
# Memory Usage: 14.2 MB, less than 87.57% of Python3 online submissions for Zigzag Conversion.

# Translated solution

# Optimize me!

s = "PAYPALISHIRING"
numRows = 3

def convert(s, numRows):
    
    if numRows == 1:
        return s
    
    rows = [""] * numRows # Initialize strings and length of array
    curRow = 0 # Keep track of index to fill
    goingDown = False
    
    for c in s: # Each slot in string
        rows[curRow] += c # Append character to string present in slot of array
        
        if (curRow == 0 or curRow == numRows - 1): # If we're at either end of array, invert
            goingDown = not goingDown

        curRow += 1 if goingDown else -1 # Increase or decrease to next slot
        
    pHolder = ""
    
    for i in rows:
        pHolder += i
    
    return pHolder

print(convert(s, numRows))