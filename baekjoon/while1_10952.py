# 10952_while 
n1, n2 = map(int, input().split())
arr = []
while n1 != 0 and n2 != 0:
    arr.append(n1+n2)
    n1, n2 = map(int, input().split())

for i in range(0, len(arr)):
    print(arr[i])
