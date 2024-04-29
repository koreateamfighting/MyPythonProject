
s = "foobar"
list_s = []
target_index = 0 
answer = []
# [-1-1-1222]


# print(s.count('a'))

for ii,ss in enumerate(s):
    if(not list_s.__contains__(ss)):
        answer.append(-1)
        list_s.append(ss)
    else:
        for i,a in enumerate(list_s):
            if(a == ss):
                target_index = i
        list_s.append(ss)
        answer.append(i-target_index+1)
        
print(answer)
        

         
         

         
         
