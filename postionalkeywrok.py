#positional Keyword
def greet(name,branch):
  print(f"Hi {name}")
  print(f"Are you from {branch} department?")
greet("akshith",branch="cse")
# greet(branch="cse","akshith")#here error since always keyword argument should follow positional arguments but here postional argument is following keyword argument