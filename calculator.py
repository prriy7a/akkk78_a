def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def divison(a,b):
    return a/b
operator={"+":addition,
          "-":subtraction,
          "*":multiplication,
          "/":divison}
def calculator():
    n1=float(input("Enter a number:"))
    for keys in operator:
        print(keys)
    continue_flag=True
    while continue_flag:
        operation=input("Pick an Operation:")
        n2=float(input("Enter a number:"))
        calculation=operator[operation]
        output=calculation(n1,n2)
        print(f"{n1} {operation} {n2} = {output}")
        should_continue=input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit").lower()
        if should_continue=="y":
            n1=output
        elif should_continue=="n":
            continue_flag=False
            calculator()
        else:
            continue_flag=False
            print("Bye")
calculator()