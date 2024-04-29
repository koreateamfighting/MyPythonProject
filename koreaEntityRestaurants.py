# 200만건 넘는 빅데이터 엑셀 데이터 필터링 하는 예
import pandas as pd
import openpyxl
import time



restaurant_dic = {}

sheet = openpyxl.load_workbook(r'C:/Users/MEDIAZEN/Desktop/전국식당현황.xlsx')
datasets = pd.DataFrame([])

for i in sheet:

    dataset = pd.read_excel(r'C:/Users/MEDIAZEN/Desktop/전국식당현황.xlsx',sheet_name = i,                            
                        usecols = "A,V",
                        names = ['Index','식당이름'],skiprows = 1)
    datasets = dataset.concat([datasets,dataset])
    
    
# datasets.to_excel("result.xlsx",index=False)
print('결과')
print(dataset[0])
