# 2869
A, B, V = map(int,input().split())
k = (V-B)/(A-B) # (V-A)/(A-B)하면 남은높이/그날 올라간 길이 = 달팽이가 오르는 데 필요한 날짜 수

print(int(k) if k == int(k) else int(k)+1)  # 날짜는 자연수이므로 나눠 떨어지지 않으면 +1