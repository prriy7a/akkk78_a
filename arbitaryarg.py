#arbitary arguments
def add(*nos):#single astreik(*) means arbitary positional argument
  c=0
  for i in nos:
    c=c+i
  print(f"sum is {c}")
add(5,7,9)
add(1,2,3,4,5)
#arbitary
def add(a,*nos,):
  c=0
  print(nos)
  print(a)
  for i in nos:
    c+=i
  print(f"Sum is {c}")
add(1,2,5)