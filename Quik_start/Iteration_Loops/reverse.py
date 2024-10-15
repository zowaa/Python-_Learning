def reverse(l):
	ret = []
	for i in range(len(l)):
		ret.append(l[-(i+1)])
	return ret

print(reverse([1, 2, 3, 4, 5]))