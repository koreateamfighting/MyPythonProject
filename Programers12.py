before = [1,2,3,100,99,98]
after = []
result = 0

while True:
    for a in before:
    
        if (a>= 50 and a % 2 == 0):
            a = a / 2
            after.append(int(a))
        elif (a < 50 and a % 2 == 1):
            a = (a * 2) + 1
            after.append(int(a))
        else:
            after.append(int(a))
    print(f'{result}회차 before 리스트 결과 : {before}')
    print(f'{result}회차 after 리스트 결과 : {after}')
    
    if(before == after):
        print(f'{result}에 before는 {before}이고 , after는 {after}로써 같음. 프로그램 종료.')        
        break
    
    else:
        before.clear()
        before = after.copy()      
        # print(f'새로바뀐 before : {before}')
        result = result + 1
        
        after.clear()

print(result)
        
        


