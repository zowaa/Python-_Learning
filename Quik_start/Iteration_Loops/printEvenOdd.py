def printEvenOdd(n):
	while n > 0:
		if n % 2 == 0:
			print(f'Even number: {n}')
		else:
			print(f'Odd number: {n}')
		n -= 1

printEvenOdd(10)