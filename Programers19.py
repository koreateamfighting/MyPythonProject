food = [1,7,1,2]
answer = ''


for ii,f in enumerate(food[1:len(food)]):
    if(f==1):
        answer = answer
    elif(f % 2 == 0):
        n = int(f/2)
        print(f'{f}의 반복횟수는 {n}이고 인덱스는 {ii+1}이다')
        for i in range(0,n):
            answer = answer + str(ii+1)
            
        
    else:
        n = int(f/2)
        print(f'{f}의 반복횟수는 {n}이고, 인덱스는 {ii+1}이다')
        for i in range(0,n):
            answer = answer + str(ii+1)

answer = answer + '0' + answer[::-1]

print(answer)

    