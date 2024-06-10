class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        # self.pi=3.14
    def circumference(self):
        return 2*self.pi*self.radius
    def area(self):
        return self.pi*self.radius**2
r=int(input("Enter radius of circle:"))
circle=Circle(r)
print(circle.circumference())
print(circle.area())