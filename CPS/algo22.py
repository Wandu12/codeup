# algo22
N, K = map(int, input().split())
temp = list(map(int, input().split())) 
sumTemp = [0 for i in range(N-K+1)]
# 온도가 최대가 되는 값만 출력. 인덱스 필요 X
# 0부터 K까지, i부터 K+i까지의 합을 저장할 리스트

for i in range(0, len(sumTemp)):
    sumTemp[i] = sum(temp[i:i+K])

print(max(sumTemp))
