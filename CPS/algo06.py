# algo06
import re
a = input()
num = re.findall(r"\d", a)
numStr = int(''.join(num))
divisor = 0

for i in range(1, numStr+1):
    if (numStr%i == 0):
        divisor += 1

print(numStr)        
print(divisor)