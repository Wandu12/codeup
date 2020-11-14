# 1080
a = input()
n = int(a)
numSum = 0

for i in range(1, n):
    numSum += i
    if(numSum >= n) :
        print(i)
        break