def prime(number):
    is_prime=True
    if n==1:
        is_prime=False
    for i in range(2,number):
        if n%i==0:
            is_prime=False
    if is_prime:
        print("It is a prime no")
    else:
        print("It is not a prime no")
n=int(input("Enter a number"))
prime(n)