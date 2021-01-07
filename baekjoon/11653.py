# 11653
N = int(input())
result = []
while N != 1:
    for i in range(2, N + 1):
        if N % i == 0:
            result.append(i)
            N = N // i
            break

for j in result:
    print(j)
