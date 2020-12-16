# string2_11720
N = int(input())
mul = input()
mulList = list(mul)   # 문자열을 글자마다 끊어 리스트에 저장
mulList = list(map(int, mulList))  # 문자열 배열을 int 배열로 변환
sum = 0
for i in mulList:
    sum += i

print(sum)