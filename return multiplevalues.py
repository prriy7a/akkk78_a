import statistics
def mean_median_mode(list):
    return statistics.mean(list),statistics.median(list),statistics.mode(list)
a=mean_median_mode([3,4,5,45,3,2,1,2,3,4])
print(list(a))
def add(a,b):
  if a==0 & b==0:
    return "You have an egg"
  else:
    return a+b
d=int(input("enter no:\n"))
e=int(input("enter no:\n"))
result=add(d,e)
print(result)
def name(fname,lname):
  if fname=="" and lname=="":
    return "please enter a valid input"
  else:
    fname.title()
    lname.title()
    return f"{fname}, {lname}"
a=input("Enter first name")
b=input("Enter last name")
print(name(a,b))