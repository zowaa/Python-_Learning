def getSquare():
	l = [x*x for x in range(0,21,2) if x%3 != 0]
	return l

print(getSquare())