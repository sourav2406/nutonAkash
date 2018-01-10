
def rotateArr(arr, size):
    temp = arr[0]
    for i in range(1, size):
        arr[i-1] = arr[i]
    arr.pop()
    arr.append(temp)

def printArr(arr, size):
    for i in range(size):
        print("%d"% arr[i], end=' ')

arr = [1, 2, 3, 4, 5, 6, 7]
print(arr)
rotateArr(arr, len(arr))
printArr(arr, len(arr))
