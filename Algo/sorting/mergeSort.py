#Merge Sort algo
def merge(arr, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(0,n1):
        L[i] = arr[start + i]

    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    i, j = 0, 0
    k = start

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr,start,end):
    if start < end:
        mid = int((start+end)/2)

        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        merge(arr, start, mid, end)

#Driver programe
arr = [7, 6, 5, 4, 3, 2, 1]
print(arr)
mergeSort(arr, 0, len(arr)-1)
print(arr)
