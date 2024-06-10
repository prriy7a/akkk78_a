class Instructor:
    followers=0
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.followers=0
    def display(self,subject_name):
        print(f"Hi, I am {self.name} and I teach {subject_name}")
    def update_followers(self,follower_name):
        self.followers+=1
instructor_1=Instructor("Jenny","Delhi")
instructor_1.display("Python")
instructor_1.update_followers("sai")
print(instructor_1.followers)
instructor_2=Instructor("Payal","Up")
instructor_2.display("Java")

instructor_2.update_followers("sai")
print(instructor_2.followers)