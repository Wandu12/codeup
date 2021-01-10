# algo34 : 버블정렬
N = int(input())
num_list = list(map(int, input().split()))

for i in range(0, len(num_list)-1):
    for j in range(i+1, len(num_list)):
        if num_list[i] > num_list[j]:
            temp = num_list[j]
            num_list[j] = num_list[i]
            num_list[i] = temp

print(num_list)