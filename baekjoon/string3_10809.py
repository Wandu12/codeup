# string3_10809
import string
mul = input()
alpha = list(string.ascii_lowercase)

for i in alpha:
    print(mul.find(i), end=" ") # 원하는 문자가 몇 번째에 있는지 찾는 find()