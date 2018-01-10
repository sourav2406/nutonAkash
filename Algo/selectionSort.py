#Selection sort programe
def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        min_id = i
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                min_id = j
        
        arr[i], arr[min_id] = arr[min_id], arr[i]
        

#driver Programe
arr = [7, 6, 5, 4, 3, 2, 1]

print(arr)
selectionSort(arr)
print(arr)