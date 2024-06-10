# #method overloading "same class same methods with differnt arguments"
#compile time polymorphism
# class Demo:
#   def add(self,a,b,c=0):
#     return a+b+c
#   def add(self,a,b,c=0):
#      return a+b+c
# d=Demo()
# print(d.add(1,2))
# print(d.add(1,2,3))
class Demo:
    def add(self,*args):
        total=0
        for i in args:
            total=total+i
        return total
d=Demo()
print(d.add(2,3))
print(d.add(4,5,6,7))
print(d.add(2,3,4,5,6,7,8))