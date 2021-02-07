# algo02
n1, n2 = input().split()
a = int(n1)
b = int(n2)
numSum = 0

for i in range(a, b+1):
    numSum += i
    if(i == b): 
        print("%d"%i, end="")
    else:
        print("%d + "%i, end="")
print(" = %d"%numSum)