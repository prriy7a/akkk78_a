phon=dict({'Ram':1234,
    'Shyam':3456,
    'mohan':8479})
print(phon.popitem())#it deletes last item in dict and returns that
print(phon)
print(phon.keys())
print(phon.values())
print(phon.items())
for i in phon:
  print(i)
  print(phon[i])
for i in phon.items():
  print(i)
p=phon.copy()
print(p)