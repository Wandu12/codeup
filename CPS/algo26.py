# algo26
N = int(input())
skill = list(map(int, input().split())) # 각 선수들의 평소 실력을 담은 리스트

print("1", end=" ")
for i in range(1, N):
    ranking = 1  # 최선의 등수
    for j in range(i-1, -1, -1):   # for(j = i-1; j >= 0; j--)
        if skill[j] >= skill[i] :
            ranking += 1
    print(ranking, end=" ")