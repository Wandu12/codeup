# 1099 : 수정 필요(9 출력 불가)

matrix = [[int(col) for col in input().split()] for row in range(10)]

i = 1
j = 1

while True: # (2,2)부터 시작하므로
        if matrix[i][j] == 0:
            matrix[i][j] == 9
        elif matrix[i][j] == 2:
            matrix[i][j] == 9
            break
        if (matrix[i][j+1] == 1 and matrix[i+1][j]) == 1 or (i == 9 and j == 9):
            break
        if matrix[i][j+1] != 1:
            j += 1
        elif matrix[i+1][j] != 1:
            i += 1

for m in matrix:        # matrix에서 안쪽 리스트를 꺼냄
    for o in m:    # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(o, end=' ')
    print()