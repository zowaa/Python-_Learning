def oldestStudent(dict):
	max_age = 0
	max_name = 0
	for key, val in dict.items():
		if val > max_age :
			max_age = val
			max_name = key
	return max_name


students = {
     "Peter": 10,
     "Isabel": 11,
     "Anna": 9,
     "Thomas": 10,
     "Bob": 10,
     "Joseph": 11,
     "Maria": 12,
     "Gabriel": 10,
 }
print(oldestStudent(students))