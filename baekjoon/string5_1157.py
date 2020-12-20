# string5_1157
import string
text = input()
text = text.lower()  # 대문자로 변경
alpha = list(string.ascii_uppercase)
count = [0 for i in range(0, 26)]

# alpha에 있는(a~z)가 주어진 문자열에 몇 개 있는지 검색
for i in range(26) :
    count[i] = text.count(alpha[i])

idx = [i for i,x in enumerate(count) if x==max(count)]

if len(idx) > 1:
    print("?")
else :
    print(alpha.index(max(count)))