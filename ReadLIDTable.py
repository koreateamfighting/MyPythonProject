import sys
import pandas as pd


allData = {}
first_column = []
second_column = []
third_column = []

dataset = pd.read_excel(r'C:/Users/MEDIAZEN/Desktop/(통합)_UI Scenario_VR System_v3.0.8_20231025_LID_table.xlsx',sheet_name='1. Prompt',skiprows = 2, usecols='C,K,L',names=['LID','영어','한국어'])

for i in dataset['한국어']:
        # textEdit1.append(f'{i}\n') 
        first_column.append(f'{i}')               
             
for j in dataset['영어'] :
        # textEdit1.append(f'{j}\n')
        second_column.append(f'{j}')               
            
for k in dataset['LID']:
        # textEdit1.append(f'{k}\n')
        third_column.append(f'{k}')        
            
            
allData['LID'] = third_column
allData['한국어'] = first_column
allData['영어'] = second_column

print(allData.values())
