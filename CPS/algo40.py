# algo40
# 방법1(파이썬)
n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

print(sorted(set.intersection(a, b)))

# 방법2
a = sorted(list(a))
b = sorted(list(b))
c = [0 for i in range(max(n, m)+1)]

p1 = 0; p2 = 0; p3 = 0
while p1 < n and p2 < m:    # p1<n이고 p2<m인 동안
    if a[p1] == b[p2]:      # if a의 p1번째와 b의 p2번째 요소가 같으면
        c[p3] = a[p1]       # c의 p3번째에 a의 p1번째 요소 넣기
        p1 += 1; p3 += 1    # p1, p3을 증가시키고
        p2 += 1             # p2 증가
    elif a[p1] < b[p2]:     # else a의 p1번째보다 b의 p2번째 요소가 크면
        p1 += 1             # p1 증가(a랑 b 비교하는데 b가 더 크면 a 다음 인덱스 값과 비교)
    else: p2 += 1           # 아니면 p2 증가(a랑 b 비교하는데 a가 더 크면 b의 다음 인덱스 값과 비교)

# 0 제거
for i in c:
    if i == 0:
        c.remove(0)

for i in range(0, len(c)):
    print(c[i], end=" ")

