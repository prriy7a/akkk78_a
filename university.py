class University:
    def __init__(self,name):
        self.name=name
    def showDetails(self):
        print(f"Welcome to {self.name} University")
class Course(University):
    def __init__(self,name,course):
        University.__init__(self,name)
        self.course=course
    def showDetails(self):
        super().showDetails()
        print(f"You have chosen {self.course} ")
class Branch(University):
    def __init__(self,branch):
        self.branch=branch
    def showDetails(self):
        print(f"You have selected {self.branch} branch")
class Student(Course,Branch):
    def __init__(self,name,course,branch,sname):
        Course.__init__(self,name,course)
        Branch.__init__(self,branch)
        self.name=sname

    def showDetails(self):

        print(f"Student name: {self.name}")

class Faculty(Branch):
        def __init__(self, branch, name):
            Branch.__init__(self, branch)
            self.name = name

        def showDetails(self):
            print(f"Faculty name: {self.name}")

c1 = Course("mbu", "ENgineering")
c1.showDetails()
b = Branch("Cse")
s = Student("mbu", "ENgineering", "cse", "Akshith")
Branch.showDetails(s)
s.showDetails()
f = Faculty("CSE", "HOD")
f.showDetails()


