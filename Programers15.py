sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
answer = 0
left = []
right = []

for size in sizes:
    
    if (size[0] < size[1]):
        temp = 0
        temp = size[0]
        size[0] = size[1]
        size[1] = temp
    left.append(size[0])
    right.append(size[1])


answer = max(left) * max(right)

print(answer)           
            
