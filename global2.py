def display():
  a=20
  def show():
    global a
    a=30
    print(f"value of a before calling show functionis {a}")
  show()
  print(f"value of a after calling show function is {a}")
display()
print(a)