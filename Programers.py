t = '3141592'
p = '271'
answer = 0
splits = []

#p보다 작거나 같은 수를 체크.

for i,v in enumerate(t[0:len(t)-len(p)+1]):
    
    splits.append(t[i:i+len(p)])
    
    



for split in splits:
    if(int(split) <= int(p)):
        answer += 1
        
print(answer)
