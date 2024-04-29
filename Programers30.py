days = ["FRI","SAT","SUN","MON","TUE","WED","THU",]

case1 =  list(range(1,31))
case2 =  list(range(1,32))
case3 =  list(range(1,30))

month_day = []
a = 2
b = 12
ab = str(a)+str(b)
answer = ""

for i in range(1,13):
    if i in [4,6,9,11]:
        for j in case1:
            month_day.append(f'{i}{j}')
        
    elif i in [1,3,5,7,8,10,12]:
        for j in case2:
            month_day.append(f'{i}{j}')                 
    else:
        for j in case3:
            month_day.append(f'{i}{j}')
        

print("-----------------------------------------------------------------")
print(month_day)
print("-----------------------------------------------------------------")

if (month_day.index(ab) % 7 == 0):
    answer = days[0]
elif(month_day.index(ab) % 7 == 1):       
    answer = days[1]
elif(month_day.index(ab) % 7 == 2):       
    answer = days[2]
elif(month_day.index(ab) % 7 == 3):       
    answer = days[3]
elif(month_day.index(ab) % 7 == 4):       
    answer = days[4]
elif(month_day.index(ab) % 7 == 5):       
    answer = days[5]    
else:      
    answer = days[6]


print(ab)
print(answer)




