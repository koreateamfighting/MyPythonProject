#일반적인 100만건 데이터 생성 시간 측정

import math
import time

start = time.time()

million_data = {}
million_data["1"] = '홍길동'
for i in range(1,1000001):
    million_data[f"{i}"] = f'값:{i}'
print(million_data)
end = time.time()


print(f"{end - start:.5f}초 나온다.")
