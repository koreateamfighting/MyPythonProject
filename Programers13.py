num_list = [12, 4, 15, 1, 14]
answer = []
cnt = 0


for num in num_list:
    print(f'타겟 num : {num}')
    while True:
        if(num % 2 == 0):
            num = int(num / 2)
            cnt = cnt + 1
        elif(num == 1):
            break
        else:
            num = int((num-1)/2)
            cnt = cnt + 1
            
        
    print(f'너덜너덜해진 숫자 {num}')
    
print(cnt)

        
        

    
    