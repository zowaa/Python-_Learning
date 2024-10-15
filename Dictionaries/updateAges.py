def updateAges(dict, n):
	upd = {}
	for x in dict:
		upd[x] = dict[x] + n
	return upd


ages = {
     "Peter": 10,
     "Isabel": 11,
     "Anna": 9,
     "Thomas": 10,
     "Bob": 10,
     "Joseph": 11,
     "Maria": 12,
     "Gabriel": 10,
 }

print(updateAges(ages, 1))