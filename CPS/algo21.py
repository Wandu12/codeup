# algo21
A = []
B = []
A = list(map(int, input().split()))  # 문자열 입력 -> int로 -> 리스트로 변환
B = list(map(int, input().split())) 

# 필요할 때 해당 위치에 선언
Ascore = [0 for i in range(10)]  # index out of range 방지
Bscore = [0 for i in range(10)]

for i in range(10):
    if A[i] > B[i]:
        Ascore[i] = 3
    elif A[i] < B[i]:
        Bscore[i] = 3
    elif A[i] == B[i]:
        Ascore[i] = 1
        Bscore[i] = 1

print("%d %d" % (sum(Ascore), sum(Bscore)))

# 왜 이 아래가 안 뜨지? 16 13까지만 뜸
if sum(Ascore) > sum(Ascore):
    print("A")
elif sum(Ascore) < sum(Bscore):
    print("B")
elif sum(Ascore) == sum(Bscore):
    if sum(Ascore) == 10 and sum(Bscore) == 10:
        print("D")
    else:
        Ascore.reverse()
        Bscore.reverse()
        if Ascore.index(3) > Bscore.index(3):
            print("A")
        else:
            print("B")
