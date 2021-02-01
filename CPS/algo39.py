# algo39
N = int(input())
array1 = list(map(int, input().split()))
M = int(input())
array2 = list(map(int, input().split()))
array3 = [0 for i in range(N+M+1)]

array1.insert(0, 0)
array2.insert(0, 0)
p1 = 1
p2 = 1
p3 = 1
while p1 <= N and p2 <= M:
    if array1[p1] < array2[p2]:
        array3[p3] = array1[p1]
        p3 += 1
        p1 += 1
    else:
        array3[p3] = array2[p2]
        p3 += 1
        p2 += 1

print(p1, p2, p3)

while p1 <= N:
    array3[p3] = array1[p1]
    p3 += 1
    p1 += 1    
while p2 <= M:
    array3[p3] = array2[p2]
    p3 += 1
    p2 += 1
    print(p1, p2, p3)

array3.remove(0) 

print(array3)
