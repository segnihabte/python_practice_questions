import random
import numpy as np

arr_list= np.array([])
n=int(input())
for i in range(n):
    list_item = random.randint(0,n)
    arr_list = np.append(arr_list,list_item)
print(arr_list)
print(arr_list.size)
for i in range(n):
    if arr_list[i+1]==arr_list[i]:
        new_arr = np.array()
        new_arr=np.append(new_arr, arr_list[i+1])
# hello this is a comment
print("hello brothers")

        



