todo_list = ["problemsolving", "practiceguitar", "swim", "studygraph"]
finished = [True, False, True, False]
answer = []



for i in range(0,len(finished)):
    if finished[i] == False:
        answer.append(todo_list[i])
        
        
print(answer)
        



