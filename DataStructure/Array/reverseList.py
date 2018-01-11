'''reverse a list using recursive'''
def reverseList(A, start, end):
    if start < end:
        A[start], A[end] = A[end], A[start]
        reverseList(A, start+1, end-1)

#driver programe
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr)
reverseList(arr, 0, len(arr)-1)
print(arr)
