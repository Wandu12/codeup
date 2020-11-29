# 1083: 33은 XX로 나오게 수정
n = int(input())
for i in range(1, n+1):
    a = int(i/10)
    b = i%10
    if(a == 3 or a == 6 or a == 9): 
        if(b == 3 or b == 6 or b == 9):
            print("XX", end=" ")
            continue
        print("X", end=" ")
    elif(b == 3 or b == 6 or b == 9):
        print("X", end=" ")    
    else:
        print(i, end=" ")
