# 1085
x, y, w, h = list(map(int, input().split()))
print(min(h-y, w-x, x, y))
