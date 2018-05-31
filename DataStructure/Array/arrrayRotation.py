def rotate(arr, d, n):
    for i in range(d):
        rotateByOne(arr, n)

def rotateByOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1] = temp    

def printArray(arr, n):
    for i in range(n):
        print("%d"% arr[i],end=" ")

arr = [1,2,3,4,5,6,7]
rotate(arr, 2, 7)
printArray(arr, 7)
