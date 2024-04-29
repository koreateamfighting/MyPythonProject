num_list = [4, 2, 6, 1, 7, 6]

groupA = []
groupB = []
answer = 0

for i in range(0,len(num_list)):
    if i % 2 == 0:
        groupA.append(num_list[i])
    else:
        groupB.append(num_list[i])
        
        
if (groupA>groupB):
    answer =  sum(groupA)
elif (groupA<groupB):
    answer = sum(groupB)
else:
    answer = sum(groupB)
    
    
print(sum(groupA))
print(sum(groupB))
print(answer)