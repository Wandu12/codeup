# 1161
a, b = input().split(' ')
if(int(a) % 2 == 1) :
    if(int(b) % 2 == 1) :
        print("홀수+홀수=짝수")
    else:
        print("홀수+짝수=홀수")
else:
    if(int(b) % 2 == 1) :
        print("짝수+홀수=홀수")
    else:
        print("짝수+짝수=짝수")
