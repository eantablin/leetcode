arr = [1,1,3,2,1]

def countingSort(arr):
    count = [0] * 100 # Create the empty array with a fixed size of 100 (They specified)
    for n in arr: # Loop through parameter array
        count[n] += 1 # Whichever position it's in our holder array, increase the count by 1
    return count # return the counts

print(countingSort(arr))