names = ["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]
result = []


#5 ≤ names의 길이 ≤ 30
#1 ≤ names의 원소의 길이 ≤ 10
#names의 원소는 영어 알파벳 소문자로만 이루어져 있습니다.
def solution(names):
    answer = []
for i,d in enumerate(names):
    if i % 5 == 0:
        result.append(d)
        
print(result)