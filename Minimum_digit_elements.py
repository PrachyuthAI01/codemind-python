n=int(input())
a=list(map(int,input().split()))
s=min(a)
k=len(str(s))
c=0
for i in a:
    d=str(i)
    if len(d)==k:
        c+=1
print(c)