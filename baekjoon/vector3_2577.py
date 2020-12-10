# vector3_2577
A = int(input())
B = int(input())
C = int(input())
mul = str(A*B*C)
mulList = list(mul)  # 문자열을 글자마다 끊어 리스트에 저장
cnt = len(mulList)
mulList = list(map(int, mulList))  # 문자열 배열을 int 배열로 변환
numCount = [0 for i in range(10)]

for i in range(0, cnt): # range를 빼서 계속 안 됐음.
    if mulList[i] == 0:
        numCount[0] += 1
    elif mulList[i] == 1:
        numCount[1] += 1
    elif mulList[i] == 2:
        numCount[2] += 1
    elif mulList[i] == 3:
        numCount[3] += 1
    elif mulList[i] == 4:
        numCount[4] += 1
    elif mulList[i] == 5:
        numCount[5] += 1
    elif mulList[i] == 6:
        numCount[6] += 1
    elif mulList[i] == 7:
        numCount[7] += 1
    elif mulList[i] == 8:
        numCount[8] += 1
    elif mulList[i] == 9:
        numCount[9] += 1

for i in range(0, 10):
    print(numCount[i])