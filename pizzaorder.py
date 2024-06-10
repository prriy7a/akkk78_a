# small_pizza=100
# medium_pizza=200
# large_pizza=300
# peppicorne for small pizza=30
# peppicorne for large pizza=50
# extra cheese for any size pizza=20
size=input("What size pizza do you want(s/m/l)?").lower()
bill=0
if size=="s":
    bill+=100
    print(f"Small pizza price is {bill} Rs")
elif size=="m":
    bill+=200
    print(f"Medium pizza price is {bill} Rs")
elif size=="l":
    bill+=300
    print(f"Large pizza price is {bill} Rs")
else:
    print("Enter a valid pizza")
add=input("Do you want peppicorne(y/n)?").lower()
if add=="y":
    if size=="s":
        bill+=30
    else:
        bill+=50
cheese=input("Do you want cheese(y/n)?").lower()
if cheese=="y":
    bill+=20
print(f"Your Total bill is {bill}")

