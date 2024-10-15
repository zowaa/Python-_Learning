def calculateAverageAge(dict):
	leng = len(dict)
	summ = 0
	for d in dict.values():
		summ += d['age']
	return summ / leng

students = {
	"zowa" : {'age': 28, 'add': 'bg'},
	"simba" : {'age': 26, 'add': 'fes'}
}
print(calculateAverageAge(students))