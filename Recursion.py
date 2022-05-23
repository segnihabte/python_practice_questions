def countdown(i):
	print(i)
	countdown(i-1)


countdown(4)

def recurAddArray(arr):
	total=0
	for i in arr:
		total=total+i
	return total


