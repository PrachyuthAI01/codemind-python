n=int(input())
a=list(map(int,input().split()))
k,l=map(int,input().split())
d=[]
for i in a:
    if k<=i and i<=l:
        d.append(i)
if len(d)==0:
    print(-1)
else:
    print(*d)
        