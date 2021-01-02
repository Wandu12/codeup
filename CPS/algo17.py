# algo17
N = int(input())
a = []

for i in range(N):
    a.extend(input().split())

list_n = list(map(int, a))

def func(n):
    sum = 0
    for i in range(1, int(n)+1):
        sum += i
    return sum

for j in range(0, N*2, 2):
    if(func(list_n[j]) == list_n[j+1]):
        print("YES")
    else:
        print("NO")    
