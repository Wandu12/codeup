# 1093.py
a = int(input())
stuCall = input().split()
stuCnt = [0 for _ in range(24)]

for i in range(0, a):
    for j in range(0, 24):
        if int(stuCall[i]) == j:
            stuCnt[j] += 1

for j in range(1, 24):
    print(stuCnt[j], end=" ")
print("\n")
