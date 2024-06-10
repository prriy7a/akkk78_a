#Duck TYping
class Duck:
    def sum(self):
        print("I am a Duck and I can Swim")
    def speaks(self):
        print("Quack Quack")
class Dog:
    def sum(self):
        print("I am a Dog and I can swim")
    def speaks(self):
        print("Woof Woof")
class Person:
    def speaks(self):
        print("blah blah blah")
def display(duck):
    duck.sum()
    duck.speaks()
    print("Information displayed")
duck=Duck()
dog=Dog()
person=Person()
display(dog)
