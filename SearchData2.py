import time
from openpyxl import load_workbook
start = time.time() # 시작 시간
wb = load_workbook(filename = r'C:/Users/MEDIAZEN/Desktop/(통합)_UI Scenario_VR System_v3.0.8_20231025_LID_table.xlsx', read_only= True)
ws = wb['1. Prompt']
whole_list = []

for row in ws.rows:
    for cell in row:        
        whole_list.append(cell.value)
        
end = time.time() # 끝나는 시간
print(f"파일 읽는 시간 {end - start:.5f}초 나온다.") #파읽 읽기 시간 출력   
     
print(whole_list[6243])
        
wb.close()