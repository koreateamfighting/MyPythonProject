strings = ["abce", "abcd", "cdx"]
n = 2
answer = [] # ["abcd", "abce", "cdx"]


for i in range(0,len(strings)):
    #print(strings[i])
    if (i == 0):
        answer.append(strings[i])
    else:
        
        answer.append(strings[i])
        temp = ''
        before_n = str(strings[i-1])[n] 
        after_n =  str(strings[i])[n]       
        if(before_n < after_n):
            continue
        elif(before_n > after_n):
            temp = strings[i-1]
            strings[i-1] = strings[i]
            strings[i] = temp
        elif(before_n == after_n):
            if(strings[i-1] > strings[i]):
                temp = strings[i-1]
                strings[i-1] = strings[i]
                strings[i] = temp
                
            
answer = strings            
print(strings)
        
    
    
    
