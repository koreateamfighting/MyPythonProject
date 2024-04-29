a = 3
b = 1
n = 20
answer = 0


while (n>=a):
    remain_bottle = n % a
    n = (n//a) * b
    answer += n
    n += remain_bottle
print(answer)