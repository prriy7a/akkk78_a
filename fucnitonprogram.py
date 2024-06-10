def addnewstudent(name,rollno,age,course):
  d={}
  d["Name"]=name
  d["rollno"]=rollno
  d["age"]=age
  d["course"]=course
  print(d)
  data.append(d)
data=[
{"name":"ram","rollno":10,"age":20,"course":"pyton"},
  {"name":"mohan","rollno":20,"age":23,"course":'Java'}
]
addnewstudent("Shyam",22,18,"C++")
print(data)