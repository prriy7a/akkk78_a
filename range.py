total=0
for i in range(101):
    total+=i
print(total)
'''sum of even numbers from 1 to 100,
it should include in range 1 and 100 also'''
total=0
for i in range(1,101):
    if i%2==0:
        total+=i
print(total)
#another method
total=0
for i in range(2,101,2):
    total+=i
print(total)