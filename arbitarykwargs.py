#arbitary(keyword)
def info(**kwargs):
  for key,value in kwargs.items():
    print(key,value)

info(name="ram",age=30,dept="cse")
info(name="akki",age=40,dept="it")
info(name="aj",dept="cse")
#multiply(2,3,-6,8)
#multiply(2,5,8,9,0,6)
def multiply(*nos):
    c=1
    for i in nos:
        c*=i
    print(c)
multiply(2,3,-6,8)
multiply(2,5,8,9,0,6)