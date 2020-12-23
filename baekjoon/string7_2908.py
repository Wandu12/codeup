# string7_2908
A, B = input().split()
A = "".join(list(reversed(A)))  # str.join()으로 리스트를 문자열로 변환
B = "".join(list(reversed(B)))

if int(A) > int(B):
    print(A) 
else:
    print(B)