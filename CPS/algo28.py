# algo28
import math

N = int(input())
facto = str(math.factorial(N))  # N의 팩토리얼 구하는 함수 이용
reversedFacto = list(map(int, list(facto[::-1])))
count = 0
i = 0

while reversedFacto[i] == 0:
    count += 1
    i += 1

print(count)
