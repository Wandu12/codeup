# algo37
# VScode 변수이름 한번에 바꾸는 단축키: 심볼 찍고 ctrl+d
S, N = list(map(int, input().split()))  # 캐시 크기와 작업의 개수 정하기
t_list = list(map(int, input().split()))  # 작업번호 리스트
cache = [0 for i in range(S)]  # 캐시메모리

for i in t_list:
    if i in cache:  # Cache Hit
        # cache를 뒤로 한 칸씩 밀고 i는 cache[0]에 넣기
        cache.remove(i)
        cache.insert(0, i)
    else:  # Cache Miss
        # i를 cache[0]에 넣고 cache[1]부터 한칸씩 뒤로 밀기(맨 앞에 추가하고 맨 뒤를 삭제)
        cache.pop()
        cache.insert(0, i)

for i in cache:  # 캐시메모리 상태 출력
    print(i, end=" ")