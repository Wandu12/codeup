# vector7_4344
c = int(input())
for i in range(c):
    n = list(map(int, input().split())
    avg = sum(n[1:]) / n[0]
    cnt = 0

    for j in n[1:]:
        if j > avg : 
            cnt += 1
            
    print(str("%.3f" %round((cnt/n[0])*100, 3))+"%")
