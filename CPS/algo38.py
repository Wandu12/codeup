# algo38
N = int(input())
inv_seq = list(map(int, input().split()))  # 주어지는 수열(inversion sequence)
seq = [0 for i in range(N+1)] # 원래의 수열(출력해야 할 수열)

# inversion sequence 
# 4 8 6 2 5 1 3 7일 때 0 0 1 3 2 5 4 1 
# 1~8 순서대로 정렬하면 5 3 4 0 2 1 1 0
inv_seq.insert(0, 0)  # 1부터 시작
pos = 0
print(inv_seq)

i = N
for i in range(i, 0, -1):  # N부터 1까지 1씩 감소
    pos = i
    j = 1

    # for (int j = 1; j <= inv_seq[i]; j++) 대신 while문
    while j <= inv_seq[i]:
        seq[pos] = seq[pos+1]
        pos += 1
        j += 1
    seq[pos] = i

seq.remove(0)
for i in seq:
    print(i, end=" ")
