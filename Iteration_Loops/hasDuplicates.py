def hasDuplicates(l):
	new_l = l.copy()
	new_l.sort()
	for i in range(len(new_l) - 1):
		if new_l[i] == new_l[i+1]:
			return True
	return False

listt = [11, 23, 3, 1]
print(hasDuplicates(listt))
