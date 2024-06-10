class Student:
    def __init__(self,name,rolno,age):
        self.name=name
        self.rollno=rolno
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if self.__age>35:
            print("Invalid age give age should be less than 35")
        else:
            self.__age=age
name=input("Enter name:")
rollno=int(input("Enter rollno:"))
age=int(input("enter age:"))
s1=Student(name,rollno,age)
s1.set_age(30)
print(s1.get_age())