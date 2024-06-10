year=int(input("Enter a year:"))
def func(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("Leap year")
                return True

            else:
                print("Not a Leap Year")
                return False

        else:
            print("Leap year")
            return True


    else:
        print("Not a Leap Year")
        return False
print(func(year))
