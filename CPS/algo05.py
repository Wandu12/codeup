# algo05
regnum = input()
sex = int(regnum[7:8])
birthYear = int(regnum[0:2])
thisYear = 2019

if (sex > 2) and (birthYear < thisYear):
    birthYear += 2000
else:
    birthYear += 1900

print("%d "%(thisYear - birthYear + 1), end="")

if sex%2 == 0:
    print("W")
else:
    print("M")