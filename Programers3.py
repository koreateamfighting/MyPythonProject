number = [-3,-2,-1,0,1,2,3]
result = 0



for i in range(0, len(number)):   
    
    for j in range(1,len(number)):
        
        for k in range(2,len(number)):
                      
            
             if(i == k or j == k or i== j ):
                 
                 continue        
             if(number[i] + number[j] + number[k] == 0):
                 result += 1                 
                 print(f'이때 나가는것( 값 ) {number[i]} {number[j]} {number[k]}')
           
           
print(int(result/3))
                


                
