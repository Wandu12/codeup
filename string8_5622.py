#string8_5622
words = input().lower()
dial = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
time = 0

for i in range(len(words)):
    for j in dial:
        if(words[i] in j):
            time += dial.index(j) + 3

print(time)