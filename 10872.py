# 10872
def facto(num):
    if num == 0:
        return 1
    return num*facto(num-1)

n = int(input())
print(facto(n))
