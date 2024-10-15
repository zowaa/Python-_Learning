def findMaximum(l):
	maxx = 0
	for n in l:
		if n > maxx:
			maxx = n
	return maxx

print(findMaximum([1, 4, 9, 10, -23]))