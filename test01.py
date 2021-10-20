import openpyxl
import datetime

# from openpyxl import Workbook
# from openpyxl import load_workbook
# from openpyxl.worksheet.table import Table, TableStyleInfo

# ref_workbook = openpyxl.load_workbook('data.xlsx')
path = 'C:/Users/User/PycharmProjects/scrape_test_01/venv/data.xlsx'
wb = openpyxl.load_workbook(path)

workbook_name = 'data_test.xlsx'
# wb = load_workbook(workbook_name)
ws = wb.active
# ws.title = "Races"


col_c = ws['c']
len_table = int(len(col_c))
# print print(len_table - 5)
fifth_row = int(len_table - 7)

# row_range = ws[fifth_row: len_table]
# print(row_range)

col_b = int(fifth_row)
col_c = int(len_table)
# col_bf = str('B') + str(col_b)
# col_cf = str('C') + str(col_c)
# # print(col_bf)
# # print(col_cf)

time_race_list = []

row_time_race = ws.iter_rows(min_row=fifth_row, max_row=len_table, min_col=2, max_col=3)

for time, race in row_time_race:
    time_race_list.append([time.value, race.value])

jokey_list = []

row_jokey = ws.iter_rows(min_row=fifth_row, max_row=len_table, min_col=7, max_col=7)

for jokey in row_jokey:
    for jokey_value in jokey:
        jokey_list.append(jokey_value.value)

for time_race_jokey in range(len(time_race_list)):
    time_race_list[time_race_jokey].append(jokey_list[time_race_jokey])

print(time_race_list)
# print(jokey_list)

# def index_in_list_of_lists(time_race_list, jokey_list):
#     for i, lst in enumerate(time_race_list):
#         if jokey_list in lst:
#             break
#         else:
#             raise ValueError("%s not in list_of_lists" %jokey_list)
#
#     return i, lst.index(jokey_list)
#
#
# print(index_in_list_of_lists(time_race_list, jokey_list))
#
# h = index_in_list_of_lists(time_race_list, jokey_list)
# print(h[0])

# if [datetime.time(7, 10), 'Newcastle', 'Jesse James\nBrodie Loy'] in time_race_list:
#     print(time_race_list.index([datetime.time(7, 10), 'Newcastle', 'Jesse James\nBrodie Loy']))
#     print('found')
# else:
#     print('not found')
#     race_to_check.append([a.value, b.value, c.value, e.value, f.value])
# for a, b, c, d, e, f in row_01:
#     race_to_check.append([a.value, b.value, c.value, e.value, f.value])
# if [datetime.time(6, 50), 'Queanbeyan', 'AUS', 'Milamoo\nAmy Mc Lucas'] in race_to_check:
#     print("found")
#     break
# print(a.value, b.value)
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

# row_02 = ws.iter_rows(min_row=fifth_row, max_row=len_table, min_col=7,  max_col=7)
# #
# for c in row_02:
#     for jokey in c:
#         print(race_to_check[0])
# race_to_check.insert(0, [jokey.value])
# print(jokey.value)

# race_to_check = [[] for _ in range(7)]
# race_to_check[0:-1].append([jokey.value])

# print(race_to_check)

# wb.save(filename=workbook_name)
