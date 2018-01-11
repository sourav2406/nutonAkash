def waveform(arr,n):
    arr.sort()

    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr1)
waveform(arr1, len(arr1))
print(arr1)
