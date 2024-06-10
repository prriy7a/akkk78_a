#dictonaries
phone_no={
    'Ram':1234,
    'Shyam':3456,
    'mohan':8479
}
phon=dict({'Ram':1234,
    'Shyam':3456,
    'mohan':8479})
print(phone_no)
print(type(phone_no))
print(phone_no["Shyam"])
print(phon)
phone_no['mohan']=9999
print(phone_no)
phone_no['madhav']=1111,2222
print(phone_no)
phone_no['Shyam']={"Shyam_Home":4444,'Shyam work':5678}
print(phone_no)
print(phone_no['Shyam']["Shyam work"])
print(phone_no.get('Ram'))
print(phone_no.pop('mohan'))
print(phone_no)

