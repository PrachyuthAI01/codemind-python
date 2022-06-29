import math
n=int(input())
s=int(math.sqrt(n))
for i in range(1,s+1):
    if(i*i==n):
        print(True)
        break
else:
    print(False)