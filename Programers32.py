answers = [1,3,2,4,2]

mrA = []
mrB = []
mrC = []
cnt = 1
cnt2 = 3
cntA = 0
cntB = 0
cntC = 0
for i in range(0,len(answers)):
    if(i % 5 == 0):
        mrA.append(1)
    elif(i % 5 == 1):
        mrA.append(2)
    elif(i % 5 == 2):
        mrA.append(3)
    elif(i % 5 == 3):
        mrA.append(4)
    else:
        mrA.append(5)
        


for i in range(0,len(answers)):
    if(i % 2 == 0):
        mrB.append(2)
    else:
        mrB.append(cnt)
        cnt = cnt+1
        if(cnt == 2):
            cnt = cnt + 1
        if(cnt == 5):
            cnt = 1
            
            
for i in range(0,len(answers)):
    if(i % 2 == 0):
        mrC.append(cnt2)
    else:
        mrC.append(cnt2)
        cnt2 += 1
        if(cnt2 == 4):
            cnt2 = 1
        if(cnt2 == 3):
            cnt2 = 4
        if(cnt2 == 6):
            cnt2 = 3
# print(mrA)        
# print(mrB)        
# print(mrC)


for i in range(0,len(answers)):
    if(mrA[i] == answers[i]):
        cntA += 1
    
    if(mrB[i] == answers[i]):
        cntB += 1
    if(mrC[i] == answers[i]):
        cntC += 1

result = [cntA,cntB,cntC]
print(result)
    


        
    
    