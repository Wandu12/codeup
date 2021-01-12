# algo36 : 삽입정렬
N = int(input())
num_list = list(map(int, input().split()))
# num_list = [11, 7, 5, 6, 10, 9]

# key와 정렬된 리스트를 비교해 알맞은 위치에 값 삽입

for i in range(1, len(num_list)):  # 0은 이미 정렬
    key = num_list[i]
    j = i-1  # 없으면 j 선언범위 벗어남

    while j >= 0 and num_list[j] > key:  # key값보다 정렬된 배열에 있는 값이 크면
        num_list[j+1] = num_list[j]  # j+1번째로 j를 이동(레코드 오른쪽으로 이동)
        j = j-1

    num_list[j+1] = key    

print(num_list)