def evenSquare():
	l = [x*x for x in range(0,21) if (x%2 == 0)]
	return sum(l)

print(evenSquare())