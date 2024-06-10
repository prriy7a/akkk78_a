#union
set1={1,2,3,4,5}
set2={4,5,6,10,11}
print(set1.union(set2))
print(set2.union(set1))
print(set1 | set2)
set1.update(set2)
print(set1)
print(set1.union(("mohan","jenny")))# first tuple converted into set and union operation applied
#intersection
set1={'ram','shyam','jenny'}
set2={'jenny','jiya','akash'}
set3={'jenny'}
print(set1.intersection(set2))
print(set1 & set2 & set3)
set1.intersection_update(set2)
print(set1)
print(set2)
set1.intersection_update('jem')#it returns empty set because no common attribute or element or argument
print(set1)
#difference
set1={'ram','shyam','jenny'}
set2={'jenny','jiya','akash'}
set3={'ankur','pradeep','ram'}
print(set1.difference(set2))
print(set2-set1)
print(set1.difference(['mohan','ram']))
print(set1.difference(set2,set3))
set1.difference_update(set2)
print(set1)
set2.difference_update(set1)
print(set2)
#symmetric difference
set1={'ram','shyam','jenny'}
set2={'jenny','jiya','akash'}
set3={'ankur','pradeep','ram'}
print(set1.symmetric_difference(set2))
set2.symmetric_difference_update(set1)
print(set2)
#disjoint,subset,superset
set1={'ram','shyam','jenny'}
set2={'jenny','jiya','akash'}
print(set1.isdisjoint(set2))
print(set1.isdisjoint(('a')))
print(set1.issubset(set2))
print(set1.issubset(('ram','jenny','shyam')))
print(set1<=set2)#subset operator
print(set1.issuperset(set2))
print(set1.issuperset(('ram','jenny','shyam')))
print(set1>=set2)#superset operator
#clear and del
set1={'ram','shyam','jenny'}
set2={'jenny','jiya','akash'}
set2.clear()
print(set2)
del set1
print(set1)
