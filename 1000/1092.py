# 1092
from math import gcd
n1, n2, n3 = input().split()
a = int(n1)
b = int(n2)
c = int(n3)
d = (int)(a*b/gcd(a, b))
print("%d"%(int(c*d)/gcd(c, d)))