number = [-2, 3, 0, 2, -5]
result = 0


# a = 0
for first in range(0, len(number)-2):
    
    for second in range(first+1,len(number)-1):
        
        for third in range(second+1,len(number)):
        
            # print(f'first:{number[first]}, second: {number[second]},third:{number[third]}')
            if(number[first]+number[second]+number[third] == 0):
                    result = result + 1
                    
print(result)
                    