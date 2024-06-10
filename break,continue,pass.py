#break
count=0
while count<=10:
    print(count)
    count+=1
    if count==7:
        break
    print("Hi")
print("Out of loop")
l1=["hi","hello","welcome"]
names=["krishna","ram","mdav"]
for item in l1:
  for name in names:
    print(item,name)
    if item=="hello" and name=="ram":
      break
  print("out of inner loop")
print("out of outer loop")
#continue
count=0
while count<=10:
  print(count)
  count+=1
  if count==7:
    continue
  print("Hi")
print("out of loop")
#pass
count=0
while count<=10:
  print(count)
  count+=1
  if count==7:
    pass

  print("Hi")
print("out of loop")