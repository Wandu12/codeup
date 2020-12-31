# algo29
N = int(input())
countThree = ""

for i in range(1, N+1):
    countThree += str(i)

countThree = list(countThree)
print(countThree.count('3'))