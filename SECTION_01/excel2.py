import openpyxl

filename = 'score.xlsx'
wb = openpyxl.load_workbook(filename)

sheet = wb['Sheet1']

sum = 0
cols = 'BCD'

for y in range(2, 5):
    for x in cols:
        sum += int(sheet[(x + str(y))].value)
    sheet[('E'+str(y))].value = str(sum )
    sheet[('F'+str(y))].value = str(sum / len(cols))
    sum = 0  

wb.save(filename)
wb.close()


