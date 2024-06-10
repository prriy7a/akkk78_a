#default arguments
def greet(name,subject,dept="cs"):
  print(f"hi {name}")
  print(f"Are you from {dept} department?")
  print(f"Do you teach {subject} subject?")
greet("akshith","python","cse")
greet("sai","c")