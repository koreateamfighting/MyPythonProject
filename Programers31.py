nums = [3,3,3,2,2,2]	
answer = 0
numset = {}
n = len(nums)//2
numset = set(nums)


if (n==len(numset)):
    answer = n
elif (n > len(numset)):
    answer = len(numset)
else:
    answer = n
    
print(answer)