import openpyxl
from openpyxl import Workbook
# 用python建立一個Excel空白活頁簿
excel_file = Workbook()
# 建立一個工作中表
sheet = excel_file.active
# 先填入第一列的欄位名稱
sheet['A1'] = 'Action'
sheet['B1'] = 'Time'
sheet['C1'] = 'text before change'
sheet['D1'] = 'change texts'
sheet['E1'] = 'text after change'

i = 2
while i < 10:
    columnA = '刪除'
    columnB = '1:55'
    columnC = '今天星期'
    columnD = '三，我去'
    columnE = '學校上課今天'
#     實際將資料寫入每一列
    sheet.append([columnA, columnB, columnC, columnD,columnE])
    i = i + 1
# 儲存成XLSX檔
excel_file.save('sample.xlsx')










