k = 4
score= [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
toplist = []
result= [] #[0, 0, 0, 0, 20, 40, 70, 70, 150, 300] 



for i in range(0, len(score)):
    if (i<k):
        toplist.append(score[i])
        toplist.sort(reverse=True)
        result.append(toplist[i])
        print(f'toplist 현재 들어간 상황 1 : {toplist}')
        
    else:
        if(toplist[i-1] < score[i]): # 0 20
            toplist.remove()
            toplist.append(score[i])            
            toplist.sort(reverse=True)
            result.append(toplist[i])
            print(f'toplist 현재 들어간 상황 2 : {toplist}')
        else:
            toplist.sort(reverse=True)
            result.append(result[i-1])
            print(f'toplist 현재 들어간 상황 3 : {toplist}')
            
print(result)

            
        
        
   

    
    

