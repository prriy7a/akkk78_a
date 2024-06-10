class Student:
    def __init__(self,name,rollno,age):
        self.name=name#public
        self._rollno=rollno#protected(_ represents protected)
        self.__age=age#private
    def __display(self):
        print(f"Hi myself {self.name} with rollno {self._rollno} from student class")
    def displayPrivateData(self):#by  calling like this we can access private methods also
        self.__display()
class Branch(Student):
    def show(self):
        print(f"my Rollno is {self._rollno}")
s1=Student("Rahul",23,20)
print(dir(s1))
print(s1._Student__age)
print(s1._Student__display())