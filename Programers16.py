lowerAlphabet = 'abcdefghijklmnopqrstuvwxyz'
upperAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
space = ' '
result = ''

s = "Z"
n = 1



for ss in s:
    if(lowerAlphabet.__contains__(ss)):
        if(lowerAlphabet.index(ss)+ n > len(lowerAlphabet)-1):
            temp = len(lowerAlphabet)-lowerAlphabet.index(ss) - 1
            print(temp)
            ss = lowerAlphabet[n-temp-1]
            
        else:
            ss = lowerAlphabet[lowerAlphabet.index(ss)+n]
    elif(upperAlphabet.__contains__(ss)):
        if(upperAlphabet.index(ss)+n > len(upperAlphabet)-1):
            temp = len(upperAlphabet)-upperAlphabet.index(ss) -1   
            ss = upperAlphabet[n-temp-1]
            
        else:
            ss = upperAlphabet[upperAlphabet.index(ss)+n]
            
    else:
        ss = ' '
    result = result + ss
        
        
print(result)
        

    
