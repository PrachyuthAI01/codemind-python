import math
n=int(input())
while(n):
    a=list(map(int,input().split()))
    for i in range(0,len(a)):
        t=a[i]
        x=1
        d=int(math.sqrt(a[i]))
        x=d*d
        if(t==x):
            print(True)
        else:
            print(False)
    n-=1
        
    