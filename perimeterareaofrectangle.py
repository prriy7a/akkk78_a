class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def area(self):
        return self.length*self.breadth
l=int(input("Enter length:\n"))
b=int(input("Enter breadth:\n"))
rectangle=Rectangle(l,b)
print(rectangle.perimeter())
print(rectangle.area())