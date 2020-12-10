# vector4_3052
arr = []
for i in range(10):
    arr.append(int(input())%42)

mySet = set(arr) # 집합 자료형 set으로 중복 제거
print(len(mySet))

