name1=input("Enter your name:")
name2=input("Enter your name:")
result=name1+name2
result.lower()
T=result.count('t')
R=result.count('r')
U=result.count('u')
E=result.count('e')
true=T+R+U+E
L=result.count('l')
O=result.count('o')
V=result.count('v')
E=result.count('e')
love=L+O+V+E
lovescore=int(str(true)+str(love))
print(lovescore)
if lovescore<10 or lovescore>90:
    print(f"Your score is {lovescore} and you go together like coke and mentos")
elif lovescore>=40 and lovescore<=50:
    print(f"You are alright together")
else:
    print(f"Your lovescore is {lovescore}")