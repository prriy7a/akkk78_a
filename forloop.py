a="akshith"
for i in a:
    print(i,end=",")
#square of each item in a list
list=[2,3,4,-2,10]
squares=[]
for i in list:
    square=i**2
    squares.append(square)
print(squares)
#for else loop
tuple=(2,56,34,5,-1)
for i in tuple:
    print(i)
    # break
else:
        print("Successfully completed and we are in else block now")
print("Out of for else loop")