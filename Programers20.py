array = [1,5,2,6,3,7,4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []



for cmd in commands:
    temp = []
    temp = array[cmd[0]-1:cmd[1]]
    temp.sort()
    answer.append(temp[cmd[2]-1])
    
print(answer)
