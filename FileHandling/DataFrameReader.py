import pandas as pd
import os

file = pd.read_excel(io="test.xlsx", sheet_name="Sheet1", index_col=0)

# file = pd.read_csv("test.csv", index_col=0)
print(file)

rowDict = file.T.to_dict('dict')['TC01']
print(rowDict)
print(rowDict['Name'])
