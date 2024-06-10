set1={10,True,'jenny',1.11,True,2}
set2={1,2,10,-129,-10,0,53}
print(type(set1))
print(set1)
set1.discard(10)
print(set1)
print(set1.pop())
set1.add(20)
print(set1)
set1.remove(20)
print(set1)
#we can add immutable datatypes in set
set1.add((10,12,20))
print(set1)
