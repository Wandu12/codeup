# algo43 : 이분탐색 응용
# N: 총 들어가는 곡 수, M: DVD 개수
# 1번, 5번 녹화하려면 무조건 1~5 사이도 녹음해야 함
n, m = list(map(int, input().split()))

# 라이브에서 부른 순서대로 주어지는 곡의 길이 리스트(분 단위)
a = list(map(int, input().split()))

# M개에 나눠 담는데 순서대로, 묶어서 담아야 함
def cnt(cap):  # capacity 체크용
    cnt = 1
    sum_cnt = 0
    for x in a:
        if sum_cnt + x > cap:  # 합+x > capacity보다 크면
            cnt += 1  # cnt+1
            sum_cnt = x  # 합을 x로 초기화
        else:
            sum_cnt += x
    return cnt            

start = min(a)  # lt
end = sum(a)  # rt
result = 0

while start <= end:
    mid = (start + end) // 2  # 하나의 DVD에 담길 노래 길이
    if cnt(mid) <= m:  # 주어진 DVD의 개수가 cnt(mid)보다 클 경우
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)        
