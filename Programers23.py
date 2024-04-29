park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]
result = []  # [2,1]
new_park = []
new_routes = []
current_point = [] #[0,0]

#공원 좌표 리스트 형식으로 재설정
for p in park:   
    new_park.append(list(p))     
    
print(f"공원 좌표(new_park) : {new_park}")


h = len(new_park)
w = len(new_park[0])

#방향 지시 리스트 형식으로 재설정
for r in routes:
    temp = r.split(" ")
    new_routes.append(temp)
print(f"방향 지시 리스트(new_routes) : {new_routes}")

#스타팅 포인트 리스트형식으로 설정
for  i in range(0, len(new_park)):
    for j in range(0, len(new_park[0])):
        if(new_park[i][j] == 'S'):
            current_point.append(i)
            current_point.append(j)
            break

print(f"현재 위치(current_point) : {current_point}")



print("============================좌표 분기 흐름(i[0],i[1])===========================")
for i in new_routes:
    pass_available = True
    
    print(i[0], i[1])    
    if(i[0]=='E'):
        
        for n in range(current_point[1],int(i[1])+1):
            if(current_point[1]+int(i[1])+1>w):
                print("영역을 벗어남")
                pass_available = False
                break
            if(new_park[current_point[0]][n] == 'X'):
                print("장애물 발견")
                pass_available = False
                break
        
    elif(i[0]=='W'):
        
        for n in range(int(i[1]),current_point[1],-1):
            if(current_point[1]-int(i[1])<0):
                print("영역을 벗어남")
                pass_available = False
                break
            if(new_park[current_point[0]][n] == 'X'):
                print("장애물 발견")
                pass_available = False
                break
        
    elif(i[0]=='S'):        
        for n in range(current_point[0],int(i[1])+1):
            if(current_point[0]+int(i[1])+1>h):
                print("영역을 벗어남")
                pass_available = False
                break
            if(new_park[n][current_point[1]] == 'X'):
                print("장애물 발견")
                pass_available = False
                break
            
        
    else: #N
        
        for n in range(int(i[1]),current_point[0],-1):
            if(current_point[0]-int(i[1])<0):
                print("영역을 벗어남")
                pass_available = False
                break
            if(new_park[n][current_point[1]] == 'X'):
                print("장애물 발견")
                pass_available = False
                break
        
        
    if(pass_available==True):
        if(i[0]=='E'):
            current_point[1] += int(i[1])
        elif(i[0]=='W'):
            current_point[1] -= int(i[1])
        elif(i[0]=='S'):
            current_point[0] += int(i[1])
        else:
            current_point[0] -= int(i[1]) 
print(f"최종 위치(current_point): {current_point}")


