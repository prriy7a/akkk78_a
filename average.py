#Program to calculate average height from a list of heights
#constraints are not to use sum and len function in a list
#replicate using for loop
heights=input("Enter heights separated by space:")
heightslist=heights.split()
print(heightslist)
count=0
for i in heightslist:
    count+=1
print(count)
for j in range(count):
    heightslist[j]=int(heightslist[j])
print(heightslist)
total=0
for k in heightslist:
    total+=k
print(total)
avg=total/count
print(round(avg))