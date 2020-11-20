# 1087
n1 = input()
n = int(n1)
numSum = 0

for i in range(1, n+1):
    numSum += i
    if numSum >= n :
        break    
print(numSum)