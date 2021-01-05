# algo33
n = int(input())
stuList = sorted(set(map(int, input().split())), reverse=True)

print(stuList[2])