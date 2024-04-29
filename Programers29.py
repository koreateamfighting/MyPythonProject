cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
result = 'Yes'



# print(cards1)
# cards1.remove("i")
# print(cards1)


for i, g in enumerate(goal):
    
    if g == cards1[0]:
        cards1.remove(g)
        if not cards1 :
            cards1.append(0)
    elif g == cards2[0]:
        cards2.remove(g)
        if not cards2 :
            cards2.append(0)
            
            
    else:
        result = 'No'
        break
    
print(result)
    
        
    
    
