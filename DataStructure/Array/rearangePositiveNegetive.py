#Rearanging positive and negative numbers in alternative order

def printArr(arr,n):
    for i in range(n):
        print(arr[i], end=' ')
    print('\n')

def rearange(arr, n):
    i = -1
    for j in range(n):
        if arr[j] < 0 :
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    pos, neg = i+1, 0

    while pos < n and neg < pos and arr[neg] < 0:
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg += 2

#driver programe

arr = [1, -2, 3, -4, -5, 6, 7]
printArr(arr, len(arr))
rearange(arr, len(arr))
printArr(arr, len(arr))
