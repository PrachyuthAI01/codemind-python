n=int(input())
d=0
s=0
while(n>0):
    m=int(input())
    d=m*(m+1)//2
    s=0
    a=list(map(int,input().split()))
    for i in a:
        s+=i
    print(d-s)
    n-=1
        
        