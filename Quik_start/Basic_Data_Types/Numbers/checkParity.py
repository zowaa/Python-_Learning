def checkParity(n):
	if n % 2 == 0:
		return 0
	else:
		return 1
	
	# Another approach
	# res = n % 2
	# return res
	
print(checkParity(42))
print(checkParity(3221))