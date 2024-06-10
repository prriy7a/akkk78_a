r1=['😁','😁','😁']
r2=['😁','😁','😁']
r3=['😁','😁','😁']
matrix=[r1,r2,r3]
# print(matrix)
# print(f"{r1}\n{r2}\n{r3}")
position=input("Enter position to hide the money:")
rowno=int(position[0])
columnno=int(position[1])
rowselected=matrix[rowno-1]
rowselected[columnno-1]='X'
print(f"{r1}\n{r2}\n{r3}")
