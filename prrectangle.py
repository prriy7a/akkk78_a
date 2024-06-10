#another method
class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth
    self.area=length*breadth
  def perimeter(self):
    return 2*(self.length+self.breadth)
rectangle_1=Rectangle(2,5)
print(rectangle_1.perimeter())
print(rectangle_1.area)
#in this code area is defined as attribute in __init__ method only