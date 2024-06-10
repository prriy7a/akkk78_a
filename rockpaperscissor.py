import random
userch=int(input("Enter choice:0 for rock,1 for paper,2 for scissor"))
if userch>=3 or userch<0:
    print("Invalid choice")
else:
    compch=random.randint(0,2)
    print(f"computer choice is {compch}")
    if userch==compch:
        print(f"Its a draw")
    elif userch==2 and compch==0:
        print("computer wins")
    elif userch==0 and compch==2:
        print("User wins")
    elif userch>compch:
        print("User wins")
    elif userch>compch:
        print("computer wins")