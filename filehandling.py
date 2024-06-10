#read mode
# f1=open("file1.txt","r")
# f2=f1.read()
# print(f2)
#write mode
# f3=open("file1.txt","w")
# f3.write("Welcome to my world ")
#r+mode
# f4=open("file1.txt","r+")
# print(f4.tell())#it will tell where our cursor was
# f4.write("Hi")
# print(f4.tell())
# print(f4.read())
# print(f4.tell())
# f4.write("This is python course")
#w+mode
# f5=open("file1.txt","w+")
# print(f5.tell())
# f5.write("Hi, Welcome to my world of Love")
# print(f5.tell())
# f5.seek(0)#seek will mmove the pointer to the given position
# print(f5.tell())
# data=f5.read()
# print(data)
# print(f5.tell())
# f5.close()
#append mode
# f6=open("file1.txt","a")
# f6.write("Hello World")
# f7=open("file1.txt","a+")
# f7.seek(0)
# print(f7.read())
f8=open("download.jpeg","rb")
f9=open("download1.jpeg","wb")
for i in f8:
    f9.write(i)

