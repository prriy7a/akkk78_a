#random pay the bill without using choice function
# import random
# name=input("Enter your names separted by comma:")
# list=name.split(",")
# print(list)
# b=len(list)
# randomchoice=random.randint(0,b-1)
# print(f"{list[randomchoice]} will pay the bill")
#with choice function
import random
name=input("Enter your names separted by comma:")
list=name.split(",")
print(list)
personselected=random.choice(list)
print(f"{personselected} will pay the bill")
