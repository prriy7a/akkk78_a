class Human:
    def __init__(self,heart):#attributes
        self.num_eyes=2#attributes
        self.num_nose=1#attributes
        self.heart=heart
    def eat(self):#methods
        print("I can eat")
    def work(self):#methods
        print("I can work")
class Male(Human):#child class
    def __init__(self,name,heart):
        super().__init__(heart)
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()#accessing parent class method
        print("I can code")

    def display(self):
        print(f" Hi, I am {self.name} and I have{self.num_eyes} eyes,{self.num_nose} nose and{self.heart} heart ")
male_1=Male("akash",1)
male_1.flirt()
male_1.work()
print(male_1.num_eyes)
print(male_1.num_nose)
print(male_1.heart)
male_1.display()


