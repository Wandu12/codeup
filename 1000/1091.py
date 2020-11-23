# 1091
n1, n2, n3, n4 = input().split()
a = int(n1)
m = int(n2)
d = int(n3)
n = int(n4)
result = a
for i in range(1, n):
    result = (result * m) + d

print(result)