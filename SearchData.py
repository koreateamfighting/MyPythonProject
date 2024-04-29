import pandas as pd
import time
from collections import defaultdict
from itertools import chain
import dask
import dask.dataframe as dd
from dask.delayed import delayed
from difflib import get_close_matches



restraunt_dic = {}

total_dic = defaultdict(list)
# start = time.time() # 시작 시간
# dataset = pd.read_excel(r'C:/Users/MEDIAZEN/Desktop/전국식당현황2.xlsx',sheet_name = '일반음식점_1',\
#     usecols="A,B",
#     names = ['index','restraunt_name'],
#     skiprows=1)
# dataset.to_pickle(r'C:/Users/MEDIAZEN/Desktop/전국식당현황2.pkl')


df = pd.read_pickle(r'C:/Users/MEDIAZEN/Desktop/전국식당현황2.pkl')
names_list = []


for i in df['restraunt_name']:
     names_list.append(str(i).lstrip())
     
start = time.time() # 시작 시간
names_list.sort()

# print(names_list[0:100])
end = time.time() # 끝나는 시간
print(f"파일 읽는 시간 {end - start:.5f}초 나온다.") #파읽 읽기 시간 출력   




start2 = time.time()

def find (names_list,target):
     start = 0
     end = len(names_list)-1
     
     while start <= end:
          middle = (start+end)//2
          midpoint = names_list[middle]
          if midpoint > target:
               end = middle -1
          elif midpoint < target:
               start = middle + 1
          else : 
               return midpoint,target,middle
          
          
print(find(names_list, '이루리샌드위치'))
print(names_list[0])
end2 = time.time() # 끝나는 시간
print(f"검색 시간은  {end2 - start2:.5f}초 나온다.") #검색 시간 출력   



# word = '마곡'
# n = 50
# cutoff = 0.6
# close_matches = get_close_matches(word,names_list,n,cutoff)
# print(close_matches)




# for i in pckl.index:   
#     restraunt_dic.update({pckl['index'][i] : pckl['restraunt_name'][i]})

# for k , v in chain(restraunt_dic.items()):
#     total_dic[k].append(v)



# df = pd.read_excel(r'C:/Users/MEDIAZEN/Desktop/전국식당현황2.xlsx')
# df.to_pickle(r'C:/Users/MEDIAZEN/Desktop/전국식당현황2.pkl')
# pckl = pd.read_pickle(r'C:/Users/MEDIAZEN/Desktop/전국식당현황.pkl')








