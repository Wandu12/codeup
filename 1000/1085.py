# 1085
n1, n2, n3, n4 = input().split()
h = int(n1)
b = int(n2)
c = int(n3)
s = int(n4)
dataSize = (((h*b*c*s)/8)/1024)/1024
print("%.1f MB" % dataSize)
