#multilevel inheritance
class Human:
  def __init__(self,heart):
    print("Calling init from HUman")
    self.eyes=2
    self.heart=heart
  def eat(self):
    print("I can eat")
  def work(self):
    print("I can work")
class Male(Human):
  def __init__(self,name):
    print("Calling init from Male")
    self.name=name
  def sleep(self):
    print("I can seleep")
  def work(self):
    print("I can code")
class Boy(Male):
  def __init__(self,heart,name,can_dance):
    Human.__init__(self,heart)
    Male.__init__(self,name)
    self.dance=can_dance
  def work(self):
    super().work()
    print("I can test")
boy_1=Boy(1,"Rahul",True)
boy_1.sleep()
boy_1.work()
Human.work(boy_1)
print(boy_1.name)
print(boy_1.dance)