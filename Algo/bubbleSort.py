#Bubble Sort Algo
def bubbelSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if swapped == False:
            break

#driver Program
arr = [7, 6, 5, 4, 3, 2, 1]
print(arr)
bubbelSort(arr)
print(arr)