def miniMaxSum(arr):
    arr = sorted(arr)

    minarr = arr[:4:]
    maxarr = arr[1::]

    print(f"{sum(minarr)} {sum(maxarr)}")
