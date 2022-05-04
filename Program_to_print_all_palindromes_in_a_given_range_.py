n=int(input())
m=int(input())
for n in range(n,m+1,1):
    t=n
    r=0
    while(n):
        d=n%10
        r=r*10+d
        n=n//10
    if(t==r):
        print(t,end=' ')
        