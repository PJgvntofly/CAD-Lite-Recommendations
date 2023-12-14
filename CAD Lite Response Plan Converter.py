import pandas as pd

# Script for converting CAD Lite response plans from a JSON file to an 
# Excel workbook for ease of viewing
df = pd.read_json(r"response_plans.json", typ='frame')

SNO911 = df['SNO911'].apply(pd.Series)
SNO911 = SNO911.transpose()

writer = pd.ExcelWriter(r"CAD Lite Response Plans.xlsx", engine='openpyxl')
for column in SNO911.columns:
    SNO911[column].apply(pd.Series).to_excel(writer, sheet_name=column)
writer.close()