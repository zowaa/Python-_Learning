class Rectangle:
	def __init__(self, x1, x2, y1, y2):
		if x1 < x2 and y1 > y2:
			self.x1 = x1
			self.x2 = x2
			self.y1 = y1
			self.y2 = y2
			print('Rectangle created')
		else:
			print('You cannot create a rectangle with these coord')


rec = Rectangle(2,3,5,1)