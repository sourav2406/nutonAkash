#array rotation by index

def leftRotate(arr2, d, n):
    j = 0
    k = 0
    temp = []
    for i in range(n+d):
        
        if i < d:
            temp.append(arr2[i])
        else:
            if j < (n-d):
                arr2[j] = arr2[i]
            else:
                arr2[j] = temp[k]
                k += 1
            j += 1

def printArr(arr1, size):
    for i in range(size):
        print("%d"% arr1[i], end=" ")
    print("\n")

arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 3, 7)
printArr(arr, 7)
