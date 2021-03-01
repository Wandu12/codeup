# algo42: 이분검색
# 이분 탐색: 검색할 범위를 반으로 줄여가며 탐색

# N개의 숫자와 그 중 하나의 수인 M이 입력으로 주어짐
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

# N개의 숫자를 오름차순으로 정렬
a = sorted(list(a))

# 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하기
start = 0
end = len(a) - 1

while start <= end:
    mid = (start + end) // 2
    if m == a[mid]:
        print(mid+1)
        break
    elif m > a[mid]:
        start = mid + 1
    else:
        end = mid - 1