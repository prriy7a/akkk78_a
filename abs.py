from abstraction import Vehicle
class Bike(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color=color
    def start(self):
        print("Start with kick")
    def display(self):
        print(f"My color is {self.color}")
class Scooty(Vehicle):
    def __init__(self,n):
        self.nooftyres=n
    def start(self):
        print("self start")
class Car(Vehicle):
    def __init__(self,n,x):
        self.nooftyres=n
        self.noofgears=x
    def start(self):
        print("Start with key")
