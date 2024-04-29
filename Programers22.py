players = ["mumu", "soe", "poe", "kai", "mine"]
calling = ["kai", "kai", "mine", "mine"]
answer = []




for call in calling:
    n = players.index(call)
    players[n]         
    players[n-1] 
    
    temp = players[n]    
    players[n] = players[n-1]    
    players[n-1] = temp
    
answer = players
print(answer)
    

