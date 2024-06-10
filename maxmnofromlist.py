max=input("Enter numbers separated by space:")
maxlist=max.split()
print(maxlist)
count=0
for i in maxlist:
    count+=1
print(count)
for j in range(count):
    maxlist[j]=int(maxlist[j])
print(maxlist)
maxno=maxlist[0]
for k in maxlist:
    if k>maxno:
        maxno=k
print(f"maximum number is {maxno}")