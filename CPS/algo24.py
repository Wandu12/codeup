# algo24
N = int(input())
arr = list(map(int, input().split()))
jumper = [0 for i in range(N)]  # 차를 저장하는 리스트
jollyJumper = [i for i in range(0, N)]  # jolly Jumper인지 여부를 확인하기 위한 리스트

for i in range(1, N):
    jumper[i-1] = abs(arr[i]-arr[i-1])

jumper.sort()

if jumper == jollyJumper:
    print("YES")
else:
    print("NO")



