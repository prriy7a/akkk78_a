import openpyxl
import xlrd
loc=("C:\\Users\\Sai Akshith\\Desktop\\Book1.xlsx")
wb=openpyxl.load_workbook(loc)

sheet = wb['Sheet1']
cell_value = sheet['A1'].value
print(cell_value)
