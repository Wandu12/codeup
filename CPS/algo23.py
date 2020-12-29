# algo23 : incLen 리스트 없이 풀 수 있음
N = int(input())
arr = list(map(int, input().split()))
incLen = [0 for i in range(N)]  # 값이 같거나 증가하는 부분을 저장하는 수열
inc = 0  

for i in range(1, N):
    if arr[i] == arr[i-1] or arr[i] > arr[i-1]:
        incLen[inc] += 1  # 값이 같거나 증가하면 증가하는 부분 수열의 길이 +1
    else:
        inc += 1  # 값이 같거나 증가하지 않으면 최대길이 증가수열을 끊음

print(max(incLen)+1)

