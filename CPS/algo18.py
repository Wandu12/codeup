# algo18
N, M = map(int, input().split())
a = []
max = -1
now = 0

a.extend(input().split())  # 이미 여기서 나뉘어지므로 for문 돌릴 필요 없음
list_a = list(map(int, a))

for j in range(0, N):
    if(list_a[j] >= M):
        now += 1
        if(max <= now):  # 방향 잘 볼 것
            max = now
    else:
        now = 0

print(max)