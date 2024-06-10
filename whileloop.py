i=1
while i<=5:
    print(i)
    i+=1
list=[1,2,3,4,5]
while list:
    print("Hello")
    list.pop()
i=1
while i<=5:
    print(i)
    i+=1
else:
    print("Else block")
print("Out from loop")
i=1
while i<=5:
    print(i)
    i+=1
    if i==3:
        break
    else:
        print("Else block")
print("Out from loop")
for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("else block")
print("Out of loop")