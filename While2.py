no=int(input("Enter a no(-1 to quit)"))
while no!=-1:
    print(no)
    no=int(input("Enter a no (-1 to quit)"))
else:
    print("This is else block")
print("out of loop")
total=0
number=int(input("Enter a number(0 or -1 to quit)"))
while number!=0 and number!=-1:
    total+=number
    number = int(input("Enter a number(0 or -1 to quit)"))
print(total)