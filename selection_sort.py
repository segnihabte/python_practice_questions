def findSmallest(arr):
    smallest = arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index, int (smallest)

def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        print(type(arr), type(smallest))
        newArr.append(arr.pop(smallest))
    return newArr
# the problem is 
# TypeError: 'tuple' object cannot be interpreted as an integer
print(findSmallest([5, 3, 6, 2, 10]))
print(selectionSort([5, 3, 6, 2, 10]))