n=int(input())
a=list(map(int,input().split()))
d=max(a)
s=len(str(d))
c=0
for i in a:
    k=str(i)
    if len(k)==s:
        c+=1
print(c)