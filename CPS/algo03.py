# algo03
n1 = input()
n = int(n1)
properDivisor = 0
for i in range(1, n):
    if(n%i == 0):
        properDivisor += i
        if(i == 1):
            print("%d "%i, end="")
        else:
            print("+ %d "%i, end="")
print("= %d"%properDivisor)    