# 1098
h,w = map(int,input().split())
n = int(input())
array = [[0 for col in range(w)] for row in range(h)]

for i in range(n):
    l,d,x,y = map(int,input().split())
    if d == 1 :
        for q in range(l) :
            array[x-1+q][y-1] = 1
    if d == 0 :
        for w in range(l) :
            array[x-1][y+w-1] = 1

for z in array :
    for k in z :
        print(k, end=" ")
    print(")
