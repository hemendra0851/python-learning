import pandas as pd
import os
from os.path import dirname, abspath, realpath


# fileName = filePath + fileDetail.split('.')[0] + ".xls"
# if os.path.exists(fileName) == False:
#     fileName = filePath + fileDetail.split('.')[0] + ".xlsx"
# sheetName = fileDetail.split('.')[1]
fileName= 'ESACollectionData.xlsx'
dataframe = pd.read_excel(fileName, 'Drug')
rowDict = dataframe.set_index('_id').T.to_dict('dict')[21376311]
print(rowDict)
#     return rowDict
