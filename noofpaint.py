import math
def paint(height,width,cover):
    area=height*width
    noofpaintcans=math.ceil(area/cover)
    print(f"You will need {noofpaintcans} paint cans")
h=int(input("Enter height of the wall:"))
w=int(input("Enter width of the wall:"))
coverage=7
paint(height=h,cover=coverage,width=w)