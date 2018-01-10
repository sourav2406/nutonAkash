#Binary search on sorted array
class BinarySearch:
    
    #constructer of class
    def __init__(self,arr):
        self.arrayGiven = arr
        #self.size = len(arr)

    #search function
    def search(self,key,start,end):

        if end >= start:
            mid = int((start + end) / 2)
            
            if self.arrayGiven[mid] == key:
                return mid
            elif self.arrayGiven[mid] > key:
                return self.search(key, start, mid-1)
            else:
                return self.search(key, mid+1, end)
        else:
            return -1

#driver programe
arr1 = [1, 2, 3, 4, 5, 6, 7]
key = 2

result = BinarySearch(arr1)
output = result.search(key, 0, len(arr1)-1)

print(output)