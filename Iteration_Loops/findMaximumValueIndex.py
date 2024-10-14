def findMaximumValueIndex(l):
	maxx = 0
	index = 0
	for i in range(len(l)):
		if l[i] > maxx:
			maxx = l[i]
			index = i
	return [index, maxx]

[index, maxx] = findMaximumValueIndex([1, 4, 23, 10, 9])
print(f'index = {index}, max = {maxx}')