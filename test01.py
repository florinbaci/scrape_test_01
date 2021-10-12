import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

# ref_workbook = openpyxl.load_workbook('data.xlsx')
path ='C:/Users/User/PycharmProjects/scrape_test_01/venv/data.xlsx'
wb = openpyxl.load_workbook(path)

# headers = ['Date', 'Hour', 'Race', 'Country', 'Money', 'Against_odds', 'Jokey', 'Win_Lost', 'Bank']

workbook_name = 'data.xlsx'
# wb = load_workbook(workbook_name)
ws = wb.active
ws.title = "Races"
# ws.append(headers)

ws.delete_rows(2, 7)

# col_c = ws['c']
# len_table = int(len(col_c))
# # print print(len_table - 5)
# fifth_row = int(len_table - 7)

# row_range = ws[fifth_row: len_table]
# print(row_range)

# col_b = int(fifth_row)
# col_c = int(len_table)
# col_bf = str('B') + str(col_b)
# col_cf = str('C') + str(col_c)
# # print(col_bf)
# # print(col_cf)
#
# row = ws.iter_rows(min_row=fifth_row, max_row=len_table, min_col=2,  max_col=3)
#
# for a, b in row:
#     print(a.value, b.value)
    # if "Philip" in a.value and "Gent" in b.value:
    #     print(a.value, b.value)
    #     # ws.cell(row=1, column=9).value = 23
    #     # print(b)
    #     row_no = str(b)
    #     row_final = int(row_no[16:-1])
    #     # ws.cell(row=row_final, column=9).value = 99
    #
    #     pattern = int(re.findall(r'\d+', row_no)[-1])
    #     print(pattern)
    #     ws.cell(row=pattern, column=9).value = 89

wb.save(filename=workbook_name)
