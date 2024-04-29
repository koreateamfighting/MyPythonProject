friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
give_list = []
receive_list = []
score_list = []
gift_result_table = [[0 for col in range(len(friends))] for row in range(len(friends))]
givecount = 0
receivecount = 0
friendsScore = [0 for col in range(len(friends))]
answer = 0

# 1. <선물 주는 자 , 선물 받는 자 리스트 만들기 >
for gift in gifts:
   split = gift.split(' ')
   give_list.append(split[0])
   receive_list.append(split[1])

# print(give_list)
# print(receive_list)

# 2. 선물 결과 2차원 테이블 만들기
for i in range(0, len(give_list)):
    for f1 in friends:        
        for f2 in friends:            
            
            if(give_list[i] == f1 and receive_list[i] == f2):                 
                 gift_result_table[friends.index(f1)][friends.index(f2)] += 1
                 
# print(gift_result_table)

# 3. <준 선물 , 받은 선물 , 선물 지수 리스트>
for friend in friends: 
    for gift in gifts:
        if(gift.find(friend)==0):
            givecount += 1
        elif(gift.find(friend)>0):
            receivecount += 1
    score_list.append([givecount,receivecount,givecount-receivecount])
    givecount = 0; receivecount = 0
    
# print(score_list)

# 4. gift_result_table에서 가장 선물 많이 받을 사람 찾기


for i in range(0, len(gift_result_table)):
    for j in range(i,len(gift_result_table)):
        
        if(i==j):            
            continue
        else:
            print(f'{i} : {j}')    
            if(gift_result_table[i][j] > gift_result_table[j][i]):
                friendsScore[i] += 1
                print(f'{friends[i]}가 선물 하나 더 받습니다.')
            elif(gift_result_table[i][j] < gift_result_table[j][i]):
                friendsScore[j] += 1
                print(f'{friends[j]}가 선물 하나 더 받습니다.')
            elif(gift_result_table[i][j] == gift_result_table[j][i] or (gift_result_table[i][j] == 0 and gift_result_table[j][i] == 0)):
                if(score_list[i][-1] > score_list[j][-1]):
                    friendsScore[i] += 1
                    print(f'{friends[i]}가 선물 하나 더 받습니다.')
                elif(score_list[i][-1] == score_list[j][-1]):
                    continue
                else:
                    friendsScore[j] += 1    
                    print(f'{friends[j]}가 선물 하나 더 받습니다.')

                        
                
print(friendsScore)
print(max(friendsScore))
            





    
            
    
   
    





