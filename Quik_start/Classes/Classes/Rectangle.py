class Rectangle:
	def __init__(self, x1, y1, x2, y2):
		if x1 < x2 and y1 > y2:
			self.x1 = x1
			self.x2 = x2
			self.y1 = y1
			self.y2 = y2
			print('Rectangle created')
		else:
			print('You cannot create a rectangle with these coord')

	def __str__(self):
		return f'{self.x1}, {self.y1}, {self.x2}, {self.y2}'
	
	def width(self):
		return self.x2 - self.x1
	
	def height(self):
		return self.y1 - self.y2
	
	def area(self):
		return self.width() * self.height()

	def perimeter(self):
		return 2 * (self.width() + self.height())
		


rec = Rectangle(2,7,5,3)
print(rec)