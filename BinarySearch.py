# after thousands of trials my first BinarySearch
num_list = [1,2,3,4,5,6,7,8,9,]
def BinarySearch(list, k):
    low = 0
    high = len(list)
    while low != high:
        mid = round((low+high))/2
        mid = int(mid)
        if k==list[mid]:
            return mid
        elif k>list[mid]:
            low = mid +1
        elif k<list[mid]: 
            high=mid-1
        else:
            return None
print(BinarySearch(num_list, 8))
print("hello")













