# algo31
import re
a = input()
chemi = re.findall('\d+', a)  # 숫자 묶음 추출(C2H4 -> 2, 4)
ans = 0

if len(chemi) == 2:  # C, H 둘 다 있으면
    ans = int(chemi[0])*12 + int(chemi[1]*1)
elif len(chemi) == 1:
    ans = (12 + int(chemi[0]*1)) if a.find('CH') == -1 else (int(chemi[0])*12 + 1) 
        # CH이면 C가 1, 아니면 H가 1
elif len(chemi) == 0:
    ans = 13

print(ans)