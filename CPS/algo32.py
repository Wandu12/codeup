# algo32
n = int(input())
sort = list(map(int, input().split()))
temp = 0

for i in range(0, len(sort)-1):
    minIndex = i
    for j in range(i+1, len(sort)):
        if sort[j] < sort[minIndex]:  # 가장 작은 값의 인덱스보다 값이 작으면
            minIndex = j
    temp = sort[minIndex] # 가장 작은 값의 인덱스를 이용해 접근
    sort[minIndex] = sort[i]
    sort[i] = temp

print(sort)
