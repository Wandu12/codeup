# 11
n = int(input())
sum = 0
check = 9
digit = 1

while(n > check):
    sum += check*digit
    n = n - check
    check = check * 10
    digit += 1

sum += n * digit
print(sum)
