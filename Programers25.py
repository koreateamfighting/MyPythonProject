numbers = [2,1,3,4,1]
result = [] #  [2,3,4,5,6,7]



for i in range(0, len(numbers)):
    for j in range(0, len(numbers)):
        if (i == j):
            continue
        else:
            result.append(numbers[i]+numbers[j])


result.sort()

answer = list(set(result))
answer.sort()
print(answer)