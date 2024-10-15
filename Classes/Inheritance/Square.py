class Rectangle:
  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
        
  def width(self):
    return self.x2 - self.x1
      
  def height(self):
    return self.y2 - self.y1
  
  def area(self):
    return self.width() * self.height()

class Square(Rectangle):
  def __init__(self, x1, y1, l):
    x2 = x1 + l
    y2 = y1 + l
    super().__init__(x1, y1, x2, y2)


sq = Square(2, 7, 7)
a = sq.area()
print(a)