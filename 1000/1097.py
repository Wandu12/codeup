# 1097 : 십자 뒤집기
badukBoard = [] # 생성 먼저

for i in range(0, 19): # 0도 생략 가능
    badukBoard.append([])
    for j in range(0, 19):
        badukBoard[i].append(0)

for i in range(0, 19):
    badukBoard[i] = list(map(int, input().split()))

n = int(input())

for i in range(0, n):
    x, y = map(int, input().split())

    for j in range(0, 19):
            if badukBoard[x-1][j] == 0:
                badukBoard[x-1][j] = 1
            else:
                badukBoard[x-1][j] = 0   
                 
            if badukBoard[j][y-1] == 0:
                badukBoard[j][y-1] = 1
            else:
                badukBoard[j][y-1] = 0

for i in range(0, 19):
    for j in range(0, 19):
        print(badukBoard[i][j], end=' ')
    print()
