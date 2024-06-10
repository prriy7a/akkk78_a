#public
class Student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Hi myself {self.name} from Student class")
s1=Student("Akshith")
print(s1.name)
s1.display()