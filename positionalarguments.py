#types of arguments
#positional
def greet(name,branch):
  print(f"Hi {name}")
  print(f"Are you from {branch} department?")
greet("akshith","cse")
#keyword
def greet(name,branch):
  print(f"Hi {name}")
  print(f"Are you from {branch} department?")
greet(name="akshith",branch="cse")
