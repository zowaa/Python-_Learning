def removeList():
	l = [1, 4, 9, 10, 23]
	l[1:3] = []
	# OR
	# l.remove(4)
	# l.remove(9)
	return l

print(removeList())