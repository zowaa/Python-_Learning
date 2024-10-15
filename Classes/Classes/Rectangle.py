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
	
	def width(self):
		return self.x2 - self.x1
	
	def height(self):
		return self.y1 - self.y2
	
	def area(self):
		return self.width() * self.height()

	def perimeter(self):
		return 2 * (self.width() + self.height())
		


rec = Rectangle(2,7,5,3)
h = rec.height()
w = rec.width()
print(f'height = {h}, wigth = {w}')
a = rec.area()
print(f'area = {a}')
p = rec.perimeter()
print(f'perimeter = {p}')