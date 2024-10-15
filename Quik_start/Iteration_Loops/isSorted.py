def isSorted(l):
	for i in range(len(l) - 1):
		if l[i] > l[i+1]:
			return False
	return True

print(isSorted([1, 2, 3, 2]))