# vector5_1546
n = int(input())
arr = []
arr = list(map(int, input().split()))  # 입력받은 수들을 리스트에 저장
maxArr = max(arr)

for i in range(0, len(arr)):
    arr[i] = (arr[i]/maxArr)*100

print(sum(arr)/n)