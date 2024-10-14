def ListofEvenOdds():
	even = [x for x in range(1,21) if x%2 == 0]
	odd = [x for x in range(1, 21) if x%2 != 0]
	return [even, odd]

[even, odd] = ListofEvenOdds()
print(f'even = {even}')
print(f'odd = {odd}')