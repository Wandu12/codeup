# vector2_2562
arr = []
for i in range(9):
    arr.append(int(input()))

print(max(arr))
print(arr.index(max(arr))+1) # 최댓값의 인덱스는 index() 활용