# 1082
a = input()
n = int(a, 16)
for i in range(1, 16):
    multi = n*i
    print("%X*%X=%X" %(n, i, multi))
