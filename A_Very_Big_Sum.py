n=int(input())
s=0
a=list(map(int,input().split()))
while(n>0):
    s=0
    for i in a:
        s=s+i
    n-=1
print(s)
        