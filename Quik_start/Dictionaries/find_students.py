def find_students(dict, addr):
	l = []
	for key, d in dict.items():
		if d['add'] == addr:
			l.append(key)
	l.sort()
	return l

students = {
	"zowa" : {'age': 28, 'add': 'bg'},
	"simba" : {'age': 26, 'add': 'fes'},
	'ax' : {'age': 3, 'add': 'fes'}
}
print(find_students(students, 'fes'))