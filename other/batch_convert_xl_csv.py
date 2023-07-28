# import os
# import pyexcel as pe

# input_directory = '/Users/nolaneley/Desktop/school_spending_proj/spending/FY18-19'
# output_directory = '/Users/nolaneley/Desktop/school_spending_proj/spending/FY18-19_csv'

# for filename in os.listdir(input_directory):
# 	if filename == '.DS_Store':
# 		continue
# 	if filename.endswith('.xlsx') or filename.endswith('.xls'):
# 		excel_file = os.path.join(input_directory, filename)
# 		output_file = os.path.join(output_directory, filename[:7] + '.csv')

# 		sheets = pe.get_book(file_name=excel_file)
# 		sheet_name = sheets.sheet_names()[0]

# 		sheet = sheets[sheet_name]
# 		sheet.save_as(output_file)

import pandas as pd
import os

input_directory = '/Users/nolaneley/Desktop/school_spending_proj/spending/FY18-19'
output_directory = '/Users/nolaneley/Desktop/school_spending_proj/spending/FY18-19_csv'

for filename in os.listdir(input_directory):
	if filename == '.DS_Store':
		continue
	if filename.endswith('.xlsx') or filename.endswith('.xls'):
 		excel_file = os.path.join(input_directory, filename)
 		output_file = os.path.join(output_directory, filename[:7] + '.csv')

 		df = pd.read_excel(excel_file)
 		df.to_csv(output_file, index=False)