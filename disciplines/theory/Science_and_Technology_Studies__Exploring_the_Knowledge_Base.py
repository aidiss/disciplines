#Science_and_Technology_Studies__Exploring_the_Knowledge_Base.py
URL = 'D:\My Documents\Desktop\TO IMPLEMENT'
filename = 'temporary.xlsx'
full_url = '\\'.join([URL, filename])

print (full_url)

import pandas as pd 
dfs = [pd.read_excel(full_url, sheetname=x) for x in range(9)]
table2 = dfs[0]
table3 = dfs[1]
figure2 = dfs[2]
figure3 = dfs[3]
table4 = dfs[4]
table5 = dfs[5]
