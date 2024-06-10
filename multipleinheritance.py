#multiple inheritance
class Human:
  def __init__(self):
    print("Calling init from Human")
    self.num_eyes=2
    self.num_nose=1
  def eat(self):
    print("I can eat")
  def work(self):
    print("I can work")

class Male:
  def __init__(self,name):
    print("Calling init from self")
    self.name=name
  def flirt(self):
    print("I can flirt")
  def work(self):
    print("I can code")

class Boy(Human,Male):
  def __init__(self,name,language):
    Human.__init__(self)
    Male.__init__(self,name)
    self.language=language
  def sleep(self):
    print("I can sleep")
  def work(self):
    print("I can test")
  def display(self):
    print(f"Hi i am {self.name} and i work on {self.language}")
boy_1=Boy("akash","python")
boy_1.flirt()
boy_1.eat()
boy_1.work()
Male.work(boy_1)# it accesses the second parent class work because there are 2 works are defined it will take default first given derived class
print(Boy.mro())
print(boy_1.num_eyes)
print(boy_1.num_nose)
print(boy_1.name)
print(boy_1.language)
boy_1.display()

