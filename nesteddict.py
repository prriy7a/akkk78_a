data={
    "ram":{"rollno":10,"age":20,"course":"pyton"},
    "mohan":{"rollno":20,"age":23,"course":'Java'}
}
print(data["mohan"])
print(data['mohan']['rollno'])
print(data["mohan"].pop('rollno'))
print(data["mohan"])
traveldata={
    "Gujarat":["dwarakadhish","somnath","statue of unity"],
    "Rajasthan":["Jaipur","Udaipur"]
}
print(traveldata)
print(traveldata["Rajasthan"])
#nested dictionary in a list
data=[
{"name":"ram","rollno":10,"age":20,"course":"pyton"},
  {"name":"mohan","rollno":20,"age":23,"course":'Java'}
]
print(data)
print(type(data))
print(data[0])
print(data[0]["name"])
data.append({"name":'Shyam',"rollno":22,"age":18,"couse":"c++"})
print(data)