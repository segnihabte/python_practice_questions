import random
# num= "{:.6f}".format(num)
def findTheMedian():
	print("fuck the median")
print("value must be an odd number")
n = int(input())
while (n % 2) == 0:
	print("please re enter value as an odd number")
	n=int(input())
	continue
num_list = []
for i in range(n):
	list_rand = random.randint(0, n)
	num_list.append(list_rand)
num_list.sort()
print(num_list)
for i in (num_list):
	num_list[i]=num_list[i]+1
# hello



































































