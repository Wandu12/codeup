# 1096 19*19
badukBoard = [[0]*19 for i in range(19)]

num = int(input())
for i in range(num):
    b, c = map(int, input().split())
    badukBoard[b-1][c-1] = 1

for i in range(19):    
    for j in range(19):
        print(badukBoard[i][j], end=' ')
    print()
