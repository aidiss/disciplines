#new_discipline_announcements.py
"""Anouncing a new discipline


Author:
	Aidis Stukas
"""

url = r'C:\Users\Main\Dropbox\Research\announcements of new disciplines in scientific journals\spreadsheet_2014_10_10.xlsx'
import pandas as pd 
df = table = pd.read_excel(url, sheetname=1)

'''
import xlrd
workbook = xlrd.open_workbook(url)
worksheet = workbook.sheet_by_name('Slctd')
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1
curr_row = -1
while curr_row < num_rows:
	curr_row += 1
	row = worksheet.row(curr_row)
	print('Row:', curr_row)
	curr_cell = -1
	while curr_cell < num_cells:
		try:
			curr_cell += 1
			# Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
			cell_type = worksheet.cell_type(curr_row, curr_cell)
			cell_value = worksheet.cell_value(curr_row, curr_cell)
			print('	', cell_type, ':', cell_value)
		except:
			print('ERROR')
			link = mainData_sheet.hyperlink_map.get((curr_row, curr_cell))
			print('	', cell_type, ':', cell_value)
'''
df_all = pd.read_excel(url, sheetname='All')
print(df_all)

names_of_all_sheets = [
	'Emergence', 'All', 'Selected',	'Extra', 
	'Sheet1', 'Abstracts', 'Liles', 'Ziman'
					   ]
