#method overriding #there must be two classes used in inheritance
#there must be two classes same method in child class same no of arguments but they differ in locaitn in its own way
#run time polymorphism
class Father:
  def sleep(self):
    print("Sleeps from 10 to 5")
  def eat(self):
    print("eating")
class Son(Father):
  def sleep(self):
    super().sleep()
    print("sleeps from 2 to 10")
Ram=Son()
Ram.sleep()
Ram.eat()