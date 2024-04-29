str_list = ["l"]
answer = []


for i in range(0,len(str_list)):
    
    if(str_list[i] == "l" or str_list[i] == "r"):
        if(str_list[i] == "l"):
            for j in range (0,i) :
                print(j)
                answer.append(str_list[j])
            break
        else:
            for j in range(i+1, len(str_list)):
                answer.append(str_list[j])
            break
        
    else:
        answer = []
    
    
print(answer)
    
