height=int(input("Enter a height:"))
if height>=3:
    print("You can ride")
    age=int(input("Enter your age"))
    if age<12:
        bill=150
        print(f"Ticket price is {bill} Rs")
    elif age<=18:
        bill=250
        print(f"Ticket price is {bill} Rs")
    else:
        bill=500
        print(f"Ticket price is {bill} Rs")
    wantphoto=input("Do you want photo(Y or N)?").lower()
    if wantphoto=="y":
        bill=bill+50
    print(f"Your total bill is {bill}")
else:
    print("You can't ride")
print("Thank you ... Enjoy the world!")