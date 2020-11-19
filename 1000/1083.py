# 1083
n = input()
n1 = int(n)
for i in range(1, n1+1):
    if(i%3 == 0): 
        print("X", end=" ")
    else:
        print(i, end=" ")