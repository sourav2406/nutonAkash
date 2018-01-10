#programe to search element exponential
def binarySearch(arr, key, low, high):

    if low > high:
        return -1
    else:
        mid = int((low+high)/2)

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            return binarySearch(arr, key, low, mid-1)
        else:
            return binarySearch(arr, key, mid+1, high)

def exponentialSearch(arr, n, x):
    if arr[0] == x:
        return 0

    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    return binarySearch(arr, x, i/2, min(i,n))

#driver programe
arr = [1, 2, 3, 4, 5, 6, 7]
high = len(arr) - 1
res = exponentialSearch(arr, high, 7)
print(res)
