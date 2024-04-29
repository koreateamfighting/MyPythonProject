s = "123"

result = []
temp_string = ''
answer = 0

dic = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
dic2 = {v:k for k,v in dic.items()}

for i,ss in enumerate(s):
    if(dic.keys().__contains__(ss)):
        result.append(ss)
    
    else:
        temp_string = temp_string + ss
        if(dic2.keys().__contains__(temp_string)):
            result.append(dic2.get(temp_string))
            temp_string = ''
            
answer = int(''.join(result))

print(answer)
        
                
