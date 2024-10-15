def calculateAvg(dict):
	summ = sum(dict.values())
	length = len(dict)
	return summ / length

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

print(calculateAvg(ages))
