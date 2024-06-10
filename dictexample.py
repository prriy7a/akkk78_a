studentmarks={
    "jenny":92,
    "akshith":78,
    "vinay":56,
    "vijay":49,
    "veeresh":99,
    "pavan":34
}
studentgrade={}
for i in studentmarks:
    marks=studentmarks[i]
    if marks>90:
        studentgrade[i]="A+"
    elif marks>80:
        studentgrade[i]="A"
    elif marks>70:
        studentgrade[i]="B+"
    elif marks>60:
        studentgrade[i]="B"
    elif marks>50:
        studentgrade[i]="C"
    elif marks>40:
        studentgrade[i]="D"
    else:
        studentgrade[i]="E"
print(studentgrade)

