list1=[0,1,2,3]
print(len(list1))
class Author:
    def __init__(self,name,book_name,pages):
        self.name=name
        self.book_name=book_name
        self.pages=pages
    def __str__(self):
        return f"{self.book_name} by {self.name}"
    def __len__(self):
        return self.pages
    def __call__(self,*args,**kwargs):
        print("Hi")
d=Author("Jenny","Python Basic to Advance",300)
print(d)
print(len(d))
d()

print(d)