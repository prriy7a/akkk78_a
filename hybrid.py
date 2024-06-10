#Hybrid inheritance
class A:
  def display(self):
    print("display from A")
class B(A):
  def display(self):
    print("display from B")
class C:
  def show(self):
    print("Hi from C class")
class D(B,C):
  def display(self):
    print("display from D class")
d1=D()
A.display(d1)
print(D.mro())
