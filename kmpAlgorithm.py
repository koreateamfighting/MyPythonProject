#KMP 검색 알고리즘 소스 코드 예제
def kmp(all_string , pattern):
    table = [0 for _ in range(len(pattern))]  # 패턴의 길이만큼 테이블에 0 값 추가 (초기화)    
    i = 0
    for j in range(1,len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]
            
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = 1
            
    result = []
    i = 0
    for j in range(len(all_string)):
        while i > 0 and pattern[i] != all_string[j]:
            i = table[i-1]
        
        if pattern[i] == all_string[j]:
            i += 1
            if i == len(pattern):
                result.append(j- i+1)
                i = table[i-1]
        
    return result

print(kmp('xabxxbaxbaxbaxbaxabxbaxbabx','abx'))
print(kmp('abababab','abab'))