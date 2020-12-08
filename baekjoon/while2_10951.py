# while2_10951 : 각 테스트 케이스마다 출력한다는 부분을 놓침. 
# Python 예외처리: try-except 사용(자바의 try-catch-finally와 유사)
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
