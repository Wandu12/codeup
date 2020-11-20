# 1086
n1, n2, n3 = input().split()
w = int(n1)
h = int(n2)
b = int(n3)
dataSize = (((w*h*b)/8)/1024)/1024
print("%.2f MB"%dataSize)