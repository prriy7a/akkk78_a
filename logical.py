a=4
b=3
print(a and b)
print(not(a and b))
print(a or b)
#bitwise operators
a=5
b=4
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)
#identity operators
a=10
b=10
print(a is b)
c=[]
d=[]# both are same but lists are mutable it can be updated and location will be changed so it returns false
print(c is d)
#membership operators
f="Jenny"
print("J" in f)