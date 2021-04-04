import openpyxl

wb = openpyxl.load_workbook('score.xlsx')

sheet = wb['Sheet1']

print(sheet['B1'].value)   # 국어
print(sheet['C1'].value)   # 영어
print(sheet['D1'].value)   # 수학

wb.close()


