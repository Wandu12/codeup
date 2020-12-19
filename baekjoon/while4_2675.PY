# while4_2675 : 수정 필요

T = int(input())  # 테스트 횟수

for i in range(T):
    R, S = input().split() 
    R = int(R)  # 반복 횟수
    string = ""
    # S = list(S)  # 반복할 문자열
    for i in S:
        string += R * i
    print(string)   


