# 1098 : 오류 수정(격자판 세로, 가로 입력. 가로, 세로 입력X)
h, w = map(int, input().split()) # 격차판 세로, 가로 입력 h, w
n = int(input()) # 놓을 막대의 개수 n

# w*h 배열 만들고 0으로 초기화
matrix = [[0 for col in range(w)] for row in range(h)] 
    # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    #일차원은 wList = [0 for i in range(w)]

for i in range(0, n):
    l, d, x, y = map(int, input().split()) 
        # 막대길이 l, 방향 d = 0이 가로 1이 세로, 좌표(x,y)
    if d==1:
        for j in range(l): #(0, l)에서 변경
            matrix[x-1+j][y-1] = 1
    if d==0:
        for k in range(l):
            matrix[x-1][y+k-1] = 1

for m in matrix:        # a에서 안쪽 리스트를 꺼냄
    for o in m:    # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(o, end=' ')
    print()
