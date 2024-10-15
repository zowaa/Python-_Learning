def findOccurence(s):
	return [s.find('b'), s.find('ccc')]

[a, b] = findOccurence('aaabbbccc')
print(f'a = {a}, b = {b}')