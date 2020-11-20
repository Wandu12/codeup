# 1084
n1, n2, n3 = input().split()
r = int(n1)
g = int(n2)
b = int(n3)
numSum = 0

for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(("%d %d %d")%(i, j, k))
            numSum += 1
print(numSum)            