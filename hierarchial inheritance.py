#hierarchial inheritance
class Human:
  def __init__(self,name,age):
    print("Calling init from Human")
    self.name=name
    self.age=age
  def showDetails(self):
    print(f"{self.name} and {self.age}")
  def eat(self):
    print("I cane at")
class Male(Human):
  def __init__(self,name,age,location):
    print("Calling init from Male class")
    Human.__init__(self,name,age)
    self.location=location
  def sleep(self):
    print("I can sleep")
class Female(Human):
  def __init__(self,name,age,can_Dance):
    print("Calling inti from Female")
    super().__init__(name,age)
    self.knowdance=can_Dance
  def showDetails(self):
    Human.showDetails(self)
    print(f"{self.knowdance}")

  def work(self):
    print("I can work")
female_1=Female("jenny",18,True)
male_1=Male("Akash",18,"Hyd")
female_1.eat()
female_1.showDetails()
male_1.sleep()
male_1.eat()
male_1.showDetails()
female_1.showDetails()